"""
This is an exercise in class and API design.

Setup
- An `Animal` has the following properties:
    - Name
    - Number of legs
    - Sound that it makes
- A `Monster` is created from two different `Animals` with the same number of legs: 
  one for the head and one for the body.
- A `Monster` has the following properties:
    - Name (the combination of the names of the head and body)
    - Number of legs
    - `Animal` head
    - `Animal` body
    - Sound that it makes (the combination of the sounds of its `Animal` head and 
      body)

Tasks:

1. An `Animal` class
    - Example constructor call: `Animal(name: "Octopus", numLegs: 8, sound: "Burble")`
2. A `Monster` class, that creates a `Monster` from an `Animal` head and an `Animal` 
   body
    - Example constructor call: `Monster(head: Animal(Octopus), body: Animal(Scorpion))`
        - `Monster.name` → `OctopusScorpion`
        - `Monster.sound` → `BurbleHiss` 
    - Your code should ensure that we can only create a `Monster` with the head 
      and body of two different `Animals`, who have the same number of legs.
3. A function `createAllMonsters` that takes as input a number of legs and 
   returns an array of all `Monsters` that can be made with that number of legs. 
   A `Monster` with `Animal` A head and `Animal` B body is distinct from a `Monster` 
   with `Animal` B head and `Animal` A body. Please use the animals.txt file linked 
   at the beginning of this problem.
    - Example function call: `createAllMonsters(8)` → `[Monster(OctopusScorpion), 
      Monster(ScorpionOctopus)]`
    - The crux of this function is: how do we produce all of the combinations 
      of heads and bodies for animals with a given number of legs?
4. A function `getRandomMonster` that takes as input a number of legs and returns 
   a random Monster with that number of legs.
    - Example function call: `getRandomMonster(8)` → `Monster(OctopusScorpion)`
    - This function should call your `createAllMonsters` function
"""

# Animals: have 2 attributes and 1 method

# Monsters: have 4 attributes and 1 method (that might require overwriting inherited
# method)
from __future__ import annotations
from typing import List
from pathlib import Path
import csv
import random


class Animal:
    def __init__(self, name: str, number_of_legs: int, sound: str):
        self.name: str = name
        self.number_of_legs: int = number_of_legs
        self.sound: str = sound

    def play_sound(self):
        print(self.sound)

    @classmethod
    def load_data_as_Animals(self) -> List[Animal]:
        ANIMAL_PATH: Path = Path("Monster_Maker/tests/fixtures/animals.txt")

        animals_list: List[Animal] = []
        # Loop over each animal in the dataset
        with open(ANIMAL_PATH, mode="r") as f:
            for idx, animal in enumerate(csv.reader(f)):
                # Skip the header
                if idx == 0:
                    continue

                animals_list.append(
                    Animal(
                        name=animal[0],
                        number_of_legs=int(animal[2]),
                        sound=animal[3],
                    )
                )

        return animals_list


class Monster(Animal):
    def __init__(self, animal1: Animal, animal2: Animal):
        assert (
            animal1.number_of_legs == animal2.number_of_legs
        ), "Animals must have the same number of legs."

        self.name: str = animal1.name + animal2.name
        self.number_of_legs: int = animal1.number_of_legs
        self.head: str = animal1.name
        self.body: str = animal2.name
        self.sound: str = animal1.sound + animal2.sound

    def __repr__(self):
        r: str = f"Monster({self.name}, number_of_legs={self.number_of_legs}, "
        r += f"sound={self.sound})"

        return r

    @classmethod
    def create_all_monsters(self, n_legs: int) -> List[Monster]:
        """
        Takes as input a number of legs and returns an array of all `Monsters`
        that can be made with that number of legs.
        """

        # Filter animals for number of legs
        animal_subset: List[Animal] = [
            animal
            for animal in Monster.load_data_as_Animals()
            if animal.number_of_legs == n_legs
        ]

        # Combine animal names into viable monsters - permuation
        possible_monsters: List[Monster] = []
        for idx in range(len(animal_subset)):
            curr_animal: Animal = animal_subset[idx]
            if idx == 0:
                remaining_animals = animal_subset[idx + 1 :]
            elif idx != 0 and idx != len(animal_subset) - 1:
                remaining_animals = animal_subset[0:idx] + animal_subset[idx + 1 :]
            else:
                remaining_animals = animal_subset[0:idx]

            for animal_object in remaining_animals:
                result: Monster = Monster(curr_animal, animal_object)
                possible_monsters.append(result)

        return possible_monsters

    @classmethod
    def get_random_monster(self, number_of_legs: int) -> Monster:
        """
        takes as input a number of legs and returns
        a random Monster with that number of legs.

        This function should call your `createAllMonsters` function
        """

        viable_monsters: List[Monster] = Monster.create_all_monsters(number_of_legs)
        random_monster: Monster = random.choice(viable_monsters)
        return random_monster


"""
You only need to redefine inherited functions if you'd like to change their function.
"""

if __name__ == "__main__":
    # 1st test: Animal interface
    print("Test 1: Animal interface\n")
    a1: Animal = Animal(name="chicken", number_of_legs=2, sound="bock")
    a2: Animal = Animal(name="horse", number_of_legs=2, sound="nay")

    # 2nd test: Monster interface
    print("Test 2: Monster interface")
    m_test = Monster(animal1=a1, animal2=a2)
    m_test.play_sound()
    print()

    # 3rd test: Monster.create_all_monsters(number_of_legs)
    print("Test 3: Monster.create_all_monsters(number_of_legs)")
    results: List[str] = Monster.create_all_monsters(2)
    for r in results:
        print(r)
    print()

    # 4th test: Monster.get_random_monster(number_of_legs)
    print("Test 4: Monster.get_random_monster(number_of_legs)")
    random_monster: Monster = Monster.get_random_monster(4)
    print(random_monster)
    print()
