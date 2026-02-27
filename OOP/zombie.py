from Enemigo import *
import random


class Zombie(Enemigo):
    def __init__(self, punto_energia=10, ataque=1):
        super().__init__(tipo_enemigo='Zombie', punto_energia=punto_energia, ataque=ataque)

    def habla(self):
        print("Hummmm......")

    def propagar_enfermedad(self):
        print("El xombie esta tratando de propagar la enfermedad!!")

    def ataque_especial(self):
        print("ogro ataque especial")
        funciona_ataque_especial = random.random() < 0.50
        if funciona_ataque_especial:
            self.ataque += 2
            print("zombie ha regenerado su energia con 2HP!!!!")
