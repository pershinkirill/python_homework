# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

the_string = input("please enter a string:  ")
deletion = 'абв'
new_string = the_string.replace(deletion, '')
print(f'initial string: "{the_string}", \nresulted string: "{new_string}"')
