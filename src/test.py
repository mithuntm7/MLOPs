import pandas as pd
import pickle 
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn import datasets
import pandas as pd
import json


iris = datasets.load_iris()
df = pd.DataFrame(data=iris.data, columns = ['sepal_length', 'sepal_width', 'petal_length', 'peta_width'] )
df['label'] = iris.target
df = df [120:]

filename = "models/saved_model"

RF_model = pickle.load(open(filename, 'rb'))
y_pred = RF_model.predict(df[['sepal_length', 'sepal_width', 'petal_length', 'peta_width']])
acc = accuracy_score(df['label'], y_pred)

print("Accuracy : ",acc)

with open("reports/test_metrics.txt", 'w') as outfile:
    outfile.write("Test Accuracy : %2.3f " % acc)

with open("reports/test_metrics.json", 'w') as outfile:
    json.dump({"test accuracy": acc, "test datapoints" : df.shape[0]}, outfile)





