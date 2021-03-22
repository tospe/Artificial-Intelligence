

class Perceptron:

    def __init__(self, inputs, weights, threshold):
        self.threshold  = threshold
        self.inputs     = inputs 
        self.weights    = weights 


    def predict(self):
        activation = 0.0
        for i in range(len(self.inputs)):
            activation += self.inputs[i] * self.weights[i]
            
        return 1.0 if activation >= self.threshold else 0.0

