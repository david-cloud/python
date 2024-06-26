# import types
#
# def func(arg):
#     # if callable(arg):
#     if isinstance(arg,types.FunctionType):
#         print(arg())
#     else:
#         print(arg)
#
#
# func(123)
# func(lambda :"666")


class Foo(object):

    def __init__(self,a1):
        print(a1)
        self.a = a1

    def __new__(cls, *args, **kwargs):
        """
        1. 根据类创建对象，并返回
        2. 执行返回值得__init__
        :param args:
        :param kwargs:
        :return:
        """
        # return "孙接龙"
        return object.__new__(cls)

obj = Foo(123)
print(obj)
