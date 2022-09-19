class Persona:

    especie= "mamifero"
    alimentacion = "omniboro"

    def __init__(self, edad, nombre, genero):
        self.edad = edad
        self.nombre = nombre
        self.genero = genero 

    def mostrar_info(self):
        print(f"Es un {Persona.especie}, generalemente {Persona.alimentacion}")
        print(f"Es una Persona, su nombre es {self.nombre} tiene {self.edad} de edad y es del genero {self.genero}")

    def accion(self, acccion):
        self.acccion = acccion
        print(f"{self.nombre} esta por, {acccion}")

Jony= Persona(27,"Jony","Masculino")
Carla= Persona(15, "Carla", "Femenino")

print("*"*90)
Jony.mostrar_info()
Jony.accion("dormir")
print("*"*90)
Carla.mostrar_info()
Carla.accion("ir al colegio")