# import necessary libraries
import pandas as pd, os
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB

os.chdir(os.path.dirname(__file__))
data = pd.read_csv('p-tennis.csv')
print("The first 5 Values of data is :\n", data.head())

X = data.iloc[:, :-1]
y = data.iloc[:, -1]

encoder = LabelEncoder()
X.Outlook = encoder.fit_transform(X.Outlook)
X.Temperature = encoder.fit_transform(X.Temperature)
X.Humidity = encoder.fit_transform(X.Humidity)
X.Windy = encoder.fit_transform(X.Windy)
print("\nNow the Train input is\n", X.head())

y = encoder.fit_transform(y)
print("\nNow the Train output is\n", y)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

classifier = GaussianNB()
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)

from sklearn.metrics import accuracy_score

print("Accuracy is:", accuracy_score(y_test, y_pred))