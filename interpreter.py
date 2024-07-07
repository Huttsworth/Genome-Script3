import tensorflow as tf
import cProfile


class NeuralNetwork:

    def __init__(self):
        self.model = tf.keras.Sequential()

    def add(self, layer):
        if layer.type == 'Dense':
            self.model.add(
                tf.keras.layers.Dense(units=layer.units,
                                      activation=layer.activation))

    def compile(self, optimizer, loss):
        self.model.compile(optimizer=optimizer, loss=loss)

    def train(self, data, labels, epochs, batch_size):
        print("Training model with TensorFlow")
        self.model.fit(data, labels, epochs=epochs, batch_size=batch_size)


class Layer:

    def __init__(self, type, units, activation):
        self.type = type
        self.units = units
        self.activation = activation


def load_data(filename):
    # Simulate loading data using tf.data API for efficient input pipeline
    data = tf.data.Dataset.from_tensor_slices(tf.random.normal([100, 10]))
    return data.batch(32)


def load_labels(filename):
    # Simulate loading labels and one-hot encode them using tf.data API
    raw_labels = tf.random.uniform([100], minval=0, maxval=10, dtype=tf.int32)
    labels = tf.data.Dataset.from_tensor_slices(
        tf.one_hot(raw_labels, depth=10))
    return labels.batch(32)


def preprocess_data(data):
    # Normalize data
    return data.map(lambda x: (x - tf.reduce_mean(x)) / tf.math.reduce_std(x))


def main():
    # Example script execution
    data = load_data('data.csv')
    labels = load_labels('labels.csv')

    # Apply preprocessing to the data
    data = preprocess_data(data)

    model = NeuralNetwork()
    model.add(Layer(type='Dense', units=64, activation='relu'))
    model.add(Layer(type='Dense', units=10, activation='softmax'))

    model.compile(optimizer='adam', loss='categorical_crossentropy')
    for epoch in range(10):
        for d, l in zip(data, labels):
            model.train(d, l, epochs=1, batch_size=32)


if __name__ == "__main__":
    cProfile.run('main()')
