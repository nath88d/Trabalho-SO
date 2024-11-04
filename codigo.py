import threading
from time import sleep
from leitura_e_gravacao import *
from janela import Saida
import tkinter as tk
saida = ''

arquivo = leitura_processos('entrada.txt')
processos = arquivo[0] # Extrai informacoes dos processos do arquivo
tempo = arquivo[1] # Extrai a quantidade de surtos para contabilizar o tempo
quantum = 4
Fila = []
executando = 0

def criar_janela():
    menu = tk.Tk()
    janela = Saida(menu)
    menu.mainloop()
        
def inserir_fila(processo, tempo): # Operacao IO | Prioridade da Fila -> quem sofre IO
    global executando
    global processos
    #################################################
                # Variaveis temporarias
    resultadoExtra = ''
    resultadoFila = 'Nao ha processos na fila'
    resultadoCPU = ''
    #################################################
                # Condicoes
    chegada_do_processo = (processo.chegada == tempo) 
    sofre_IO = processo.is_IO()                          
    sofre_Quantum = processo.is_Quantum()
    esta_executando = (executando == processo.num_PID)
    fim_de_surtos = (processo.surtos == 1)
    #################################################
    
    if chegada_do_processo:             # Condicao de chegada
        if executando != 0:             # Caso algum processo esteja rodando
            print(processo.num_PID)
            Fila.append(processo)
            resultadoExtra += '#[evento] CHEGADA <%s>'%(processo.PID)

    if not sofre_IO and not sofre_Quantum and esta_executando and not fim_de_surtos: # Apenas executa o processo caso nao sofra nenhuma interrupcao
        resultadoCPU = executa(processo)# Executa o processo atual
        
    elif sofre_Quantum and esta_executando and not (fim_de_surtos or processo.encerrado):# Caso sofra Quantum
        if len(Fila) > 0:
            temp_processo = Fila[0] 
            Fila.pop(0)
            executando = temp_processo.num_PID
            Fila.append(processo)
            resultadoExtra += '#[evento] FIM Quantum <%s>'%(processo.PID)
            if processo.num_PID < temp_processo.num_PID:
                resultadoCPU = executa(processo)# Executa o proximo processo
            else:
                resultadoCPU = executa(temp_processo)# Executa o proximo processo
                
        else:                                                   # Caso tenha chegado ao fim da fila
            resultadoExtra += '#[evento] FIM Quantum <%s>'%(processo.PID)
            resultadoCPU = executa(processo)# Executa o proximo processo
                
    elif sofre_IO and esta_executando and not (fim_de_surtos or processo.encerrado):# Caso sofra I/O
        if len(Fila) > 0:
            temp_processo = Fila[0] 
            Fila.pop(0)
            executando = temp_processo.num_PID
            Fila.append(processo)
            resultadoExtra += '#[evento] OPERACAO I/O <%s>'%(processo.PID)
            if processo.num_PID < temp_processo.num_PID:
                resultadoCPU = executa(processo)# Executa o proximo processo
            else:
                resultadoCPU = executa(temp_processo)# Executa o proximo processo
                
        else:                                            # Caso tenha chegado ao fim da fila
            resultadoExtra += '#[evento] OPERACAO I/O <%s>'%(processo.PID)
            resultadoCPU = executa(processo)# Executa o processo atual
                
    elif fim_de_surtos and esta_executando and not processo.encerrado: # Caso o processo tenha chegado ao fim
        if len(Fila) > 0:
            temp_processo = Fila[0] 
            Fila.pop(0)
            processo.encerrar()
            executando = temp_processo.num_PID
            resultadoExtra += '#[evento] ENCERRANDO <%s>'%(processo.PID)
            if processo.num_PID < temp_processo.num_PID:
                    resultadoCPU = executa(processo)# Executa o proximo processo
            else:
                resultadoCPU = executa(temp_processo)# Executa o proximo processo
                
        else:                                           # Caso tenha chegado ao fim da fila
            processo.encerrar()
            executando = 0
            resultadoExtra += '#[evento] ENCERRANDO <%s>'%(processo.PID)
            resultadoCPU = executa(processo)# Executa o processo atual
            
    if tempo == 0 and chegada_do_processo:# Executado somente no primeiro tempo 
        executando = processo.num_PID
        resultadoCPU = processo.executar()
        
    resultadoFila = 'FILA: %s'%(Fila) if (len(Fila) != 0) else '' # Retorna o resultado da fila final
    return  resultadoExtra, resultadoFila, resultadoCPU # Retorna as string para mais tarde serem organizadas

def resultado(resultadoExtra, resultadoFila, resultadoCPU): # Saida dos resultados
    global saida
    if not resultadoExtra == None and not resultadoFila == None: 
        saida += resultadoExtra + resultadoFila +'\n'+ resultadoCPU +'\n'
    elif not resultadoExtra == None: 
        saida += resultadoExtra + resultadoCPU +'\n'
    elif not resultadoFila == None:
        saida += resultadoFila +'\n'+ resultadoCPU +'\n'
    else:
        saida += 'Nao ha processos na fila' +'\n'+ resultadoCPU +'\n'
    return
    
    
def executa(processo):
    global executando
    return processo.executar() if (processo.num_PID == executando) else ''

# Main
salvar_saida("***********************************\n\
***** ESCALONADOR ROUND ROBIN *****\n\
-----------------------------------\n\
------- INICIANDO SIMULACAO -------\n\
-----------------------------------\n")

threading.Thread(target=criar_janela).start()

for t in range(tempo + 1):
    saida = '********** TEMPO %d **************\n'%(t)
    resultadoExtra = ''
    resultadoFila = 'Nao ha processos na fila'
    resultadoCPU = ''
    for processo in processos:
        tempExtra, tempFila, tempCPU = inserir_fila(processo,t)
        if tempCPU != '':
            resultadoCPU = tempCPU
        if tempFila != '' and tempFila != None :
            resultadoFila = tempFila
        if tempExtra != '':
            resultadoExtra += tempExtra + '\n' if not tempExtra == None else ''
    resultado(resultadoExtra, resultadoFila, resultadoCPU)
    if(executando == 0):
        saida += "ACABARAM OS PROCESSOS!!!\n\
-----------------------------------\n\
------- Encerrando simulacao ------\n\
-----------------------------------\n"
    salvar_saida(saida +"\n")
    sleep(1)
