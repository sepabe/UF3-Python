def validate(var):
    while len(var)>100:
        var = input(" (!) Texto demasiado largo. Intente de nuevo: ")
    return var

def manipulate_file(fpath, foption, fcontent):
    with open(fpath, foption) as f:
        f.write(fcontent)
    f.close()

def main():
    text = input("Ingrese texto: ")
    text = validate(text)
    path = "/home/sebas/Documents/testing/text.txt"
    option = "a"
    try:
        manipulate_file(path, option, text)
    except FileNotFoundError:
        print(" (!) Archivo no encontrado:", FileNotFoundError)
    except OSError:
        print(" (!) Error del sistema:", OSError)
    finally:
        print("\n[FIN]")


if __name__ == '__main__':
    main()
