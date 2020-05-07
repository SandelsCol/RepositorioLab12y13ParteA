import random

#Creación de la función imprimir 
cartas = ["Payne" , "Hendrix" , "Stone", "Coffey" , "Whitaker" , "Pope" , "Bleach" , "Arc" , "Fleming" , "Hardin" , "Robiar" , "Mccullough" , "Mooney" , "Reynolds" , "Short" , "Stanton" , "Deadman" , "Stonehammer" , "Smith" , "Patrick", "Crane" , "Cargane" , "Powers" , "Wade" , "Joseph" , "Savage" , "Houston", "Merritt" , "Nuke" , "Barnett" , "Acosta" , "Duke" , "Sellers" , "Blake", "Schneider" , "Stone" , "Cannon" , "Garrison" , "Randall" , "Leon" , "Buck" , "Shannon" , "Delaney" , "Mckinney" , "Dodademocles" , "Flowers" , "Whitehead" , "Kirby" , "Park" , "Shannon" , "Vlad" , "Pepin" , "Mcguire" , "Murray" , "Rush" , "Aramis" , "Fletcher" , "Mcfadden" , "Deleon" , "Luke" , "Lindsay" , "Payne" , "Gerbvo" , "Hubbard" , "Burnett" , "Bryan" , "Ratliff" , "Carlson" , "Parsons" , "Deadmeat" , "Crimson", "Wilson" , "Terry" , "Hancock" , "Hightower" , "Burns" , "Austin" , "Nightwalker" , "Thetis" , "Owen" , "Tate" , "Simmons" , "Grant" , "Barber" , "Talos" , "Ashes" , "Alston" , "Clayton" , "Mcbride" , "Huffman" , "Lightbringer" , "Blankenship" , "Higgins" , "Saint" , "Graham" , "Hodor" , "Ellison" , "Roberts" , "Odom" , "Mann"]
premium = ["AIVLIS", "LEIRBAG", "NAILUJ", "SOLRAC", "ANAID"]
Conteo_final_Normal= len(cartas)
Conteo_final_premium= len(premium)
def imprimir(x,y):
    Conteo_final_=  Conteo_final_Normal + Conteo_final_premium
    print("El numero de cartas normales es",Conteo_final_Normal,",El de cartas premium es",Conteo_final_premium,"Y en total del juego son",Conteo_final_,"Cartas")
    print("Estas son las cartas estandares",cartas,"y a continuación las premium",premium)
imprimir(Conteo_final_Normal,Conteo_final_premium)

#Creación de la función generador/Relación de cartas con generador
def generador(n,p):

        cartas = ["Payne" , "Hendrix" , "Stone", "Coffey" , "Whitaker" , "Pope" , "Bleach" , "Arc" , "Fleming" , "Hardin" , "Robiar" , "Mccullough" , "Mooney" , "Reynolds" , "Short" , "Stanton" , "Deadman" , "Stonehammer" , "Smith" , "Patrick", "Crane" , "Cargane" , "Powers" , "Wade" , "Joseph" , "Savage" , "Houston", "Merritt" , "Nuke" , "Barnett" , "Acosta" , "Duke" , "Sellers" , "Blake", "Schneider" , "Stone" , "Cannon" , "Garrison" , "Randall" , "Leon" , "Buck" , "Shannon" , "Delaney" , "Mckinney" , "Dodademocles" , "Flowers" , "Whitehead" , "Kirby" , "Park" , "Shannon" , "Vlad" , "Pepin" , "Mcguire" , "Murray" , "Rush" , "Aramis" , "Fletcher" , "Mcfadden" , "Deleon" , "Luke" , "Lindsay" , "Payne" , "Gerbvo" , "Hubbard" , "Burnett" , "Bryan" , "Ratliff" , "Carlson" , "Parsons" , "Deadmeat" , "Crimson", "Wilson" , "Terry" , "Hancock" , "Hightower" , "Burns" , "Austin" , "Nightwalker" , "Thetis" , "Owen" , "Tate" , "Simmons" , "Grant" , "Barber" , "Talos" , "Ashes" , "Alston" , "Clayton" , "Mcbride" , "Huffman" , "Lightbringer" , "Blankenship" , "Higgins" , "Saint" , "Graham" , "Hodor" , "Ellison" , "Roberts" , "Odom" , "Mann"]
        Lista_r1= cartas[n-1:p]
        return Lista_r1

n=int(input("""Digite Una cantidad de N elementos,Siendo 1 su minimo y 50 su máximo
"""))
p=int(input("""Digite Una cantidad de N elementos,Siendo 50 su minimo y 100 su máximo
"""))

generador(n,p)
jugador=generador

print(jugador)

#Creación de la función combinador/relacioón de cartas premium con normales con combinador

def combinador(personaje_1,personaje_2,personaje_3,personaje_4,personaje_5,personaje_premium):
    if 1<=personaje_1<=100 and 1<=personaje_2<=100 and 1<=personaje_3<=100  and 1<=personaje_4<=100 and 1<=personaje_5<=100 and 1<=personaje_premium<=5:
        cartas = ["Payne" , "Hendrix" , "Stone", "Coffey" , "Whitaker" , "Pope" , "Bleach" , "Arc" , "Fleming" , "Hardin" , "Robiar" , "Mccullough" , "Mooney" , "Reynolds" , "Short" , "Stanton" , "Deadman" , "Stonehammer" , "Smith" , "Patrick", "Crane" , "Cargane" , "Powers" , "Wade" , "Joseph" , "Savage" , "Houston", "Merritt" , "Nuke" , "Barnett" , "Acosta" , "Duke" , "Sellers" , "Blake", "Schneider" , "Stone" , "Cannon" , "Garrison" , "Randall" , "Leon" , "Buck" , "Shannon" , "Delaney" , "Mckinney" , "Dodademocles" , "Flowers" , "Whitehead" , "Kirby" , "Park" , "Shannon" , "Vlad" , "Pepin" , "Mcguire" , "Murray" , "Rush" , "Aramis" , "Fletcher" , "Mcfadden" , "Deleon" , "Luke" , "Lindsay" , "Payne" , "Gerbvo" , "Hubbard" , "Burnett" , "Bryan" , "Ratliff" , "Carlson" , "Parsons" , "Deadmeat" , "Crimson", "Wilson" , "Terry" , "Hancock" , "Hightower" , "Burns" , "Austin" , "Nightwalker" , "Thetis" , "Owen" , "Tate" , "Simmons" , "Grant" , "Barber" , "Talos" , "Ashes" , "Alston" , "Clayton" , "Mcbride" , "Huffman" , "Lightbringer" , "Blankenship" , "Higgins" , "Saint" , "Graham" , "Hodor" , "Ellison" , "Roberts" , "Odom" , "Mann"]
        premium = ["AIVLIS", "LEIRBAG", "NAILUJ", "SOLRAC", "ANAID"]
        Lista_R2=[cartas[personaje_1-1],cartas[personaje_2-1],cartas[personaje_3-1],cartas[personaje_4-1],cartas[personaje_5-1],premium[personaje_premium-1]]
        print(Lista_R2)
    else:
        print("El sistema no toma esos valores")

print("Escoja un número entre el 1 al 100 con respecto a las cartas normales y entre el 1 al 5 para el personaje exclusivo premium")

personaje_1=int(input("""Personaje Estandar 1
"""))
personaje_2=int(input("""Personaje Estandar 2
"""))
personaje_3=int(input("""Personaje Estandar 3
"""))
personaje_4=int(input("""Personaje Estandar 4
"""))
personaje_5=int(input("""Personaje Estandar 5
"""))
personaje_premium=int(input("""Personaje premium
"""))

combinador(personaje_1,personaje_2,personaje_3,personaje_4,personaje_5,personaje_premium)

juego=combinador

print("Su juego constara de los siguientes personajes",juego,"Siendo",premium[personaje_premium-1],"Su personaje exclusivo")

#Creación de las listas Sobre_1 , Sobre_2 , Sobre_3


p=int(input("""Digite dos digitos entre 1 y 100 
"""))
n=int(input("""Digite dos digitos entre 1 y 100 con una diferencia de 5 con respecto al sobre anterior
"""))

Sobre_x= generador(n,p-1)
Sobre_y= generador(n+5 ,p+4)
Sobre_z= generador(n+15,p+14)

sobre_1=Sobre_x
sobre_2=Sobre_y
sobre_3=Sobre_z

diferencia= p-n

if diferencia==5: 
    print("Su primer sobre es",sobre_1)
    print("Su segundo sobre es",sobre_2)
    print("Su tercer sobre es",sobre_3)
else:
    print("Por favor haga bien los procedimientos")


