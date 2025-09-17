# function is aset of instructions labeld 
# under a custom name, that a computer will run


# function syntax (rules of how its written)
# functio have 2 phase: function definition and function call

# function definition
# we are describing the instructions for our custom code
# we are adding logic to the computers vocabulary
# this code does not run, it only gives the computer the meaning
# not action

def example():
    print('mohamed is ugly') # 1 instruction :print mohamed is ugly

# phase 2: function call
# once we have the definition, we can now run the instruction
# by writting the function name

example()

# we indent to inform the computer
# that we are about to write instrutions
# if we dont, we will get an error
def example2():
    print('good boy')
    a= input('enter a number ')
    print(a)

example2()  

def math():
    a = input('please enter a number ')
    b = 20
    print('what is your result! ')
    print(int(a) + int(b))

# creat a function that will calculate 2 numbers
# with differnt arithmatic operation 

def calculation():
    numx = input('please enter a number' )
    numx2 = input('please entyer another number')
    print(numx, numx2)


