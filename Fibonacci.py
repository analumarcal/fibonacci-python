fibonacci = [0, 1]
numero = 0
continuar = True

for i in range(0, 50):
    push = fibonacci[i] + fibonacci[i + 1] 
    fibonacci.append(push)

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