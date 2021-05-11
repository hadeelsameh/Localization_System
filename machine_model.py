import sklearn
from pandas import read_csv
import numpy 
import pandas
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
import urllib.request
import re
url=r"C:\Users\Hadeel\Desktop\local.csv"
dataset=read_csv(url)
array = dataset.values
X = array[:,0:4]
y = array[:,4]
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.20, random_state=5)
model = KNeighborsClassifier(n_neighbors=7)
model.fit(X_train, Y_train)
predictions = model.predict(X_test)
pred_arr=[]
for pred in predictions:
    pred_arr.append(pred)
print(pred_arr)
print(sklearn.metrics.accuracy_score(Y_test, pred_arr,normalize=True, sample_weight=None))
import threading
def predict():
    data=urllib.request.urlopen("https://api.thingspeak.com/channels/1199190/feeds.json?results=2")
    select=repr(data.read())
    select=select[450:]
    pick_data1=re.search(',"field1":"(.+?)"' ,select)
    pick_data1=int(pick_data1.group(1))
    #print(pick_data1)
    pick_data2=re.search(',"field2":"(.+?)"' ,select)
    pick_data2=int(pick_data2.group(1))
    #print(pick_data2)
    pick_data3=re.search(',"field3":"(.+?)"' ,select)
    pick_data3=int(pick_data3.group(1))
    #print(pick_data3)
    pick_data4=re.search(',"field4":"(.+?)"' ,select)
    pick_data4=pick_data4.group(1)
    pick_data4=int(re.findall(r'[0-9$]+\d*', pick_data4)[0])
    #print(pick_data4)
    y=[]
    y.append(pick_data1)
    y.append(pick_data2)
    y.append(pick_data3)
    y.append(pick_data4)
    y=[y]
    print(y)
    t=int(model.predict(y))
    print(t)
    data=urllib.request.urlopen("https://api.thingspeak.com/update?api_key=2M89LD7OYM59EIP3&field1=0"+str(t))
    threading.Timer(1, predict).start()

predict()


