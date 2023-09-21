#Напишите программу, 
#которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
#Функцию hex используйте для проверки своего результата.
def turn_to_hex(number: int) -> str:
    return f'0x{number:0x}'

assert hex(100500) == turn_to_hex(100500), \
    f'Expected "{hex(100500)}" to be equal to "{turn_to_hex(100500)}"'