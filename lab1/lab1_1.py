def funct (a:int ,b:int)->bool:
    if a < 0 or b < 0:
        ex = ValueError("Invalid numbers")
        raise ex
    return a%b==0

    
try:
    print (funct(4,2))
except ValueError as message:
    print(str(message))
    
 