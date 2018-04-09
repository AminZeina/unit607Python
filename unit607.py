# Created By: Amin Zeina 	
# Created On: Apr 2018

age = 15

while True:
    
    ageGuessed = int(input( 'Guess My Age: ' ))
    
    if ageGuessed == age:
        print( 'You got it right!')
        break
    elif ageGuessed > age:
    	print( 'You are too high. Try again.' )
    else: 
    	print( 'You are too low. Try again.' )

input( 'Program End.')