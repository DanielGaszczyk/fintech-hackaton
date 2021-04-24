
import numpy as np

def ri_fa (col): 
    def ri (Pt, Ptm):
        return np.log(Pt/Ptm)
    return [ ri (col[t], col[t+1]) for t,x in enumerate(col[0:len(col)-1]) ]
    
# returns of stock
def ret(AT_CLOSE):
     [ri_fa(x) for x in AT_CLOSE.values.transpose()]

# mean return
def mean_ret(ret):
    return [np.mean(x) for x in ret]

# matrix of excess returns
def mer(mean_ret, returns):
    return np.asarray([[x-i for x in returns[t]] for t,i in enumerate(mean_ret)])

# variance covariance matrix
def vcm(A, ret):
    return np.matmul(A, A.transpose())/len(ret[1])

# correlation matrix
def corrmat (A):
    return np.corrcoef(A)

