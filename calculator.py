final_num = 0
num1 = float(input("what is your first number"))
num2 = float(input("what is your second number"))
operator = input("what operation would you like to apply to your numbers (+,-,*,/)")

if operator == "+":
    final_num = (num1 + num2)
elif operator == "-":
    final_num = (num1 - num2)
elif operator == "*":
    final_num = (num1 * num2)
elif operator == "/":
    final_num = (num1 / num2)
else:
    print("invaled operation")
print(final_num)    