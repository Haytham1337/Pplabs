def funct(a:int,b:int):
    while a<b:
        i=2
        while(i<a):
            if a%i==0:
                break
            elif i==a-1:
                print(a)
            i+=1
        a+=1

            
funct(2,100)        
