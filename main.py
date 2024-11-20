def calcular(horas_trabajadas,tarifa):
    if horas_trabajadas>40:
        horas_extra=horas_trabajadas-40
        sueldo=(40*tarifa)+(horas_extra*tarifa*1.5)
    else:
        sueldo=horas_trabajadas*tarifa
    print('El sueldo es de €. '+str(sueldo))
def leer_tarifa(horas_trabajadas):
    try:
        tarifa=float(input('Ingresar tarifa por hora: '))
        calcular(horas_trabajadas,tarifa)
    except ValueError:
        print('No es un valor correcto')
        leer_tarifa(horas_trabajadas)
def leer_horas_trabajadas():
    try:
        horas_trabajadas=float(input('Ingresar horas trabajadas: '))
        leer_tarifa(horas_trabajadas)
    except ValueError:
        print('No es un valor correcto.')
        leer_horas_trabajadas()
leer_horas_trabajadas()
