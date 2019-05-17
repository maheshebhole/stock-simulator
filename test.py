from Stocks import Stocks

s = Stocks()

price = s.get_stock_price("aapl", "20190416")

print("Price = ", price)

p = s.get_stock_price("fb", "20190416")
print("fb price = ", p)