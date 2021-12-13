8791# Aluno: Jackson Cardoso de Oliveira

pi = 3.1415  # define um valor para PI


# Função que verifica se é par ou impar e realiza a divisão ou cálculo da área e perímetro
def calculaDivAreaPerim(numeros):
    for numero in numeros.split(" "):
        numero = int(numero)
        
        # Verifica e a entrada é PAR
        if numero % 2 == 0:
            print(f'Divisores de {numero} são:', end="")
            for i in range(1, numero + 1):
                if numero % i == 0:
                    # A cada iteração exibe um DIVISOR na mesma linha do anterior
                    print("", i, end="")
            print()
        # A entrada impar entra no bloco
        else:
            perimetro = 2 * pi * numero    # Calcula o PERÍMETRO
            area = (numero ** 2) * pi      # Calcula a ÁREA
            # Exibe a ÁREA E O PERÍMETRO
            print(f'Área e Perímetro do Círculo de Raio {numero} são: {area:.2f} e {perimetro:.2f}.')


numeros = ""
while True:
    entrada = input()
    # Se a entrada for vazia encerra a aplicação
    if entrada == "":
        # Chama a função passando a variável "entrada" convertida em inteiro como parâmetro
        calculaDivAreaPerim(numeros.strip())
        exit()
    else:
        numeros += entrada + " "

