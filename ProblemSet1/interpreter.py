n = input('use this as a calculator: ').strip().lower()
x, y, z = n.split(' ')

match y:
    case '+':
        print(int(x) + int(z))
    case '-':
        print(int(x) - int(z))
    case '*':
        print(int(x) * int(z))
    case '/':
        print(int(x) / int(z))