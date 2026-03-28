# ---------------------------------------------
# SISTEMA INTELIGENTE DE RUTAS DE TRANSPORTE
# Autor: Yorquis Murillo
# ---------------------------------------------

# Se importa deque para manejar la cola del algoritmo BFS
from collections import deque

# ---------------------------------------------
# BASE DE CONOCIMIENTO
# Representa el sistema de transporte como un grafo
# Cada estación tiene conexiones con otras estaciones
# ---------------------------------------------
transporte = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F", "G"],
    "F": ["C", "E", "H"],
    "G": ["E", "H"],
    "H": ["F", "G"]
}

# ---------------------------------------------
# REGLA LÓGICA
# Permite verificar si existe conexión directa
# entre dos estaciones
# ---------------------------------------------
def estan_conectados(origen, destino):
    return destino in transporte.get(origen, [])

# ---------------------------------------------
# ALGORITMO DE BÚSQUEDA (BFS)
# Encuentra la ruta más corta entre dos nodos
# ---------------------------------------------
def buscar_ruta(inicio, destino):
    
    # Cola para almacenar los nodos a explorar
    cola = deque()
    cola.append((inicio, [inicio]))

    # Conjunto de nodos visitados
    visitados = set()

    # Mientras existan nodos por explorar
    while cola:
        nodo_actual, ruta = cola.popleft()

        # Si llegamos al destino, retornamos la ruta
        if nodo_actual == destino:
            return ruta

        # Evitar procesar nodos repetidos
        if nodo_actual not in visitados:
            visitados.add(nodo_actual)

            # Explorar vecinos del nodo actual
            for vecino in transporte[nodo_actual]:
                nueva_ruta = list(ruta)
                nueva_ruta.append(vecino)
                cola.append((vecino, nueva_ruta))

    # Si no existe ruta
    return None

# ---------------------------------------------
# FUNCIÓN PRINCIPAL
# ---------------------------------------------
def main():
    print("\nSISTEMA INTELIGENTE DE RUTAS\n")

    inicio = input("Ingrese punto de origen: ").upper()
    destino = input("Ingrese punto de destino: ").upper()

    ruta = buscar_ruta(inicio, destino)

    if ruta:
        print("\nRuta encontrada:")
        print(" -> ".join(ruta))
    else:
        print("\nNo existe ruta disponible")

# Ejecutar el programa
if __name__ == "__main__":
    main()