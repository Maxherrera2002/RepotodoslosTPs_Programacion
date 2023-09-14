fecha = input("Ingrese la fecha actual, formato: dia, DD/MM.: ")

#separar dia
x = fecha.find(",")
e = slice(x)
lower = fecha[e].lower()

#separar numeros y parseo
num = fecha.find("/")
mm_slice = slice(num+1, None, None)
dd_slice = slice(num-2, num, None)
dd_num = int(fecha[dd_slice])
mm_num = int(fecha[mm_slice] )

#verificamos errores en la fecha
if lower[e] != "lunes" and lower[e] != "martes" and lower[e] != "miercoles" and lower[e] != "jueves" and lower[e] != "viernes":
    print("El dia introducido no existe")
elif dd_num > 31 or dd_num < 0:
    print("El dia introducido, es mayor a 31 o menor a 0")
elif mm_num > 12 or mm_num < 0:
    print("El mes introducido, es mayor a 12 o menor a 0")
#empezamos con los casos, lunes, martes y miercoles
elif lower[e] == "lunes" or lower[e] == "martes" or lower[e] == "miercoles":
    #para separar un poco
    print("Fecha introducida de forma correcta")
    print(" ")
    examen_entrada = input("Se tomaron examenes el dia de hoy, Presione Y para si, y N para no: ")
    examen = examen_entrada.lower()
    #anidamos un if para el caso de si hay o no examen
    if examen == "y" or examen == "si" or examen == "yes":
        aprobados = int(input("Ingrese la cantidad de alumnos aprobados: "))
        no_aprobados = int(input("Ingrese la cantidad de alumnos que NO aprobaron: "))
        todos = aprobados + no_aprobados
        calculo = (aprobados * 100) / todos 
        print(f"El porcentaje de aprobados de la clase es: {int(calculo)}%")
    #agregado propio
    elif examen == "n" or examen == "no":
        print("Exelente ejecuccion")
    else:
        print("Hubo un error, por favor introdusca Y para si, y N para no")
#caso jueves
elif lower[e] == "jueves":
    print("Fecha introducida de forma correcta")
    print(" ")
    asistencia = int(input("Ingrese el procentaje de asistencia de la clase "))
    if asistencia > 50: 
        print("Asistió la mayoría")
    else:
        print("No asistió la mayoría")
#caso viernes
elif lower[e] == "viernes":
    print("Fecha introducida de forma correcta")
    print(" ")
    if dd_num == 1 and mm_num == 7 or mm_num == 1:
        print("Comienzo de nuevo ciclo")
        alumnos = input("ingrese la cantidad de alumnos del nuevo ciclo y su arancel, formato: cantidad, $arancel: ")
        #sacamos el precio del arancel
        x_a = alumnos.find("$")
        e_a = slice(x_a+1, None, None)
        aranceles = int(alumnos[e_a])
        #sacamos la cantidad de alumnos
        x_c = alumnos.find(",")
        e_c = slice(x_c)
        c_alumnos = int(alumnos[e_c])
        #calculamos
        calc = aranceles * c_alumnos
        print(f"El ingreso total de dinero es de: {calc}")
    #Caso propio, supuse que podiamos hacer lo mismo que en el dia jueves
    else:
        print("Fecha introducida de forma correcta")
        print(" ")
        asistencia = int(input("Ingrese el procentaje de asistencia de la clase "))
        if asistencia > 50: 
            print("Asistió la mayoría")
        else:
            print("No asistió la mayoría")
