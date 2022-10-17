def fun1(to_replace, replacer):
    def fun2(string):
        nonlocal to_replace, replacer 
        result = string.replace(replacer, to_replace) 
        return result 
    return fun2 

if __name__  == "__main__": 
    x = input("введите исходную строку")
    c = input("введите внещнюю функцию")
    h = input("введите внутреннюю функцию") 
    replace = fun1(h,c) 
    print(replace(c))