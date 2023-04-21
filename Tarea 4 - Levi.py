#Tarea 4 Levi Ciclos

number = -20

if number > 0:
    print("Numero Positivo")

elif number == 0:
    print('Cero')
else:
    print('Numero Negativo')

print('La declaracion es ejecutada')

number = 8

# outer if statement
if (number >= 0):
    # inner if statement
    if number == 0:
      print('Numero es 0')
    
    # inner else statement
    else:
        print('Numero es positivo')

# outer else statement
else:
    print('Numero es negativo')

# Output: Numero es positivo