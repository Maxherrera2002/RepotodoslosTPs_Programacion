class motocicleta:
    def __init__(self, color, matricula, combustible_L, 
                 numero_R, marca, modelo, fecha_F, 
                 velocidad_P, peso, motor):
        self.color = color
        self.matricula = matricula
        self.combustible_L = combustible_L
        self.numero_R = numero_R
        self.marca = marca
        self.modelo = modelo
        self.fecha_F = fecha_F
        self.velocidad_P = velocidad_P
        self.peso = peso
        self.__motor = False
    #Metodo arrancar
    def arrancar(self):
        if self.__motor:
            print("El motor ya esta en marcha")
        else:
            self.__motor: True
            print("El motor a sido arrancado")
    #Metodo deneter
    def detener(self):
        if self.__motor:
            self.__motor: False
            print("El motor se a detenido")
        else:
            print("El motor ya esta detenido")
    #Metodo Precio
    def consulta_precio(self):
        print(f"El precio de la moto: {self.marca}, {self.modelo}, es de {self.precio}$")


#Instancio dos motocicletas
new_motocicleta = motocicleta("azul", "HRG320", 10, 2, "Renault", 2023, 1985, "200KM/H", "200KG", "IDK")
new_motocicleta2 = motocicleta("rojo", "HRGa320", 10, 2, "Logan", 2012, 1948, "2003KM/H", "2030KG", "IDK")

#Pruebo uno de los metodos
print(new_motocicleta.arrancar())

#Nuevo atributo
new_motocicleta.precio = 200
#Pruebo si se agrego correctamente
print(f"El precio de la motocicleta {new_motocicleta.marca}, {new_motocicleta.modelo} es de {new_motocicleta.precio}$.")

#Sin error al consultar el precio
print(new_motocicleta.consulta_precio())
#Larga error, ya que el atributo creado previamente se creo para una de las motocicletas
#Ya que para crear el atributo para ambos casos, se deberia agregar en la clase misma
#Sucederia lo mismo si intentamos averiguar el precio, antes de instansiar el nuevo atributo
print(new_motocicleta2.consulta_precio())





