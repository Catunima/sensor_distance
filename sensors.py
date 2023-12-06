import numpy as np
from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import StandardScaler
from joblib import dump
X = np.array([[0.23,10.0],[20,5],[40,2],[20,50],[50,10],[10,50],[65,20],[20,65],
              [75,30],[30,75],[40,250]])
y = np.array([[1],[0],[0],[1],[0],[1],[0],[1],[0],[1],[1]])

X = np.tile(X, (2,1))
y = np.tile(y, (2,1))

noise = np.random.normal(0,0.1, X.shape)
X = X + noise
synthetic_data = np.random.rand(3, 2)  # Genera 3 filas, 2 columnas de valores entre 0 y 1
X_extended = np.vstack([X, synthetic_data])
y_extended = np.vstack([y, np.ones((synthetic_data.shape[0], 1))])

synthetic_data = np.random.rand(3, 2)  # Genera 3 filas, 2 columnas de valores entre 0 y 1
X = np.vstack([X, synthetic_data])
y = np.vstack([y, np.ones((synthetic_data.shape[0], 1))])

clf = CategoricalNB(force_alpha=True)
clf.fit(X,y)

row_to_predict = X[0, :]
test = [[5,50]]
row_to_predict = row_to_predict.reshape(1, -1)

prediction = clf.predict(test)

dump(clf,'direction.joblib')
print(test)
print("Prediccion: ", prediction)