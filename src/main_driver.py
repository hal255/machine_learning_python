"""
    Created by Tazzie
    This is a sample python project that incorporates machine learning
    Tested with Python 3.5.4, 64 bit
"""

import tensorflow as tf


debug = True


class MyTensorFlow:

    def __init__(self):
        if debug:
            print('created new tensor flow object')


def main():
    print('hello machine learning')
    tf.enable_eager_execution()
    tf.executing_eagerly()
    example1()
    example2()
    example3()


def example1():
    x = [[2.]]
    m = tf.matmul(x, x)
    print("hello, {}".format(m))  # => "hello, [[4.]]"


def example2():
    a = tf.constant([[1, 2],
                     [3, 4]])
    print(a)
    # => tf.Tensor([[1 2]
    #               [3 4]], shape=(2, 2), dtype=int32)

    # Broadcasting support
    b = tf.add(a, 1)
    print(b)
    # => tf.Tensor([[2 3]
    #               [4 5]], shape=(2, 2), dtype=int32)

    # Operator overloading is supported
    print(a * b)
    # => tf.Tensor([[ 2  6]
    #               [12 20]], shape=(2, 2), dtype=int32)

    # Use NumPy values
    import numpy as np

    c = np.multiply(a, b)
    print(c)
    # => [[ 2  6]
    #     [12 20]]

    # Obtain numpy value from a tensor:
    print(a.numpy())
    # => [[1 2]
    #     [3 4]]

def example3():
    import tensorflow.contrib.eager as tfe

    w = tfe.Variable([[1.0]])
    with tfe.GradientTape() as tape:
        loss = w * w

    grad = tape.gradient(loss, [w])
    print(grad)  # => [tf.Tensor([[ 2.]], shape=(1, 1), dtype=float32)]

    # A toy dataset of points around 3 * x + 2
    NUM_EXAMPLES = 1000
    training_inputs = tf.random_normal([NUM_EXAMPLES])
    noise = tf.random_normal([NUM_EXAMPLES])
    training_outputs = training_inputs * 3 + 2 + noise

    def prediction(input, weight, bias):
        return input * weight + bias

    # A loss function using mean-squared error
    def loss(weights, biases):
        error = prediction(training_inputs, weights, biases) - training_outputs
        return tf.reduce_mean(tf.square(error))

    # Return the derivative of loss with respect to weight and bias
    def grad(weights, biases):
        with tfe.GradientTape() as tape:
            loss_value = loss(weights, biases)
        return tape.gradient(loss_value, [weights, biases])

    train_steps = 200
    learning_rate = 0.01
    # Start with arbitrary values for W and B on the same batch of data
    W = tfe.Variable(5.)
    B = tfe.Variable(10.)

    print("Initial loss: {:.3f}".format(loss(W, B)))

    for i in range(train_steps):
        dW, dB = grad(W, B)
        W.assign_sub(dW * learning_rate)
        B.assign_sub(dB * learning_rate)
        if i % 20 == 0:
            print("Loss at step {:03d}: {:.3f}".format(i, loss(W, B)))

    print("Final loss: {:.3f}".format(loss(W, B)))
    print("W = {}, B = {}".format(W.numpy(), B.numpy()))

if __name__ == '__main__':
    main()
