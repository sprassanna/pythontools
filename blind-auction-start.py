from replit import clear

toBeContinued= 'yes'

bid_amount = {}

while toBeContinued=='yes':
  name = input('Whats your name ?')
  bidVal =  int(input('whats your bid ?'))
  toBeContinued = input('Are there any other bidders Yes or No').lower()
  bid_amount[name] = bidVal
  clear()
  
temp = 0

for key in bid_amount:
  if(bid_amount[key]>temp):
     temp = bid_amount[key]
   
print(f'the highest bidder value is {temp}')



