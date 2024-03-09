import os
import datetime

class Empleado:
    def __init__(self, nombre, edad, sexo, horas_trabajadas, valor_hora, fecha_ingreso):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.horas_trabajadas = horas_trabajadas
        self.valor_hora = valor_hora
        self.fecha_ingreso = fecha_ingreso
    
    def calcular_sueldo_mensual(self):
        return self.horas_trabajadas * self.valor_hora
    
    def calcular_antiguedad(self):
        hoy = datetime.date.today()
        antiguedad = hoy.year - self.fecha_ingreso.year - ((hoy.month, hoy.day) < (self.fecha_ingreso.month, self.fecha_ingreso.day))
        return antiguedad
    
    def calcular_anios_para_pensionarse(self):
        if self.sexo == 'Mujer':
            if self.edad >= 60:
                return 0
            else:
                return 60 - self.edad
        else:
            if self.edad >= 65:
                return 0
            else:
                return 65 - self.edad
    
    def calcular_descuentos_salud_pension(self):
        salud = self.calcular_sueldo_mensual() * 0.04
        pension = self.calcular_sueldo_mensual() * 0.04
        return salud, pension
    
    def calcular_abono_pension_anual(self):
        return self.calcular_sueldo_mensual() * 0.04 * 12
    
    def guardar_empleado(self, nombre_archivo):
       with open(nombre_archivo, 'a') as archivo:
            archivo.write(f"Nombre: {self.nombre}\n")
            archivo.write(f"Edad: {self.edad}\n")
            archivo.write(f"Sexo: {self.sexo}\n")
            archivo.write(f"Horas trabajadas: {self.horas_trabajadas}\n")
            archivo.write(f"Valor por hora: {self.valor_hora}\n")
            archivo.write(f"Fecha de ingreso: {self.fecha_ingreso} años\n")
            archivo.write("\n")

empleado1 = Empleado("Juan", 30, "Hombre", 160, 10, datetime.date(2015, 1, 1))
print("Sueldo Mensual:", empleado1.calcular_sueldo_mensual())
print("Antigüedad:", empleado1.calcular_antiguedad())
print("Años para pensionarse:", empleado1.calcular_anios_para_pensionarse())
print("Descuentos de Salud y Pensión:", empleado1.calcular_descuentos_salud_pension())
print("Abono a la pensión anual:", empleado1.calcular_abono_pension_anual())

empleado1.guardar_empleado("empleados.txt")
