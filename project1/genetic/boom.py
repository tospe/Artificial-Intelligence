import Dna
from Population import Population
from numpy import genfromtxt

def main():
    mutationTimes = 10
    mutationRate = 0.2
    maxPopulation = 200
    targetLength = 10

    maxGen = 500
    
    population = Population(mutationTimes,mutationRate, maxPopulation, targetLength)
    

    while population.generations < maxGen:

        population.calculateFitness()

        # population.naturalSelection()

        population.generate()
    print(population.best)

if __name__ == '__main__':
	main()
