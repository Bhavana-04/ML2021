#evaluate function performs operations according to the given expression
def evaluate():
    #takes input from the user
    expr=input("Enter an expression: ")
    #throws an exception if we enter wrong expression
    try:
        print("Result of the given expression is: ",eval(expr))
    except Exception as e:
        print(e)