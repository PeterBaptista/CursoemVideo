# Escreva um programa que converta uma temperatura digitada em °C
# e converta para °F

Celsius = float(input('Qual a temperatura em celsius? °C'))

F = Celsius * 1.8 + 32
K = Celsius + 243

print(f'Celsius: {Celsius}°C'
      f'\nFahrenheit: {F:.1f}°F'
      f'\nKelvin: {K}K')