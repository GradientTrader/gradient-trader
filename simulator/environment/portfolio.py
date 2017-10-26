import pandas as pd 
import numpy as np


class Portfolio:
    def __init__(self, portfolio_cash=1000.0, coin=None):
        self.starting_cash = portfolio_cash
        self.coin = coin # note this is a coin obj
        self.portfolio_coin = 0
        self.portfolio_cash = portfolio_cash
        self.latest_coin_value = self.coin.getCurrentValue()

    def getCurrentValue(self):
        return self.portfolio_coin * self.coin.getCurrentValue() + self.portfolio_cash

    def getReturnsPercent(self):
        return 100 * (self.getCurrentValue() - self.starting_cash) / self.starting_cash

    def getCurrentHoldings(self):
        return "%.2f coins, %.2f cash, %.2f current value, %.2f percent returns" % (self.portfolio_coin, self.portfolio_cash, self.getCurrentValue(), self.getReturnsPercent())

    def buy(self, coins_to_buy=0):
        current_price = self.coin.getCurrentValue()
        if not current_price:
            return 0
        amount_to_buy = min(self.portfolio_cash / current_price, coins_to_buy)
        self.portfolio_coin += amount_to_buy
        self.portfolio_cash -= amount_to_buy * current_price
        return amount_to_buy
    
    def sell(self, coins_to_sell=0):
        current_price = self.coin.getCurrentValue()
        if not current_price:
            return 0
        coin_to_sell = min(coins_to_sell, self.portfolio_coin)
        self.portfolio_coin -= coin_to_sell
        self.portfolio_cash += coin_to_sell * current_price
        return coin_to_sell
        
        coin_to_buy = min(self.portfolio_cash / current_price, coins_to_buy)
        self.portfolio_coin += coin_to_buy
        self.portfolio_cash -= coin_to_buy * current_price
        return coin_to_buy
