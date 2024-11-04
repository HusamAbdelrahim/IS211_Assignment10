import sqlite3

def get_person_and_pets(person_id):
    conn = sqlite3.connect('pets.db')
    cursor = conn.cursor()
    
    # Get person info
    cursor.execute('''
        SELECT first_name, last_name, age 
        FROM person 
        WHERE id = ?
    ''', (person_id,))
    
    person = cursor.fetchone()
    
    if person is None:
        conn.close()
        return None
    
    # Get their pets
    cursor.execute('''
        SELECT p.name, p.breed, p.age
        FROM pet p
        JOIN person_pet pp ON p.id = pp.pet_id
        WHERE pp.person_id = ?
    ''', (person_id,))
    
    pets = cursor.fetchall()
    conn.close()
    
    return person, pets

def main():
    while True:
        try:
            person_id = int(input("Enter person ID number: "))
            
            if person_id == -1:
                break
                
            result = get_person_and_pets(person_id)
            
            if result is None:
                print("Error: Person does not exist")
                continue
                
            person, pets = result
            print(f"{person[0]} {person[1]}, {person[2]} years old")
            
            for pet in pets:
                print(f"{person[0]} {person[1]} owned {pet[0]}, a {pet[1]}, that was {pet[2]} years old")
                
        except ValueError:
            print("Please enter a valid number!")


if __name__ == "__main__":
    print("Running query_pets.py")
    main()
