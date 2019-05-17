from Stocks import Stocks

s = Stocks()


print("AAPL Open Price = ", s.get_stock_open_price("aapl", "20190416"))
print("AAPL Close Price = ", s.get_stock_close_price("aapl", "20190416"))

print("FB Open Price = ", s.get_stock_open_price("fb", "20190416"))
print("FB Close Price = ", s.get_stock_close_price("fb", "20190416"))
