from empleado import Gerente
from empleado import Tecnico 
from empleado import Gestora
from empleado import Administrador
from reportes import ReporteContabilidad
from reportes import ReporteEmpleados
from reportes import ReporteProgramacion
from programacion import Matutino
from programacion import Vespertino

empleados = [
    Gerente("Roberto","Arias","20,000",Matutino()),
    Gestora("Alejandra","Blázquez","8,000",Matutino()),
    Gestora("Selene","Negrete","8,000",Matutino()),
    Tecnico("Artemio","Hernández","9,000",Vespertino()),
    Tecnico("Salvador","Nolasco","9,000",Vespertino()),
    Tecnico("Rolando","Gutiérrez","9,000",Matutino()),
    Administrador ("Marco","Ayala","15,000",Vespertino())
]

reportes = [
    ReporteContabilidad(empleados),
    ReporteEmpleados(empleados),
    ReporteProgramacion(empleados)
]

for r in reportes:
    r.print_reporte()

#Reportes y lista de empleados ya están desacoplados, al implementar en un módulo distinto los reportes
#reporteContabilidad = ReporteContabilidad(empleados)
#reporteContabilidad.reporte_contabilidad()
#reporteEmpleados = ReporteEmpleados(empleados)
#reporteEmpleados.reporte_empleados()