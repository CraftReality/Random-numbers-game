import random as rd

while 1:
    b = rd.randint(10 , 50)
    c = rd.randint(10, 50)
    try:
        if b > c:
            d = rd.randint(c , b)
            large_number = b
            small_number = c
        
        if c > b:
            d = rd.randint(b , c)
            large_number = c
            small_number = b
        
        a = int(input("write a random number from " + str(small_number) + " to " + str(large_number) + " : "))
        if a == d:
            print("you said correct!! it is " + str(d))
        
        if a != d:
            print("you said wrong!!! it is " + str(d))
    
    except ValueError:
        print("Bruh!! that not a number...")