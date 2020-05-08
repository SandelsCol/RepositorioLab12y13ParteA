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

jugador=generador(n,p)

print("La cartas correspondientes son",jugador)

#Creación de la función combinador/relacioón de cartas premium con normales con combinador

def combinador(personaje_1,personaje_2,personaje_3,personaje_4,personaje_5,personaje_premium):
    cartas = ["Payne" , "Hendrix" , "Stone", "Coffey" , "Whitaker" , "Pope" , "Bleach" , "Arc" , "Fleming" , "Hardin" , "Robiar" , "Mccullough" , "Mooney" , "Reynolds" , "Short" , "Stanton" , "Deadman" , "Stonehammer" , "Smith" , "Patrick", "Crane" , "Cargane" , "Powers" , "Wade" , "Joseph" , "Savage" , "Houston", "Merritt" , "Nuke" , "Barnett" , "Acosta" , "Duke" , "Sellers" , "Blake", "Schneider" , "Stone" , "Cannon" , "Garrison" , "Randall" , "Leon" , "Buck" , "Shannon" , "Delaney" , "Mckinney" , "Dodademocles" , "Flowers" , "Whitehead" , "Kirby" , "Park" , "Shannon" , "Vlad" , "Pepin" , "Mcguire" , "Murray" , "Rush" , "Aramis" , "Fletcher" , "Mcfadden" , "Deleon" , "Luke" , "Lindsay" , "Payne" , "Gerbvo" , "Hubbard" , "Burnett" , "Bryan" , "Ratliff" , "Carlson" , "Parsons" , "Deadmeat" , "Crimson", "Wilson" , "Terry" , "Hancock" , "Hightower" , "Burns" , "Austin" , "Nightwalker" , "Thetis" , "Owen" , "Tate" , "Simmons" , "Grant" , "Barber" , "Talos" , "Ashes" , "Alston" , "Clayton" , "Mcbride" , "Huffman" , "Lightbringer" , "Blankenship" , "Higgins" , "Saint" , "Graham" , "Hodor" , "Ellison" , "Roberts" , "Odom" , "Mann"]
    premium = ["AIVLIS", "LEIRBAG", "NAILUJ", "SOLRAC", "ANAID"]
    Lista_R2=[cartas[personaje_1-1],cartas[personaje_2-1],cartas[personaje_3-1],cartas[personaje_4-1],cartas[personaje_5-1],premium[personaje_premium-1]]
    print(Lista_R2)
    return Lista_R2
    
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
print(combinador)

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

#Creación de paquete

if diferencia==5: 
    paquete=[sobre_1[0],sobre_2[3],sobre_3[4],sobre_1[2],sobre_2[1]]
    print ("La combinación de su paquete es ",paquete)
    p=int(input("""Digite un numero del 1 al 10 el cual si le atina tiene la posibilidad de recibir una carta exclusiva
    """))
else:
    print("Por favor haga bien los procedimientos")

#creación de la función loteria

def loteria(p):

    if diferencia==5: 
        if p==7:
            Paquete_3=paquete.append(premium[p-6])
            print("Felicitaciones , ahora su paquete sera",Paquete_3,"Con la imprementacion de la carta exclusiva",premium[p-6])
            return Paquete_3
        elif 0<p<=10:
            print("Lo siento intente a la próxima , si baraja seguira siendo",paquete)
        else:
            if p<0 and p>10:
                print("Por favor haga bien el procedimiento")
    else:
        print("Por favor haga bien los procedimientos")

loteria(p)

#Cartas premium:

uno_1=int(input("""Digite Una cantidad de N elementos,Siendo 1 su minimo y 50 su máximo
"""))
dos_2=int(input("""Digite Una cantidad de N elementos,Siendo 50 su minimo y 100 su máximo
"""))
paquete=[sobre_1[0],sobre_2[3],sobre_3[4],sobre_1[2],sobre_2[1]]
Lista_r1= cartas[uno_1-1:dos_2]
Juego_Pro=[Lista_r1,paquete,premium[p-6]]
print("Su combinación es",Juego_Pro)
Tamaño_Premium=Juego_Pro[2]
print("Sus cartas premiums son",Juego_Pro[2],"Siendo un total de",len(Tamaño_Premium),"Cartas")


