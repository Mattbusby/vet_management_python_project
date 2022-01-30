import pdb
from models.pet import Pet
from models.vet import Vet

import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository

pet_repository.delete_all()
vet_repository.delete_all()

vet1 = Vet(   NAME  ETC    )
vet_repository.save(vet1)
vet2 = Vet(   NAME  ETC    )
vet_repository.save(vet2)


pet_1 = Pet(   NAME  ETC    , vet1)
pet_repository.save(pet_1)

pet_2 = Pet(   NAME  ETC    , vet1)
pet_repository.save(pet_2)

pet_3 = Pet(   NAME  ETC    , vet2)
pet_repository.save(pet_3)

Pet_4 = Pet(   NAME  ETC    , vet1)
pet_repository.save(pet_1)

pet_5 = Pet(   NAME  ETC    , vet1)
pet_repository.save(pet_2)

pet_6 = Pet(   NAME  ETC    , vet2)
pet_repository.save(pet_3)

pdb.set_trace()


# pets and vets needed