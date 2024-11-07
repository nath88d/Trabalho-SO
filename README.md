# Escalonador Round Robin

**Visão Geral**

Este projeto é uma simulação de um Escalonador Round Robin. Utilizando conceitos de sistemas operacionais, o simulador organiza processos em uma fila circular, 
realizando uma série de operações para processar cada tarefa de acordo com o tempo de quantum. A execução de cada processo considera ainda operações de I/O e outras 
interrupções.

# Estrutura do Projeto

**entrada.txt:** Arquivo de entrada contendo os processos a serem executados, incluindo PID, tempo de chegada, surtos e operações de I/O.

**main.py:** Contém o código principal da simulação.

**janela.py e janelaGantt.py:** Geram as janelas gráficas para visualização dos processos e do gráfico Gantt.

**Processo.py:** Define a classe Processo, que modela o comportamento dos processos na fila.

**leitura_e_gravacao.py:** Funções auxiliares para leitura do arquivo de entrada e gravação dos resultados.

# Funcionamento

**Entrada:** A simulação carrega processos definidos no entrada.txt, cada linha descreve o PID, tempo de chegada, surtos e I/O.

**Execução dos Processos:** Os processos são executados de acordo com a política Round Robin. Cada processo passa por operações de I/O e pode sofrer interrupções.

**Gráficos e Saídas:**

**Janela de saída:** Mostra o log da execução em tempo real.

**Gráfico Gantt:** Exibe visualmente o estado dos processos ao longo do tempo.

# Como Executar
Execute o arquivo principal "main.py":
As janelas de saída e gráfico serão abertas automaticamente e atualizadas com os resultados.

link do git: #https://github.com/nath88d/Trabalho-SO

# Contribuidores
Ana Beatriz de Souza (24.122.018-5)

Nathan Dantas Mendes (24.122.041-7)

Luísa Graça Barbado (24.122.058-1)
