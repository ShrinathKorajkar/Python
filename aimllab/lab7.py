from sklearn import datasets
from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.mixture import GaussianMixture

iris = datasets.load_iris()
print(iris.feature_names)
print(iris.target_names)

#------------K Means Clustering---------------
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target)
model = KMeans(n_clusters=3)
model.fit(X_train, y_train)
model.score
print('K-Mean: ', metrics.accuracy_score(y_test, model.predict(X_test)))

#-------Expectation and Maximization----------
model2 = GaussianMixture(n_components=3)
model2.fit(X_train, y_train)
model2.score
print('EM Algorithm:', metrics.accuracy_score(y_test, model2.predict(X_test)))
