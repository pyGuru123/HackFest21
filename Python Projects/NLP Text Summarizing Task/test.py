	##########################################################################################################################################

#Required Modules

import re,os,sys
WORD = re.compile(r'\w+')
import string
import math
import time
import collections
import nltk
from nltk.corpus import stopwords
from collections import Counter
from nltk.corpus import wordnet as wn
from nltk.corpus import brown
import numpy as np
from nltk.stem.porter import *

############################################################################################################################################

#THRESHOLDS

class THRESHOLDS:
   
	#Class: Scorers
	TFIDFThreshold = 0.0
		
	
	#Class: StackDecoder
	MAXIMUM_LENGTH_SUMMARY_ALLOWED = 100
	MINIMUM_LENGTH_SENTENCE_ALLOWED= 6
	SIMILARITY_BOUND = 0.5


class PROVIDE_ID:
	
	topic_id_no = -1
	doc_id_no = -1
	sen_id_no = -1

	@staticmethod
	def getNexttopic_id_no():
		PROVIDE_ID.topic_id_no = PROVIDE_ID.topic_id_no+1
		return PROVIDE_ID.topic_id_no
		

	@staticmethod   
	def getNextdoc_id_no():
		PROVIDE_ID.doc_id_no = PROVIDE_ID.doc_id_no+1
		return PROVIDE_ID.doc_id_no

	@staticmethod
	def getNextsen_id_no():
		PROVIDE_ID.sen_id_no = PROVIDE_ID.sen_id_no+1
		return PROVIDE_ID.sen_id_no

###########################################################################################################################################

#Similarity_Score

class SIMILARITY_SCORE:    
	
	def __init__(self):
		pass
		
	def get_score(self,sentence1, sentence2):
		raise NotImplementedError("Subclass must implement abstract method")


class Jaccard_Similarity (SIMILARITY_SCORE):

	def __init__(self):
		pass

	def text_to_vector(self,list_of_words):
		return Counter(list_of_words)

	def get_score(self,sentence1, sentence2):
		vec1 = self.text_to_vector(sentence1.getList_of_words())
		vec2 = self.text_to_vector(sentence2.getList_of_words())
		intersection = set(vec1.keys()) & set(vec2.keys())
		union = set(vec1.keys()) | set(vec2.keys())
		return (len(intersection))/(len(union))


class TF_IDF_Similarity(SIMILARITY_SCORE):

	def __init__(self):     
		pass

	def text_to_vector(self,list_of_words):
		return Counter(list_of_words)

	def get_cosine(self,vec1, vec2):
		intersection = set(vec1.keys()) & set(vec2.keys())
		numerator = sum([vec1[x] * vec2[x] for x in intersection])
		sum1 = sum([vec1[x]**2 for x in vec1.keys()])
		sum2 = sum([vec2[x]**2 for x in vec2.keys()])
		denominator = math.sqrt(sum1) * math.sqrt(sum2)
		if not denominator:
			return 0.0
		else:
			return float(numerator) / denominator

	def get_score(self,sentence1, sentence2):
		return self.get_cosine(self.text_to_vector(sentence1.getList_of_words()),self.text_to_vector(sentence2.getList_of_words()))


class WORD_NET_SIMILARITY(SIMILARITY_SCORE):

	def __init__(self):

		self.DELTA = 0.85
		self.ALPHA = 0.2
		self.BETA = 0.45
		self.ETA = 0.4
		self.PHI = 0.2

		self.brown_freqs = dict()
		self.N = 0

	######################### word similarity ##########################

	def get_best_synset_pair(self,word_1, word_2):
	    """ 
	    Choose the pair with highest path similarity among all pairs. 
	    Mimics pattern-seeking behavior of humans.
	    """
	    max_sim = -1.0
	    synsets_1 = wn.synsets(word_1)
	    synsets_2 = wn.synsets(word_2)
	    if len(synsets_1) == 0 or len(synsets_2) == 0:
	        return None, None
	    else:
	        max_sim = -1.0
	        best_pair = None, None
	        for synset_1 in synsets_1:
	            for synset_2 in synsets_2:
	               sim = wn.path_similarity(synset_1, synset_2)
	               if sim is not None and sim > max_sim:
	                   max_sim = sim
	                   best_pair = synset_1, synset_2
	        return best_pair

	def length_dist(self,synset_1, synset_2):
	    """
	    Return a measure of the length of the shortest path in the semantic 
	    ontology (Wordnet in our case as well as the paper's) between two 
	    synsets.
	    """
	    l_dist = sys.maxsize
	    if synset_1 is None or synset_2 is None: 
	        return 0.0
	    if synset_1 == synset_2:
	        # if synset_1 and synset_2 are the same synset return 0
	        l_dist = 0.0
	    else:
	        wset_1 = set([str(x.name()) for x in synset_1.lemmas()])        
	        wset_2 = set([str(x.name()) for x in synset_2.lemmas()])
	        if len(wset_1.intersection(wset_2)) > 0:
	            # if synset_1 != synset_2 but there is word overlap, return 1.0
	            l_dist = 1.0
	        else:
	            # just compute the shortest path between the two
	            l_dist = synset_1.shortest_path_distance(synset_2)
	            if l_dist is None:
	                l_dist = 0.0
	    # normalize path length to the range [0,1]
	    return math.exp(-self.ALPHA * l_dist)

	def hierarchy_dist(self,synset_1, synset_2):
	    """
	    Return a measure of depth in the ontology to model the fact that 
	    nodes closer to the root are broader and have less semantic similarity
	    than nodes further away from the root.
	    """
	    h_dist = sys.maxsize
	    if synset_1 is None or synset_2 is None: 
	        return h_dist
	    if synset_1 == synset_2:
	        # return the depth of one of synset_1 or synset_2
	        h_dist = max([x[1] for x in synset_1.hypernym_distances()])
	    else:
	        # find the max depth of least common subsumer
	        hypernyms_1 = {x[0]:x[1] for x in synset_1.hypernym_distances()}
	        hypernyms_2 = {x[0]:x[1] for x in synset_2.hypernym_distances()}
	        lcs_candidates = set(hypernyms_1.keys()).intersection(
	            set(hypernyms_2.keys()))
	        if len(lcs_candidates) > 0:
	            lcs_dists = []
	            for lcs_candidate in lcs_candidates:
	                lcs_d1 = 0
	                if lcs_candidate in hypernyms_1.keys():
	                    lcs_d1 = hypernyms_1[lcs_candidate]
	                lcs_d2 = 0
	                if lcs_candidate in hypernyms_2.keys():
	                    lcs_d2 = hypernyms_2[lcs_candidate]
	                lcs_dists.append(max([lcs_d1, lcs_d2]))
	            h_dist = max(lcs_dists)
	        else:
	            h_dist = 0
	    return ((math.exp(self.BETA * h_dist) - math.exp(-self.BETA * h_dist)) / 
	        (math.exp(self.BETA * h_dist) + math.exp(-self.BETA * h_dist)))
	    
	def word_similarity(self,word_1, word_2):
	    synset_pair = self.get_best_synset_pair(word_1, word_2)
	    return (self.length_dist(synset_pair[0], synset_pair[1]) * 
	        self.hierarchy_dist(synset_pair[0], synset_pair[1]))

	######################### sentence similarity ##########################

	def most_similar_word(self,word, word_set):
	    """
	    Find the word in the joint word set that is most similar to the word
	    passed in. We use the algorithm above to compute word similarity between
	    the word and each word in the joint word set, and return the most similar
	    word and the actual similarity value.
	    """
	    max_sim = -1.0
	    sim_word = ""
	    for ref_word in word_set:
	      sim = self.word_similarity(word, ref_word)
	      if sim > max_sim:
	          max_sim = sim
	          sim_word = ref_word
	    return sim_word, max_sim
	    
	def info_content(self,lookup_word):
	    """
	    Uses the Brown corpus available in NLTK to calculate a Laplace
	    smoothed frequency distribution of words, then uses this information
	    to compute the information content of the lookup_word.
	    """
	    if self.N == 0:
	        # poor man's lazy evaluation
	        for sent in brown.sents():
	            for word in sent:
	                word = word.lower()
	                if not word in self.brown_freqs.keys():
	                    self.brown_freqs[word] = 0
	                self.brown_freqs[word] = self.brown_freqs[word] + 1
	                self.N = self.N + 1
	    lookup_word = lookup_word.lower()
	    n = 0 if not lookup_word in self.brown_freqs.keys() else self.brown_freqs[lookup_word]
	    return 1.0 - (math.log(n + 1) / math.log(self.N + 1))
	    
	def semantic_vector(self,words, joint_words, info_content_norm):
	    """
	    Computes the semantic vector of a sentence. The sentence is passed in as
	    a collection of words. The size of the semantic vector is the same as the
	    size of the joint word set. The elements are 1 if a word in the sentence
	    already exists in the joint word set, or the similarity of the word to the
	    most similar word in the joint word set if it doesn't. Both values are 
	    further normalized by the word's (and similar word's) information content
	    if info_content_norm is True.
	    """
	    sent_set = set(words)
	    semvec = np.zeros(len(joint_words))
	    i = 0
	    for joint_word in joint_words:
	        if joint_word in sent_set:
	            # if word in union exists in the sentence, s(i) = 1 (unnormalized)
	            semvec[i] = 1.0
	            if info_content_norm:
	                semvec[i] = semvec[i] * math.pow(self.info_content(joint_word), 2)
	        else:
	            # find the most similar word in the joint set and set the sim value
	            sim_word, max_sim = self.most_similar_word(joint_word, sent_set)
	            semvec[i] = self.PHI if max_sim > self.PHI else 0.0
	            if info_content_norm:
	                semvec[i] = semvec[i] * self.info_content(joint_word) * self.info_content(sim_word)
	        i = i + 1
	    return semvec                
	            
	def semantic_similarity(self,sentence_1, sentence_2, info_content_norm):
	    """
	    Computes the semantic similarity between two sentences as the cosine
	    similarity between the semantic vectors computed for each sentence.
	    """
	    words_1 = sentence_1.getList_of_words()
	    words_2 = sentence_2.getList_of_words()
	    joint_words = set(words_1).union(set(words_2))
	    vec_1 = self.semantic_vector(words_1, joint_words, info_content_norm)
	    vec_2 = self.semantic_vector(words_2, joint_words, info_content_norm)
	    return np.dot(vec_1, vec_2.T) / (np.linalg.norm(vec_1) * np.linalg.norm(vec_2))

	######################### word order similarity ##########################

	def word_order_vector(self,words, joint_words, windex):
	    """
	    Computes the word order vector for a sentence. The sentence is passed
	    in as a collection of words. The size of the word order vector is the
	    same as the size of the joint word set. The elements of the word order
	    vector are the position mapping (from the windex dictionary) of the 
	    word in the joint set if the word exists in the sentence. If the word
	    does not exist in the sentence, then the value of the element is the 
	    position of the most similar word in the sentence as long as the similarity
	    is above the threshold self.ETA.
	    """
	    wovec = np.zeros(len(joint_words))
	    i = 0
	    wordset = set(words)
	    for joint_word in joint_words:
	        if joint_word in wordset:
	            # word in joint_words found in sentence, just populate the index
	            wovec[i] = windex[joint_word]
	        else:
	            # word not in joint_words, find most similar word and populate
	            # word_vector with the thresholded similarity
	            sim_word, max_sim = self.most_similar_word(joint_word, wordset)
	            if max_sim > self.ETA:
	                wovec[i] = windex[sim_word]
	            else:
	                wovec[i] = 0
	        i = i + 1
	    return wovec

	def word_order_similarity(self,sentence_1, sentence_2):
	    """
	    Computes the word-order similarity between two sentences as the normalized
	    difference of word order between the two sentences.
	    """
	    words_1 = sentence_1.getList_of_words()
	    words_2 = sentence_2.getList_of_words()
	    joint_words = list(set(words_1).union(set(words_2)))
	    windex = {x[1]: x[0] for x in enumerate(joint_words)}
	    r1 = self.word_order_vector(words_1, joint_words, windex)
	    r2 = self.word_order_vector(words_2, joint_words, windex)
	    return 1.0 - (np.linalg.norm(r1 - r2) / np.linalg.norm(r1 + r2))

	######################### overall similarity ##########################

	def get_score(self,sentence_1, sentence_2):
	    """
	    Calculate the semantic similarity between two sentences. The last 
	    parameter is True or False depending on whether information content
	    normalization is desired or not.
	    """
	    return self.DELTA * self.semantic_similarity(sentence_1, sentence_2, True) + (1.0 - self.DELTA) * self.word_order_similarity(sentence_1, sentence_2)	


#############################################################################################################################################

#Models

class Sentence:
	def __init__(self, sen_id_no, senLength, list_of_words, actual_sentence, location_in_sentence, doc_id_no):
		self.location_in_sentence = 0
		self.score = 0
		self.sen_id_no = sen_id_no
		self.sentenceLength = senLength
		#self.list_of_words = self.preProcess(list_of_words)
		self.list_of_words = list_of_words
		self.actual_sentence = actual_sentence
		self.location_in_sentence = location_in_sentence
		self.doc_id_no = doc_id_no
		self.partOfHumanSummary = False
		self.isPositiveSample = False


	def setActual_sentence(self, actual_sentence):
		self.actual_sentence = actual_sentence
	
	def isPartOfHumanSummary(self):
		return self.partOfHumanSummary

	def setPartOfHumanSummary(self, value):
		self.partOfHumanSummary = value

	def getLocation_in_sentence(self):
		return self.location_in_sentence

	def setLocation_in_sentence(self, location_in_sentence):
		self.location_in_sentence = location_in_sentence

	def getdoc_id_no(self):
		return self.doc_id_no

	def getList_of_words(self):
		return self.list_of_words

	def getScore(self):
		return self.score

	def setScore(self, score):
		self.score = score

	def getActual_sentence(self):
		return self.actual_sentence

	def isPositiveSample(self):
		return self.isPositiveSample

	def setPositiveSample(self, isPositiveSample):
		self.isPositiveSample = isPositiveSample

	def getSentenceLength(self):
		return self.sentenceLength

	def getId(self):
		return ""+str(self.sen_id_no)

	def toString(self):
		return self.getActual_sentence() + " - " + str(self.getScore())


	def preProcess(self,list_of_words):
		stemmer = PorterStemmer()
		result = []
		for i in list_of_words:
			if i not in stopwords.words('english'):
				result.append(stemmer.stem(i))
		return result



class Document: 
	def __init__(self, sentences=[], filename="", doc_id_no=0):
		self.sentences = sentences
		self.filename = filename
		self.doc_id_no = doc_id_no
		
	def addSentence(self, sentence):
		self.sentences.append(sentence)   

	def getSentences(self):
		return self.sentences

	def getdoc_id_no(self):
		return self.doc_id_no

	def getNumberOfSentences(self):
		return len(self.sentences)


class Summary(Document):

	def __init__(self,filename=None,doc_id_no=0,isHuman=False):        
		self.isHuman = isHuman
		if filename is not None:
			super().__init__(SentenceProcessor.getSentences(filename,doc_id_no),filename,doc_id_no)

	def isHuman (self):
		return self.isHuman



class Topic:
	def __init__(self, filename=None, topic_id_no=123456):
		self.summaries = []
		self.sentenceMap = {}
		if filename is not None:            
			self.documents = SentenceProcessor.getDocuments(filename,self.sentenceMap)
		else:
			self.documents = [] 
		self.topic_id_no = topic_id_no
		

	def getSentenceMap(self):
		return self.sentenceMap

	def addDocument(self,doc):
		self.documents.append(doc)

	def getDocuments(self):
		return self.documents

	def addSummary(self,s):
		self.summaries.append(s)

	def getSummaries(self):
		return self.summaries

	def gettopic_id_no(self):
		return self.topic_id_no



class DataSet:

	def __init__(self,dirPath=None):
		self.topicMap={}
		self.nameMap={}
		self.simScorer = TF_IDF_Similarity()
		self.EXT_SUMMARY = "sum"
		self.EXT_SOURCE = "txt"

		if dirPath is not None:
			topic_id_no=0
			files = self.getFiles(dirPath)
			t = None
			s = None

			#Process Topics
			for file in files:                
				fname = file.split('/')
				fname = fname[-1]
				fname = fname.split('.')
				
				file_name = fname[0]
				extension = fname[-1]

				if(extension == self.EXT_SOURCE):   
					print("Processing: " + file)        
					topic_id_no = PROVIDE_ID.getNexttopic_id_no()
					t = Topic(file, topic_id_no)  
					topic = file_name
					self.topicMap[topic] = t
					self.nameMap[topic_id_no] = topic


			#Add Summaries
			for file in files:
				
				fname = file.split('/')
				fname = fname[-1]
				fname = fname.split('.')
				
				file_name = fname[0]
				extension = fname[-1]

				if(extension == self.EXT_SUMMARY):
					print("Processing: " + file)
					s = Summary(file, PROVIDE_ID.getNextdoc_id_no(), True);
					topic = file_name
					t = self.topicMap[topic]
					t.addSummary(s);    
				


	def getFiles(self,path): 
		
		files = [f for f in os.listdir(path) if (f.endswith(self.EXT_SOURCE) or f.endswith(self.EXT_SUMMARY))]
		fileNames = sorted(files, key=lambda y: (y.rsplit('.')[0]))
		result = [os.path.join(path,f) for f in fileNames]
		return result
	

		

	def calculateImportanceScores(self,weights):
		for t in self.topicMap.values():
			totalSet = []
			for doc in t.getDocuments():
				totalSet.append(doc)
			for summary in t.getSummaries():
				totalSet.append(summary)
			impModule = ImportanceModule(totalSet)
			impModule.setWeightsForImpScorers(weights)
			impModule.setValues(totalSet)

	def getTopicMapSize(self):
		return len(self.topicMap)
	
	def getTopic(self, key):
		return self.topicMap[key]

	def getTopicName(self,topic_id_no): 
		return self.nameMap[topic_id_no]


	def getTopicMap(self):
		return self.topicMap

	def getTopics(self):
		res = []
		for t in self.topicMap.values():
			res.append(t)
		return res

	def getTopicNames(self):
		res = []
		for t in self.topicMap.keys():
			res.append(t)
		return res   

############################################################################################################################################

#Sentence Preprocessor


class SentenceProcessor:

	SENTENCE_MARKER = "Sentence:"
	WORD_MARKER = "\tS:"
	PUNCTUATION = "\"'`!?&_/\\);][<>~@-({}:"
	TERMINAL = "#"

	@staticmethod
	def getDocuments(filename,sentenceMap):
		
		documents = []
		sentences = []

		lineNum=0
		doc_id_no = PROVIDE_ID.getNextdoc_id_no()

		f = open(filename, "r")
		text = None
		noSpace = False

		text = f.readline()
	   
		
		while(text is not None and text.strip() == SentenceProcessor.SENTENCE_MARKER):
			
			#Sentence starts
			senLength=0
			sb = ""
			list_of_words= []
			lineNum = lineNum+1
			
			while (text is not None):
				
				text = f.readline()
			
				if(text is not None and not (text =="") and not (text.strip()==SentenceProcessor.SENTENCE_MARKER)): 
						  
					if(not text.startswith(SentenceProcessor.WORD_MARKER)):
							continue
				  
					word = text.split("S: ")[1]
					word = word.replace('\n','')
				   
					#filter spurious chars
					if word in SentenceProcessor.PUNCTUATION:
						continue
					else:

						if(word == ",") or (word == "."):
							noSpace=True
						
					if word.strip()==SentenceProcessor.TERMINAL:        
							  
						#Document ends
						d = Document(sentences, filename, doc_id_no)
						documents.append(d)
						lineNum=0
						sentences = []
						doc_id_no = PROVIDE_ID.getNextdoc_id_no()
						text = f.readline()
						break
						
					split=None
					cWord = ""
					if '-' in word:
						splitted = word.split("-")
						senLength = senLength+1
						for cword in splitted:                      
							cWord = word.replace("\\W", "");
							if len(cWord)>0:
								list_of_words.append(cWord)
						
						
					else:                   
						cWord = word.replace("\\W", "")
						if len(cWord)>0:
							senLength = senLength+1
							list_of_words.append(cWord)
						
					
					if len(sb)== 0:
						sb += word
					else:
					
						if noSpace:
							noSpace = False
							sb += word
							
						else:
							sb+=' '
							sb += word

				   
				
				else:
					break
				
								
			if(len(list_of_words)>0 and len(sb)>0):   
					  
				id_no = PROVIDE_ID.getNextsen_id_no()
				s = Sentence(id_no, senLength, list_of_words, sb, lineNum, doc_id_no)
				sentences.append(s)
				sentenceMap[id_no] = s

		return documents

	

	@staticmethod
	def getSentences(filename,doc_id_no):
		
		sentences = []

		lineNum=0
		
		f = open(filename, "r")
		text = None
		noSpace = False

		text = f.readline()
		
			
		while(text is not None and text.strip().startswith(SentenceProcessor.SENTENCE_MARKER)):          
			#Sentence starts
			senLength=0
			sb = ""
			list_of_words= []
			lineNum = lineNum+1
			
			while (text is not None):               
				text = f.readline()
				
				if(text is not None and not (text =="") and not (text.strip().startswith(SentenceProcessor.SENTENCE_MARKER))): 
						  
					if(not text.startswith(SentenceProcessor.WORD_MARKER)):
							continue
					
					word = text.split("S: ")[1]
					word = word.replace('\n','')
				

					#filter spurious chars
					if word in SentenceProcessor.PUNCTUATION:
						continue
					else:

						if(word == ",") or (word == "."):
							noSpace=True
						
					split=None
					cWord = ""
					if '-' in word:
						splitted = word.split("-")
						senLength = senLength+1
						for cword in splitted:                      
							cWord = word.replace("\\W", "");
							if len(cWord)>0:
								list_of_words.append(cWord)
						
						
					else:                   
						cWord = word.replace("\\W", "")
						if len(cWord)>0:
							senLength = senLength+1
							list_of_words.append(cWord)
						
					
					if len(sb)== 0:
						sb += word
					else:                    
						if noSpace:
							noSpace = False
							sb += word
							
						else:
							sb+=' '
							sb += word

				   
				
				else:
					break
				
								
			if(len(list_of_words)>0 and len(sb)>0):   
					  
				id_no = PROVIDE_ID.getNextsen_id_no()
				s = Sentence(id_no, senLength, list_of_words, sb, lineNum, doc_id_no)
				s.setPositiveSample(True)
				s.setPartOfHumanSummary(True)
				sentences.append(s)

		return sentences


###############################################################################################################################################


#Importance Scorers


class ImportanceScorer:
	
	def __init__(self):
		pass

	def initialize(self,docs):
		raise NotImplementedError("Subclass must implement abstract method")

	def getImportanceScore(self,doc,sentence):
		raise NotImplementedError("Subclass must implement abstract method")

	def setWeightage(self,weight):
		raise NotImplementedError("Subclass must implement abstract method")

	def getWeightage(self):
		raise NotImplementedError("Subclass must implement abstract method")

	def getName(self):
		raise NotImplementedError("Subclass must implement abstract method")
		



class UpperCaseCalculator(ImportanceScorer):
	def __init__(self):
		self.docMap = None
		self.weightage = 1.0

	def initialize(self,docs):
		docMap = {}
		for doc in docs:
			pair = self.getDocStats(doc)
			docMap[doc.getdoc_id_no()] = pair
		self.docMap = docMap

	def getDocStats(self,doc):
		p = Pair()
		for sent in doc.getSentences():
			p.avg += self.getSentenceSum(doc.getdoc_id_no(), sent)
		p.avg /= doc.getNumberOfSentences()

		for sent in doc.getSentences():
			p.stdDev += (self.getSentenceSum(doc.getdoc_id_no(), sent) - p.avg)**2

		p.stdDev /= doc.getNumberOfSentences()
		p.stdDev = math.sqrt(p.stdDev)
		return p

	def getSentenceSum(self,docId,s):
		score = 0.0
		for word in s.getList_of_words():
			score += self.getWordScore(s.getdoc_id_no(), word)
		return score


	
	def getWordScore(self,docId, word):
		word = word.strip()
		if len(word)>0:
			ascii = ord(word[0])
			if ascii >= 65 and ascii <= 90:
				return 1
			
		return 0
	
	def getImportanceScore(self, doc, sentence):
		p = None
		if doc.getdoc_id_no() in self.docMap:
			p = self.docMap[doc.getdoc_id_no()]
		else:
			p = self.getDocStats(doc)
			self.docMap[doc.getdoc_id_no()] = p

		score = self.getSentenceSum(doc.getdoc_id_no(), sentence)
		return float(score)/sentence.getSentenceLength()

	def getName(self):
		return "UpperCaseCalculator"

	def getWeightage(self):
		return self.weightage

	def setWeightage(self, weight):
		self.weightage = weight



class Pair:
	def __init__(self):
		self.avg = 0
		self.stdDev = 0


class NounsCalculator(ImportanceScorer):
	def __init__(self):
		self.docMap = None
		self.weightage = 1.0

	def initialize(self,docs):
		docMap = {}
		for doc in docs:
			pair = self.getDocStats(doc)
			docMap[doc.getdoc_id_no()] = pair
		self.docMap = docMap

	def getDocStats(self,doc):
		p = Pair()
		for sent in doc.getSentences():
			p.avg += self.getSentenceSum(doc.getdoc_id_no(), sent)
		p.avg /= doc.getNumberOfSentences()

		for sent in doc.getSentences():
			p.stdDev += (self.getSentenceSum(doc.getdoc_id_no(), sent) - p.avg)**2

		p.stdDev /= doc.getNumberOfSentences()
		p.stdDev = math.sqrt(p.stdDev)
		return p

	def getSentenceSum(self,docId,s):
		score = 0.0
		tags = nltk.pos_tag(s.getList_of_words())
		for tuple in tags:
			if tuple[1]=='NN' or tuple[1]=='NNP' or tuple[1]=='NNS': 
				score = score+1
		return score 


	
	def getImportanceScore(self, doc, sentence):
		p = None
		if doc.getdoc_id_no() in self.docMap:
			p = self.docMap[doc.getdoc_id_no()]
		else:
			p = self.getDocStats(doc)
			self.docMap[doc.getdoc_id_no()] = p

		score = self.getSentenceSum(doc.getdoc_id_no(), sentence)
		return float(score)/sentence.getSentenceLength()

	def getName(self):
		return "UpperCaseCalculator"

	def getWeightage(self):
		return self.weightage

	def setWeightage(self, weight):
		self.weightage = weight


class VerbsCalculator(ImportanceScorer):
	def __init__(self):
		self.docMap = None
		self.weightage = 1.0

	def initialize(self,docs):
		docMap = {}
		for doc in docs:
			pair = self.getDocStats(doc)
			docMap[doc.getdoc_id_no()] = pair
		self.docMap = docMap

	def getDocStats(self,doc):
		p = Pair()
		for sent in doc.getSentences():
			p.avg += self.getSentenceSum(doc.getdoc_id_no(), sent)
		p.avg /= doc.getNumberOfSentences()

		for sent in doc.getSentences():
			p.stdDev += (self.getSentenceSum(doc.getdoc_id_no(), sent) - p.avg)**2

		p.stdDev /= doc.getNumberOfSentences()
		p.stdDev = math.sqrt(p.stdDev)
		return p

	def getSentenceSum(self,docId,s):
		score = 0.0
		tags = nltk.pos_tag(s.getList_of_words())
		for tuple in tags:
			if tuple[1]=='VB' or tuple[1]=='VBD' or tuple[1]=='VBG' or tuple[1]=='VBN' or tuple[1]=='VBP' or tuple[1]=='VBZ':
				score = score+1
		return score 


	
	def getImportanceScore(self, doc, sentence):
		p = None
		if doc.getdoc_id_no() in self.docMap:
			p = self.docMap[doc.getdoc_id_no()]
		else:
			p = self.getDocStats(doc)
			self.docMap[doc.getdoc_id_no()] = p

		score = self.getSentenceSum(doc.getdoc_id_no(), sentence)
		return float(score)/sentence.getSentenceLength()

	def getName(self):
		return "UpperCaseCalculator"

	def getWeightage(self):
		return self.weightage

	def setWeightage(self, weight):
		self.weightage = weight


class AdjectivesCalculator(ImportanceScorer):
	def __init__(self):
		self.docMap = None
		self.weightage = 1.0

	def initialize(self,docs):
		docMap = {}
		for doc in docs:
			pair = self.getDocStats(doc)
			docMap[doc.getdoc_id_no()] = pair
		self.docMap = docMap

	def getDocStats(self,doc):
		p = Pair()
		for sent in doc.getSentences():
			p.avg += self.getSentenceSum(doc.getdoc_id_no(), sent)
		p.avg /= doc.getNumberOfSentences()

		for sent in doc.getSentences():
			p.stdDev += (self.getSentenceSum(doc.getdoc_id_no(), sent) - p.avg)**2

		p.stdDev /= doc.getNumberOfSentences()
		p.stdDev = math.sqrt(p.stdDev)
		return p

	def getSentenceSum(self,docId,s):
		score = 0.0
		tags = nltk.pos_tag(s.getList_of_words())
		for tuple in tags:
			if tuple[1]=='JJ' or tuple[1]=='JJR' or tuple[1]=='JJS':
				score = score+1
		return score 


	
	def getImportanceScore(self, doc, sentence):
		p = None
		if doc.getdoc_id_no() in self.docMap:
			p = self.docMap[doc.getdoc_id_no()]
		else:
			p = self.getDocStats(doc)
			self.docMap[doc.getdoc_id_no()] = p

		score = self.getSentenceSum(doc.getdoc_id_no(), sentence)
		return float(score)/sentence.getSentenceLength()

	def getName(self):
		return "UpperCaseCalculator"

	def getWeightage(self):
		return self.weightage

	def setWeightage(self, weight):
		self.weightage = weight






class SentenceLengthCalculator(ImportanceScorer):
	def __init__(self):
		self.docMap = None
		self.weightage = 1.0

	def initialize(self,docs):
		docMap = {}
		for doc in docs:
			pair = self.getDocStats(doc)
			docMap[doc.getdoc_id_no()] = pair
		self.docMap = docMap

	def getDocStats(self,doc):
		p = Pair()
		for sent in doc.getSentences():
			p.avg += sent.getSentenceLength()
		p.avg /= doc.getNumberOfSentences()

		for sent in doc.getSentences():
			p.stdDev += (sent.getSentenceLength() - p.avg)**2

		p.stdDev /= doc.getNumberOfSentences()
		p.stdDev = math.sqrt(p.stdDev)
		return p

	
	def getImportanceScore(self, doc, sentence):
		p = None
		if doc.getdoc_id_no() in self.docMap:
			p = self.docMap[doc.getdoc_id_no()]
		else:
			p = self.getDocStats(doc)
			self.docMap[doc.getdoc_id_no()] = p

		return sentence.getSentenceLength()

	def getName(self):
		return "SentLength"

	def getWeightage(self):
		return self.weightage

	def setWeightage(self, weight):
		self.weightage = weight



class NumLiteralsCalculator(ImportanceScorer):
	def __init__(self):
		self.docMap = None
		self.weightage = 1.0

	def initialize(self,docs):
		docMap = {}
		for doc in docs:
			pair = self.getDocStats(doc)
			docMap[doc.getdoc_id_no()] = pair
		self.docMap = docMap

	def getDocStats(self,doc):
		p = Pair()
		for sent in doc.getSentences():
			p.avg += self.getSentenceSum(doc.getdoc_id_no(), sent)
		p.avg /= doc.getNumberOfSentences()

		for sent in doc.getSentences():
			p.stdDev += (self.getSentenceSum(doc.getdoc_id_no(), sent) - p.avg)**2

		p.stdDev /= doc.getNumberOfSentences()
		p.stdDev = math.sqrt(p.stdDev)
		return p

	def getSentenceSum(self,docId,s):
		score = 0.0
		for word in s.getList_of_words():
			score += self.getWordScore(s.getdoc_id_no(), word)
		return score


	
	def getWordScore(self,docId, word):
		score = 0
		word = word.strip()
		if len(word)>0:
			try:
				float(word)
				score = 1
			except:
				score = 0

		return score
	
	def getImportanceScore(self, doc, sentence):
		p = None
		if doc.getdoc_id_no() in self.docMap:
			p = self.docMap[doc.getdoc_id_no()]
		else:
			p = self.getDocStats(doc)
			self.docMap[doc.getdoc_id_no()] = p

		score = self.getSentenceSum(doc.getdoc_id_no(), sentence)

		if p.stdDev!=0:
			alpha = (score - p.avg) / p.stdDev
		else:
			alpha = 0

		alpha = float(alpha)


		return score/sentence.getSentenceLength()

	def getName(self):
		return "NumLiteralsCalculator"

	def getWeightage(self):
		return self.weightage

	def setWeightage(self, weight):
		self.weightage = weight



class SentencePosCalculator(ImportanceScorer):
	def __init__(self):
		self.weightage = 1.0

	def initialize(self,docs):
		pass
		#Do Nothing

	def getImportanceScore(self, doc, sentence):
		totSentences = doc.getNumberOfSentences()
		return float(sentence.getLocation_in_sentence()) / float(totSentences)

	def getName(self):
		return "SentPost"

	def getWeightage(self):
		return self.weightage

	def setWeightage(self, weight):
		self.weightage = weight


class TfIdfCalculator(ImportanceScorer):
	
	def __init__(self):
		self.stats = None
		self.totalDocs = 0
		self.docMap = None
		self.weightage = 1.0

	def initialize(self,docs):
		self.stats = {}
		self.totalDocs = len(docs)

		processes_docs = []
		for doc in docs:
			processes_docs.append(self.process(doc))

		self.normalize()

		self.initDocStats(docs)

	def initDocStats(self,docs):
		docMap = {}
		for doc in docs:
			pair = self.getDocStats(doc)
			docMap[doc.getdoc_id_no()] = pair
		self.docMap = docMap


	def getDocStats(self,doc):
		p = Pair()
		for sent in doc.getSentences():
			p.avg += self.getSentenceSum(doc.getdoc_id_no(), sent)
		p.avg /= doc.getNumberOfSentences()

		for sent in doc.getSentences():
			p.stdDev += (self.getSentenceSum(doc.getdoc_id_no(), sent) - p.avg)**2

		p.stdDev /= doc.getNumberOfSentences()
		p.stdDev = math.sqrt(p.stdDev)
		return p

	def getSentenceSum(self,docId,s):
		score = 0.0
		for word in s.getList_of_words():
			score += self.getImportanceScore2(s.getdoc_id_no(), word)
		return score

	def getImportanceScore2(self, docId, word):
		return self.stats[word][docId]


	def getImportanceScore(self, doc, sentence):
		p = None
		if doc.getdoc_id_no() in self.docMap:
			p = self.docMap[doc.getdoc_id_no()]
		else:
			p = self.getDocStats(doc)
			self.docMap[doc.getdoc_id_no()] = p

		score = self.getSentenceSum(doc.getdoc_id_no(), sentence)
		return float(score)/sentence.getSentenceLength()

	def process(self,doc):
		inverted_index = self.stats
		id_no = doc.getdoc_id_no()
		for sent in doc.getSentences():
			for word in sent.getList_of_words():
				ls = {}
				
				if word in inverted_index:
					ls = inverted_index[word]
					if id_no in ls:
						count = ls[id_no]
						ls[id_no] = count+1
					else:
						ls[id_no] = 1

				else:   
					ls[id_no]=1         
				
				inverted_index[word] = ls
		self.stats = inverted_index

	def normalize(self):
		inverted_index = self.stats
		for word in inverted_index.keys():
			posting = inverted_index[word]
			docfreq = len(posting.keys())
			idf = 1
			if self.totalDocs != docfreq:
				idf = math.log(self.totalDocs/docfreq)

			

			for docid in inverted_index[word].keys():
				tfidf = (1+math.log(inverted_index[word][docid]))*idf
				inverted_index[word][docid] = tfidf


		self.stats = inverted_index 


	def getName(self):
		return "TFIDFSum"

	def getWeightage(self):
		return self.weightage

	def setWeightage(self, weight):
		self.weightage = weight



class TopKImpWordsCalculator(ImportanceScorer):
	
	def __init__(self):
		self.tfIdfStats = None
		self.weightage = 1.0

	
	def initialize(self,docs):
		#Do Nothing
		pass

	def setTfIDFCalculator(self, tfidfcalculator):
		self.tfIdfStats = tfidfcalculator
	


	def getImportanceScore(self, doc, sentence):
		if self.tfIdfStats is None:
			return len(sentence.getList_of_words())
		else:
			sum=0
			for word in sentence.getList_of_words():
				score = self.tfIdfStats.getImportanceScore2(sentence.getdoc_id_no(), word)
				if score >= THRESHOLDS.TFIDFThreshold:
					sum = sum+1
				
			return sum

	def getName(self):
		return "TopKImpWords"

	def getWeightage(self):
		return self.weightage

	def setWeightage(self, weight):
		self.weightage = weight


#################################################################################################################################################

#Overall Importance Module

class ImportanceModule:
	def __init__(self,docs):
		self.scorers=[]
		
		is1 = TfIdfCalculator()
		is1.setWeightage(1.0)
		is1.initialize(docs)
		self.scorers.append(is1)

		is2 = SentenceLengthCalculator()
		is2.setWeightage(1.0)
		is2.initialize(docs)
		self.scorers.append(is2)

		is3 = SentencePosCalculator()
		is3.setWeightage(1.0)
		is3.initialize(docs)
		self.scorers.append(is3)

		is4 = NumLiteralsCalculator()
		is4.setWeightage(1.0)
		is4.initialize(docs)
		self.scorers.append(is4)

		is5 = UpperCaseCalculator()
		is5.setWeightage(1.0)
		is5.initialize(docs)
		self.scorers.append(is5)

		is6 = NounsCalculator()
		is6.setWeightage(1.0)
		is6.initialize(docs)
		self.scorers.append(is6)

		is7 = VerbsCalculator()
		is7.setWeightage(1.0)
		is7.initialize(docs)
		self.scorers.append(is7)

		is8 = AdjectivesCalculator()
		is8.setWeightage(1.0)
		is8.initialize(docs)
		self.scorers.append(is8)

	def setValues(self,docs):
		for doc in docs:
			for sentence in doc.getSentences():
				sentence.setScore(self.getSentenceScore(doc,sentence))

	def getSentenceScore(self,doc,sentence):
		hyp = -0.839757
		for imp_scr in self.scorers:
			hyp+=(imp_scr.getImportanceScore(doc,sentence)*imp_scr.getWeightage())
		return hyp

	def setWeightsForImpScorers(self,weights):
		for i in range(0,len(weights)):
			self.scorers[i].setWeightage(weights[i])

###############################################################################################################################################

#Stack Decoder

class StackDecoder:
	def __init__(self,documents):
		self.stacks = []
		self.simScoreCache = {}
		self.documents = documents
		self.sentences = self.buildSentenceList()
		self.setUpStacks()
		self.simScorer = TF_IDF_Similarity()


	def setUpStacks(self):
		for i in range(THRESHOLDS.MAXIMUM_LENGTH_SUMMARY_ALLOWED+2):
			self.stacks.append(Stack())

	
	
	def runStackDecoder(self):
		self.initializeStack()

		for i in range(THRESHOLDS.MAXIMUM_LENGTH_SUMMARY_ALLOWED+1):
			print ("StackDecoder:runStackDecoder:: Running stack: " + str(i))
			if self.stacks[i].pq.size==0:
				continue
			
			pqClone = self.stacks[i].pq.clone()


			while(pqClone.hasNext()):
				summary = pqClone.next()
				for j in range(len(self.sentences)):
					if j in summary:
						continue
					s = self.sentences[j]
					newIndex = THRESHOLDS.MAXIMUM_LENGTH_SUMMARY_ALLOWED+1
					if i+s.getSentenceLength() <= THRESHOLDS.MAXIMUM_LENGTH_SUMMARY_ALLOWED:
						newIndex = i+s.getSentenceLength()

					if self.isIncludeSentence(summary, s, j):
						newSummary = list(summary)
						newSummary.append(j)
						priority = self.getObjectiveFunction(newSummary)

						if priority > self.stacks[newIndex].pq.getPriority():
							self.stacks[newIndex].add(newSummary, priority)

			self.stacks[i].printStackPQ()
	
	
	def initializeStack(self):
		for i in range(len(self.sentences)):
			s = self.sentences[i]
			l = []
			l.append(i)
			index = THRESHOLDS.MAXIMUM_LENGTH_SUMMARY_ALLOWED+1
			if s.getSentenceLength()<=THRESHOLDS.MAXIMUM_LENGTH_SUMMARY_ALLOWED:
				index = s.getSentenceLength()
			self.stacks[index].add(l, self.getObjectiveFunction(l))

	
	def printStack(self, num):
		self.stacks[num].printStackPQ()
	
	def getObjectiveFunction(self,senRefList):
		summaryObjectiveScore = 0
		for i in senRefList:
			summaryObjectiveScore += self.sentences[i].getScore()		
		return summaryObjectiveScore
		
	def buildSentenceList(self):
		sentences = []
		senNum=-1;
		for i in range(len(self.documents)):
			print("StackDecoder:buildSentenceList:: Doc: " + str(i+1))
			d = self.documents[i]
			for s in d.getSentences():
				if s.getSentenceLength()>=THRESHOLDS.MINIMUM_LENGTH_SENTENCE_ALLOWED:
					sentences.append(s);
					senNum = senNum+1
					print("StackDecoder:buildSentenceList:: (" + str(senNum) + ")" + str(s.getActual_sentence()) + " - " + str(s.getScore()))
				
		return sentences


	
	def isIncludeSentence(self,summary, s, sIndex):
	
		#returns whether the sentence should be included in the summary or not
		for i in range(len(summary)):
			key = str(sIndex)+","+ str(summary[i])
			sim = 0;
			if key in self.simScoreCache.keys():
				sim = self.simScoreCache[key]
			else:
				sim = self.simScorer.get_score(s, self.sentences[summary[i]])
				self.simScoreCache[key] = sim
		
			if sim > THRESHOLDS.SIMILARITY_BOUND:
				return False
		
		return True

	def dumpBestSummary(self,fileName):
		f = open(fileName, 'w')
		bestSummary = self.stacks[THRESHOLDS.MAXIMUM_LENGTH_SUMMARY_ALLOWED].getBest()
		length = THRESHOLDS.MAXIMUM_LENGTH_SUMMARY_ALLOWED

		while(bestSummary is None):
				print(length)
				length = length-1
				bestSummary = self.stacks[length].getBest()
				print(bestSummary)
			
		bestSummary = sorted(bestSummary)
		for senIndex in bestSummary:
			s = self.sentences[senIndex]
			f.write(s.getActual_sentence())
			f.write('\n')
		
		f.close()	
			
		
################################################################################################################################################

#Stack for StackDecoder

class Stack:
	
	def __init__(self):
		self.pq = SpecialPQ()

	def add(self,key,priority):
		self.pq.add(key, priority) 
	
	def getBest(self):
		return self.pq.peek()
		
	
	def printStackPQ(self):
		print ("StackDecoder:Stack:printStackPQ:: Stack print..")
		print(self.pq.toString(self.pq.size))
		
		
###############################################################################################################################################
	
#Special Priority Queue

class SpecialPQ:
	def __init__(self):
		self.size = 0
		self.capacity = self.getLegalCapacity(128)
		self.elements = []
		self.priorities = []
		for i in range(self.capacity):
			self.priorities.append(0)
		


	def parent(self,loc):
		return int((loc -1)/2)

	def leftChild(self,loc):
		return 2*loc+1

	def rightChild(self,loc):
		return 2*loc+2

	def heapifyUp(self,loc):
		if loc==0:
			return
		parent = self.parent(loc)
		if (self.priorities[loc] > self.priorities[parent]):
			self.swap(loc, parent)
			self.heapifyUp(parent)

	def heapifyDown(self,loc):
		max_ = loc;
		leftChild = self.leftChild(loc)
		if (leftChild < self.size):
			priority = self.priorities[loc]
			leftChildPriority = self.priorities[leftChild]
			if (leftChildPriority > priority):
				max_ = leftChild
			rightChild = self.rightChild(loc)
			if (rightChild < self.size):
				rightChildPriority = self.priorities[self.rightChild(loc)]
				if (rightChildPriority > priority and rightChildPriority > leftChildPriority):
					max_ = rightChild
			
		
		if (max_ == loc):
			return;
		self.swap(loc, max_)
		self.heapifyDown(max_)

	def swap(self,loc1,loc2):
		tempPriority = self.priorities[loc1]
		tempElement = self.elements[loc1]
		self.priorities[loc1] = self.priorities[loc2]
		self.elements[loc1] = self.elements[loc2]
		self.priorities[loc2] = tempPriority
		self.elements[loc2] = tempElement
	
	def removeFirst(self):
		if (self.size < 1):
			return
		self.swap(0, self.size - 1)
		self.size = self.size-1
		self.elements.pop(self.size)
		self.heapifyDown(0)
	
	def hasNext(self):
		return not self.isEmpty()
	

	def next(self):
		first = self.peek()
		self.removeFirst()
		return first
	
	def peek(self):
		if self.size > 0:
			return self.elements[0]
		else:
			return None
	
	def getPriority(self):
		if (self.size > 0):
			return self.priorities[0]
		else:
			return -1
	
	def isEmpty(self):
		return (self.size == 0)
	
	def add(self,key, priority):
		size = self.size
		if (self.size == self.capacity): 
			index = self.getFringeIndex(self.capacity-1)
			if(self.priorities[index] < priority):
				self.elements.pop(index)
				self.elements.append(key)
				self.priorities[index] = priority
				self.heapifyUp(index)
			
		else:
			self.elements.append(key)
			self.priorities[size] = priority
			self.heapifyUp(size)
			self.size = self.size+1
		
		return True
	

	def getFringeIndex(self, i):
		minIndex=-1;
		parent = self.parent(i)
		if(self.priorities[self.leftChild(parent)] < self.priorities[self.rightChild(parent)]):
			minIndex = self.leftChild(parent)
		else:
			minIndex = self.rightChild(parent)
		
		if(parent%2 == 0):
			parent = parent+1
		else:
			parent = parent-1
		if(self.priorities[self.leftChild(parent)] < self.priorities[self.rightChild(parent)]):
			minIndex = self.leftChild(parent)
		else:
			minIndex = self.rightChild(parent);
		
		return minIndex
	

	def toString(self, maxKeysToPrint):
		pq = self.clone()
		sb = "["
		numKeysPrinted = 0
		while (numKeysPrinted < maxKeysToPrint and pq.hasNext()):
			priority = pq.getPriority()
			element = pq.next()
			sb+=str(element)
			sb+=" : "
			sb+=str(priority)
			if (numKeysPrinted < self.size - 1):
				sb+=", "
			numKeysPrinted = numKeysPrinted+1
		
		if (numKeysPrinted < self.size):
			sb+="..."
		sb+="]"
		return sb
	
	def clone(self):
		clonePQ = SpecialPQ()
		clonePQ.size = self.size
		clonePQ.capacity = self.capacity
		clonePQ.elements = list(self.elements)
		clonePQ.priorities = []
		for i in range(clonePQ.capacity):
			clonePQ.priorities.append(0)
		if (self.size > 0):
			for i in range(self.size):
				clonePQ.priorities[i] = self.priorities[i]
			
		return clonePQ
	
	
	def getLegalCapacity(self,capacity):
		legalCapacity = 0
		while (legalCapacity < capacity):
			legalCapacity = 2 * legalCapacity + 1
		
		return legalCapacity
	

	def isPowerOfTwo(self, num):
		while(num > 1):
			if(num %  2 != 0):
				return False
			num /= 2
		
		return True
	

	def trim(self, newsize):
		if(newsize >= self.size):
			return

		if(not self.isPowerOfTwo(newsize+1)):
			print("size must be of form (2^n)-1")
			
		self.capacity = newsize;

		newelems = []
		newpriorities = []

		for i in range(newsize):
			pri = self.getPriority()
			elem = self.next()
			newelems.append(elem)
			newpriorities.append(pri)		

		self.elements = newelems
		self.priorities = newpriorities
		self.capacity = newsize
		self.size = newsize





###############################################################################################################################################

#Start Function

class Start:
	
	@staticmethod
	def main():
		if len(sys.argv)!=2:
			Start.usage()
			sys.exit(-1)

		in_time = int(round(time.time() * 1000))
		print("In Time: "+str(in_time))
		testDataSet = DataSet(sys.argv[1])
		testDataSet.calculateImportanceScores(Start.getWeights())
		print("DataSet Initialized")       
		print("Start:main:: Running stack decoder ..")
	   
		
		for t in testDataSet.getTopics():
			sd = StackDecoder(t.getDocuments())
			sd.runStackDecoder()
			path = "/home/shivankit/Desktop/IR_Stack_decoder/summaries/" + str(testDataSet.getTopicName(t.gettopic_id_no()).upper())+".sum"
			sd.dumpBestSummary(path)
		


		out_time = int(round(time.time() * 1000))
		print(out_time)
		print ("Start:main:: Time taken by Stack decoder (s): " + str((out_time-in_time)/1000))
			


	@staticmethod
	def usage():
		print ("Usage: python <main> <path to data>")
		print ("Note: 'data' folder contains the sample input files.")
	

	@staticmethod
	#Note: Set theta_0 in importance module
	#TFIDFSum,SentLength,SentPost,NumLiteralsCalculator,UpperCaseCalculator
	def getWeights():
		res = []
		res.append(0.197971)
		res.append(0.283136)
		res.append(-0.300287)
		res.append(0.1664)
		res.append(0.160681)

		#Semantic Features
		res.append(0.160681)
		res.append(-0.160681)
		res.append(-0.160681)
		return res


###############################################################################################################################################

#Main Function

if __name__ == "__main__": 
	Start.main()
















