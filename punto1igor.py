"""Crea una clase llamada Persona con atributos nombre, edad y sexo. 
Implementa un método que permita cambiar la edad de la persona y otro que muestre la información de la persona."""

class persona:
    def __init__(self, nombre, edad, sexo):
        self._nombre = nombre
        self._edad = edad
        self._sexo = sexo
        
    def mostrar_informacion(self):
        return f"Datos de la persona: {self._nombre}, {self._edad}, {self._sexo}"
    
    "GETTERS"
    
    def get_nombre(self):
        return self._nombre
    def get_edad(self):
        return self._edad
    def get_sexo(self):
        return self._sexo
    
    "SETTERS"
    def set_nombre(self, nombre):
        self._nombre = nombre
    def set_edad(self, edad):
        self._edad = edad
    def set_sexo(self, sexo):
        self._sexo = sexo
        
    def cambiarEdad(self, EdadNueva):
        if EdadNueva > 0:
            self._edad = EdadNueva
        else:
            print("Edad inválida")
    

persona1 = persona("Juan", 330, "Masculino")
print(persona1.mostrar_informacion())
