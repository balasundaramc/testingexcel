#New-style classes inherit from object, or from another new-style class
class Dog(object):

    name = 'fggfgdfg'
    moves = []

    def __init__(self, name):
        self.name = name

    def moves_setup(self):
        self.moves.append('walk')
        self.moves.append('run')

    def get_moves(self):
        return self.moves

class Superdog(Dog):

    #Let's try to append new fly ability to our Superdog
    def moves_setup(self):
        #Set default moves by calling method of parent class
        super(Superdog, self).name
        self.moves.append('fly')
		

dog = Superdog('Freddy')
print dog.name # Freddy
dog.moves_setup()
print dog.get_moves() # ['walk', 'run', 'fly']. 
#As you can see our Superdog has all moves defined in the base Dog class