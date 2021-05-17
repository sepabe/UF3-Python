import mysql.connector
from mysql.connector import errorcode


def connect_to_mysql():
    cnx = mysql.connector.connect(user='admin_campaign',
                                  password='4dm1n_c4mp41gn',
                                  host='localhost',
                                  database='db_campaign')
    print(cnx)
    return cnx


def input_validate_day(m):
    d = int(input('   · Día: '))
    if m == 2:
        while d < 1 or d > 28:
            d = int(input('   (!) Día no valido. Ingrese un día entre 1 y 28: '))
    elif m in (4, 6, 9, 11):
        while d < 1 or d > 30:
            d = int(input('   (!) Día no valido. Ingrese un día entre 1 y 30: '))
    else:
        while d < 1 or d > 31:
            d = int(input('   (!) Día no valido. Ingrese un día entre 1 y 31: '))
    return d


def input_validate_int(prompt, minimum, maximum, errprompt):
    var = int(input(prompt))
    while var < minimum or var > maximum:
        var = int(input(errprompt))
    return var


def input_validate_length(prompt, minimum, maximum, errprompt):
    var = input(prompt)
    while len(var) < minimum or len(var) > maximum:
        var = input(errprompt)
    return var


def format_date():
    print(' - Fecha')
    year = input_validate_int('   · Año: ', 1000, 9999, '   (!) Año no valido. Ingrese otro: ')
    month = input_validate_int('   · Mes: ', 1, 12, '   (!) Mes no valido. Ingrese otro: ')
    day = input_validate_day(month)
    return str(year) + '-' + str(month) + '-' + str(day)


def get_fields(crs):
    idkey = int(input(' - ID: '))
    while idkey in get_ids(crs):
        idkey = int(input(f' · (!) ID ({idkey}) ya existe. Ingrese otro: '))
    author = input_validate_length(' - Grupo/cantante: ', 1, 50, ' · (!) Texto demasiado largo. Ingrese otro: ')
    song = input_validate_length(' - Cancion: ', 1, 50, ' (!) Texto demasiado largo. Ingrese otro: ')
    rel_date = format_date()
    views = input_validate_int(' - Vistas: ', 1, 2147483647, ' (!) Valor no valido. Ingrese otro: ')
    return idkey, author, song, rel_date, views


def get_ids(crs):
    crs.execute('Select id from tb_video')
    return [row[0] for row in crs]


def main():
    try:
        db = connect_to_mysql()
        crs = db.cursor()

        amount = int(input(" ¿Cuántas filas desea introducir? >"))

        data = list()
        for x in range(amount):
            print(f'\n Fila {x + 1}:')
            data.append(get_fields(crs))

        query = 'INSERT INTO tb_video (id, author, song, rel_date, views) VALUES (%s, %s, %s, %s, %s);'
        crs.executemany(query, data)
        db.commit()

        crs.close()

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Something is wrong with your user name or password')
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print('Database does not exist')
        else:
            print(err)
    else:
        db.close()


if __name__ == '__main__':
    main()
