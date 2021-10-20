


class User():
    def __init__(self, Nickname, password):
        self.Nickname = Nickname
        self.password = password
        self.intentosAcceso = 0

    def ingresar(self):
        while self.intentosAcceso <3:
            clave = int(input('ingrese su contraseña'))
            if self.password == clave:
                print('Bienvenido')
             
            else:
                print('Contraseña incorrecta')
                print(clave)
                break
            self.intentosAcceso+=1
        if self.intentosAcceso==3:
            print('haz sobre pasado el numeor d eintentos, intentelo de nuevo más tarde')

user1=User('Logan',12345)
user1.ingresar()