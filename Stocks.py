
import requests


class Stocks(object):

    def __init__(self):
        self.base_url = "https://cloud.iexapis.com/stable"

        # Token for accessing the API
        self.token = "pk_f2cc1a067d7245679c5aeb34770b9357"

    def get_stock_price(self, stock_symbol, date):
        """
        This function will take stock symbol as input and date.
        It will return the price of stock on input date

        :param stock: string
        :param date: string
        :return: float
        """
        get_url = "/stock/"+stock_symbol+"/chart/date/" + date + "/"

        url = self.base_url + get_url + "?token=" + self.token
        req = requests.get(url)
        htmldata = req.text

        return htmldata

