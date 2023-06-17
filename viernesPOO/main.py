from cosas import  *

def main():
    per1 = Persona("Jose", 19)
    print(per1)
    print(Persona.descripcion)

    print("------Herencia alumno------")
    al1 = Alumno("Jose", 19, "32154648", "ICO")
    print(al1)
    print(Alumno.descripcion)

    al2 = Alumno.constructor_defecto()
    print(al2)
    al2.nombre= "Juan"
    print(al2)
    al2.dormir()

    print("--------Herencia profe--------")
    profe1 = Profesor("Jesús", 30 +161, 2321554, "Ingeniería de software")
    print(profe1)
    profe1.dormir()

    print("--------Herencia multiple--------")
    ayudante = AyudanteProfesor("Adrián", 20, "25252", "ICO", 232323, "Ing. de Software", 4)
    print(ayudante)
    ayudante.dormir()
    ayudante.nombre = "Abraham"
    ayudante.dar_clase("P.O.O")
main()