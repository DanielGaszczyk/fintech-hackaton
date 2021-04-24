import numpy as np
import random
from scipy.stats import norm,lognorm

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


# sigma of stocks
def sigma_of_stocks(proportion, var_cov):
    return np.sqrt(np.matmul(np.matmul(proportion.transpose(), var_cov ), proportion))


# mean of stocks
def mean_of_stocks(proportion, mean):
    return np.matmul(np.array(mean).transpose(), proportion)


# matrix of excess returns
def mer(mean_ret, returns):
    return np.asarray([[x-i for x in returns[t]] for t,i in enumerate(mean_ret)])

# variance covariance matrix
def vcm(A, ret):
    return np.matmul(A, A.transpose())/len(ret[1])

# correlation matrix
def corrmat (A):
    return np.corrcoef(A)

# normall distribution
def norm_ret(initial, mean, sigma, size = 100000):
    return np.random.normal((1+mean)* initial, sigma * initial, size)

# The probability that the end-of-year portfolio value is less than X is about value_percent%
def value_percent (normal_dist, value):
    return len([x for x in normal_dist if x < value])/len(normal_dist) *100


# Value at risk 

# VaR at p% normal
def var_normal(p, initial, mean, sigma):
    return initial - norm.ppf(p, loc=(1+mean)* initial, scale=sigma * initial)

# VaR at p% normal
def var_lognormal(p, initial, mean, sigma, time = 1):
    return initial - lognorm.ppf(p, sigma * np.sqrt(time), loc=0, scale=np.exp(np.log(initial) + (mean - (sigma**2)/2) *time))


# Future value with annual deposits
def fvad (c0 , r, t):
    return(c0 * (1 - (1+r)**(t+1))/ (1  - (1 + r)) - c0)


# Stock simulation
def simulate_stock(S0, sigma, mu, time0):
    return [ S0 * np.exp(mu*x + sigma*np.random.normal(mu, sigma) * np.sqrt(x)) for x in np.linspace(0,time0,time0+1) ]