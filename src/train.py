import pandas as pd
import pickle 
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn import datasets
import pandas as pd
import json

filename = "models/saved_model"

iris = datasets.load_iris()
df = pd.DataFrame(data=iris.data, columns = ['sepal_length', 'sepal_width', 'petal_length', 'peta_width'] )
df['label'] = iris.target
df = df [:120]

RF_model = RandomForestClassifier(n_estimators=10, max_depth = 5)
RF_model.fit(df[['sepal_length', 'sepal_width', 'petal_length', 'peta_width']], df['label'])
y_pred = RF_model.predict(df[['sepal_length', 'sepal_width', 'petal_length', 'peta_width']])
acc = accuracy_score(df['label'], y_pred)

print("Accuracy : ", acc)
pickle.dump(RF_model, open(filename, 'wb'))

with open("reports/train_metrics.txt", 'w') as outfile:
    outfile.write("Training Accuracy : %2.3f" % acc)

with open("reports/train_metrics.json", 'w') as outfile:
    json.dump({"train accuracy": acc, "train datapoints" : df.shape[0] }, outfile)
