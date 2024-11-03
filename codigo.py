from processo import Processo
        


def ler_processos(arquivo):
    processos = []
    with open(arquivo, 'r') as file:
        linhas = file.readlines()
        
        for linha in linhas:
            partes = linha.strip().split()
            id_processo = partes[0]
            numeros = []
            
            for num in partes[1:]:
                if ',' in num:
                    numeros.extend(num.split(','))
                else:
                    numeros.append(num)
                    
            # Criando uma instância de Processo e adicionando à lista
            processos.append(Processo(id_processo, numeros))
    
    return processos


processos = ler_processos('dados.txt')

# Exibindo os processos
for processo in processos:
    print(processo)
