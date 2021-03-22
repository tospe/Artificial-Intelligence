from Dna import Dna
import random


def map(x, in_min, in_max, out_min, out_max):
    
    result = (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    return result

class Population:

    def __init__(self,mutationTimes,mutationRate, maxPopulation, targetLength):
        self.mutationTimes  = mutationTimes
        self.generations    = 0
        self.targetLength   = targetLength
        self.generations    = 0
        self.mutationRate   = mutationRate
        self.maxPopulation  = maxPopulation
        self.population     = []
        self.matingPool     = []
        self.best           = ''
        self.bestFit        = 0

        for __ in range(maxPopulation):
            self.population.append(Dna(targetLength))

    def calculateFitness(self):
        maxFit = 0
        for i in range(self.maxPopulation):
            self.population[i].calculateFitness()
            if self.population[i].fitness > maxFit:
                maxFit = self.population[i].fitness
                self.best = self.population[i]

            

    def naturalSelection(self):
        self.matingPool = []

        maxFitness = 0

        for i in range(self.maxPopulation):
            if self.population[i].fitness > maxFitness:
                maxFitness = self.population[i].fitness

        print "max fit" + str(maxFitness)
        for i in range(self.maxPopulation):
            mappedFitness = map(self.population[i].fitness, 0.0, maxFitness, 0.0, 1.0)
            # print "mappedFitness" + str(mappedFitness)
            numberOnTimesOnList = int(round(mappedFitness,2)*100)
            #print "numberOnTimesOnList" + str(numberOnTimesOnList)
            
            for __ in range(numberOnTimesOnList):
                self.matingPool.append(self.population[i])
        
    def generate(self):
        firstParent  = ''
        secondParent = ''

        maxFitness = 0
        secondMaxFitness= 0

        for i in range(self.maxPopulation):
            if self.population[i].fitness > maxFitness:
                if firstParent != '':
                    secondParent = firstParent
                    secondMaxFitness = firstParent.fitness

                maxFitness = self.population[i].fitness
                firstParent = self.population[i]

                if maxFitness > self.bestFit:
                    self.best = firstParent
                    self.bestFit = maxFitness

            elif self.population[i].fitness > secondMaxFitness:
                secondParent = self.population[i]
                secondMaxFitness = self.population[i].fitness

        for i in range(self.maxPopulation):
            child = firstParent.crossover(secondParent)
            child.mutate(self.mutationRate)
            self.population[i] = child

        self.calculateFitness()
        
        for i in range(self.maxPopulation):
            if self.population[i].fitness > self.bestFit:
                    self.best = self.population[i]
                    self.bestFit = self.population[i].fitness
        # indexWorstPosition  = 99 
        # indexWorstPositionFitness = 99
        # index2WorstPosition = 99
        # index2WorstPositionFitness = 99

        # for i in range(self.maxPopulation):
        #     if self.population[i].fitness < indexWorstPositionFitness:
        #         index2WorstPositionFitness = indexWorstPosition
        #         index2WorstPosition = indexWorstPosition

        #         indexWorstPositionFitness = self.population[i].fitness
        #         indexWorstPosition = i

        #     elif self.population[i].fitness < index2WorstPositionFitness:
        #         index2WorstPosition = i
        #         index2WorstPositionFitness = self.population[i].fitness

        # if self.population[indexWorstPosition].fitness < firstParent.fitness:
        #     self.population[i] = firstParent

        # if self.population[index2WorstPosition].fitness < firstParent.fitness:
        #     self.population[i] = firstParent

        # if self.population[indexWorstPosition].fitness < secondParent.fitness:
        #     self.population[i] = secondParent
        # if self.population[index2WorstPosition].fitness < secondParent.fitness:
        #     self.population[i] = secondParent

        self.generations += 1
        print "Generation --> " + str(self.generations) + " Max Fit " + str(maxFitness) + " Second Fit " + str(secondMaxFitness) + " Best " + str(self.bestFit)
        print(self.best)

    def __repr__(self):
        return "Population: %s \n" % (self.population)

    def __str__(self):
        return "Population: %s \n" % (self.population)
