def multiply(val):
    def multiply_two(x):
        print(f'Умножение {x} на {x} = {val*x}')
    return multiply_two
f_2 = multiply(2)
f_2(5)
f_2(15)
f_3 = multiply(3)
f_3(5)
f_3(15)
f_3(120)