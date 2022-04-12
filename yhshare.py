#获取股票历史数据
import yfinance as yf

share = "002307.SZ"
fileName = share + '.csv'


data = yf.download(share, period="max")
data.to_csv(fileName)

