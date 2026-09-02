from nicegui import ui

resultado = ui.label('Resultado: 0').classes('text-2xl')

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

ui.dark_mode()

ui.label('Calculadora de Gonza con NiceGUI').classes('text-3xl font-bold')

input1 = ui.number(label='Primer número')
input2 = ui.number(label='Segundo número')

with ui.row():
    ui.button('+', on_click=lambda: calcular('+'))
    ui.button('-', on_click=lambda: calcular('-'))
    ui.button('*', on_click=lambda: calcular('*'))
    ui.button('/', on_click=lambda: calcular('/'))

if __name__ in {"__main__", "__mp_main__"}:
    ui.run()
