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
