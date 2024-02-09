# Vetores e variáveis
fibonacci = [0, 1]
fibonacciExibir = []
numero = 0
continuar = True

# Criando o vetor que contém a sequência de Fibonacci
for i in range(0, 100):
    push = fibonacci[i] + fibonacci[i + 1] 
    fibonacci.append(push)

# Parte do sistema onde o usuário insere um valor inteiro e o sistema valida se este valor faz parte ou não da sequência de Fibonacci
while continuar:
    try:
        numero = int(input("Digite um número inteiro para descobrir se ele faz parte da sequência de Fibonacci: "))
        if numero in fibonacci:
            print(f"O número {numero} faz parte da sequência de Fibonacci.")
        else:
            print(f"O número {numero} faz parte da sequência de Fibonacci.")
        finalizar = int(input("Você deseja inserir outro número? 1-Sim 2-Não: "))
        if finalizar == 1:
            continuar = True
        elif finalizar == 2:
            print("Até logo.")
            continuar = False
    except TypeError:
        print("Digite um número inteiro e válido!")
    except ValueError:
        print("Digite um número inteiro e válido!")
 
# Criando vetor que guarda apenas os 10 primeiros valores da sequência de Fibonacci
for i in range(0, 9):
    fibonacciExibir.append(fibonacci[i])
    
# Exibbindo os 10 primeiros valores da sequência de Fibonacci
print(f"10 primeiros valores da sequência de Fibonacci: {fibonacciExibir}.")