import sys
def fun1(to_replace, replacer):
    def fun2(string):
        nonlocal to_replace, replacer
        result = string.replace(replacer, to_replace)
        return result
    return fun2
if __name__ == "__main__":
    x = input(" 111111 ")
    c = input(" 11 ")
    h = input(" 2 ")
    rep = fun1(h, c)
    print(rep(x))
