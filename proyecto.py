import heapq

def dijkstra(grafo,origen,destino):

    distancias = {nodo: float('inf') for nodo in grafo} 
    distancias[origen] = 0 
    
    padres = {nodo: None for nodo in grafo} 
    cola = [(0, origen)] 

    while cola:

        dias_actuales, isla_actual = heapq.heappop(cola) 

        if isla_actual == destino: 
            break 

        if dias_actuales > distancias[isla_actual]: 
            continue 

        for vecino in grafo[isla_actual]: 

            isla_vecina = vecino['destino']
            dias_viaje = vecino['dias']
            nuevos_dias = dias_actuales + dias_viaje 

            if nuevos_dias < distancias[isla_vecina]: 
                distancias[isla_vecina] = nuevos_dias
                padres[isla_vecina] = isla_actual 
                heapq.heappush(cola, (nuevos_dias, isla_vecina))

    ruta = [] 
    nodo_actual = destino

    while nodo_actual is not None:
        ruta.append(nodo_actual) 
        nodo_actual = padres[nodo_actual]

    ruta.reverse()
    return distancias[destino], ruta

def main():

    N, M = map(int, input().split())
    
    Pinicial, C = map(int, input().split())
    origen, destino = input().split()

    grafo = {}
    
    for _ in range(M):

        isla1, isla2, dias = input().split()
        dias = int(dias)

        if isla1 not in grafo:
            grafo[isla1] = []
        if isla2 not in grafo:
            grafo[isla2] = []

        grafo[isla1].append({'destino': isla2, 'dias': dias})
        grafo[isla2].append({'destino': isla1, 'dias': dias})

    dias_totales, ruta_final = dijkstra(grafo, origen, destino)

    print(f"{' -> '.join(ruta_final)}") 

    consumo_total = dias_totales * C 
    Rfinal = Pinicial - consumo_total 

    if Rfinal > 0: 
        print(f"Atenea los guió sabiamente en {dias_totales} dias. Provisiones restantes: {Rfinal}") 

    elif Rfinal < 0: 
        print("Los hombres no sobrevivieron a la furia de Poseidón, lamentablemente todos han perecido en el viaje, Atenea se encuentra decepcionada") 

    elif Rfinal == 0: 
        print(f"Los hombres llegaron a su hogar con lo justo. Atenea los guió en {dias_totales} días a su destino ")

if __name__ == "__main__":
    main()