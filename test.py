"""
python test.py my-api-key
"""

import ondemand
import sys

od = ondemand.OnDemandClient(api_key=sys.argv[1])
od.debug = True

# Get a Quote
resp = od.quote('AAPL', 'bid,ask')
print('')
print(resp)
print('')

for q in resp['results']:
    print('Symbol: %s, Last Price: %s' % (q['symbol'], q['lastPrice']))

# Get Historical Data
resp = od.history('AAPL', 'minutes', maxRecords=50, interval=1)
# print('')
# print('getHistory', resp)
# print('')

resp = od.profile('AAPL', fields='qtrOneEarnings,qtrTwoEarnings')
print('')
print('getProfile', resp)
print('')

resp = od.financial_highlights('AAPL', fields='lastQtrEPS')
print('')
print('getFinancialHighlights', resp)
print('')

resp = od.financial_ratios('AAPL')
print('')
print('getFinancialRatios', resp)
print('')

resp = od.income_statements('AAPL', 'Quarter', rawData=1)
print('')
print('getIncomeStatements', resp)

resp = od.competitors('AAPL', fields='fiftyTwoWkLowDate', maxRecords=1)
print('')
print('getCompetitors', resp)
print('')

resp = od.ratings('AAPL', 'strongBuy')
print('')
print('getRatings', resp)
print('')

resp = od.index_members('$SPX')
print('')
print('getIndexMembers', resp)
print('')

resp = od.cash_flow('AAPL,GOOG', reportPeriod='12M', numberOfYears=2)
print('')
print('getCashFlow', resp)
print('')

# resp = od.futures_options('ES')
# print('')
# print('getFuturesOptions', resp)
# print('')

# resp = od.equity_options('AAPL', optionType='Monthly')
# print('')
# print('getEquityOptions', resp)
# print('')

resp = od.usda_grain_prices(commodityTypes='SWW')
print('')
print('getUSDAGrainPrices', resp)
print('')

resp = od.chart('AAPL', height=400, width=400, type='LINE')
print('')
print('getChart', resp)
print('')

resp = od.get('getQuote', symbols='AAPL,EXC', fields='bid,ask')
print('')
print('generic get', resp)
print('')

resp = od.insiders('AAPL', 'H')
print('')
print('getInsiders', resp)
