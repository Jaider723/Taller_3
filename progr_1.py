class Avion:
    def __init__(self,modelo,aerolinea,capacidad,altura_max):
        self.modelo=modelo
        self.aerolinea=aerolinea
        self.capacidad=capacidad
        self.altura_max=altura_max

    def despegar(self):
        print("El avion ha despegado")
        
    def aterrizar(self):
        print("El avion ha aterrizado")
        
class Celular:
    def __init__(self,marca,procesador,memoria,bateria):
        self.marca=marca
        self.procesador=procesador
        self.memoria=memoria
        self.bateria=bateria

    def llamar(self):
        numero=int(input("Ingrese el numero al que quiere llamar: "))
        print(f"Llamando a {numero}...")
        
    def mensajeSMS(self):
        numero=int(input("Ingrese el numero al que quiere enviar un SMS: "))
        mensaje=input("Ingrese el mensaje: ")
        print("Mensaje enviado.")
        
class Asignatura:
    def __init__(self,nombre,creditos,facultad,profesor):
        self.nombre=nombre
        self.creditos=creditos
        self.facultad=facultad
        self.profesor=profesor
        
    def matricular(self):
        print("Asignatura matriculada")
        
    def cancelar(self):
        motivo=input("Ingrese el motivo de cancelación: ")
        print("Asignatura cancelada")
        
class Ejercito:
    def __init__(self,pais,comandante,num_soldados,presupuesto):
        self.pais=pais
        self.comandante=comandante
        self.num_soldados=num_soldados
        self.presupuesto=presupuesto
    
    def atacar(self):
        pass
    
    def defenderse(self):
        pass
    
class Silla:
    def __init__(self,material,color,altura,inclinacion):
        self.material=material
        self.color=color
        self.altura=altura
        self.inclinacion=inclinacion
        
    def regular_altura(self):
        altura=int(input("Ingrese la nueva altura: "))
        self.altura=altura
        print("Altura regulada")
        
    def reclinarse(self):
        grados=int(input("Ingrese los grados de inclinación: "))
        self.inclinacion=grados
        print("La silla ha sido reinclinada")
        
class Audifonos:
    def __init__(self,marca,modelo,color,volumen):
        self.marca=marca
        self.modelo=modelo
        self.color=color
        self.volumen=volumen
        
    def subir_volumen(self):
        self.volumen+=1
        
    def bajar_volumen(self):
        self.volumen-=1
        