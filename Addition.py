#!user/bin/python
def VariableArgsAdd (*args):
    print (type (args))
    for x in args:
        print (x)
VariableArgsAdd (1, 2, 3)
VariableArgsAdd (1, 2, 3, 4, 5, 6, 7, 8)
