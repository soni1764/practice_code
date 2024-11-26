# class Calculator:
#     def add(a, b):
#         print(a + b)
#
#
# Calculator.add(2, 3)
#
#
# def new_add(a, b):
#     print((a + b) * 100)
#
#
# def sub(a, b):
#     print(a - b)
#
#
# Calculator.add = new_add
# Calculator.sub = sub
#
# Calculator.add(2, 3)
# Calculator.sub(10, 2)



try:
    raise ExceptionGroup('Example ExceptionGroup', (
    TypeError('Example TypeError'),
    ValueError('Example ValueError'),
    KeyError('Example KeyError'),
    AttributeError('Example AttributeError')
    ))
except* TypeError:
    print(TypeError)
except* ValueError as e:
    print(e)
except* (KeyError, AttributeError) as e:
    print(TypeError)












