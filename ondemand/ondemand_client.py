"""
Simple Python client for Barchart OnDemand

https://www.barchartondemand.com/api

"""

import requests


class OnDemandError(RuntimeError):
    pass


class OnDemandClient(object):
    """
        Example usage::

        import ondemand
              
        od = ondemand.OnDemandClient(api_key='CHANGE_ME')
              
        od.debug = True # turn on debug logging
              
        quotes = od.quote('AAPL,NEM')['results']
        print(quotes)
    """

    debug = False

    def __init__(self, api_key=None, end_point='https://ondemand.websol.barchart.com/', debug=False, format='json'):
        self.endpoint = end_point
        self.api_key = api_key
        self.debug = debug
        if format not in ['json', 'csv', 'xml']:
            raise OnDemandError('Invalid format: %s. Supported: json, csv, xml' % format)
        self.format = format
        if self.debug:
            print('Barchart OnDemand Client: ' + self.endpoint)

    def _do_call(self, url, params):
        if not isinstance(params, dict):
            params = dict()

        if self.api_key:
            params['apikey'] = self.api_key

        headers = dict()
        headers['X-OnDemand-Client'] = 'bc_python'

        if self.debug:
            print('do call with params: %s, url: %s' % (params, url))

        resp = requests.get(url, params=params, timeout=60, headers=headers)

        if self.debug:
            print('resp code: %s, resp text: %s' % (resp.status_code, resp.text))

        if resp.status_code != 200:
            raise OnDemandError('Request Failed: %s. Text: %s' % (resp.status_code, resp.text))

        try:
            if self.format == 'json':
                result = resp.json()
            else:
                result = resp.text
        except Exception as e:
            raise OnDemandError(
                'Failed to parse JSON response %s. Resp Code: %s. Text: %s' % (e, resp.status_code, resp.text))
        finally:
            resp.connection.close()

        return result

    def quote(self, symbols, fields=''):
        params = dict(symbols=symbols, fields=fields)
        return self._do_call(self.endpoint + 'getQuote.' + self.format, params)

    def quote_eod(self, symbols, exchange):
        params = dict(symbols=symbols, exchange=exchange)
        return self._do_call(self.endpoint + 'getQuoteEod.' + self.format, params)

    def profile(self, symbols, fields=''):
        params = dict(symbols=symbols, fields=fields)
        return self._do_call(self.endpoint + 'getProfile.' + self.format, params)

    def equities_by_exchange(self, exchange, fields=''):
        params = dict(exchange=exchange, fields=fields)
        return self._do_call(self.endpoint + 'getEquitiesByExchange.' + self.format, params)

    def futures_by_exchange(self, exchange, **kwargs):
        params = dict(exchange=exchange)
        kwargs.update(params)
        return self._do_call(self.endpoint + 'getFuturesByExchange.' + self.format, params)

    def futures_options(self, root, **kwargs):
        params = dict(root=root)
        kwargs.update(params)
        return self._do_call(self.endpoint + 'getFuturesOptions.' + self.format, params)

    def special_options(self, root, **kwargs):
        params = dict(root=root)
        kwargs.update(params)
        return self._do_call(self.endpoint + 'getSpecialOptions.' + self.format, params)

    def equity_options(self, underlying_symbols, **kwargs):
        params = dict(underlying_symbols=underlying_symbols)
        kwargs.update(params)
        return self._do_call(self.endpoint + 'getEquityOptions.' + self.format, params)

    def equity_options_intraday(self, underlying_symbols, **kwargs):
        params = dict(underlying_symbols=underlying_symbols)
        kwargs.update(params)
        return self._do_call(self.endpoint + 'getEquityOptionsIntraday.' + self.format, params)

    def equity_options_history(self, symbol, **kwargs):
        params = dict(symbol=symbol)
        kwargs.update(params)
        return self._do_call(self.endpoint + 'getEquityOptionsHistory.' + self.format, kwargs)

    def forex_forward_curves(self, symbols, **kwargs):
        params = dict(symbols=symbols)
        kwargs.update(params)
        return self._do_call(self.endpoint + 'getForexForwardCurves.' + self.format, kwargs)

    def history(self, symbol, historical_type, **kwargs):
        params = dict(symbol=symbol, type=historical_type)
        kwargs.update(params)
        return self._do_call(self.endpoint + 'getHistory.' + self.format, kwargs)

    def financial_highlights(self, symbols, fields=''):
        params = dict(fields=fields, symbols=symbols)
        return self._do_call(self.endpoint + 'getFinancialHighlights.' + self.format, params)

    def financial_ratios(self, symbols, fields=''):
        params = dict(fields=fields, symbols=symbols)
        return self._do_call(self.endpoint + 'getFinancialRatios.' + self.format, params)

    def cash_flow(self, symbols, **kwargs):
        params = dict(symbols=symbols)
        kwargs.update(params)
        return self._do_call(self.endpoint + 'getCashFlow.' + self.format, kwargs)

    def ratings(self, symbols, fields=''):
        params = dict(fields=fields, symbols=symbols)
        return self._do_call(self.endpoint + 'getRatings.' + self.format, params)

    def index_members(self, symbol, fields=''):
        params = dict(fields=fields, symbol=symbol)
        return self._do_call(self.endpoint + 'getIndexMembers.' + self.format, params)

    def income_statements(self, symbols, frequency, **kwargs):
        params = dict(symbols=symbols, frequency=frequency)
        kwargs.update(params)
        return self._do_call(self.endpoint + 'getIncomeStatements.' + self.format, kwargs)

    def competitors(self, symbol, **kwargs):
        params = dict(symbol=symbol)
        kwargs.update(params)
        return self._do_call(self.endpoint + 'getCompetitors.' + self.format, kwargs)

    def insiders(self, symbol, insider_type, **kwargs):
        params = dict(symbol=symbol, type=insider_type)
        kwargs.update(params)
        return self._do_call(self.endpoint + 'getInsiders.' + self.format, kwargs)

    def balance_sheets(self, symbols, frequency, **kwargs):
        params = dict(symbols=symbols, frequency=frequency)
        kwargs.update(params)
        return self._do_call(self.endpoint + 'getBalanceSheets.' + self.format, kwargs)

    def corporate_actions(self, symbols, **kwargs):
        params = dict(symbols=symbols)
        kwargs.update(params)
        return self._do_call(self.endpoint + 'getCorporateActions.' + self.format, params)

    def earnings_estimates(self, symbols, **kwargs):
        params = dict(symbols=symbols)
        kwargs.update(params)
        return self._do_call(self.endpoint + 'getEarningsEstimates.' + self.format, params)

    def chart(self, symbols, **kwargs):
        params = dict(symbols=symbols)
        kwargs.update(params)
        return self._do_call(self.endpoint + 'getChart.' + self.format, kwargs)

    def technicals(self, symbols, **kwargs):
        params = dict(symbols=symbols)
        kwargs.update(params)
        return self._do_call(self.endpoint + 'getTechnicals.' + self.format, kwargs)

    def leaders(self, asset_type, **kwargs):
        params = dict(assetType=asset_type)
        kwargs.update(params)
        return self._do_call(self.endpoint + 'getLeaders.' + self.format, kwargs)

    def highs_lows(self, asset_type, **kwargs):
        params = dict(assetType=asset_type)
        kwargs.update(params)
        return self._do_call(self.endpoint + 'getHighsLows.' + self.format, kwargs)

    def sectors(self, sector_period, **kwargs):
        params = dict(sectorPeriod=sector_period)
        kwargs.update(params)
        return self._do_call(self.endpoint + 'getSectors.' + self.format, kwargs)

    def news(self, sources, **kwargs):
        params = dict(sources=sources)
        kwargs.update(params)
        return self._do_call(self.endpoint + 'getNews..' + self.format, kwargs)

    def news_sources(self, **kwargs):
        return self._do_call(self.endpoint + 'getNewsSources.' + self.format, kwargs)

    def news_categories(self, **kwargs):
        return self._do_call(self.endpoint + 'getNewsCategories.' + self.format, kwargs)

    def sec_filings(self, symbols, filing_type, **kwargs):
        params = dict(symbols=symbols, filingType=filing_type)
        kwargs.update(params)
        return self._do_call(self.endpoint + 'getSECFilings.' + self.format, kwargs)

    def weather(self, **kwargs):
        return self._do_call(self.endpoint + 'getWeather.' + self.format, kwargs)

    def grain_bids(self, **kwargs):
        return self._do_call(self.endpoint + 'getGrainBids.' + self.format, kwargs)

    def usda_grain_prices(self, **kwargs):
        return self._do_call(self.endpoint + 'getUSDAGrainPrices.' + self.format, kwargs)

    def etf_details(self, symbols, **kwargs):
        kwargs.update(dict(symbols=symbols))
        return self._do_call(self.endpoint + 'getETFDetails.' + self.format, kwargs)

    def etf_constituents(self, symbol, **kwargs):
        kwargs.update(dict(symbol=symbol))
        return self._do_call(self.endpoint + 'getETFConstituents.' + self.format, kwargs)

    def crypto(self, symbols, **kwargs):
        params = dict(symbols=symbols)
        kwargs.update(params)
        return self._do_call(self.endpoint + 'getCrypto.' + self.format, kwargs)


    def get(self, api_name, **kwargs):
        return self._do_call(self.endpoint + api_name + '.' + self.format, kwargs)
