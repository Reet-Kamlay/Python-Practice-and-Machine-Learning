from sklearn import datasets
import numpy as np
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

cancer=datasets.load_iris()
print(cancer['data'])
print(cancer['target'])
print(cancer['DESCR'])

X=cancer['data'][:,3:]
y=(cancer['target']==2).astype(np.int64)

clf=LogisticRegression()
clf.fit(X,y)


X_new=np.linspace(0,3,1000).reshape(-1,1)
Y_new=clf.predict_proba(X_new)
plt.plot(X_new,Y_new[:,1],'g-',label="virginica")
plt.show()