class Processo:
    def __init__(self, PID, surtos, IO):
        self.PID = PID
        self.surtos = surtos
        self.IO = IO

    def __repr__(self):
        #return f"Processo(PID='{self.PID}', numeros={self.numeros})"
        return f"CPU: {self.PID}({self.surto})"