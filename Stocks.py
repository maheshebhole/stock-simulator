
import requests
import json

class Stocks(object):

    def __init__(self):
        self.base_url = "https://cloud.iexapis.com/stable"

        # Token for accessing the API
        self.token = "pk_f2cc1a067d7245679c5aeb34770b9357"

    def get_stock_open_price(self, stock_symbol, date):
        """
        This function will take stock symbol as input and date.
        It will return the price of stock at the time of opening of market on input date

        :param stock: string
        :param date: string
        :return: float
        """
        get_url = "/stock/"+stock_symbol+"/chart/date/" + date + "/"

        url = self.base_url + get_url + "?token=" + self.token

        req = requests.get(url)
        data_store = req.json()

        return data_store[0]["open"]

    def get_stock_close_price(self, stock_symbol, date):
        """
        This function will take stock symbol as input and date.
        It will return the price at the time of closing of market on input date

        :param stock: string
        :param date: string
        :return: float
        """
        get_url = "/stock/"+stock_symbol+"/chart/date/" + date + "/"

        url = self.base_url + get_url + "?token=" + self.token

        req = requests.get(url)
        data_store = req.json()

        return data_store[-1]["close"]

