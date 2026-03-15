# Codigo desarrollado por el estudiante: Roberth Fernando Fernandez Llori.
#Tarea: Crear un método basado en un problema de la vida real.
#Problema: Calcular promedio de notas.
Materias = [
    "Matemáticas",
    "Lengua y Literatura",
    "Inglés",
    "Física",
    "Química",
    "Biología"
]
def Calcular_Promedio_de_Notas(nota1, nota2, nota3, nota4, nota5, nota6):
    promedio = (nota1 + nota2 + nota3 + nota4 + nota5 + nota6) / 6
    return promedio
def main():
    print("----Bienvenido al programa de cálculo de promedio de notas----")
    print("Materias del estudiante:")
    for m in Materias:
        print(m)

    nota1 = float(input("Ingrese la nota de Matemáticas: "))
    nota2 = float(input("Ingrese la nota de Lengua y Literatura: "))
    nota3 = float(input("Ingrese la nota de Inglés: "))
    nota4 = float(input("Ingrese la nota de Física: "))
    nota5 = float(input("Ingrese la nota de Química: "))
    nota6 = float(input("Ingrese la nota de Biología: "))
    promedio = Calcular_Promedio_de_Notas(nota1, nota2, nota3, nota4, nota5, nota6)
    print(f"El promedio de notas del estudiante es: {promedio}")

main()