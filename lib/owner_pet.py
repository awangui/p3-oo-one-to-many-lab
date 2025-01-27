class Pet:
    
    all = []
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        if pet_type in Pet.PET_TYPES:
            self.pet_type = pet_type
        else:
            raise Exception("Invalid pet type")
        self._owner = owner
        Pet.all.append(self)
    
    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, owner):
        if isinstance(owner, Owner):
            self._owner = owner
        else:
            raise Exception("Invalid owner instance")

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise Exception("Invalid pet instance")

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)