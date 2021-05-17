def menu():
    index = int(input(
        "\n\t\t MENU"
        "\n 1 - Crear un fichero"
        "\n 2 - Mostrar el contenido de un fichero"
        "\n 3 - Modificar el contenido de un fichero"
        "\n 0 - Salir"
        "\n>"
    ))
    index = validate(index, 0, 3, "\n (!) Ingrese un valor del menu: ")
    return index


def validate(variable, minimum, maximum, prompt):
    while variable < minimum or variable > maximum:
        variable = int(input(prompt))
    return variable


def get_file_name():
    the_file = input("\nIngrese el nombre del fichero: ")
    path = "/home/sebas/Documents/testing/" + the_file
    return path


def get_file_content(index):
    if index == 3:
        text = input("\nIngrese el contenido: ")
    else:
        text = ""
    return text


def manipulate_file(path, index, text):
    try:
        with open(path, "r" if index == 2 else "w") as f:
            print(f"\nContenido en {path}:\n", f.read()) if index == 2 else f.write(text)
        f.close()
    except FileNotFoundError:
        print("\n (!) Archivo no encontrado:", FileNotFoundError)
    except OSError:
        print("\n (!) Error del sistema:", OSError)
    finally:
        print("\n[HECHO]")


def main():
    while True:
        index = menu()
        if index == 0:
            print("\n¡Hasta la próxima!")
            exit(0)

        path = get_file_name()
        text = get_file_content(index)

        manipulate_file(path, index, text)


if __name__ == '__main__':
    main()
