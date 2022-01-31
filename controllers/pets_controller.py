from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.pet import Pet
import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository

pets_blueprint = Blueprint("pets", __name__)

@pets_blueprint.route("/pets")
def pets():
    pets = pet_repository.select_all()
    return render_template("pets/index.html", all_pets = pets)

@pets_blueprint.route("/pets/new", methods = ['GET'])
def new_pet():
    vets = vet_repository.select_all()
    return render_template("pets/new.html", all_vets = vets)

@pets_blueprint.route("/pets", methods=['POST'])
def create_pet():
    pet_name = request.form['pet_name']
    dob = request.form['dob']
    type_of_animal = request.form['type_of_animal']
    owner_name = request.form['owner_name']
    owner_ph = request.form['owner_ph']
    treatment_notes = request.form['treatment_notes']
    pet = Pet(pet_name, dob, type_of_animal, owner_name, owner_ph, treatment_notes)
    pet_repository.save(pet)
    return redirect('/pets')

@pets_blueprint.route("/pets/<id>", methods=['GET'])
def show_pet(id):
    pet = pet_repository.select(id)
    return render_template('pets/view.html', pet = pet)

@pets_blueprint.route("/pets/<id>/edit", methods=['GET'])
def edit_pet(id):
    pet = pet_repository.select(id)
    vets = vet_repository.select_all()
    return render_template('pets/edit.html', pet = pet, all_vets = vets)

@pets_blueprint.route("/pets/<id>", methods = ['POST'])
def update_pet(id):
    pet_name = request.form['pet_name']
    dob = request.form['dob']
    type_of_animal = request.form['type_of_animal']
    owner_name = request.form['owner_name']
    owner_ph = request.form['owner_ph']
    treatment_notes = request.form['treatment_notes']
    vet = vet_repository.select(request.form['vet_id'])
    pet = Pet(pet_name, dob, type_of_animal, owner_name, owner_ph, treatment_notes, vet, id)
    print(pet.vet.full_name())
    # above line needed??
    pet_repository.update(pet)
    return redirect('/pets')

@pets_blueprint.route("/pets/<id>/delete", methods=['POST'])
def delete_pet(id):
    pet_repository.delete(id)
    return redirect('/pets')
    
    
    





# check line 7 blueprint name vs other files
# new/create/show/edit/update/delete