import random


class DNA:
    def __init__(self, target):
        self.genes = []
        self.target = target
        self.fitness = 0
        self.length = len(target)

    def crossover(self, partner):
        if random.random() > 0.1:
            sp = random.randint(0, self.length) // 2  # single random point crossover
            offspring1 = DNA(self.target)
            offspring2 = DNA(self.target)
            offspring1.genes = self.genes[:sp] + partner.genes[sp:]
            offspring2.genes = partner.genes[:sp] + self.genes[sp:]
            return [offspring1, offspring2]
        else:
            return [self, partner]

    def mutation(self):
        if random.random() < 0.1:
            num = random.randint(0, self.length - 1)
            char = random.randint(32, 127)
            self.genes[num] = chr(char)
        else:
            return

    def evaluate(self):
        score = 0
        for i, j in zip(self.genes, list(self.target)):
            if i == j:
                score += 1
        self.fitness = score / self.length
