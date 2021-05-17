import pandas as pd


def main():
    videos = {
        'ID': list(),
        'Grupo/cantante': list(),
        'Nombre': list(),
        'Fecha': list(),
        'Vistas': list()
    }
    amount = int(input(" ¿Cuántos videos desea introducir? >"))
    for x in range(amount):
        print(f'\n Video {x + 1}:')
        for key in videos:
            if key == 'ID' or key == 'Vistas':
                input_var = initialize_validate(f'{key}: ', 0, 1000000000, ' (!) Ingrese un número entero: ')
            elif key == 'Fecha':
                print(f'{key}: ')
                year = initialize_validate('· Año: ', 1000, 3000, ' (!) Ingrese un año válido: ')
                month = initialize_validate('· Mes: ', 1, 12, ' (!) Ingrese un mes válido: ')
                day = day_validation(month)
                input_var = str(day) + '/' + str(month) + '/' + str(year)
            else:
                input_var = input(f'{key}: ')
            videos[key].append(input_var)

    print('\n', pd.DataFrame(videos),
          '\n\nÍndice customizado...')

    custom_index = list()
    for x in range(amount):
        custom_index.append(input(f'- {videos["ID"][x]} ({videos["Nombre"][x]}): '))
    print('\n', pd.DataFrame(videos, index=custom_index))


def initialize_validate(prompt, minimum, maximum, eprompt):
    var = int(input(prompt))
    while var < minimum or var > maximum:
        var = int(input(eprompt))
    return var


def day_validation(m):
    if m == 2:
        d = initialize_validate('· Día: ', 1, 28, ' (!) Ingrese un día entre 1 y 28: ')
    elif m in (4, 6, 9, 11):
        d = initialize_validate('· Día: ', 1, 30, ' (!) Ingrese un día entre 1 y 30: ')
    else:
        d = initialize_validate('· Día: ', 1, 31, ' (!) Ingrese un día entre 1 y 31: ')
    return d


if __name__ == "__main__":
    main()

'''
implementar un programa que demani per teclat:
    quants vídeos vol introduir i per a cada vídeo, emmagatzemar:
        identificador (numèric)
        grup/cantant (text)
        nom de la cançó (text)
        data de publicació (text en format dd/mm/yyyy)
        nombre de visualitzacions (numèric)
    validar que les dades introduïdes tenen el format correcte
    mostri les dades tabulades i permeti mostra-les segons l’índex introduït per teclat
'''
