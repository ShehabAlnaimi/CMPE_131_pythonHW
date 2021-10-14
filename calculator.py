def calculator(number1, number2, operator):
    '''
    Take three parameters
    :param number1:
    :param number2:
    :param operator:
    :return:
    The result of the operation used
    :return
    False if the operation invalid
    '''
    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '*':
        return number1 * number2
    elif operator == '/':
        return number1 / number2
    elif operator == '//':
        return number1 // number2
    elif operator == '**':
        return number1 ** number2
    else :
        return False

def parse_input():
    '''
    Take input from the user - one equation
    Call calculator()
    :return:
    The result
    '''
    usersInput = input('Enter equation: ')
    number1, operator, number2 = usersInput.split()
    number1 = float(number1)
    number2 = float(number2)
    print(calculator(number1, number2, operator))







