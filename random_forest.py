import pandas  as pd
import matplotlib.pyplot  as plt
from sklearn.ensemble  import RandomForestClassifier
df=pd.read_csv('social.csv')
df.head()
# features and label
f=df.iloc[:,:-1].values
l=df.iloc[:,-1].values
#ploting graph
plt.scatter(f[:,2],f[:,1])
plt.xlim(1,100)
from sklearn.model_selection import train_test_split
train_x,test_x,train_y,test_y=train_test_split(f[:,2:4],l)
# features scalling 
from sklearn.preprocessing  import StandardScaler
std=StandardScaler()
strainx=std.fit_transform(train_x)
stestx=std.transform(test_x)
clf=RandomForestClassifier(n_estimators=40,criterion='entropy')
trained=clf.fit(strainx,train_y)
result=trained.predict(stestx)
result
from  sklearn.metrics import accuracy_score
accuracy_score(test_y,result)
