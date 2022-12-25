def calculate(x:float, y:float, operation:str='a') -> None:
    '''калькулятор'''
    def addition():
        print(float(x+y))

    def subtraction():
        print(float(x-y))

    def division():
        if y == 0:
            print('На ноль делить нельзя!')
        else:
            print(float(x/y))

    def multiplication():
        print(float(x*y))

    if operation== 'a':
         addition()
    elif operation == 's':
         subtraction()
    elif operation == 'd':
         division()
    elif operation == 'm':
         multiplication()
    else:
        print('Ошибка. Данной операции не существует.')

calculate(10,4)