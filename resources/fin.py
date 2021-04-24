import numpy as np
from scipy.stats import norm, lognorm
from flask_restful import reqparse, Resource


def ri_fa(col):
    def ri(Pt, Ptm):
        return np.log(Pt / Ptm)

    return [ri(col[t], col[t + 1]) for t, x in enumerate(col[0:len(col) - 1])]


# returns of stock
def ret(AT_CLOSE):
    return [ri_fa(x) for x in AT_CLOSE.values.transpose()]


# mean return
def mean_ret(ret):
    return [np.mean(x) for x in ret]


# sigma of stocks
def sigma_of_stocks(proportion, var_cov):
    return np.sqrt(np.matmul(np.matmul(proportion.transpose(), var_cov), proportion))


# mean of stocks
def mean_of_stocks(proportion, mean):
    return np.matmul(np.array(mean).transpose(), proportion)


# matrix of excess returns
def mer(mean_ret, returns):
    return np.asarray([[x - i for x in returns[t]] for t, i in enumerate(mean_ret)])


# variance covariance matrix
def vcm(A, ret):
    return np.matmul(A, A.transpose()) / len(ret[1])


# correlation matrix
def corrmat(A):
    return np.corrcoef(A)


# normall distribution
def norm_ret(initial, mean, sigma, size=100000):
    return np.random.normal((1 + mean) * initial, sigma * initial, size)


# The probability that the end-of-year portfolio value is less than X is about value_percent%
def value_percent(normal_dist, value):
    return len([x for x in normal_dist if x < value]) / len(normal_dist) * 100


# Value at risk 

# VaR at p% normal
def var_normal(p, initial, mean, sigma):
    return initial - norm.ppf(p, loc=(1 + mean) * initial, scale=sigma * initial)


# VaR at p% normal
def var_lognormal(p, initial, mean, sigma, time=1):
    return initial - lognorm.ppf(p, sigma * np.sqrt(time), loc=0,
                                 scale=np.exp(np.log(initial) + (mean - (sigma ** 2) / 2) * time))


# Future value with annual deposits
def fvad(c0, r, t):
    return (c0 * (1 - (1 + r) ** (t + 1)) / (1 - (1 + r)) - c0)


# Stock simulation
def sim(S0, sigma, mu, time0):
    return S0 * np.exp(mu * time0 + sigma * np.random.normal(0, 1) * np.sqrt(time0))


def simulate_stock(S0, sigma, mu, time0):
    x = [S0]
    for i in range(time0 - 1):
        x.append(sim(x[i], sigma, mu, (1 / time0)))
    return x[1:]


simulate_stock_parser = reqparse.RequestParser()
simulate_stock_parser.add_argument(
    's0',
    required=False,
    location='json',
    type=float
)
simulate_stock_parser.add_argument(
    'sigma',
    required=False,
    location='json',
    type=float
)
simulate_stock_parser.add_argument(
    'mu',
    required=False,
    location='json',
    type=float
)
simulate_stock_parser.add_argument(
    'time',
    required=False,
    location='json',
    type=int
)
simulate_stock_parser.add_argument(
    'p',
    required=False,
    location='json',
    type=float
)
simulate_stock_parser.add_argument(
    'initial',
    required=False,
    location='json',
    type=float
)
simulate_stock_parser.add_argument(
    'c0',
    required=False,
    location='json',
    type=float
)
simulate_stock_parser.add_argument(
    'r',
    required=False,
    location='json',
    type=float
)


class FunctionSimulateStock(Resource):
    def post(self):
        data = simulate_stock_parser.parse_args()
        result = simulate_stock(data.s0, data.sigma, data.mu, data.time)
        return {'value': result}, 200


class FunctionVad(Resource):
    def post(self):
        data = simulate_stock_parser.parse_args()
        result = fvad(data.c0, data.r, data.time)
        return {'value': result}, 200


class FunctionVarNormal(Resource):
    def post(self):
        data = simulate_stock_parser.parse_args()
        result = var_normal(data.p, data.initial, data.mu, data.sigma)
        return {'value': result}, 200


class FunctionVarLog(Resource):
    def post(self):
        data = simulate_stock_parser.parse_args()
        result = var_lognormal(data.p, data.initial, data.mu, data.sigma, data.time)
        return {'value': result}, 200