# BTC Widget

import json;
import requests;
from datetime import datetime

# import Kivy Specific Modules
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import DictProperty
from kivy.clock import Clock
from kivy.core.window import Window
Window.size = (420, 200)

# API url to get data from ( see https://dirtprotocol.github.io/openmarketcap-api/ for more details )
apiUrl = 'http://api.openmarketcap.com/api/v1/tokens?size=5'

# Data request interval in seconds
updateData = 120

# Time to show each currency in seconds
displayCurrency = 10

class BtcWidget(Widget):
    cryptoDict = DictProperty(
       {
           'name': '',
           'price': '',
           'change': '',
           'volume': ''
       }
    )
    
    marketData = {}
    currentKey = 0
            
    def getPrice(self, dt=False):
        
        request = requests.get( apiUrl )
        self.marketData = request.json()
    
    def formatData(self, dt=False):
        currencyDets = self.marketData['data'][self.currentKey]

        if float(currencyDets['price_usd']) > 1:
            cryptoPrice = round(float(currencyDets['price_usd']),2)
        else:
            cryptoPrice = round(float(currencyDets['price_usd']), 4)
        
        self.cryptoLogo.source = './logos/' + currencyDets['symbol'] + '.png'
        self.cryptoDict['name'] = currencyDets['name']
        self.cryptoDict['price'] = '$' + str(cryptoPrice) + ' USD'
        
        if float( currencyDets['price_change'] ) > 0:
            priceChange = '[color=18ff06]' + str( currencyDets['price_change'] ) + '[/color]'
        else:
            priceChange = '[color=fd1e22]' + str( currencyDets['price_change'] ) + '[/color]'
            
        self.cryptoDict['change'] = '24h Price Change: ' + priceChange + '%'
        
        currencyVol = round( float(currencyDets['volume_usd']) )
        self.cryptoDict['volume'] = '24 Hour Volume: $' + str( currencyVol ) + ' USD'
        
        if self.currentKey < 4:
            self.currentKey += 1
        else:
            self.currentKey = 0
        

class BtcApp(App):
    
    def build(self):
        self.title = 'Crypto Market Data'
        btcWidget = BtcWidget()
        
        # Get the market data
        btcWidget.getPrice();
        
        # Format and display the data in widget
        btcWidget.formatData();

        # Set clock events to periodically get fresh market data and change the currency shown
        Clock.schedule_interval(btcWidget.formatData, displayCurrency)        
        Clock.schedule_interval(btcWidget.getPrice, updateData)

        return btcWidget


if __name__ == '__main__':
    BtcApp().run()
