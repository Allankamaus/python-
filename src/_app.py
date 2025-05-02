#defining our vairables
total = 0
x=0
y=0

#all the caluculator signs as functions
def add(x,y):
    total = x + y
    print(x , " + " , y, ' =' , total)

def subtract(x,y):
    total = x - y
    print(x , " - " , y, ' = ' , total) 

def multiply(x,y):
    total = x * y
    print(x , " * " , y ,' = ' , total)


def divide(x,y):
#if statments for when the user wants to divide by 0
        if y == 0:
            print('invalid you cant divide by 0') 

        elif x ==0:
            print('invalid you cant divide by 0') 

        else:      
            total = x/y
            print(x , " / " , y ,' = ' , total)
            

#main menu
print("what would you like to do:\n1.add \n2.subtract \n3.multiply \n4.divide")

#loops when user inputs are invalid
while True:

    #choice from menu
    option = int(input("your choice(on of the numbers):"))
    if option in [1,2,3,4]:
        
        #taking the users input
        x = int(input("first number :"))
        y = int(input("second number :"))
        
        
        if option == 1:
            add(x,y)
        
        elif option == 2:
            subtract(x,y)

        elif option == 3:
           multiply(x,y)

        elif option == 4:
            divide(x,y)

        break

    print("try again")

