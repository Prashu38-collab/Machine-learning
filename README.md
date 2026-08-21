Through this repository, I am learning and understanding machine learning. I am documenting my learning process in this repository.

Neural Network Implementation

While implementing the basic Version 1 neural network layer, I understood how the zip() function works with for loops.

We cannot manually write 50 inputs × weights + bias for every neuron.

So, we use for loops. The first zip() is used to pair the weights and biases for each neuron. Then, in the inner for loop, we use another zip() to pair each input with its corresponding weight and multiply them. We add the results together add the bias and finally append the neuron's output to the layered_output list.