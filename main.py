#Program to check if numer is a power of 4
def powerof4(number):
    count=0
    #If only one set bit exists
    if(number&(~(number&(number-1)))):
        while(number>1):
            number>>=1
            count+=1
        #If count is even return true else false
        if(count%2==0):
            return True
        else:
            return False
number=int(input('Enter your number'))
if(powerof4(number)):
    print('Number is a power of 4')
else:
    print('Number is not a power of 4')