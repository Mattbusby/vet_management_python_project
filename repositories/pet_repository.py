from db.run_sql import run_sql
from models.pet import Pet
from models.vet import Vet
import repositories.vet_repository as vet_repository

def save(pet):
    sql = "INSERT INTO pets (pet_name, dob, type_of_animal, owner_name, owner_ph, treatment_notes, vet_id) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [pet.pet_name, pet.dob, pet.type_of_animal, pet.owner_name, pet.owner_ph, pet.treatment_notes, pet.vet.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    pet.id = id
    return pet

def select_all():
    pets = []
    sql = "SELECT * FROM pets"
    results = run_sql(sql)
    for row in results:
        vet = vet_repository.select(row['vet_id'])
        pet = Pet(row['pet_name'], row['dob'], row['type_of_animal'], row['owner_name'], row['owner_ph'], row['treatment_notes'], vet)
        pets.append(pet)
    return pets

def select(id):
    pet = None
    sql = "SELECT * FROM pets WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        vet = vet_repository.select(result['vet_id'])
        pet = Pet(result['pet_name'], result['dob'], result['type_of_animal'], result['owner_name'], result['owner_ph'], result['treatment_notes'], vet)
    return pet

def delete_all():
    sql = "DELETE FROM pets"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM pets WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(pet):
    sql = "UPDATE pets set (pet_name, dob, type_of_animal, owner_name, owner_ph, treatment_notes, vet_id) = (%s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [pet.pet_name, pet.dob, pet.type_of_animal, pet.owner_name, pet.owner_ph, pet.treatment_notes, pet.vet.id, pet.id]
    print(values)
    run_sql(sql, values)



# check delete all & delete(id) work
# does update need 'VALUES' before %s's to work?