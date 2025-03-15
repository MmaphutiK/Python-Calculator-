number1 = input ("Please enter first number:")
number2 = input ("Please enter second number:")

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
         answer = number1 / number2
print(f"{number1} / {number2} = {answer}") 