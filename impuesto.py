ingreso=int(input("ingrese su sueldo mensual: "))

mes=int(input("Ingrese la cantidad de meses trabajados: "))

gratificacion=int(input("Cantidad de gratificaciones recibidas: "))
UIT=4300
afiliacion=int(input("Estas afiliado a: \n1)ESSALUD - 1 \n2)ESP - 2 \n3)Ninguno - 3 \nIngrese un número: "))

if afiliacion==1:
    plus=ingreso*0.09
elif afiliacion==2:
    plus=ingreso*0.0675
elif afiliacion==3:
    plus=0
else:
    print("no existe")

RemuneracionBrutalAnual = (ingreso * mes) + ((gratificacion*(ingreso*2))+plus)

if RemuneracionBrutalAnual<=(7*UIT):
    print("\nSueldo anual : ", RemuneracionBrutalAnual)
else:
    RemuneracionNetaAnual=RemuneracionBrutalAnual-30100
    if RemuneracionBrutalAnual<=(5*UIT):
        ImpuestoAnualProyectado = RemuneracionBrutalAnual*0.08
    elif RemuneracionBrutalAnual<=(20*UIT):
        ImpuestoAnualProyectado=RemuneracionBrutalAnual*0.14
    elif RemuneracionBrutalAnual<=(35*UIT):
        ImpuestoAnualProyectado=RemuneracionBrutalAnual*0.17
    elif RemuneracionBrutalAnual<=(45*UIT):
        ImpuestoAnualProyectado=RemuneracionBrutalAnual*0.2
    elif RemuneracionBrutalAnual>(45*UIT):
        ImpuestoAnualProyectado=RemuneracionBrutalAnual*0.3
    
    ImpuestoMensual=ImpuestoAnualProyectado/mes

    ganancia = ingreso-ImpuestoMensual
    print("╔═════════════════════════════════════════════════")
    print("║Ingreso mensual: ", ingreso)
    print("║Impuesto mensual: ", ImpuestoMensual)
    print("║Sueldo mensual menos impuesto mensual: ",ganancia)
    print("║Ingreso Anual: ",RemuneracionBrutalAnual)
    print("║Impuesto anual: ", ImpuestoAnualProyectado)
    print("╚═════════════════════════════════════════════════")

    


