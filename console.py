import pdb
from models.pet import Pet
from models.vet import Vet
# import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository
import repositories.pet_repository as pet_repository

pet_repository.delete_all()
vet_repository.delete_all()

vet1 = Vet("William", "Rennie", "01.02.2010", "He likes turtles")
vet_repository.save(vet1)
vet2 = Vet("Billy", "Rennie", "01.02.2010", "He likes snakes")
vet_repository.save(vet2)
# # vet2 = Vet(   NAME  ETC    )
# # vet_repository.save(vet2)


pet1 = Pet("Esiotrot", "01.01.2020", "Tortoise", "Bob Ross", "0123456789", "Likes lettuce", vet1)
pet_repository.save(pet1)

# pet2 = Pet(   NAME  ETC    , vet1)
# pet_repository.save(pet2)

# pet3 = Pet(   NAME  ETC    , vet2)
# pet_repository.save(pet3)

# Pet4 = Pet(   NAME  ETC    , vet1)
# pet_repository.save(pet4)

# pet5 = Pet(   NAME  ETC    , vet1)
# pet_repository.save(pet5)

# pet6 = Pet(   NAME  ETC    , vet2)
# pet_repository.save(pet6)

pdb.set_trace()


# pets and vets needed