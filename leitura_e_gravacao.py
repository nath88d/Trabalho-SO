from processo import Processo as P
import os
global tempo_total

def leitura_processos(arquivo):
    try:
        os.remove('./saida.txt')
    except:
        pass
    processos = []
    tempo_total = 0
    with open(arquivo, 'r') as file:
        linhas = file.readlines()
        
        for linha in linhas:
            partes = linha.strip().split()
            print(partes)
            print()
            PID = partes[0]
            entrada = partes[1]
            surtos = partes[2]
            tempo_total += int(surtos)
            IO = []
            for num in partes[3:]:
                if ',' in num:
                    IO.extend(num.split(','))
                else:
                    IO.append(num)
                    
            # Criando uma instância de Processo e adicionando à lista
            processos.append(P(PID, entrada, surtos, IO))
    file.close()
    return [processos, tempo_total]

def salvar_saida(texto):
    with open('saida.txt', 'a') as file:
        file.write(texto)
    return print()
