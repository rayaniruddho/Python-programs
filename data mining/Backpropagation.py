# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 23:16:35 2017

@author: Aniruddho
"""
import math

layers = list(input("Enter the network topology(eg. 321): "))
for i in range(0,len(layers)):
    layers[i] = int(layers[i])

num_layers = len(layers)
num_inputs = layers[0]
num_outputs = layers[-1]
num_hidden_layers = num_layers - 2
num_hidden_nodes = []

network = {}
#inputs = []
weights = {}
biases = {}

count = 1
learn_rate = 0.9

I = {}
O = {}
Err = {}

delta_w_ij = {}
delta_t_ij = {}

epoch = 0

"""
Store the nodes per layer in a dictionary called network
key = layer number
value = list of nodes in that layer
"""
for j in range(0,num_layers):
    temp = []
    while count<=sum(layers[:j+1]):
        temp.append(count)
        count += 1
    network["layer "+str(j+1)] = temp

"""
Calculate number of hidden nodes
"""
for i in range(0,num_hidden_layers):
    #num_hidden_nodes contains the number of nodes in each hidden layer as a list 
    num_hidden_nodes.append(layers[i+1])
    
"""
Take the inputs of input layer and store as output of that layer
"""
#for testing the weights,inputs and biases are taken as user input
#need to change it so bias and weights are generated randomly and inputs are read from a file
for i in range(0,num_inputs):
    O[i+1] = float(input("Enter input "+str(i+1)+": "))
    #inputs.append(x)

"""
Take the biases as input
"""
for i in range(1,sum(layers[1:])+1):
    biases[(layers[0]+i)] = float(input("Enter bias value theta "+str(layers[0]+i)+": "))

"""
Take the weights of connections as input
"""
for i in range(1,num_layers):
    for j in network["layer "+str(i)]:
        for k in network["layer "+str(i+1)]:
            weights[(j,k)] = float(input("Enter weight w"+str(j)+str(k)+": "))
            
while True:
    terminate = True
    epoch += 1
            
    """
    Calculate the input and output of intermediate and final layers
    """
    for i in range(layers[0]+1,sum(layers[:])+1):
        I[i] = 0
        for k in weights:
            if k[1] == i:
                I[i] += weights[k]*O[k[0]]
        I[i] += biases[i]
        O[i] = 1/(1+math.exp(-I[i]))
        
    """
    Error of output layer
    """
    Err[sum(layers[:])] = O[sum(layers[:])]*(1- O[sum(layers[:])])*(1- O[sum(layers[:])])
    
    """
    Calculate errors of intermediate layers
    """
    for i in range(sum(layers[:-1]),layers[0],-1):
        err = 0
        for w in weights:
            if w[0] == i:
                err += Err[w[1]]*weights[w]            
        Err[i] = O[i]*(1-O[i])*err
    
    """
    Calculate change in weights and biases
    """
    for w in weights:
        delta_w_ij[w] = learn_rate*Err[w[1]]*O[w[0]]
        
    for t in biases:
        delta_t_ij[t] = learn_rate*Err[t]
        
    """
    Check for termination
    """
    for dw in delta_w_ij:
        if delta_w_ij[dw] > 0.001:
            terminate = False
            break
            
    if terminate == True:
        f = open('Trained weights','w')
        f.write("Weights:\n\n")
        f.write(str(weights))
        f.write("\n\nBiases:\n\n")
        f.write(str(biases))
        f.close()
        print("epoch "+str(epoch))
        print("Weights:")
        print(weights)
        print("Biases:")
        print(biases)
        break
            
    """
    Update weights and biases for next epoch
    """
    for w in weights:
        weights[w] += delta_w_ij[w]
        
    for t in biases:
        biases[t] += delta_t_ij[t]