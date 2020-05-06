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

#Creación de la función generador
def generador(n,p):
    if 1<=n<=10 and 1<=p<=10:
        Lista_A=[1,2,3,4,5,6,7,8,9,10]
        Lista_r=Lista_A[p:n]
        print(Lista_r)
    else:
        print("El sistema solo acepta numeros del 1 al 10")
n=int(input("""Digite Una cantidad de N elementos,Siendo 1 su minimo y 10 su máximo
"""))
p=int(input("""Digite Una cantidad de N elementos,Siendo 1 su minimo y 10 su máximo
"""))
generador(n,p)
print(generador)
