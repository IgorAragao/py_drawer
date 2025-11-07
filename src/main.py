import random

## variavel que acomoda os nomes a serem sorteados
names_input = input("Digite os nomes a serem sorteados separados por espaço: ").split()

## variavel que acomoda os nomes que ja foram sorteados
names_drawn = []


## funcao de sortear
def drawer():

    ## garantir que a acao de sortaer apenas execute enquanto tiver nomes
    while len(names_input) > 0:

        start = input('Sortear? (Sim ou Não): ')
        
        if start.lower() == 'sim':
            
            ## escolhe uma posicao aleatoria dentro do array
            num = random.randrange(0, len(names_input))
            name = names_input[num]
            
            ## adiciona o nome sorteado na variavel de controle
            names_drawn.append(name)
            
            ## remove o nome sorteado da fila
            names_input.remove(name)
            
            print (f'Nome sorteado: {name}')
            print (f'Nomes já sorteados: {names_drawn}')
            print (f'Nomes faltantes: {names_input}')
        
        else:
            ## encerra o script
            print ('py_drawer encerrado!')
            exit()


def main():
    drawer()


if __name__ == "__main__":
    main()