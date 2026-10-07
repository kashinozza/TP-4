from lista import List

superheroes = [
    {
      "nombre": "Spider-Man",
      "anio_aparicion": 1962,
      "casa": "Marvel",
      "biografia": "Peter Parker fue mordido por una araña radiactiva y obtuvo poderes de superhéroe. Trabaja como fotógrafo freelance en el Daily Bugle mientras protege Nueva York."
    },
    {
      "nombre": "Iron Man",
      "anio_aparicion": 1963,
      "casa": "Marvel",
      "biografia": "Tony Stark, genio multimillonario e inventor, construyó una armadura tecnológica para escapar de sus captores. Fundador de los Vengadores y director de Stark Industries."
    },
    {
      "nombre": "Wolverine",
      "anio_aparicion": 1974,
      "casa": "Marvel",
      "biografia": "Logan posee un esqueleto recubierto de adamantium y garras retráctiles. Su factor de curación acelerada lo hace casi inmortal. Miembro icónico de los X-Men."
    },
    {
      "nombre": "Thor",
      "anio_aparicion": 1962,
      "casa": "DC",
      "biografia": "Dios nórdico del trueno e hijo de Odín. Empuña el martillo Mjolnir y defiende tanto Asgard como la Tierra. Miembro fundador de los Vengadores."
    },
    {
      "nombre": "Black Widow",
      "anio_aparicion": 1964,
      "casa": "Marvel",
      "biografia": "Natasha Romanoff fue entrenada desde niña en el programa Habitación Roja. Es una espía y agente de élite de S.H.I.E.L.D., experta en artes marciales y tecnología."
    },
    {
      "nombre": "Batman",
      "anio_aparicion": 1939,
      "casa": "DC",
      "biografia": "Bruce Wayne presenció el asesinato de sus padres de niño y juró proteger Gotham. Sin poderes, usa su inteligencia, fortuna y entrenamiento físico para combatir el crimen. Usando un traje con muchas herramientas"
    },
    {
      "nombre": "Superman",
      "anio_aparicion": 1938,
      "casa": "DC",
      "biografia": "Kal-El fue enviado desde el planeta Krypton antes de su destrucción. Adoptado como Clark Kent en Kansas, usa sus poderes solares para defender la Tierra."
    },
    {
      "nombre": "Mujer Maravilla",
      "anio_aparicion": 1941,
      "casa": "DC",
      "biografia": "Diana, princesa de las Amazonas de la isla Temyscira, fue criada como guerrera. Porta el lazo de la verdad y las brazaletes indestructibles. Embajadora de paz y justicia."
    },
    {
      "nombre": "The Flash",
      "anio_aparicion": 1956,
      "casa": "DC",
      "biografia": "Barry Allen era un científico forense que fue alcanzado por un rayo durante un experimento. Obtuvo la capacidad de moverse a velocidades superlumínicas conectado a la Fuerza de la Velocidad."
    },
    {
      "nombre": "Green Lantern",
      "anio_aparicion": 1959,
      "casa": "DC",
      "biografia": "Hal Jordan fue elegido por el anillo de poder de los Guardianes del Universo. El anillo le permite crear construcciones de energía verde limitadas solo por su voluntad e imaginación."
    },
    {
        "nombre": "Dr. Strange",
        "anio_aparicion": 1963,
        "casa": "DC",
        "biografia": "Es un mago",
    }
]

class Superhero():

    def __init__(self, nombre, anio, casa, bio):
        self.name = nombre
        self.year = anio
        self.house = casa
        self.bio = bio

    def __str__(self):
        return f"{self.name} - {self.year} - {self.house}"

def by_name(item):
    return item.name

def by_year(item):
    return item.year

list_heroes = List()
list_heroes.add_criterion('name', by_name)
list_heroes.add_criterion('year', by_year)


for hero in superheroes:
    list_heroes.append(
        Superhero(hero['nombre'], hero['anio_aparicion'], hero['casa'], hero['biografia'])
    )


# a. eliminar el nodo que contiene la información de Linterna Verde;

deleted_value = list_heroes.delete_value("Green Lantern", 'name')
print(f'valor eliminado {deleted_value}')

print()

# b. mostrar el año de aparición de Wolverine;

wolverine = list_heroes.search("Wolverine", 'name')
if wolverine is not None:
    print(f'año de aparicion de {list_heroes[wolverine].name} es {list_heroes[wolverine].year}')
else:
    print('no esta en la lista')

# c. cambiar la casa de Dr. Strange a Marvel;

strange = list_heroes.search("Dr. Strange", "name")
if strange is not None:
    list_heroes[strange].house = "Marvel"

    print(f"Dr. Strange queda como: {list_heroes[strange]}")
else:
    print("no está en la lista")

# d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra “traje” o “armadura”;

print('Superhéroes que tienen "traje" o "armadura" en la biografía:')
list_heroes.filter_contain_on_bio(["traje", "armadura"])

# e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963;

print("Superhéroes anteriores a 1963:")
for hero in list_heroes:

    if hero.year < 1963:
        print(f"{hero.name} - {hero.house}")

# f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;

nombres_a_buscar = ["Capitana Marvel", "Mujer Maravilla"]
nombres_en_lista = [hero.name for hero in list_heroes]

for nombre in nombres_a_buscar:

    if nombre in nombres_en_lista:
        hero = next(h for h in list_heroes if h.name == nombre)
        print(f"{hero.name} - {hero.house}")
    else:
        print(f"No se encontró a {nombre}")

# g. mostrar toda la información de Flash y Star-Lord;

nombres = ["The Flash", "Star-Lord"]
for hero in list_heroes:
    if hero.name in nombres:
        print(f"Nombre: {hero.name}")
        print(f"Año de aparición: {hero.year}")
        print(f"Casa: {hero.house}")
        print(f"Biografía: {hero.bio}")
        print()

encontrados = {hero.name for hero in list_heroes}
for nombre in nombres:
    if nombre not in encontrados:
        print(f"No se encontró a {nombre}")

# h. listar los superhéroes que comienzan con la letra B, M y S;

print('Héroes que comienzan con B, M y S:')
list_heroes.filter_start_with(("B", "M", "S"))

# i. determinar cuántos superhéroes hay de cada casa de comic.

print('El recuento de cada casa queda como:')
casas = {}
for hero in list_heroes:
    casas[hero.house] = casas.get(hero.house, 0) + 1

for casa, cantidad in casas.items():
    print(f"{casa}: {cantidad}")