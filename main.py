from nicegui import ui

ui.label("Mi Calculadora")


def calcular(operacion):
    try:
        num1 = float(input1.value)
        num2 = float(input2.value)
        if operacion == 'suma':
            resultado.set_text(f'Resultado: {num1 + num2}')
        elif operacion == 'resta':
            resultado.set_text(f'Resultado: {num1 - num2}')
        elif operacion == 'multiplicacion':
            resultado.set_text(f'Resultado: {num1 * num2}')
        elif operacion == 'division':
            if num2 != 0:
                resultado.set_text(f'Resultado: {num1 / num2}')
            else:
                resultado.set_text('Error: división por cero')
    except ValueError:
        resultado.set_text('Error: ingrese números válidos')

ui.label('Calculadora con NiceGUI').style('font-size: 24px; font-weight: bold;')

input1 = ui.input('Número 1')
input2 = ui.input('Número 2')

ui.button('Sumar', on_click=lambda: calcular('suma'))
ui.button('Restar', on_click=lambda: calcular('resta'))
ui.button('Multiplicar', on_click=lambda: calcular('multiplicacion'))
ui.button('Dividir', on_click=lambda: calcular('division'))

resultado = ui.label('Resultado: ')

ui.run()
