# Alunos:
# Vinícius Santos Silva
# Maria Rafaela Tomé Braun
# Maria Eduarda Garcia Soares

#biblioteca usada:
import time
import random

def comparador():


    X = int(input("Quantos elementos inteiros serão ordenados? (Digite um número inteiro)\n")) # "X" é o número de elementos a serem gerados
    Y = int(input("Você irá querer visulizar saídas de cada ordenador?\n(Digite 1 para 'sim' ou 0 para 'não')\n"))
    if X <= 5000: # Comentando o tempo de processamento
        print("Processando...")
    elif X <= 10000:
        print("Processando... isso pode levar até 30 segundos...")
    else:
        print("Processando... isso pode demorar um pouco...")

    #gerador de lista de inteiros aleatórios--------------------------------
    def gerador(X): # "X" é o número de elementos a serem gerados
        lista = [] # criando lista
        for i in range(X):
    # Incluindo itens na lista usando append e usando a função random.randrange() incorporada na biblioteca "random"
            lista.append(random.randrange(100000))
        return lista

    lista = gerador(X) #criando lista usada pelos programas ordenadores

    #ordenação por bolha----------------------------------------------------

    def bolha_(lista): # criando a função do programa de ordenação por bolha
        for a in range(len(lista)-1,0,-1):
            for i in range(a):
                if lista[i]>lista[i+1]:
                    tempo = lista[i]
                    lista[i] = lista[i+1]
                    lista[i+1] = tempo

    ini = time.time()  # registra a hora no início
    bolha_(lista) # chamando a função do ordenador por bolha
    if Y == 1: # Se o usuário estiver colocado "sim", o programa mostrará a lista ordenada pela função
        print("Ordenação Bolha:", lista)
    time.sleep(1) # A função .sleep(1) espera por 1 segundo
    fim = time.time()  # registra a hora no final
    tempobolha = fim - ini -1  # calcula a diferença entre a hora final e inicial

    print(f'A Ordenação por Bolha demorou {tempobolha} segundos.\n')


    #ordenação por seleção----------------------------------------------------
    def selecao_(lista):
        n = len(lista)
        # percorre o arranjo lista.
        for i in range(n):
            # encontra o elemento mínimo em lista.
            m = i
            for j in range(i + 1, n):
                if lista[m] > lista[j]:
                    m = j
            # coloca o elemento mínimo na posição correta.
            lista[i], lista[m] = lista[m], lista[i]

    ini = time.time()  # registra a hora no início
    selecao_(lista) # chamando o programa de ordenação por seleção
    if Y == 1: # Se o usuário estiver colocado "sim", o programa mostrará a lista ordenada pela função
        print("Ordenação Seleção:", lista)
    time.sleep(1) # A função .sleep(1) espera por 1 segundo
    fim = time.time()  # registra a hora no final
    temposelecao = fim - ini -1 # calcula a diferença entre a hora final e inicial

    print(f'A Ordenação por Seleção demorou {temposelecao} segundos.\n')

    #ordenação por inserção----------------------------------------------------
    def insercao_(lista):
        n = len(lista)
        # percorre o arranjo lista.
        for j in range(1, n):
            c = lista[j]
            i = j - 1
            # coloca o elemento lista[j] na posição correta.
            while i >= 0 and lista[i] > c:
                lista[i + 1] = lista[i]
                i = i - 1
            lista[i + 1] = c

    ini = time.time()  # registra a hora no início
    insercao_(lista) # chamando a função de ordenação por inserção
    if Y == 1: # Se o usuário estiver colocado "sim", o programa mostrará a lista ordenada pela função
        print("Ordenação Inserção:", lista)
    time.sleep(1) # A função .sleep(1) espera por 1 segundo
    fim = time.time()  # registra a hora no final
    tempoinsercao = fim - ini -1 # calcula a diferença entre a hora final e inicial

    print(f'A Ordenação por Inserção demorou {tempoinsercao} segundos.\n')


    #Ordenação com Sort---------------------------------------------------------
    def sort_(lista): # Criando a função sort_()
        lista = lista.sort() # Aqua função sort() irá ordenar a lista

    ini = time.time()  # registra a hora no início
    sort_(lista) # chamando a função de ordenação com sort()
    if Y == 1: # Se o usuário estiver colocado "sim", o programa mostrará a lista ordenada pela função
        print("Ordenação Sort:", lista)
    time.sleep(1) # A função .sleep(1) espera por 1 segundo
    fim = time.time()  # registra a hora no final
    temposort = fim - ini -1 # calcula a diferença entre a hora final e inicial

    print(f'A Ordenação com Sort demorou {temposort} segundos.\n')

    # Aqui vamos ver qual foi o algoritmo de ordenação mais rapido
    rapido = 0
    if tempobolha < tempoinsercao and tempobolha < temposelecao and tempobolha < temposort:
        rapido = tempobolha
        nome = "Ordenação por Bolha"
    elif tempoinsercao < tempobolha and tempoinsercao < temposelecao and tempoinsercao < temposort:
        rapido = tempoinsercao
        nome = "Ordenação por Inserção"
    elif temposelecao < tempobolha and temposelecao < tempoinsercao and temposelecao < temposort:
        rapido = temposelecao
        nome = "Ordenação por Seleção"
    elif temposort < tempobolha and temposort < temposelecao and temposort < tempoinsercao:
        rapido = temposort
        nome = "Ordenação com Sort()"
    print("O Ordenador mais rápido neste caso foi o",nome,",com o tempo de:", rapido,"segundos.\n")
    # Imprimimos aqui o algorítmo foi mais rápido no teste.

comando = 1
while comando == 1: #neste passo o laço perguntará se o usuário irá querer fazer outros testes
    comparador()
    comando = int(input("Deseja fazer outro teste?\nDigite 1 para continuar\nou\nDigite 0 para encerrar\n"))
else:
    print("\nComparador encerrado com sucesso!")
    time.sleep(5) #este comando espera 5 segundos para então encerrar o programa


