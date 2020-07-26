"""
Crypto Market Ticker
"""
import requests

# import Kivy Specific Modules
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import DictProperty
from kivy.clock import Clock
from kivy.core.window import Window
Window.size = (420, 200)

# API url to get data from ( see https://messari.io/api for more details )
API_URL = "https://data.messari.io/api/v1/assets/bitcoin/metrics"

# Data request interval in seconds
UPDATE_DATA = 120

# Time to show each currency in seconds
DISPLAY_CURRENCY = 10

class BtcWidget(Widget):
    """
    Display current BTC market conditions
    """
    crypto_dict = DictProperty(
        {
            'name': '',
            'price': '',
            'change': '',
            'volume': ''
        }
    )

    market_data = {}
    current_key = 0
    crypto_logo = {'src': ''}

    def get_price(self, dt=False):
        """
        Poll the API endpoint for market data
        """
        request = requests.get(API_URL)
        self.market_data = request.json()

    def format_data(self, dt=False):
        """
        Format API data for presentation in the widget
        """
        currency_dets = self.market_data['data']

        if float(currency_dets['market_data']['price_usd']) > 1:
            crypto_price = round(float(currency_dets['market_data']['price_usd']), 2)
        else:
            crypto_price = round(float(currency_dets['market_data']['price_usd']), 4)

        self.crypto_logo.source = './logos/' + currency_dets['symbol'] + '.png'
        self.crypto_dict['name'] = currency_dets['name']
        self.crypto_dict['price'] = '$' + str(crypto_price) + ' USD'

        if float(currency_dets['market_data']['percent_change_usd_last_24_hours']) > 0:
            price_change = '[color=18ff06]'+\
                            str(currency_dets['market_data']['percent_change_usd_last_24_hours'])+\
                            '[/color]'
        else:
            price_change = '[color=fd1e22]' +\
                            str(currency_dets['market_data']['percent_change_usd_last_24_hours'])+\
                            '[/color]'

        self.crypto_dict['change'] = '24h Price Change: ' + price_change + '%'

        currency_vol = round(float(currency_dets['market_data']['real_volume_last_24_hours']))
        self.crypto_dict['volume'] = '24 Hour Volume: $' + str(currency_vol) + ' USD'

        if self.current_key < 4:
            self.current_key += 1
        else:
            self.current_key = 0


class BtcApp(App):
    """
    Create widget and display market data

    @param object
    """
    def build(self):
        self.title = 'Crypto Market Data'
        btc_widget_obj = BtcWidget()

        # Get the market data
        btc_widget_obj.get_price()

        # Format and display the data in widget
        btc_widget_obj.format_data()

        # Set clock events to periodically get fresh market data and change the currency shown
        Clock.schedule_interval(btc_widget_obj.format_data, DISPLAY_CURRENCY)
        Clock.schedule_interval(btc_widget_obj.get_price, UPDATE_DATA)

        return btc_widget_obj

if __name__ == '__main__':
    BtcApp().run()
