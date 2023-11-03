class Monitor:
    def __init__ (self, marca, polegada):
        self.marca = marca
        self.polegada = polegada

    def __str__ (self):
        return f"Monitor da marca {self.marca} com {self.polegada}"

class Computador:
    def __init__ (self, config):
        self.config = config
        self.monitor = None

    def conectaMonitor (self, monitor):
        self.monitor = monitor

    def __str__ (self):
        if self.monitor:
            return f"Computador com a configuração {self.config} está conectado no {self.monitor}"
        else:
            return f"Computador com a configuração {self.config} não está conectado a nenhum monitor"
        
monitor1 = Monitor("LG", "18 polegadas")
pc1 = Computador("I5 4gb de Ram 1Tb")

print(pc1)
print(monitor1)
pc1.conectaMonitor(monitor1)
print(pc1)