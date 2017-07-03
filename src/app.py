from bittrex import bittrex

api = bittrex('', '')

print api.getbalances()
