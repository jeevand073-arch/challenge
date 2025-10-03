# basic calcuklator 


num1 = float (input("enter  your first number")) #input first number

num2 = float( input("enter your second number")) #input second number

op = input("operator are(+,*,-,/,//,%):") # inputing operator to choose user to which operator they want use

if op == '+':
    print("reult is:",num1+num2)
elif op== '*':
    print("result is", num1*num2)
elif op == '-':
    print("result is ", num1-num2)
elif op == '/':
    if num2 != 0: # to avoid dividing by zero
        print ("result",num1/num2)
    else:
      print("zero:division not alloeded")
elif op == '//':
    if num2 != 0 :
        print("result", num1//num2) 
    else:
        print("zero:in float is not alloweded")
elif op == '%':
    if num2 != 0 :
        print("result is :", num1%num2)
    else:
        print('zero:ii module is not alloweded')