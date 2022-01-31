class Pet:

    def __init__(self, pet_name, dob, type_of_animal, owner_name, owner_ph, treatment_notes, vet, id = None):
        self.pet_name = pet_name
        self.dob = dob
        self.type_of_animal = type_of_animal
        self.owner_name = owner_name
        self.owner_ph = owner_ph
        self.treatment_notes = treatment_notes
        self.vet = vet
        self.id = id


# owner as a seperate class (many to many?), treatment notes (dated?).