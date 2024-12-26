def kolored(message, color='0', background='0', bold=False, italic=False) -> str:
    """
    Colorizes the given message with the specified color, background, and styles.

    Args:
        message (str): The text to colorize.
        color (str): The foreground color (default is '0').
        background (str): The background color (default is '0').
        bold (bool): Whether the text should be bold (default is False).
        italic (bool): Whether the text should be italic (default is False).

    Returns:
        str: The colorized message.
    """
    messager = str(message)

    colors = {
        '0': '', 'black': '\33[30m', 'red': '\33[31m', 'green': '\33[32m', 
        'yellow': '\33[33m', 'blue': '\33[34m', 'purple': '\33[35m', 'white': '\33[37m'
    }
    backcolors = {
        '0': '', 'black': '\33[40m', 'red': '\33[41m', 'green': '\33[42m', 
        'yellow': '\33[43m', 'blue': '\33[44m', 'purple': '\33[45m', 'white': '\33[47m'
    }

    kbold = '\33[1m' if bold else ''
    kitalic = '\33[3m' if italic else ''

    kolor = colors.get(color, '')
    backolor = backcolors.get(background, '')

    result = f'{backolor}{kolor}{kbold}{kitalic}{messager}\033[0m'
    return result
