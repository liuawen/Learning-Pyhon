def foo(a):
    try:
        b *= 100/a
    except ZeroDivisionError:
        print("除数不为零")
        return -1
    except:
        print("未知错误")
foo(0)
foo(1)