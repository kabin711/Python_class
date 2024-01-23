class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def makesound(self):
        pass
    
    def eat(self):
        print(f'{self.name} eating')

class Mammal(Animal):
    def __init__(self, name, species, fur_colour):
        super().__init__( name, species )
        self.fur_colour = fur_colour
        
    def makesound(self):
        print(f'{self.name} making animal sound')
    
    def givebirth(self):
        print(f'{self.name} giving birth')

class Birds(Animal):
    def __init__(self, name, species, feather_colour):
        super().__init__( name, species )
        self.feather_colour = feather_colour
        
    def makesound(self):
        print(f'{self.name} melody sound')
    
    def layegg(self):
        print(f'{self.name} lay eggs')
    
class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []
    
    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self.animals.append(animal)
            print(f'{animal.name} is add to {self.name} to zoo')
        else:
            ('invalid animal')
    
    def perform_zoo(self):
        print('welcome {self.name} to zoo')
        print('Todays Activities: ')
        for animal in self.animals:
            print(f'{animal.name}')
            animal.makesound()
            animal.eat()
            if isinstance(animal, Mammal):
                animal.givebirth()
            elif isinstance(animal, Birds):
                animal.layegg()

lion = Mammal('King', 'Lion', 'Golden')
parrot = Birds("Polly", "Parrot", "Green")

zoo = Zoo('Fantastic zoo')
  
zoo.add_animal(lion)
zoo.add_animal(parrot)          
            
        