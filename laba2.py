num1 = float(input ("Введите первое число:"))
num2 = float(input ("Введите второе число:"))
oper = input (" Выбериет тип операции:")

if oper == "+":
    result = num1 + num2
    print ("Ответ:", result)
elif oper == "-":
    result = num1 - num2
    print ("Ответ:", result)
elif oper == "*":
    result = num1 * num2
    print ("Ответ:", result)

elif oper == "**":
    result = num1 ** num2
    print ("Ответ:", result)
elif oper == "/":
    if num2 == 0:
        print ("На 0 делить нельзя!".upper())
        exit ()
    result =  num1/num2
    print ("Ответ:", result)