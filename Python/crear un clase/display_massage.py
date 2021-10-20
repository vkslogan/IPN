###########
'''Escriba una función llamanda
display_message()
que imprima en la pantalla un mensaje que indique los temas que se han visto hasta el momento.'''
###########
def display_maessage():
    print("temas vistos en clase \n -funciones sin argumentos \n -funciones con argumentos")
display_maessage()

def libro_favorito(nombre_del_libro):
    print("Mi libro favorito es: \n ¡"+nombre_del_libro.title()+"!")
libro_favorito("trading in the zone")

def hacerPlayera(frase, talla="SMALL"):
    print("Su playera es: "+talla+ " y el texto a serigrafear es: "+frase.title())
hacerPlayera(frase="hola amigos")


def hacerPlayera(frase="Yo <3 Python", talla="Grande"):
    print("Su playera es: "+talla + " y el texto a serigrafear es: "+ frase)


hacerPlayera()
