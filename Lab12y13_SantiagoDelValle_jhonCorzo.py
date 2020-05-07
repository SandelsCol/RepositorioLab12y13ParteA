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
    if 0<=n<=50 and 50<=p<=100:
        cartas = ["Payne" , "Hendrix" , "Stone", "Coffey" , "Whitaker" , "Pope" , "Bleach" , "Arc" , "Fleming" , "Hardin" , "Robiar" , "Mccullough" , "Mooney" , "Reynolds" , "Short" , "Stanton" , "Deadman" , "Stonehammer" , "Smith" , "Patrick", "Crane" , "Cargane" , "Powers" , "Wade" , "Joseph" , "Savage" , "Houston", "Merritt" , "Nuke" , "Barnett" , "Acosta" , "Duke" , "Sellers" , "Blake", "Schneider" , "Stone" , "Cannon" , "Garrison" , "Randall" , "Leon" , "Buck" , "Shannon" , "Delaney" , "Mckinney" , "Dodademocles" , "Flowers" , "Whitehead" , "Kirby" , "Park" , "Shannon" , "Vlad" , "Pepin" , "Mcguire" , "Murray" , "Rush" , "Aramis" , "Fletcher" , "Mcfadden" , "Deleon" , "Luke" , "Lindsay" , "Payne" , "Gerbvo" , "Hubbard" , "Burnett" , "Bryan" , "Ratliff" , "Carlson" , "Parsons" , "Deadmeat" , "Crimson", "Wilson" , "Terry" , "Hancock" , "Hightower" , "Burns" , "Austin" , "Nightwalker" , "Thetis" , "Owen" , "Tate" , "Simmons" , "Grant" , "Barber" , "Talos" , "Ashes" , "Alston" , "Clayton" , "Mcbride" , "Huffman" , "Lightbringer" , "Blankenship" , "Higgins" , "Saint" , "Graham" , "Hodor" , "Ellison" , "Roberts" , "Odom" , "Mann"]
        jugador=cartas[n-1:p]
        print("La nueva baraja llamada jugador contiene las siguientes cartas",jugador,"Siendo un total de",len(jugador),"cartas")
    else:
        print("El sistema no acepta esos números , siga por favor los procedimientos")
n=int(input("""Digite Una cantidad de N elementos,Siendo 1 su minimo y 50 su máximo
"""))
p=int(input("""Digite Una cantidad de N elementos,Siendo 50 su minimo y 100 su máximo
"""))
generador(n,p)
print(generador)

#Creación de la función combinador

def combinador(x,c,v,b,n):
    lista_A= ["Lee","Brekae","Vi","Teemo","Darius","Garen","Bardo","Ezreal","Taric","Ahri","Zed"]
    lista_B=["Nautilus","Jinx","Quixana","Hecarim","Zac","Veigar","Xin","Blis","Tresh","Lucian","Sett"]
    Lista_R2=[lista_A[x-1],lista_B[c-1],lista_A[v-1],lista_B[b-1],lista_A[n-1]]
    print("La nueva lista es",Lista_R2)

lista_A= ["Lee","Brekae","Vi","Teemo","Darius","Garen","Bardo","Ezreal","Taric","Ahri","Zed"]
lista_B=["Nautilus","Jinx","Quixana","Hecarim","Zac","Veigar","Xin","Blis","Tresh","Lucian","Sett"]

print(lista_A)
print(lista_B)

x=int(input("""Digite entre el 1 y el 10 para elegir a tu top
"""))
c=int(input("""Digite entre el 1 y el 10 para elegir a tu Jungla
"""))
v=int(input("""Digite entre el 1 y el 10 para elegir a tu MidLaner
"""))
b=int(input("""Digite entre el 1 y el 10 para elegir a tu Adc
"""))
n=int(input("""Digite entre el 1 y el 10 Para elegir a tu Supp
"""))

combinador(x,c,v,b,n)
Lista_Nueva_R_2=combinador

print("Tu equipo es el siguiente",combinador)