from leitura_e_gravacao import salvar_saida


def montarGrafico(tabela, tempo, processos=[]):
    saida = ''
    for p in processos:
        if p.num_PID != 9:
            saida += '|        %s         |'%(p.PID)
        else:
            saida += '|        %s          |'%(p.PID)
        for estado in p.Historico:
            if len(estado) == 2:
                saida += '  %s   |'%(estado)
            elif len(estado) == 3:
                saida += '  %s  |'%(estado)
            elif len(estado) == 1:
                saida += '  %s    |'%(estado)
        saida += '\n'
    
    saida += '|     Ciclo CPU     |'  
    for t in range(tempo):
        if t > 9:
            saida += '   %d  |'%(t)
        else:
            saida += '   %d   |'%(t)
    saida += '\n|   Tempo chegada   |'
    for t in range(tempo):
        if t > 8:
            saida += '   %d  |'%(t+1)
        else:
            saida += '   %d   |'%(t+1)

    salvar_saida('\n%s'%(saida), 'grafico', 'w')

    # _______________________________________\n \
    # |   Ciclo     |   |   |   |   |   |   |\n \
    # |    CPU      |   |   |   |   |   |   |\n \
    # |_____________|___|___|___|___|___|___|\n \
    # |   Tempo     |   |   |   |   |   |   |\n \
    # | de chegada  |   |   |   |   |   |   |\n \
    # |_____________|___|___|___|___|___|___|\n \