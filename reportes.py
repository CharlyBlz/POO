class Reporte:
    def __init__(self,_lista_empleados):
        self._lista_empleados = _lista_empleados

class ReporteContabilidad(Reporte):
    #
    #def __init__(self,lista_empleados):
    #    self._lista_empleados = lista_empleados
    #    #Será instanciado por el parámetro que está recibiendo
    def print_reporte(self):
        print("------REPORTE DE CONTABILIDAD------")
        print("-----------------------------------")
        for e in self._lista_empleados:
            #print(f'{e.nombre},{e.apellido},{e.salario}')
            print(f'{e.get_nombre_completo()},{e.salario}')

class ReporteEmpleados(Reporte):
    #def __init__(self,lista_empleados):
    #    self.lista_empleados = lista_empleados
    def print_reporte(self):
        print("------REPORTE DE EMPLEADOS------")
        print("--------------------------------")
        for e in self._lista_empleados:
            #print(f'{e.nombre},{e.apellido},{e.salario},{e.puesto}')
            print(f'{e.get_nombre_completo()},{e.puesto}')

class ReporteProgramacion(Reporte):
    def print_reporte(self):
        print("------REPORTE DE PROGRAMACIÓN------")
        print("-----------------------------------")
        for e in self._lista_empleados:
            #print(f'{e.nombre},{e.apellido},{e.salario},{e.puesto}')
            print(f'{e.get_nombre_completo()},{e.programacion.get_programacion_info()}')