import random
from Perceptron import Perceptron
from numpy import genfromtxt
import numpy as np
random.seed(1312)
class Dna:

    def __init__(self, length):
        self.fitness = 0.0
        self.genes = []
        self.length = length

        for __ in range(length):
            self.genes.append(newWeight())
    
    def calculateFitness(self):
        weights = self.genes[:-1]
        threshold = self.genes[-1]
        my_data = genfromtxt('gp-training-set.csv', delimiter=',')
        score = 0

        for e in my_data:
            inputs = e[:-1]
            target = e[-1]

            perceptron = Perceptron(inputs, weights, threshold)
            if perceptron.predict() == target:
                score+=1
        self.fitness = score
        
    def crossover(self,partner):
        child = Dna(self.length)
        midpoint = round(np.random.randint(low=0, high=self.length, size=1))


        for i in range(self.length-1):
            if i > midpoint:
                child.genes[i] = self.genes[i]
            else:
                child.genes[i] = partner.genes[i]

        # if np.random.randint(low=0, high=1, size=1) > 0.5:
        #     t = self.genes[-1]
        # else:
        #     t = partner.genes[-1]
        
        # for i in range(self.length-1):
        #     if i > midpoint:
        #         child.genes[i] = self.genes[i]
        #     else:
        #         child.genes[i] = partner.genes[i]
        # child.genes[-1] = t

        return child
    
    def mutate(self, mutationRate):
        for i in range(self.length):
            if np.random.uniform(low=0, high=1, size=1) < mutationRate:
                # print "mutate"
                self.genes[i] = newWeight()

    def __repr__(self):
        return "    DNA: %s |  Fitness %s \n" % (self.genes, self.fitness)

    def __str__(self):
                return "    DNA: %s |  Fitness%s \n" % (self.genes, self.fitness)

def newWeight():
        return np.random.uniform(low=-5, high=5, size=1)[0]

