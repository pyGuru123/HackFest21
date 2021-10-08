import argparse
from playsound import playsound
try:
    import gtts
except:
    print("Please install the requirements from requirements.txt file.")
parser = argparse.ArgumentParser()
parser.add_argument('-d','--data',dest="data",help="Input the text to convert to Speech",default="nodatagiven")
parser.add_argument('-f','--file',dest="filename",help='Take input from a file',default="nofilegiven")
parser.add_argument('-o','--output',dest="output",help='Output file name',default="nooutputfile")
args = parser.parse_args()
if args.filename=="nofilegiven" and args.data=="nodatagiven":
    print("Please Give your input as a text or file . See --help message for more info")
data=args.data
filename=args.filename
output=args.output
if data!="nodatagiven" :
    tts = gtts.gTTS(data)
    if output!="nooutputfile" :
        tts.save(output)
        playsound(output)
    else:
        tts.save("output/output.mp3")
        playsound("output/output.mp3")

if filename!="nofilegiven" :
    f = open(filename,"r")
    tts = gtts.gTTS(f.read())
    if output!="nooutputfile" :
        tts.save(output)
        playsound(output)
    else:
        tts.save("output/output1.mp3")
        playsound("output/output1.mp3")







