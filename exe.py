import urllib

base_url = "http://ichart.finance.yahoo.com/table.csv?s="
def make_url(ticker_symbol):
    return base_url + ticker_symbol

def pull_historical_data(ticker_symbol):
    filename = ticker_symbol + '.csv'
    try:
        urllib.urlretrieve(make_url(ticker_symbol), filename)
    except urllib.ContentTooShortError as e:
        outfile = open(filename, "w")
        outfile.write(e.content)
        outfile.close()

pull_historical_data('GOOG')
