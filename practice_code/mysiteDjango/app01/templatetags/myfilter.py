from django import template
register = template.Library()
# 注册到Django template模板


# 告诉Django的模板语言我现在有一个自定义的filter方法，名字叫sb
@register.filter(name="sb")
def add_sb(arg):
    return "{} sb.".format(arg)


# 告诉Django的模板语言我现在有一个自定义的filter方法，名字叫addStr
@register.filter(name="addStr")
def add_str(arg, arg2):
    """
    第一个参数永远是管道符前面那个变量
    :param arg: 道符前面那个变量
    :param arg2: 冒号后面的变量
    :return:
    """
    return "{} {}.".format(arg, arg2)
