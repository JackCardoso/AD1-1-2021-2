# Aluno: Jackson Cardoso de Oliveira

# Inicializa as variáveis
soma = 0
media = 0
maior = None
menor = None

# A variável"qtd" recebe o valor da entrada padrão
qtd = input()
# Se "qtd" for menor que 1 encerra a aplciação
if int(qtd) < 1:
    exit()
else:
    # A variável "qtd" é convertida em inteiro
    qtd = int(qtd)
    # Laço que incrementa "i" de 1 até "qtd+1" a cada iteração
    for i in range(qtd):
        # A variável "entrada" recebe um valor convertido em inteiro da entrada padrão
        linha = int(input())
        if linha != "":
            # A cada iteração verifica se a entrada é o maior/menor valor e atribui a variável correspondente
            maior = maior if maior is not None and maior > linha else linha
            menor = menor if menor is not None and menor < linha else linha
            # SOMA entrada a entrada a cada iteração
            soma += linha

    # Cacula a MÉDIA e atribui a variável "media"
    media = float(soma / qtd)

    # Exibe a o Total da SOMA das entradas, a MÉDIA, a MENOR e o MAIOR valor
    print("Soma:", soma)
    print(f'Média: {media:.2f}')
    print("Menor:", menor)
    print("Maior:", maior)




