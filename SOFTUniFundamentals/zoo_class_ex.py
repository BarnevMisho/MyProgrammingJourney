class Zoo:
    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []
        self.total_animals = 0

    def add_animal(self, species, animal_name):
        if species == "mammal":
            self.mammals.append(animal_name)
        elif species == "fish":
            self.fishes.append(animal_name)
        elif species == "bird":
            self.birds.append(animal_name)

        self.total_animals += 1

    def get_info(self, species):
        if species == "mammal":
            return f"Mammals in {self.name}: {', '.join(self.mammals)}\nTotal animals: {self.total_animals}"
        elif species == "fish":
            return f"Fishes in {self.name}: {', '.join(self.fishes)}\nTotal animals: {self.total_animals}"
        elif species == "bird":
            return f"Birds in {self.name}: {', '.join(self.birds)}\nTotal animals: {self.total_animals}"


zoo_name = input()
number_animals = int(input())
zoo = Zoo(zoo_name)

for _ in range(number_animals):
    animals = input().split()
    zoo.add_animal(animals[0], animals[1])

species = input()
print(zoo.get_info(species))

