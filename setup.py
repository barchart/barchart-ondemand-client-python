from setuptools import setup

setup(
    name='ondemand',
    version='1.0.0',
    description='Simple client for Barchart OnDemand REST APIs',
    author="Mike Ehrenberg",
    author_email="solutions@barchart.com",
    url='https://www.barchartondemand.com/api',
    download_url='https://github.com/barchart/barchart-ondemand-client-python/archive/1.0.zip',
    install_requires=[
        'requests>=2.3.0'
    ],
    license='LICENSE.txt',
    keywords=['market-data', 'futures', 'forex', 'stock-market', 'stock-quotes', 'historical-data', 'price-data'],
    packages=['ondemand'])
