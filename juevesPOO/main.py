from cosas import *

def main():

    l1 = Libro.libro_planeta("El perfume", Autor("Patrik", "PS"), 1980)
    print(l1)
    #l1.autor.pseudonimo = l1.autor.pseudonimo.lower()

    print("------Herencia------")
    al2 = Alumno("Jose", 19, "232323", "ICO", 9)
    al2.nombre = "Pepe"
    al2.edad = 20
    print(vars(al2))

main()