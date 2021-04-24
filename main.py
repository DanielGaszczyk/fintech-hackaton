from enum import Enum
from config import app, api
from resources import UserLogin, UserRegister, StockData, \
    FunctionVad, FunctionVarNormal, FunctionVarLog, FunctionSimulateStock

class Function(Enum):
    TIME_SERIES_INTRADAY = "TIME_SERIES_INTRADAY"
    TIME_SERIES_INTRADAY_EXTENDED = "TIME_SERIES_INTRADAY_EXTENDED"
    TIME_SERIES_DAILY = "TIME_SERIES_DAILY"
    TIME_SERIES_DAILY_ADJUSTED = "TIME_SERIES_DAILY_ADJUSTED"
    TIME_SERIES_WEEKLY = "TIME_SERIES_WEEKLY"
    TIME_SERIES_WEEKLY_ADJUSTED = "TIME_SERIES_WEEKLY_ADJUSTED"
    TIME_SERIES_MONTHLY = "TIME_SERIES_MONTHLY"
    TIME_SERIES_MONTHLY_ADJUSTED = "TIME_SERIES_MONTHLY_ADJUSTED"
    SYMBOL_SEARCH = "SYMBOL_SEARCH"
    OVERVIEW = "OVERVIEW"
    INCOME_STATEMENT = "INCOME_STATEMENT"
    BALANCE_SHEET = "BALANCE_SHEET"
    CASH_FLOW = "CASH_FLOW"
    LISTING_STATUS = "LISTING_STATUS"


class Symbol(Enum):
    IBM = "IBM"
    TSCO_LON = "TSCO.LON"
    SHOP_TRT = "SHOP.TRT"
    GPV_TRT = "GPV.TRT"
    DAI_DEX = "DAI.DEX"
    RELIANCE_BSE = "RELIANCE.BSE"
    SHH = "600104.SHH"
    SHZ = "000002.SHZ"
    USDEUR = "USDEUR"


class Interval(Enum):
    FIVE_MIN = "5min"
    FIFTEEN_MIN = "15min"


class OutputSize(Enum):
    FULL = "full"


class SeriesType(Enum):
    OPEN = "open"
    HIGH = "high"
    LOW = "low"
    CLOSE = "close"


class AlphaVantageEndpoint:
    base_link = 'https://www.alphavantage.co/query?'
    api_key = 'KFP41NJRNFC6AR1S'
    function = Function.TIME_SERIES_INTRADAY
    symbol = Symbol.IBM
    interval = Interval.FIVE_MIN
    output_size = OutputSize.FULL
    keywords = ""
    time_period = ""
    series_type = SeriesType.OPEN

    def __init__(self, function=Function.TIME_SERIES_INTRADAY, symbol=Symbol.IBM,
                 interval=Interval.FIVE_MIN, output_size=OutputSize.FULL,
                 keywords="", time_period="10", series_type=SeriesType.OPEN):
        self.function = function
        self.symbol = symbol
        self.interval = interval
        self.output_size = output_size
        self.keywords = keywords
        self.time_period = time_period
        self.series_type = series_type

    def add_function_to_link(self):
        self.base_link += 'function=' + self.function.value + '&'
        return self

    def add_symbol_to_link(self):
        self.base_link += 'symbol=' + self.symbol.value + '&'
        return self

    def add_interval_to_link(self):
        self.base_link += 'interval=' + self.interval.value + '&'
        return self

    def add_output_size(self):
        self.base_link += 'outputsize=' + self.output_size.value + '&'
        return self

    def add_keywords(self):
        self.base_link += 'keywords=' + self.keywords + '&'
        return self

    def add_time_period(self):
        self.base_link += 'time_period=' + self.time_period + '&'
        return self

    def add_series_type(self):
        self.series_type += 'series_type=' + self.series_type.value + '&'
        return self

    def get_link(self):
        return self.base_link + 'apikey=' + self.api_key


api.add_resource(UserLogin, '/login')
api.add_resource(UserRegister, '/register')
api.add_resource(StockData, '/stockdata')
api.add_resource(FunctionVarLog, '/varlog')
api.add_resource(FunctionVarNormal, '/varnormal')
api.add_resource(FunctionVad, '/vad')
api.add_resource(FunctionSimulateStock, '/simulatestock')

if __name__ == '__main__':
    # endpoint = AlphaVantageEndpoint(keywords="FAA", time_period="50")
    # endpoint = endpoint.add_function_to_link().add_symbol_to_link().add_output_size().add_interval_to_link().get_link()
    # response = json.loads(urllib.request.urlopen(endpoint).read().decode("utf-8").replace("'", '"'))
    # print(response)
    app.run()



