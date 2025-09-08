import mycalculator
import myrandom

def my_main():
    """Эта главная функция, которая создает 2 случайных числа \
    и применяет к ним функцию калькулятора """
    x = myrandom.random_2d()
    y = myrandom.random_1d()
    sum = mycalculator.add(x, y)
    diff = mycalculator.substract(x, y)
    print("x = {}, y = {}".format(x, y))
    print("sum is {}".format(sum))
    print("diff is {}".format(diff))

    print(globals())

"""Этот фрагмент выполняется только в случает, если специальная переменная \
    '__name__' утсановлена в качетсве главной"""

if __name__ == "__main__":
    my_main()






