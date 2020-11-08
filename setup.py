from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='ondemand',
    version='1.1.1',
    description='Simple client for Barchart OnDemand REST APIs',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Mike Ehrenberg",
    author_email="solutions@barchart.com",
    url='https://www.barchartondemand.com/api',
    download_url='https://github.com/barchart/barchart-ondemand-client-python/archive/master.zip',
    install_requires=[
        'requests>=2.3.0'
    ],
    license='LICENSE.txt',
    keywords=['market-data', 'futures', 'forex', 'stock-market', 'stock-quotes', 'historical-data', 'price-data'],
    packages=['ondemand'])
