class Automata:
    def __init__(self):
        self.estados = []
        self.estado_inicial = None
        self.estados_finales = []
        self.transiciones = []

    def cargarAutomata(self, automata_json):
        self.estados = automata_json.get("estados", [])
        self.estado_inicial = automata_json.get("estado_inicial")
        self.estados_finales = automata_json.get("estados_finales", [])
        self.transiciones = automata_json.get("transiciones", [])
        
    def agregarEstado(self, estado):
        self.estados.append(estado)
        
    def agregarEstadoFinal(self, estado):     
        self.estados_finales.append(estado) 
  
    def getEstados(self):
        return self.estados

    def getEstadoInicial(self):
        return self.estado_inicial

    def getEstadosFinales(self):
        return self.estados_finales

    def getTransiciones(self):
        return self.transiciones

    def mostrarQuintupla(self):
        print("Estados:", self.estados)
        print("Estado inicial:", self.estado_inicial)
        print("Estados finales:", self.estados_finales)
        print("Transiciones:")
        for transicion in self.transiciones:
            print(transicion)

    def mostrarValidacion(self, cadena):
        estado_actual = self.estado_inicial
        for simbolo in cadena:
            transicion_valida = False
            for transicion in self.transiciones:
                if transicion.getOrigen() == estado_actual and transicion.getSimbolo() == simbolo:
                    estado_actual = transicion.getDestino()
                    transicion_valida = True
                    break
            if not transicion_valida:
                print("La cadena no es válida")
                return
        if estado_actual in self.estados_finales:
            print("La cadena es válida")
        else:
            print("La cadena no es válida")

    def unionEntreAutomatas(self, automata1, automata2):
        nuevo_automata = Automata()

        # Combinar estados
        nuevo_automata.estados = automata1.estados + automata2.estados

        # Establecer nuevo estado inicial
        nuevo_automata.estado_inicial = "q0"
        nuevo_automata.estados.append(nuevo_automata.estado_inicial)

        # Combinar estados finales
        nuevo_automata.estados_finales = automata1.estados_finales + automata2.estados_finales

        # Combinar transiciones
        nuevo_automata.transiciones = automata1.transiciones + automata2.transiciones

        return nuevo_automata

    def interseccionEntreAutomatas(self, automata1, automata2):
        nuevo_automata = Automata()

        # Combinar estados
        nuevo_automata.estados = automata1.estados + automata2.estados

        # Establecer nuevo estado inicial
        nuevo_automata.estado_inicial = "q0"
        nuevo_automata.estados.append(nuevo_automata.estado_inicial)

        # Combinar estados finales
        nuevo_automata.estados_finales = automata1.estados_finales + automata2.estados_finales

        # Combinar transiciones
        nuevo_automata.transiciones = automata1.transiciones + automata2.transiciones

        return nuevo_automata

    def reversoAutomata(self, automata):
        nuevo_automata = Automata()

        # Copiar estados
        nuevo_automata.estados = automata.estados

        # Establecer nuevo estado inicial
        nuevo_automata.estado_inicial = "q0"
        nuevo_automata.estados.append(nuevo_automata.estado_inicial)

        # Intercambiar estados finales y no finales
        nuevo_automata.estados_finales = [estado for estado in automata.estados if estado not in automata.estados_finales]

        # Invertir transiciones
        for transicion in automata.transiciones:
            nuevo_transicion = Transicion(transicion.getDestino(), transicion.getSimbolo(), transicion.getOrigen())
            nuevo_automata.transiciones.append(nuevo_transicion)

        return nuevo_automata

    def complementoAutomata(self, automata):
        nuevo_automata = Automata()

        # Copiar estados
        nuevo_automata.estados = automata.estados

        # Establecer nuevo estado inicial
        nuevo_automata.estado_inicial = "q0"
        nuevo_automata.estados.append(nuevo_automata.estado_inicial)

        # Establecer estados finales como no finales y viceversa
        nuevo_automata.estados_finales = [estado for estado in automata.estados if estado not in automata.estados_finales]

        # Copiar transiciones
        nuevo_automata.transiciones = automata.transiciones

        return nuevo_automata


class Transicion:
    def __init__(self, origen, simbolo, destino):
        self.origen = origen
        self.simbolo = simbolo
        self.destino = destino

    def getOrigen(self):
        return self.origen

    def getSimbolo(self):
        return self.simbolo

    def getDestino(self):
        return self.destino

    def __str__(self):
        return f"{self.origen} --({self.simbolo})--> {self.destino}"
