x=int(input("Enter a number:"))
y=int(input("Enter a number:"))
op=input("select operator [+ - / * %] :")
result=0
if op=='+':
    result=x+y
elif op=='-':
    result=x-y
elif op=='*':
    result=x*y
elif op=='/':
    result=x/y  
elif op=='%':
    result=x%y
else:
    print("Invalid operator")
print( x, op, y, "=", result)                      
