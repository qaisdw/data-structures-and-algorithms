from stack_queue_animal_shelter.animal import Animal, Cat, Dog


class AnimalShelter:
    """ A shelter that holds dogs and cats, and returns  first animal that
      matches the preference"""


    def __init__(self):
        self.animals = []

    def enqueue(self, animal):
        if isinstance(animal, (Dog, Cat)):
            self.animals.append(animal)

        else:
            raise TypeError("Animal must be a Dog or Cat")

    def dequeue(self, pref = None ):

        """Remove the first animal from  shelter that matches 
        the preference, or the first animal if no preference is given"""
        
        if pref is None and len(self.animals) > 0:
            return self.animals.pop(0)

        for i, animal in enumerate(self.animals):
            if animal.species == pref:
                return self.animals.pop(i)

        return None
