a = 5 
b = 0

try: 
    print(" resource open")
    print(a/b)
    k = int(input("ENter a number"))
    print(k)
    
except Exception as e :
    print("HEY YOU CAN'T DIVIDE NO. WITH ZERO",e)
finally:
    print("resource closed")