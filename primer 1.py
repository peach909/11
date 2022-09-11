Python 3.10.3 (tags/v3.10.3:a342a49, Mar 16 2022, 13:07:40) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def add_two(a):
    x = 2
    return a + x
add_two(3)
SyntaxError: invalid syntax
print(x)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(x)
NameError: name 'x' is not defined
