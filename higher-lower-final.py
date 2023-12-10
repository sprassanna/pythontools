#from art import logo
from game_data import data
import random

#Welcome the audience
print('Welcome start the game ')
#Create two variables  - now & next ; score
now = ""
next = ""
score =0

total_datasize = len(data)

print(total_datasize)

do_Continue = True
#Get random two values and fit in now and next 

 
while(do_Continue):
 A = data[random.randint(1, total_datasize)]

 B = data[random.randint(1, total_datasize)]
  
 print(f"compare  A {A['name']} {A['description']} \n {A['country']} with B  {B['name']} {B['description']} {B['country']}")
 

 guess_value = input(('Guess who has more followers A or B')).upper()
 
 if(A['follower_count'] > B['follower_count']):
    if(guess_value == 'A'):
        do_Continue = True
    else:
      do_Continue = False

 else:
    if(guess_value == 'B'):
        do_Continue = True
    else:
        do_Continue = False
      
 score += 1
 print(f" As Follower: {A['follower_count']} Bs Follower {B['follower_count']}")
 print(f'Your score is {score}')
 if( not do_Continue):
  if(input('do you want to guess again y/n').lower() == 'y'):
    do_Continue = True
 
 
