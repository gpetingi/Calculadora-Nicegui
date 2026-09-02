from nicegui import ui

# Función para manejar las operaciones
def calcular(operacion):
    try:
        num1 = float(input1.value)
        num2 = float(input2.value)
        if operacion == '+':
            resultado.set_text(f'Resultado: {num1 + num2}')
        elif operacion == '-':
            resultado.set_text(f'Resultado: {num1 - num2}')
        elif operacion == '*':
            resultado.set_text(f'Resultado: {num1 * num2}')
        elif operacion == '/':
            if num2 != 0:
                resultado.set_text(f'Resultado: {num1 / num2}')
            else:
                resultado.set_text('Error: división por cero')
    except ValueError:
        resultado.set_text('Error: ingrese números válidos')

# Tema oscuro
ui.dark_mode()

# Título con estilo
ui.label('Calculadora de Gonza con NiceGUI') \
