from population import Population


def main():
    target = "To be or not to be, that is the question."
    population = Population(target)
    generation = 0
    while True:
        generation += 1
        population.evaluate()
        population.selection()
        population.reproduction()
        print(f"-------------{generation}------------")


if __name__ == '__main__':
    main()
