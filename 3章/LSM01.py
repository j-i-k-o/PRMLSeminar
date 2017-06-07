import numpy as np
import matplotlib.pyplot as plt

#パラメータの真の値
A=0.5
B=0.2

#データサンプリング
X=np.arange(0,10,0.2)
t=np.array([A*u+B+0.1*np.random.randn()+(np.random.randint(30)==0)*np.random.rand()*100 for u in X])

#基底関数の設定
def phi(x):
    return [1,x]

PHI=np.array([phi(x) for x in X])

w=np.linalg.solve(np.dot(PHI.T,PHI),np.dot(PHI.T,t))

def f(w, x):
    return np.dot(w, phi(x))

#プロット
xlist=np.arange(0,10,0.01)
ylist=[f(w, x) for x in xlist]
plt.plot(xlist,ylist)
plt.plot(X,t,'o')
plt.show()
'''
Created on 2017/04/15

@author: yuki
'''
