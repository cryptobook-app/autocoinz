from bittrex import bittrex

api = bittrex('', '')

from terminaltables import AsciiTable
coin_data = []
table_data = [
    ['ID','Currency', 'Available', 'Pending', 'Balance']
]

table2_data = [
    ['ASK','BID', 'LAST']
]

table = AsciiTable(table_data)
table2 = AsciiTable(table2_data)

myBalances = api.getbalances()

i = 0
while i < len(myBalances):
	
	checkthis = myBalances[i]['Available']

	if checkthis == 0.0:
		nothing = 0;
	else:
		NewAvailable = '{0:.8f}'.format(myBalances[i]['Available'])
		NewPending = '{0:.8f}'.format(myBalances[i]['Pending'])
		NewBalance = '{0:.8f}'.format(myBalances[i]['Balance'])
		
		coin_data.append([i, myBalances[i]['Currency']])
		table_data.append([i, myBalances[i]['Currency'], NewAvailable, NewPending , NewBalance])
	
	i += 1

print "***** YOU CANNOT BUY/SELL BITCOIN (BTC) WITH THIS SCRIPT ****"
print table.table

getCoinID = raw_input('Enter Coin ID: ')

ii = 0
while ii < len(coin_data):
	
	if coin_data[ii][0] == int(getCoinID):
		#print 'BTC-'+str(coin_data[ii][1])
		if str(coin_data[ii][1]) == 'BTC':
			print "You cannot trade BTC with this"
		else:
			tickerData = api.getticker('BTC-'+str(coin_data[ii][1]))
			#print tickerData['Bid']
			NewAsk = '{0:.8f}'.format(tickerData['Ask'])
			NewBid = '{0:.8f}'.format(tickerData['Bid'])
			NewLast = '{0:.8f}'.format(tickerData['Last'])

			table2_data.append([NewAsk, NewBid, NewLast])
		
	ii += 1

print table2.table