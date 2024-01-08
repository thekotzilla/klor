
def kolored(message, color='0', background='0', bold=False, italic=False):
    messager = str(message)

    colors = {'0': '', 'black': '\33[30m', 'red': '\33[31m', 'green': '\33[32m', 'yellow': '\33[33m', 'blue': '\33[34m', 'purple': '\33[35m', 'white': '\33[37m'}
    backcolors = {'0': '', 'black': '\33[40m', 'red': '\33[41m', 'green': '\33[42m', 'yellow': '\33[43m', 'blue': '\33[44m', 'purple': '\33[45m', 'white': '\33[47m'}
    ebold = {True: '\33[1m', False: ''}
    eitalic = {True: '\33[3m', False: ''}

    kbold = bold.get(bold)
    kitalic = italic.get(italic)
    kolor = colors.get(color)
    backolor = backcolors.get(background)
    result = kbold + kitalic + backolor + kolor + messager + '\033[0m'
    return result

def available_colors():
    print('\33[30m' + 'Black')
    print('\33[31m' + 'Red')
    print('\33[32m' + 'Green')
    print('\33[33m' + 'Yellow')
    print('\33[34m' + 'Blue')
    print('\33[35m' + 'Purple')
    print('\33[37m' + 'White')
