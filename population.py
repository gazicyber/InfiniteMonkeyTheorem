import random
import sys
from dna import DNA


class Population:
    def __init__(self, target):
        self.population = []
        self.selected_inds = []
        self.target = target
        self.length = len(target)
        self.pop_size = 200

        for i in range(self.pop_size):
            dna = DNA(self.target)
            for j in range(self.length):
                num = random.randint(32, 127)
                char = chr(num)
                dna.genes.append(char)
            self.population.append(dna)

    def evaluate(self):
        for individual in self.population:
            individual.evaluate()

    def selection(self):

        for i in range(self.pop_size):
            parentA = random.choice(self.population)
            parentB = random.choice(self.population)
            parentC = random.choice(self.population)

            if parentA.fitness > parentB.fitness:
                winner = parentA
            else:
                winner = parentB

            if winner.fitness > parentC.fitness:
                selected = winner
            else:
                selected = parentC

            self.selected_inds.append(selected)

    def reproduction(self):

        self.population = []

        for selected1, selected2 in zip(self.selected_inds[1::2], self.selected_inds[::2]):
            offspring1, offspring2 = selected1.crossover(selected2)
            offspring1.mutation()
            offspring2.mutation()
            self.population.append(offspring1)
            self.population.append(offspring2)
            print(''.join(offspring1.genes))
            print(''.join(offspring2.genes))
            if ''.join(offspring1.genes) == self.target or ''.join(offspring2.genes) == self.target:
                sys.exit()

        self.selected_inds = []
