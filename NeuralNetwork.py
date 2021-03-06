# code for a 3_layer neural network, and code for learning the Mnist dataset

from keras.layers import Dense
from keras.models import Sequential
from keras.datasets import mnist
from keras.utils import np_utils


def get_model(hidden_nodes, output_nodes, optimizer, loss='categorical_crossentropy', metric='accuracy'):
    model = Sequential()
    model.add(Dense(hidden_nodes))
    model.add(Dense(output_nodes, activation='softmax'))
    model.compile(loss=loss, optimizer=optimizer, metrics=[metric])
    return model


input_nodes = 784  # 图片都是28*28的
hidden_nodes = 100
output_nodes = 10


learning_rate = 0.3

optimizer ='adam'


model = get_model(hidden_nodes, output_nodes, optimizer)

(X_train, y_train), (X_test, y_test) = mnist.load_data()

num_pixels = X_train.shape[1] * X_train.shape[2]
X_train = X_train.reshape(X_train.shape[0], num_pixels).astype('float32')
X_test = X_test.reshape(X_test.shape[0], num_pixels).astype('float32')

X_train = X_train / 255
X_test = X_test / 255


y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)
num_classes = y_test.shape[1]


# 训练网络
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=10, batch_size=200, verbose=2)

# Final evaluation of the model
scores = model.evaluate(X_test, y_test, verbose=0)
print("BPNN Error: %.2f%%" % (100-scores[1]*100))


