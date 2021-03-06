# Week-5-Exercise---Neural-Networks-by-hand

Description

Back propagation neural network is a classic structure of neural network, because its structure and training are relatively simple, it is my entry algorithm when learning neural network. The Data I use is the MNIST data set. The size of the input image is 28*28. Keras also has a function to automatically download the Mnist data set. Deep learning is divided into the following three steps.

First of all, in Keras, a model is declared: model = Sequential(). Next is the model. For example, I want to stack a network. My approach is to add a fully connected network Dense() with the add() function in the model. input_nodes = 28*28, which means that the input is a 28*28 image, and we straighten it into a 28*28-dimensional vector.

Then do 10 categories. So units is set to 10. **The function is usually softmax. Next, I want to evaluate the quality of a function. Use model.compile() function and write loss ='categorical crossentropy'.
The third step is training. I download the optimizer and find a good function. To use model.fit(), four parameters need to be given. When this line is called, Keras will train my network. The first parameter is Training data, and the second parameter is label. The data set is a 3-dimensional vector (instance length, width, height). For the multi-layer perceptron, the input of the model is a two-dimensional vector, so here you need to reshape the data set, that is, convert a 28*28 vector into a 784 length Array. You can easily implement this process with numpy's reshape function. The gray value of a given pixel is 0-255. In order to make the training effect of the model better, the value is usually normalized and mapped to 0-1. The output of the model is the scoring prediction for each category. There is a prediction score for each category from 0-9 to the classification result, which indicates the probability of predicting the model input to the category. The greater the probability, the higher the reliability . Since the original data label is an integer value of 0-9, it is usually expressed as a 0ne-hot vector. For example, the label of the first training data is 5, and one-hot is represented as [0,0,0,0,0,1,0,0,0,0].

Result:
![image](https://github.com/lanxin01/Week-5-Exercise---Neural-Networks-by-hand/blob/main/neural%20network%20result.png)
