# Solicita ao usuário para inserir a resistência e a corrente
resistencia = float(input("Digite o valor da resistência em ohms (Ω): "))
corrente = float(input("Digite o valor da corrente em amperes (A): "))

# Calcula a tensão usando a fórmula U = R * i
tensao = resistencia * corrente

# Exibe o resultado da tensão
print("A tensão é:", tensao, "volts (V)")

# Solicita ao usuário para inserir a tensao e a corrente
tensao = float(input("Digite o valor da tensao em volts (V): "))
corrente = float(input("Digite o valor da corrente em amperes (A): "))

resistencia = tensao * corrente

# Exibe o resultado da resistencia
print("A resistencia é:", resistencia, "ohm (Ω)")

# Solicita ao usuário para inserir a tensao e a resistencia
tensao = float(input("Digite o valor da tensao em volts (V): "))
resistencia = float(input("Digite o valor da resistencia em ohms(Ω): "))

corrente = tensao * resistencia

# Exibe o resultado da resistencia
print("A corrente é:", corrente, "amperes (A)")