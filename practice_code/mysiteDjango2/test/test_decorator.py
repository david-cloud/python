'''
同时使用多个装饰器时，需要调用的函数本身只会执行一次
但会依次执行所有装饰器中的语句
执行顺序为从上到下依次执行

因为 @decorator1 写在上面，因此会先执行decorator1 中的代码块，后执行decorator2 中的代码块

'''


def decorator1(func):
    def wrapper(*args, **kwargs):
        print("the decoretor is decoretor1 !")
        func(*args, **kwargs)
    return wrapper


def decorator2(func):
    def wrapper(*args, **kwargs):
        print("the decoretor is decoretor2 !")
        func(*args, **kwargs)
    return wrapper


@decorator1
@decorator2
def myFun(func_name):
    print('This is a function named : {}'.format(func_name))


if __name__ == '__main__':
    print(__name__)
    myFun('myfun')
