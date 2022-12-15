from tradingview_ta import TA_Handler, Interval, Exchange

class DecisionMaking:

    def __init__(self):
        print("initialize decision making ...")
        adro = TA_Handler(
            symbol="ADRO",
            screener="indonesia",
            exchange="IDX",
            interval=Interval.INTERVAL_15_MINUTES,
            # proxies={'http': 'http://example.com:8080'} # Uncomment to enable proxy (replace the URL).
        )
        btc = TA_Handler(
            symbol="BTCUSDTPERP",
            screener="crypto",
            exchange="BINANCE",
            interval=Interval.INTERVAL_15_MINUTES,
            # proxies={'http': 'http://example.com:8080'} # Uncomment to enable proxy (replace the URL).
        )
        data_ta_adro = adro.get_analysis().indicators["RSI"]
        data_ta_btc = btc.get_analysis().indicators ["RSI"]
        self.data = {"bitcoin":data_ta_btc,"adro":data_ta_adro}
        

    def getData(self):
        return self.data

    def decide(self):
        data = self.getData()

    def calculatePossibility():
        print("Calculating possibilities")

    def __str__(self):
        return f"Return Data : {self.data}"
