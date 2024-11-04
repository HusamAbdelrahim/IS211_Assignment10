import sqlite3

if __name__ == "__main__":
    print("Running load_pets.py")
    
    # connect to db
    conn = sqlite3.connect('pets.db')
    cursor = conn.cursor()

    # create the needed tables
    cursor.execute('''
    CREATE TABLE person(
        id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        age INTEGER
    )
    ''')

    cursor.execute('''
    CREATE TABLE pet(
        id INTEGER PRIMARY KEY,
        name TEXT,
        breed TEXT,
        age INTEGER,
        dead INTEGER
    )
    ''')

    cursor.execute('''
    CREATE TABLE person_pet(
        person_id INTEGER,
        pet_id INTEGER
    )
    ''')

    # insert person data
    person_data = [
        (1, 'James', 'Smith', 41),
        (2, 'Diana', 'Greene', 23),
        (3, 'Sara', 'White', 27),
        (4, 'William', 'Gibson', 23)
    ]

    cursor.executemany('INSERT INTO person VALUES (?,?,?,?)', person_data)

    # insert pet data
    pet_data = [
        (1, 'Rusty', 'Dalmation', 4, 1),
        (2, 'Bella', 'AlaskanMalamute', 3, 0),
        (3, 'Max', 'CockerSpaniel', 1, 0),
        (4, 'Rocky', 'Beagle', 7, 0),
        (5, 'Rufus', 'CockerSpaniel', 1, 0),
        (6, 'Spot', 'Bloodhound', 2, 1)
    ]

    cursor.executemany('INSERT INTO pet VALUES (?,?,?,?,?)', pet_data)

    # insert person_pet relationships
    person_pet_data = [
        (1, 1),
        (1, 2),
        (2, 3),
        (2, 4),
        (3, 5),
        (4, 6)
    ]

    cursor.executemany('INSERT INTO person_pet VALUES (?,?)', person_pet_data)

    # excute and close
    conn.commit()
    conn.close()



