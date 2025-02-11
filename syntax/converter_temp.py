temp = float(input("Informe a temperatura monitorada em °C: "));

converter_K = lambda celsius: celsius + 273.15
converter_F = lambda celsius: (celsius*(9/5)) + 32

print(converter_K(temp))
print(converter_F(temp))