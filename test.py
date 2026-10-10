import heapq # Importamos la librería heapq que nos ayuda a elegir siempre el camino más corto disponible

def dijkstra(grafo,origen,destino):
    # Diccionario para guardar el récord de menos días para llegar a cada isla
    distancias = {nodo: float('inf') for nodo in grafo} 
    
    # La distancia para llegar a la isla donde ya estamos (origen) es 0 días
    distancias[origen] = 0 
    
    # Diccionario vital para recordar de qué isla venimos y así reconstruir la ruta final
    padres = {nodo: None for nodo in grafo} 
    
    # Cola de prioridad: una lista que se ordenará sola para explorar primero la isla más cercana
    cola = [(0, origen)] # Guardamos una pareja: (días_acumulados, nombre_de_la_isla)

    while cola: # Mientras haya islas en la cola esperando ser exploradas...
        
        # Sacamos de la cola la isla que tiene menos días de viaje acumulados hasta el momento
        dias_actuales, isla_actual = heapq.heappop(cola) 

        # Si la isla que acabamos de sacar es nuestro destino final, terminamos la búsqueda
        if isla_actual == destino: 
            break 

        # Si los días que sacamos de la cola son mayores al récord actual, ignoramos este camino (es ineficiente)
        if dias_actuales > distancias[isla_actual]: 
            continue 

        # Si es un buen camino, revisamos todas las islas vecinas conectadas a nuestra isla actual
        for vecino in grafo[isla_actual]: 
            isla_vecina = vecino['destino'] # Extraemos el nombre de la isla vecina
            dias_viaje = vecino['dias'] # Extraemos cuántos días toma viajar hacia ella
            
            # Calculamos cuántos días llevaría el viaje total si pasamos por esta nueva ruta
            nuevos_dias = dias_actuales + dias_viaje 

            # Si este nuevo cálculo es mejor (menor) que el récord anterior que teníamos para esa isla vecina...
            if nuevos_dias < distancias[isla_vecina]: 
                distancias[isla_vecina] = nuevos_dias # Actualizamos el récord con el nuevo número menor de días
                padres[isla_vecina] = isla_actual # Anotamos que llegamos a esta vecina viniendo desde la isla actual
                heapq.heappush(cola, (nuevos_dias, isla_vecina)) # Metemos la vecina a la cola para explorarla después

    # --- FASE DE RECONSTRUCCIÓN DE LA RUTA ---
    ruta = [] # Creamos una lista vacía para guardar los nombres de las islas en orden
    nodo_actual = destino # Empezamos el rastreo desde el final (el destino)

    while nodo_actual is not None: # Mientras exista una isla anterior en nuestro historial...
        ruta.append(nodo_actual) # Agregamos la isla actual a nuestra lista de ruta
        nodo_actual = padres[nodo_actual] # Retrocedemos un paso hacia la isla de donde vinimos

    ruta.reverse() # Como rastreamos desde el destino al origen, invertimos la lista para que quede al derecho

    # El algoritmo devuelve dos cosas: el total de días que tomó el viaje, y la lista con la ruta exacta
    return distancias[destino], ruta

def main():
    # 1. Leemos N (islas) y M (rutas)
    # Entrada esperada: "5 6"
    N, M = map(int, input().split())
    
    # 2. Leemos las provisiones (Pinicial) y el consumo (C)
    # Entrada esperada: "100 5"
    Pinicial, C = map(int, input().split())
    
    # 3. Leemos el origen y destino del viaje
    # Entrada esperada: "Troya Itaca"
    origen, destino = input().split()
    
    # 4. Inicializamos nuestro grafo como un diccionario (Lista de Adyacencia)
    grafo = {}
    
    # 5. Leemos las M líneas de las rutas
    for _ in range(M):
        # Entrada esperada por línea: "Troya Delos 2"
        isla1, isla2, dias = input().split()
        dias = int(dias)
        
        # Si la isla no existe en el grafo, la inicializamos con una lista vacía
        if isla1 not in grafo:
            grafo[isla1] = []
        if isla2 not in grafo:
            grafo[isla2] = []
            
        # Como el grafo es NO DIRIGIDO, conectamos la isla1 con la isla2 y viceversa
        grafo[isla1].append({'destino': isla2, 'dias': dias})
        grafo[isla2].append({'destino': isla1, 'dias': dias})

    # Llamamos a nuestro algoritmo pasándole el mapa (grafo), el inicio y el fin
    dias_totales, ruta_final = dijkstra(grafo, origen, destino)

# ---------------- FASE 3: LÓGICA DE SUPERVIVENCIA ----------------
    
    # Imprimimos la primera línea obligatoria del proyecto: los nombres de las islas separados por flechas
    print(f"{' -> '.join(ruta_final)}") 
    
    # Calculamos cuánta comida se gastó en total (días de viaje multiplicados por el consumo diario)
    consumo_total = dias_totales * C 
    
    # Calculamos la comida sobrante (provisiones iniciales menos el consumo total)
    Rfinal = Pinicial - consumo_total 
    
    # Evaluamos si la comida sobrante es mayor a 0 (les sobró comida)
    if Rfinal > 0: 
        # Imprimimos el mensaje de éxito exacto del pdf reemplazando las variables
        print(f"Atenea los guió sabiamente en {dias_totales} dias. Provisiones restantes: {Rfinal}") 
        
    # Evaluamos si la comida sobrante es menor a 0 (se quedaron sin comida antes de llegar)
    elif Rfinal < 0: 
        # Imprimimos el mensaje exacto de fracaso del pdf
        print("Los hombres no sobrevivieron a la furia de Poseidón, lamentablemente todos han perecido en el viaje, Atenea se encuentra decepcionada") 
        
    # Evaluamos si la comida sobrante es exactamente 0 (llegaron vivos pero sin nada de comida)
    elif Rfinal == 0: 
        # Imprimimos el mensaje exacto de llegar "con lo justo"
        print(f"Los hombres llegaron a su hogar con lo justo. Atenea los guió en {dias_totales} días a su destino ")

# Este bloque verifica si el script se está ejecutando directamente y llama a main()
if __name__ == "__main__":
    main()