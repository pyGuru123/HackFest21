import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# insert dataset of your own; it can be a link, or can be uploaded from your machine
# taken iris dataset 
link = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

# loading the dataset into Pandas library DataFrame
dataframe = pd.read_csv(link, names=['sepal length','sepal width','petal length','petal width','target'])

# defining features you need to add for the execution of the algorithm
features = ['sepal length', 'sepal width', 'petal length', 'petal width']
x = dataframe.loc[:,features]
y = dataframe.loc[:,'target']

# standardization of features
x = StandardScaler().fit_transform(x)

from sklearn.decomposition import PCA
p= PCA(n_components=2)
p_transform = p.fit_transform(x)
principal = pd.DataFrame(p_transform,columns=['pc1','pc2'])
final= pd.concat([principal,dataframe[['target']]],axis=1)