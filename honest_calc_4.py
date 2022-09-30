memory = 0
math_ops = ("+","-","*","/")
msg_0 = 'Enter an equation\n'
msg_1 = 'Do you even know what numbers are? Stay focused!'
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = 'Yeah... division by zero. Smart move...'
msg_4 = "Do you want to store the result? (y / n):\n"
msg_5 = "Do you want to continue calculations? (y / n):\n"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"

oper = ""

def check(v1, v2, v3):
    msg =""
    if is_one_digit(v1) == True and is_one_digit(v2) == True:
       msg = msg + msg_6
#    print(is_one_digit(v1), is_one_digit(v2))
#    print(v1, type(v1), v2, type(v2))
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + msg_7

    if (v1 == 0 or v2 == 0) and (v3 == "+" or v3 == "-" or v3 == "*"):
        msg = msg + msg_8

    if msg != "":
        msg = msg_9 + msg

    print(msg)

def is_one_digit(v):
#    print("Is called", v,  type(v))
    if -10 < v < 10 and v == int(v):
#        print("PENIS")
        output = True
        return output

def calc():
    x, oper, y = input(msg_0).split()
#    print(oper)
    if x == 'M':
        x = memory

    elif y == 'M':
        y = memory

    try:
        x = float(x)
        y = float(y)

    except (TypeError, ValueError):
        print(msg_1)


    if oper not in math_ops:
        print(msg_2)

    else:
        check(x, y, oper)
        if oper == "+":
            result = x + y
            return result
        elif oper == "-":
            result = x - y
            return result
        elif oper == "*":
            result = x * y
            return result
        elif oper == "/" and y != 0:
            result = x / y
            return result
        else:
            print(msg_3)
while True:
    calculation = calc()
    if type(calculation) == float or type(calculation) == int:
        print(calculation)

        store = input(msg_4)
        continum = input(msg_5)

        if store == 'y':
            memory = calculation
        if continum == 'n':
            break
        else:
            continue

    else:
        continue