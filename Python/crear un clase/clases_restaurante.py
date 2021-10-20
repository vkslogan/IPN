#exercises 2.3.1 y 2.3.2
#Restaurante: a) Crear una clase llamada Restaurant. El método __init__()
#debe de aceptar dos atributos: El nombre_restaurant y el tipo_cocina.
#b) Crear un método que se llame describe_restaurant que imprima: El nombre del restaurant es: ------
# y El tipo de comida que se sirve es: -------.
#c) Generar tres Restaurantes: Crear tres restaurantes utilizando la clase que se ha definido con anterioridad
# y llame al método describe_restaurant para cada instancia de la clase.
#--------------------------------------------------------------------------------------------------------------------------
#2.4.4
#Clientes atendidos: Retomar la clase de Restaurante que se generó a lo largo de este notebook y
#agregar un atributo que clientes_atendidos y agregar dos métodos:
#Clientes_Atendidos(self, numero): que pueda modificar el número de clientes.
#Aumenta_Clientes(self, numero): que pueda aumentar el número de clientes que se han atendido.

class restaurant():
    """Clase tipo restaurante"""
    def __init__(self,nombre_restaurant,tipo_cocina):
        """Inicializacion de los atributos"""
        self.nombre_restaurant=nombre_restaurant
        self.tipo_cocina=tipo_cocina
        self.client_serve = 0
    def describe_restaurant(self):
        long_name = self.nombre_restaurant+'  ' +self.tipo_cocina
        return long_name.title()
    def Clientes_Atendidos(self):
        print("se han atendido "+str(self.client_serve) + " clientes.")
    def Aumenta_Clientes(self,client):
        if client >= self.client_serve:
            self.client_serve=client
        else: print("a ocurrido un error")

restaurante1=restaurant('chimicharro','Argentina')
print(restaurante1.describe_restaurant())
restaurante1.Clientes_Atendidos(10)
#restaurante1.Aumenta_Clientes()

restaurante2=restaurant('bellini','Italiana')
restaurante3=restaurant('Los Paisas','Méxicana')

