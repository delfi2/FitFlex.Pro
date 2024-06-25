import sqlite3

DATABASE_NAME = "fit.db"


def get_db():  # devuelve un conector a la base de datos
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def create_tables():
    table_gym = [
        """CREATE TABLE IF NOT EXISTS fit( 
                ID INTEGRER PRIMARY KEY,
                ejercicio TEXT NOT NULL,
                dificultad TEXT NOT NULL,
                repeticiones INTEGRER NOT NULL,
                serie INTEGRER NOT NULL, 
                peso TEXT NOT NULL             
            )
            """
    ]
    db = get_db()
    cursor = db.cursor() #permite ejecutar comandos
    table_run = [
        """CREATE TABLE IF NOT EXISTS fit( 
                ID INTEGRER PRIMARY KEY,
                ejercicio TEXT NOT NULL,
                dificultad TEXT NOT NULL,
                distancia TEXT NOT NULL,
                tiempo INTEGRER NOT NULL,       
            )
            """
    ]
    db = get_db()
    cursor = db.cursor() #permite ejecutar comandos
    
    for table in tables:
        cursor.execute(table)


def insert_ejercicio(ID, ejercicio, dificultad, repeticiones, series,
                     peso):  # atributos
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO fit (ID, ejercicio, dificultad, repeticiones, series,
                     peso) \
    VALUES ( ?, ?, ?, ? ,?, ?, ?, ?)"
    cursor.execute(statement, [ID, ejercicio, dificultad, repeticiones, series,
                     peso])
    db.commit()
    return True


def delete_ejercicio(ID):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM fit WHERE ID = ?"
    cursor.execute(statement, [ID])
    db.commit()
    return True


def get_by_id(ID):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT ID, ejercicio, dificultad, repeticiones, series, peso FROM fit WHERE ID = ?"
    cursor.execute(statement, [ID])
    return cursor.fetchone()  # que me de un registro especifico


def get_ejercicios():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT ID, ejercicio, dificultad, repeticiones, series, peso FROM fit"
    cursor.execute(query)
    return cursor.fetchall()  # me da todos los ejercicios


def menu():
    print('******************Menu******************')
    print()
    print('ingrese 1 para agregar un ejercicio a la base de datos')
    print('ingrese 2 para eliminar un ejercicio de la base de datos')
    print('ingrese 3 para buscar un ejercicio por su ID')
    print('ingrese 4 para listar todos los ejercicios')
    print('íngrese 5 para salir del menu')


create_tables()
flag = 0
while flag:
    menu()

    opcion = int(input())

    if opcion == 1:
        ID = int(input('ingrese el ID del ejercicio: '))
        ejercicio = input('ingrese el ejercicio:')
        repeticiones = input('ingrese las repeticiones del ejercicio: ')
        peso = int(input('ingrese el peso del ejercicio: '))
        serie = int(input('ingrese el numero de serie del ejercicio: '))
        dificultad = input('ingrese la dificultad del ejercicio, - principiante; intermedio; avanzado - :')
        result = insert_ejercicio(ID, ejercicio, repeticiones, tiempo, peso, fortalece, serie, dificultad)
        if result == True:
            print('ejercicio ingresado correctamente')
            print()
            print()
        else:
            print('Error')
            print()

    elif opcion == 2:
        ID = int(input('ingrese el ID del ejercicio a eliminar: '))
        result = delete_ejercicio(ID)
        if result == True:
            print('ejercicio eliminado')
            print()
            print()
        else:
            print('Error')
            print()

    elif opcion == 3:
        ID = int(input('ingrese el ID del ejercicio a buscar: '))
        result = get_by_id(ID)  # devuelve una tupla con el registro
        print(result)
        print()
        print()

    elif opcion == 4:
        result = get_ejercicios()  # devuelve una lista de tuplas donde cada tupla es un registro
        print(result)
        print()
        print()

    elif opcion == 5:
        print()
        print('saliendo')
        print()
        flag = False

print('terminado')
print('****************************************************')
