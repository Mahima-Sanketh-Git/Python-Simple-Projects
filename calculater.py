
loops = 1

while loops <= 100:
    f_num = input('enter number : ')
    s_num = input('enter number :')
    math_eq = input('enter math equation : ')
    loops += 1
    if math_eq == '+':
        print(int(f_num) + int(s_num))

    elif math_eq == '-':
        print(int(f_num) - int(s_num))

    elif math_eq == '*':
        print(int(f_num) * int(s_num))

    elif math_eq == '/':
        print(int(f_num) / int(s_num))

    else:
        print('invalide oparetar')
