## Crypto Market Desktop Ticker

Simple desktop ticker built with [Kivy](https://kivy.org/) and [Python](https://www.python.org/) to display the market price of the top 5 cryptocurrencies. 

### Screenshots

![BTC Price](/screenshots/btc.png?raw=true "Bitcoin")

![ETH Price](/screenshots/eth.png?raw=true "Ethereum")

### Usage 

Install the requirements with PIP

_cd src/_

_pip3 install -r requirements.txt_

Then simply run using Python3

_python3 btc.py_

If you would like toiio compile to a single binary:

__pip3 install pyinstaller__

__pyinstaller --distpath=../dist --onefile btc.py__

This will generate a single executable bundle in a dist folder at the root of the project.

### Data Sources

* Price data is sourced from the [openmarketcap API](https://dirtprotocol.github.io/openmarketcap-api/).

### Licence

Copyright (C) 2019 [Anthony Mills](http://www.anthony-mills.com)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.