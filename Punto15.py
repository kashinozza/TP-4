entrenadores = [
    ["Ash", 5, 10, 40, [
        ["Pikachu", 50, "electrico", "ninguno"],
        ["Charizard", 55, "fuego", "volador"],
        ["Bulbasaur", 30, "planta", "veneno"],
        ["Squirtle", 28, "agua", "ninguno"],
    ]],
    ["Misty", 2, 15, 25, [
        ["Starmie", 45, "agua", "psiquico"],
        ["Wingull", 20, "agua", "volador"],
        ["Goldeen", 18, "agua", "ninguno"],
    ]],
    ["Brock", 4, 8, 32, [
        ["Onix", 48, "roca", "tierra"],
        ["Geodude", 25, "roca", "tierra"],
        ["Geodude", 22, "roca", "tierra"],
        ["Vulpix", 35, "fuego", "ninguno"],
    ]],
    ["Gary", 6, 5, 45, [
        ["Blastoise", 60, "agua", "ninguno"],
        ["Umbreon", 52, "siniestro", "ninguno"],
        ["Alakazam", 58, "psiquico", "ninguno"],
        ["Arcanine", 56, "fuego", "ninguno"],
    ]],
    ["Dawn", 3, 12, 28, [
        ["Piplup", 32, "agua", "ninguno"],
        ["Buneary", 24, "normal", "ninguno"],
        ["Togekiss", 40, "hada", "volador"],
    ]],
    ["Cynthia", 8, 3, 60, [
        ["Garchomp", 70, "dragon", "tierra"],
        ["Milotic", 65, "agua", "ninguno"],
        ["Lucario", 68, "lucha", "acero"],
        ["Spiritomb", 62, "fantasma", "siniestro"],
        ["Roserade", 60, "planta", "veneno"],
        ["Togekiss", 64, "hada", "volador"],
    ]],
]

def buscar_entrenador(entrenadores, nombre):
    for entrenador in entrenadores:
        if entrenador[0] == nombre:
            return entrenador
    return None


# a. obtener la cantidad de Pokémons de un determinado entrenador
def buscar_entrenador(entrenadores, nombre):
    for entrenador in entrenadores:
        if entrenador[0].lower() == nombre.lower():
            return entrenador
    return None

def cantidad_pokemon(entrenadores, nombre):
    entrenador = buscar_entrenador(entrenadores, nombre)
    return len(entrenador[4]) if entrenador else 0

nombre = input("Ingresá el nombre del entrenador: ")
cantidad = cantidad_pokemon(entrenadores, nombre)

if cantidad > 0:
    print(f"{nombre} tiene {cantidad} Pokémon.")
else:
    print(f"No se encontró al entrenador {nombre}.")


# b. entrenadores con más de tres torneos ganados
def entrenadores3torneos(entrenadores):
    return [e[0] for e in entrenadores if e[1] > 3]

ganadores = entrenadores3torneos(entrenadores)

print("Entrenadores con más de tres torneos ganados:")
for entrenador in ganadores:
    print(f"- {entrenador}")


# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados
def pokemon_mayor_nivel(entrenadores):
    mejor = max(entrenadores, key=lambda e: e[1])
    return mejor, max(mejor[4], key=lambda p: p[1])

mejor_entrenador, mejor_pokemon = pokemon_mayor_nivel(entrenadores)

print(f"El entrenador con más torneos ganados es {mejor_entrenador[0]} "
      f"con {mejor_entrenador[1]} torneos.")
print(f"Su Pokémon de mayor nivel es {mejor_pokemon[0]}.")

# d. mostrar todos los datos de un entrenador y sus Pokémon
def mostrar_entrenador(entrenadores, nombre):
    entrenador = buscar_entrenador(entrenadores, nombre)
    if not entrenador:
        print(f"No se encontró al entrenador {nombre}.")
        return
    print(f"Entrenador: {entrenador[0]}")
    print(f"Torneos ganados: {entrenador[1]}")
    print(f"Batallas perdidas: {entrenador[2]}")
    print(f"Batallas ganadas: {entrenador[3]}")
    print("Pokémon:")
    for pokemon in entrenador[4]:
        print(f"  - {pokemon[0]} (nivel {pokemon[1]}, tipo {pokemon[2]}, subtipo {pokemon[3]})")

nombre = input("Ingresá el nombre del entrenador: ")
mostrar_entrenador(entrenadores, nombre)


# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %
def porcentaje_batallas(entrenador):
    total = entrenador[2] + entrenador[3]
    return (entrenador[3] / total * 100) if total > 0 else 0


def entrenadores_mayor_79(entrenadores):
    return [e[0] for e in entrenadores if porcentaje_batallas(e) > 79]

ganadores = entrenadores_mayor_79(entrenadores)

print("Entrenadores con más del 79% de batallas ganadas:")
for entrenador in ganadores:
    print(f"- {entrenador}")


# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador (tipo y subtipo)
def fuego_y_planta(entrenador):
    tipos = [p[2] for p in entrenador[4]]
    return "fuego" in tipos and "planta" in tipos


def agua_volador(entrenador):
    return any(p[2] == "agua" and p[3] == "volador" for p in entrenador[4])


def entrenadores_fuego_planta_o_agua_volador(entrenadores):
    return [e[0] for e in entrenadores
            if fuego_y_planta(e) or agua_volador(e)]

resultado = entrenadores_fuego_planta_o_agua_volador(entrenadores)

print("Entrenadores con pokémon de tipo fuego y planta, o agua/volador:")
for entrenador in resultado:
    print(f"- {entrenador}")


# g. el promedio de nivel de los Pokémons de un determinado entrenador
def promedio_nivel_pokemon(entrenadores, nombre):
    entrenador = buscar_entrenador(entrenadores, nombre)
    if not entrenador or not entrenador[4]:
        return 0
    return sum(p[1] for p in entrenador[4]) / len(entrenador[4])


nombre = input("Ingresá el nombre del entrenador: ")
promedio = promedio_nivel_pokemon(entrenadores, nombre)

if promedio > 0:
    print(f"El promedio de nivel de los pokémon de {nombre} es {promedio}.")
else:
    print(f"No se encontró al entrenador {nombre}.")


# h. determinar cuántos entrenadores tienen a un determinado Pokémon
def cuantos_tienen_pokemon(entrenadores, nombre_pokemon):
    return sum(1 for e in entrenadores if any(p[0].lower() == nombre_pokemon.lower() for p in e[4]))


nombre_pokemon = input("Ingresá el nombre del pokémon: ")
cantidad = cuantos_tienen_pokemon(entrenadores, nombre_pokemon)

print(f"{cantidad} entrenador(es) tienen a {nombre_pokemon}.")


# i. mostrar los entrenadores que tienen Pokémon repetidos
def pokemon_repetidos(entrenadores):
    resultado = []
    for e in entrenadores:
        nombres = [p[0] for p in e[4]]
        if len(nombres) != len(set(nombres)):
            resultado.append(e[0])
    return resultado


repetidos = pokemon_repetidos(entrenadores)

print("Entrenadores con pokémon repetidos:")
for entrenador in repetidos:
    print(f"- {entrenador}")


# j. determinar los entrenadores que tengan uno de los siguientes Pokémon: Tyrantrum, Terrakion o Wingull
def pokemon_especificos(entrenadores):
    objetivo = {"Tyrantrum", "Terrakion", "Wingull"}
    return [e[0] for e in entrenadores if any(p[0] in objetivo for p in e[4])]


especificos = pokemon_especificos(entrenadores)

print("Entrenadores con Tyrantrum, Terrakion o Wingull:")
for entrenador in especificos:
    print(f"- {entrenador}")


# k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador como del Pokémon deben ser ingresados;
# además si el entrenador tiene al Pokémon se deberán mostrar los datos de ambos
def entrenador_tiene_pokemon(entrenadores, nombre_entrenador, nombre_pokemon):
    entrenador = buscar_entrenador(entrenadores, nombre_entrenador)
    if not entrenador:
        print(f"No se encontró al entrenador {nombre_entrenador}.")
        return
    for pokemon in entrenador[4]:
        if pokemon[0].lower() == nombre_pokemon.lower():
            print(f"Entrenador: {entrenador[0]}, torneos: {entrenador[1]}, "
                  f"ganadas: {entrenador[3]}, perdidas: {entrenador[2]}")
            print(f"Pokémon: {pokemon[0]}, nivel {pokemon[1]}, "
                  f"tipo {pokemon[2]}, subtipo {pokemon[3]}")
            return
    print(f"{nombre_entrenador} no tiene a {nombre_pokemon}.")


nombre_entrenador = input("Ingresá el nombre del entrenador: ")
nombre_pokemon = input("Ingresá el nombre del pokémon: ")
entrenador_tiene_pokemon(entrenadores, nombre_entrenador, nombre_pokemon)