from db.run_sql import run_sql
from models.vet import Vet
from models.pet import Pet

def save(vet):
    sql = "INSERT INTO vets (first_name, last_name, grad_date, fun_fact) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [vet.first_name, vet.last_name, vet.grad_date, vet.fun_fact]
    results = run_sql(sql, values)
    id = results[0]['id']
    vet.id = id
    return vet

def select_all():
    vets = []
    sql = "SELECT * FROM vets"
    results = run_sql(sql)
    for row in results:
        vet = Vet(row['first_name'], row['last_name'], row['grad_date'], row['fun_fact'], row['id'])
        vets.append(vet)
    return vets

def select(id):
    vet = None
    sql = "SELECT * FROM vets WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        vet = Vet(result['first_name'], result['last_name'], result['grad_date'], result['fun_fact'], result['id'])
    return vet

def delete_all():
    sql = "DELETE FROM vets"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM vets WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(vet):
    sql = "UPDATE vets SET (first_name, last_name, grad_date, fun_fact) = (%s, %s, %s, %s) WHERE id = %s"
    values = [vet.first_name, vet.last_name, vet.grad_date, vet.fun_fact]
    run_sql(sql, values)

def pets(vet):
    pets = []
    sql = "SELECT * FROM pets WHERE vet_id = %s"
    values = [vet.id]
    results = run_sql(sql, values)
    for row in results:
        pet = Pet(row['pet_name'], row['dob'], row['type_of_animal'], row['owner_name'], row['owner_ph'], row['treatment_notes'], row['vet_id'], row['id'])
        pets.append(pet)
    return pets


# check if * needed in delete all & delete(id)