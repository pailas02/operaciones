
# Importar librerías necesarias
from automata import Automata
import json
import os
import networkx as nx
import matplotlib.pyplot as plt
from tkinter import Tk, Canvas, Frame, BOTH

# Definir clase para graficar autómatas
class AutomataGraph(Frame):
    def __init__(self, parent, automata):
        Frame.__init__(self, parent)
        self.parent = parent
        self.automata = automata
        self.canvas = Canvas(self)
        self.canvas.pack(fill=BOTH, expand=True)
        self.draw_automata()

    def draw_automata(self):
        # Crear un grafo dirigido
        G = nx.DiGraph()

        # Agregar nodos y transiciones al grafo
        for estado in self.automata.getEstados():
            G.add_node(estado.getNombre(), final=estado in self.automata.getEstadosFinales())
            for transicion in self.automata.getTransiciones():
                if transicion.getOrigen() == estado.getNombre():
                    G.add_edge(transicion.getOrigen(), transicion.getDestino(), label=transicion.getSimbolo())

        # Dibujar el grafo
        pos = nx.spring_layout(G)
        nx.draw_networkx_nodes(G, pos, node_size=700, node_color='skyblue')
        nx.draw_networkx_edges(G, pos, width=2, arrows=True)
        nx.draw_networkx_labels(G, pos, font_size=20, font_weight='bold')
        edge_labels = {(n1, n2): d['label'] for n1, n2, d in G.edges(data=True)}
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=16)

        plt.axis('off')
        plt.show()

# Variables globales
automatas = []

# Funciones

def leer_automata(nombre_archivo):
    """
    Lee un archivo json y retorna un objeto automata
    :param nombre_archivo: Nombre del archivo a leer
    :return: Objeto automata
    """
    directorio_automatas = "automatas"
    ruta_completa = os.path.join(directorio_automatas, nombre_archivo) + ".json"
    if os.path.exists(ruta_completa):
        with open(ruta_completa, 'r') as archivo:
            automataJson = json.load(archivo)
            # Crear objeto automata
            automata = Automata()
            automata.cargarAutomata(automataJson)
            # Retornar objeto automata
            return automata
    else:
        print("El archivo no existe")
        return None

def ingresarAutomata():
    """
    Ingresa un automata
    :return: Objeto automata
    """
    print(
        "\nAutómatas disponibles: "
        "\n--------------------------------------------------------------------------------------------------------------------------------"
        "\n01 — Autómata que reciba números pares en binario y los acepte."
        "\n02 — Autómata que reciba números impares en binario y los acepte. "
        "\n--------------------------------------------------------------------------------------------------------------------------------"
        )
    i = int(input("Ingrese numero de automata: "))
    print("--------------------------------------------------------------------------------------------------------------------------------")
    opcion ={
              1: "pares", 2: "impares"
          }
    automata = leer_automata(opcion[i])
    if automata is not None:
        automatas.append(automata)
        automata.mostrarQuintupla()
    else:
        print("El archivo no existe")
    return

def validarCadena():
    """
    Valida una cadena en un automata
    """
    if len(automatas) == 0:
        print("No hay automatas cargados")
        return
    i = int(input("Ingrese el numero del automata que va a usar:"))
    print("-----------------------------------------------------------------------------------------------------------------------------------------")
    cadena = input("Ingrese cadena a validar: ")
    automatas[i-1].mostrarValidacion(cadena)
    return

def unionAutomatas():
    """
    Realiza la union de dos automatas
    """
    if len(automatas) < 2:
        print("No hay automatas suficientes")
        return
    i = int(input("Ingrese el numero del primer automata que va a usar: "))
    print("--------------------------------------------------------------------------------------------------------------------------------")
    j = int(input("Ingrese el numero del segundo automata que va a usar:"))
    resultante = Automata().unionEntreAutomatas(automatas[i-1], automatas[j-1])
    print("---------------------------------------------------------------------------------------------------------------------------------")
    resultante.mostrarQuintupla()
    automatas.append(resultante)
    return

def interseccionAutomatas():
    """
    Realiza la interseccion de dos automatas
    """
    if len(automatas) < 2:
        print("No hay automatas suficientes")
        return
    i = int(input("Ingrese el numero del primer automata que va a usar: "))
    print("--------------------------------------------------------------------------------------------------------------------------------")
    j = int(input("Ingrese el numero del segundo automata que va a usar:"))
    resultante = Automata().interseccionEntreAutomatas(automatas[i-1], automatas[j-1])
    print("--------------------------------------------------------------------------------------------------------------------------------")
    resultante.mostrarQuintupla()
    automatas.append(resultante)
    return

def reversoAutomata():
    """
    Realiza el reverso de un automata
    """
    if len(automatas) == 0:
        print("No hay automatas cargados")
        return
    i = int(input("Ingrese el numero del automata que va a usar: "))
    print("--------------------------------------------------------------------------------------------------------------------------------")
    resultante = Automata().reversoAutomata(automatas[i-1])
    resultante.mostrarQuintupla()
    automatas.append(resultante)
    return

def complementoAutomata():
    """
    Realiza el complemento de un automata
    """
    if len(automatas) == 0:
        print("No hay automatas cargados")
        return
    i = int(input("Ingrese el numero del automata que va a usar: "))
    print("--------------------------------------------------------------------------------------------------------------------------------")
    resultante = Automata().complementoAutomata(automatas[i-1])
    resultante.mostrarQuintupla()
    automatas.append(resultante)
    return

def graficarAutomata():
    """
    Grafica un automata
    """
    if len(automatas) == 0:
        print("No hay automatas cargados")
        return
    i = int(input("Ingrese el numero del automata que va a usar: "))
    print("--------------------------------------------------------------------------------------------------------------------------------")
    root = Tk()
    root.geometry("800x600")
    root.title("Automata")
    # Crea la interfaz gráfica para el automata
    app = AutomataGraph(root, automatas[i-1])
    app.pack(fill=BOTH, expand=True)
    root.mainloop()
    return

def menuOpciones():
    while True:
        print("-------------------------------------------------------------------------------------------------------")
        print(
            "\n                                                       AUTOMATAS"
            "\n--------------------------------------------------------------------------------------------------------------------------------"
            "\n01 — Ingresar un automata                       02 — Validar cadena automata        "
            "\n03 — Realizar la unión entre automatas          04 — Realizar la intersección entre automatas"
            "\n05 — Realizar el reverso de un automata         06 — Realizar el complemento de un automata"
            "\n07 - Gráfica de un automata                     00 — Finalizar programa"
            "\n--------------------------------------------------------------------------------------------------------------------------------"
            )
        opcion ={
            1: ingresarAutomata, 2: validarCadena, 3: unionAutomatas, 4: interseccionAutomatas, 
            5: reversoAutomata, 6: complementoAutomata, 7: graficarAutomata
            }
        i = int(input("Ingrese una opción: "))
        print("-------------------------------------------------------------------------------------------------------")
        if i == 0:
            break
        opcion[i]()

def main():
    print("Bienvenido al programa")
    menuOpciones()

if __name__ == "__main__":
    main()
