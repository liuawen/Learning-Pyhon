def f(a):
    try:
        print(1/a)
        return  1/a
    except:
        print("except")
        return "except"
    else:
        print("else")
        return "else"
    finally:
        print("finally")
        return "finally"
f(1)

#try  有return   else 不执行
