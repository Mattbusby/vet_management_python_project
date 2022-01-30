DROP TABLE IF EXISTS pets;
DROP TABLE IF EXISTS vets;

CREATE TABLE vets (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    grad_date VARCHAR(255),
    fun_fact VARCHAR(255)
);

CREATE TABLE pets (
    id SERIAL PRIMARY KEY,
    pet_name VARCHAR(255),
    dob VARCHAR(255),
    type_of_animal VARCHAR(255),
    owner_name VARCHAR(255),
    owner_ph VARCHAR(255),
    treatment_notes TEXT
    vet_id INT REFERENCES vets(id)
);


-- add owners as a class later if pushing for many to many with pets becoming the link