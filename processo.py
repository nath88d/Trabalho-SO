class Processo:
    surtos_seguidos = 0

    def __init__(self, PID, chegada, surtos, IO):
        self.PID = PID
        self.num_PID = int(PID[1:])
        self.chegada = int(chegada)
        self.surtos = int(surtos)
        self.interacao = 0
        self.IO = list(map(int,IO))
        self.isFirst = True
        self.encerrado = False

    def encerrar(self):
        self.encerrado = True
        
    def reinicia_surtos(self):
        self.surtos_seguidos = 0
        #is_io = False

    def is_IO(self):
        is_io = False
        for io in self.IO:
            if io == self.interacao:  # (io + 1)
                is_io = True
                self.reinicia_surtos()
                self.IO.pop(0)
        return is_io
    
    def is_Quantum(self):
        if self.surtos_seguidos == 4: # 5a interacao
            self.reinicia_surtos()
            return True
        else:
            return False
            
    def executar(self):
        if not self.isFirst:
            self.surtos -= 1
        self.isFirst = False
        self.interacao += 1
        self.surtos_seguidos += 1
        return "CPU: %s(%d)"%(self.PID,self.surtos)
        
    def __repr__(self):  # Chamado apenas quando utilizar print
        return f"{self.PID}({self.surtos})"
    
    # getters
    def get_PID(self):
        return self.PID
    
    def get_num_PID(self):
        return self.num_PID
    
    def get_chegada(self):
        return self.chegada
    
    def get_surtos(self):
        return self.surtos
    
    def get_interacao(self):
        return self.interacao
    
    def get_IO(self):
        return self.IO
    
    def get_surtos_seguidos(self):
        return self.surtos_seguidos
