from bittrex import bittrex

api = bittrex('', '')

from terminaltables import AsciiTable
table_data = [
    ['Currency', 'Available', 'Pending', 'Balance']
]
table = AsciiTable(table_data)

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
		
		table_data.append([myBalances[i]['Currency'], NewAvailable, NewPending , NewBalance])
	
	i += 1
	
print table.table