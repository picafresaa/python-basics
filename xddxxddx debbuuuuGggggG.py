def cal_calificacion(examen, proyecto, tareas):
    calificacion = (examen * 0.50) + (proyecto * 0.40) + (tareas * 0.10)
    return calificacion

def cal_resultado(calificacion, asistencia):
    if asistencia < 80:
        resultado = "Reprobado por asistencia"
    else:
        if calificacion >= 90:
            resultado = "Destacado"
        elif calificacion >= 80:
            resultado = "Sólido"
        elif calificacion >= 70:
            resultado = "Básico"
        else:
            resultado = "Incipiente"
    return resultado

def main():
    examen = int(input("Examen: "))
    proyecto = int(input("Proyecto: "))
    tareas = int(input("Tareas: "))
    asistencia = int(input("Asistencia: "))

    calificacion = cal_calificacion(examen, proyecto, tareas)
    resultado = cal_resultado(calificacion, asistencia)

    print(f"Calificación final = {calificacion:.2f}")
    print("Estatus = ", resultado)

main()

