"""
python test_free.py my-api-key
"""

import ondemand
import sys

od = ondemand.OnDemandClient(api_key=sys.argv[1], end_point='https://marketdata.websol.barchart.com/', format='csv')
od.debug = True

# Get a Quote
resp = od.quote('AAPL', 'bid,ask')
print('')
print(resp)
print('')

for q in resp['results']:
    print('Symbol: %s, Last Price: %s' % (q['symbol'], q['lastPrice']))

# Get Historical Data
resp = od.history('AAPL', historical_type='daily')
print('')
print('getHistory', resp)
print('')
