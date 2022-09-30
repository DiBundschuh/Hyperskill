memory = 0
math_ops = ("+","-","*","/")
msg_ = ('Enter an equation\n',
        'Do you even know what numbers are? Stay focused!',
        "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
        'Yeah... division by zero. Smart move...',
        "Do you want to store the result? (y / n):\n",
        "Do you want to continue calculations? (y / n):\n",
        " ... lazy",
        " ... very lazy",
        " ... very, very lazy",
        "You are",
        "Are you sure? It is only one digit! (y / n)\n",
        "Don't be silly! It's just one number! Add to the memory? (y / n)\n",
        "Last chance! Do you really want to embarrass yourself? (y / n)\n")
oper = ""

def check(v1, v2, v3):
    msg =""
    if is_one_digit(v1) == True and is_one_digit(v2) == True:
       msg = msg + msg_[6]
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + msg_[7]
    if (v1 == 0 or v2 == 0) and (v3 == "+" or v3 == "-" or v3 == "*"):
        msg = msg + msg_[8]
    if msg != "":
        msg = msg_[9] + msg
    print(msg)
def is_one_digit(v):
    if -10 < v < 10 and v == int(v):
        output = True
        return output
def calc():
    x, oper, y = input(msg_[0]).split()
    if x == 'M':
        x = memory
    if y == 'M':
        y = memory
    try:
        x = float(x)
        y = float(y)

    except (TypeError, ValueError):
        print(msg_[1])
    if oper not in math_ops:
        print(msg_[2])
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
            print(msg_[3])
while True:
    calculation = calc()
    if type(calculation) == float or type(calculation) == int:
        print(calculation)
        store = input(msg_[4])
        if store == 'y' and is_one_digit(calculation):
            for i in range(10, 14):
                store = input(msg_[i])
                if store == 'y':
                    if i < 12:
                        continue
                    else:
                        memory = calculation
                        break
                elif store == 'n':
                    break
                else:
                    break

        elif store == 'n':
            pass
        else:
            memory = calculation
        continum = input(msg_[5])
        if continum == 'n':
            break
        else:
            continue
    else:
        continue
