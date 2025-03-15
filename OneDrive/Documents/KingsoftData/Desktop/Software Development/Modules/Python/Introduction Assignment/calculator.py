number1 = float(input ("Please enter first number:"))
number2 = float(input ("Please enter second number:"))

Operation = input("Please enter operation(+,*,-,/):")

if Operation == '+':
    answer = number1 + number2
    print(f"{number1} + {number2}  = {answer}")

elif  Operation == '-':
     answer =  number1 - number2
     print(f"{number1} - {number2}  = {answer} ")
elif  Operation == '*':
        answer = number1 * number2
        print(f"{number1} * {number2}  = {answer}")
elif Operation == '/':
    if  number2 != 0:
     answer = number1 / number2
     print(f"{number1} / {number2} = {answer}") 
    else:
     print("Please enter another number, answer is undefined!")
     
else:
        print("Please enter operation(+,*,-,/):")
         