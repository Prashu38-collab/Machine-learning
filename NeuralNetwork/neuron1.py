#learning to build neural network from scratch to understand how things is actually working behind the scene

# neuron with three inputs
inputs=[1,2,3]
weights=[0.2, 0.8, -0.5]
bias=2
outputs=(inputs[0]*0.2+inputs[1]*0.8+inputs[2]*-0.5)+bias
print(outputs)

# neuron with 4 inputs 

inputs=[1,2,3,4]
weights=[0.2, 0.8, -0.5, 1.0]
bias=2.0
outputs=(inputs[0]*0.2+inputs[1]*0.8+inputs[2]*-0.5+inputs[3]*1.0)+bias
print(outputs)

# Layers of neurons
inputs = [1, 2, 3, 2.5]

##LIST OF WEIGHTS
weights = [[0.2, 0.8, -0.5, 1],
 [0.5, -0.91, 0.26, -0.5],
 [-0.26, -0.27, 0.17, 0.87]]

##LIST OF BIASES
biases = [2, 3, 0.5]

# Outputs of neurons
layered_output=[]
# for each neuron

for neuron_weight, neuron_bias in zip(weights,biases):
    neuron_output=0
    for n_input,weight in zip(inputs,neuron_weight):
        neuron_output+=n_input*weight ## W31*X1 + W32*X2 + W33*X3 + W34*X4
         # Add bias
    neuron_output += neuron_bias ## ## W31*X1 + W32*X2 + W33*X3 + W34*X4 + B3
 # Put neuron's result to the layer's output list
    layered_output.append(neuron_output)
print(layered_output)


