import tensorflow as tf
import numpy as np
# For plotting the images
from matplotlib import pyplot as plt
from collections import Counter


class SOM(object):
    """
    2-D Self-Organizing Map with Gaussian Neighbourhood function
    and linearly decreasing learning rate.
    """

    # To check if the SOM has been trained
    _trained = False

    def __init__(self, m, n, dim, n_iterations=100, alpha=None, sigma=None):
        """
        Initializes all necessary components of the TensorFlow
        Graph.

        m X n are the dimensions of the SOM. 'n_iterations' should
        should be an integer denoting the number of iterations undergone
        while training.
        'dim' is the dimensionality of the training inputs.
        'alpha' is a number denoting the initial time(iteration no)-based
        learning rate. Default value is 0.3
        'sigma' is the the initial neighbourhood value, denoting
        the radius of influence of the BMU while training. By default, its
        taken to be half of max(m, n).
        """

        # Assign required variables first
        self._m = m
        self._n = n
        if alpha is None:
            alpha = 0.3
        else:
            alpha = float(alpha)
        if sigma is None:
            sigma = max(m, n) / 2.0
        else:
            sigma = float(sigma)
        self._n_iterations = abs(int(n_iterations))

        ##INITIALIZE GRAPH
        self._graph = tf.Graph()

        ##POPULATE GRAPH WITH NECESSARY COMPONENTS
        with self._graph.as_default():

            ##VARIABLES AND CONSTANT OPS FOR DATA STORAGE

            # Randomly initialized weightage vectors for all neurons,
            # stored together as a matrix Variable of size [m*n, dim]
            self._weightage_vects = tf.Variable(tf.random_normal(
                [m * n, dim]))

            # Matrix of size [m*n, 2] for SOM grid locations
            # of neurons
            self._location_vects = tf.constant(np.array(
                list(self._neuron_locations(m, n))))

            ##PLACEHOLDERS FOR TRAINING INPUTS
            # We need to assign them as attributes to self, since they
            # will be fed in during training

            # The training vector
            self._vect_input = tf.placeholder("float", [dim])
            # Iteration number
            self._iter_input = tf.placeholder("float")

            ##CONSTRUCT TRAINING OP PIECE BY PIECE
            # Only the final, 'root' training op needs to be assigned as
            # an attribute to self, since all the rest will be executed
            # automatically during training

            # To compute the Best Matching Unit given a vector
            # Basically calculates the Euclidean distance between every
            # neuron's weightage vector and the input, and returns the
            # index of the neuron which gives the least value
            bmu_index = tf.argmin(tf.sqrt(tf.reduce_sum(
                tf.pow(tf.subtract(self._weightage_vects, tf.stack(
                    [self._vect_input for i in range(m * n)])), 2), 1)),
                0)

            # This will extract the location of the BMU based on the BMU's
            # index
            slice_input = tf.pad(tf.reshape(bmu_index, [1]),
                                 np.array([[0, 1]]))
            bmu_loc = tf.reshape(tf.slice(self._location_vects, slice_input,
                                          tf.constant(np.array([1, 2]))),
                                 [2])

            # To compute the alpha and sigma values based on iteration
            # number
            learning_rate_op = tf.subtract(1.0, tf.div(self._iter_input,
                                                  self._n_iterations))
            _alpha_op = tf.multiply(alpha, learning_rate_op)
            _sigma_op = tf.multiply(sigma, learning_rate_op)

            # Construct the op that will generate a vector with learning
            # rates for all neurons, based on iteration number and location
            # wrt BMU.
            bmu_distance_squares = tf.reduce_sum(tf.pow(tf.subtract(
                self._location_vects, tf.stack(
                    [bmu_loc for i in range(m * n)])), 2), 1)
            neighbourhood_func = tf.exp(tf.negative(tf.div(tf.cast(
                bmu_distance_squares, "float32"), tf.pow(_sigma_op, 2))))
            learning_rate_op = tf.multiply(_alpha_op, neighbourhood_func)

            # Finally, the op that will use learning_rate_op to update
            # the weightage vectors of all neurons based on a particular
            # input
            learning_rate_multiplier = tf.stack([tf.tile(tf.slice(
                learning_rate_op, np.array([i]), np.array([1])), [dim])
                                                for i in range(m * n)])
            weightage_delta = tf.multiply(
                learning_rate_multiplier,
                tf.subtract(tf.stack([self._vect_input for i in range(m * n)]),
                       self._weightage_vects))
            new_weightages_op = tf.add(self._weightage_vects,
                                       weightage_delta)
            self._training_op = tf.assign(self._weightage_vects,
                                          new_weightages_op)

            ##INITIALIZE SESSION
            self._sess = tf.Session()

            ##INITIALIZE VARIABLES
            init_op = tf.initialize_all_variables()
            self._sess.run(init_op)

    def _neuron_locations(self, m, n):
        """
        Yields one by one the 2-D locations of the individual neurons
        in the SOM.
        """
        # Nested iterations over both dimensions
        # to generate all 2-D locations in the map
        for i in range(m):
            for j in range(n):
                yield np.array([i, j])

    def train(self, input_vects):
        """
        Trains the SOM.
        'input_vects' should be an iterable of 1-D NumPy arrays with
        dimensionality as provided during initialization of this SOM.
        Current weightage vectors for all neurons(initially random) are
        taken as starting conditions for training.
        """

        # Training iterations
        for iter_no in range(self._n_iterations):
            # Train with each vector one by one
            for input_vect in input_vects:
                self._sess.run(self._training_op,
                               feed_dict={self._vect_input: input_vect,
                                          self._iter_input: iter_no})

        # Store a centroid grid for easy retrieval later on
        centroid_grid = [[] for i in range(self._m)]
        self._weightages = list(self._sess.run(self._weightage_vects))
        self._locations = list(self._sess.run(self._location_vects))
        for i, loc in enumerate(self._locations):
            centroid_grid[loc[0]].append(self._weightages[i])
        self._centroid_grid = centroid_grid

        self._trained = True

    def get_centroids(self):
        """
        Returns a list of 'm' lists, with each inner list containing
        the 'n' corresponding centroid locations as 1-D NumPy arrays.
        """
        if not self._trained:
            raise ValueError("SOM not trained yet")
        return self._centroid_grid

    def map_vects(self, input_vects):
        """
        Maps each input vector to the relevant neuron in the SOM
        grid.
        'input_vects' should be an iterable of 1-D NumPy arrays with
        dimensionality as provided during initialization of this SOM.
        Returns a list of 1-D NumPy arrays containing (row, column)
        info for each input vector(in the same order), corresponding
        to mapped neuron.
        """

        if not self._trained:
            raise ValueError("SOM not trained yet")

        to_return = []
        for vect in input_vects:
            min_index = min([i for i in range(len(self._weightages))],
                            key=lambda x: np.linalg.norm(vect -
                                                         self._weightages[x]))
            to_return.append(self._locations[min_index])

        return to_return


    def distances(self, input_vects):
        return


if __name__ == '__main__':

    # Training inputs for RGBcolors
    colors = np.array(
        [[0., 0., 0.],
         [0., 0., 1.],
         [0., 0., 0.5],
         [0., 1., 0.]])

    dt = np.array([[0.0033564814366400242, 736609.74843749998],
                   [0.012453703675419092, 736609.76092592592],
                   [3.4722266718745232e-05, 736609.87296296295],
                   [0.0099884259980171919, 736609.52020833339],
                   [0.0050925925606861711, 736609.95905092591],
                   [0.0015740740345790982, 736609.81136574072],
                   [3.4722266718745232e-05, 736609.45093749999],
                   [0.00082175934221595526, 736609.47546296299],
                   [0.050821759272366762, 736609.78321759263],
                   [0.15087962953839451, 736609.88443287031],
                   [4.6296278014779091e-05, 736609.88454861112],
                   [0.0026967593003064394, 736609.05383101851],
                   [0.65181712969206274, 736609.7056481482],
                   [0.0026967593003064394, 736609.05383101851],
                   [0.0013310185167938471, 736609.83358796302],
                   [0.0012962963664904237, 736609.83494212967],
                   [0.051469907397404313, 736609.50859953708],
                   [0.11136574076954275, 736609.80071759259],
                   [0.0015740740345790982, 736609.81136574072],
                   [0.0059837962035089731, 736609.75039351848],
                   [0.068333333358168602, 736609.99721064814],
                   [0.0077199074439704418, 736609.55328703707],
                   [0.0001388889504596591, 736609.5543981482],
                   [0.0, 736609.5543981482],
                   [0.0066203703172504902, 736609.5610648148],
                   [0.0028009258676320314, 736609.56390046293],
                   [0.01115740742534399, 736609.79607638891],
                   [0.00074074068106710911, 736609.84624999994],
                   [0.013379629701375961, 736609.67991898151],
                   [0.00085648149251937866, 736609.98446759256],
                   [0.00079861108679324389, 736609.04612268519],
                   [0.0018634259467944503, 736609.06064814818],
                   [0.003611111082136631, 736609.79616898147],
                   [0.0077199074439704418, 736609.55328703707],
                   [0.0001388889504596591, 736609.5543981482],
                   [0.0, 736609.5543981482],
                   [0.0066203703172504902, 736609.5610648148],
                   [0.0028009258676320314, 736609.56390046293],
                   [0.01115740742534399, 736609.79607638891],
                   [0.032291666604578495, 736609.70826388884],
                   [0.0040740740951150656, 736609.95539351855],
                   [0.189733796287328, 736609.68262731482],
                   [0.00055555556900799274, 736609.87649305561],
                   [0.00041666673496365547, 736609.87707175931],
                   [0.15087962953839451, 736609.88443287031],
                   [4.6296278014779091e-05, 736609.88454861112]])

    color_names = \
        ['black', 'blue', 'darkblue', 'skyblue',
         'greyblue', 'lilac', 'green', 'red',
         'cyan', 'violet', 'yellow', 'white',
         'darkgrey', 'mediumgrey', 'lightgrey', 'nu']

    # Train a 20x30 SOM with 400 iterations
    som = SOM(2, 2, 2, 100)
    som.train(dt)

    # Get output grid
    image_grid = som.get_centroids()

    # Map colours to their closest neurons
    mapped = som.map_vects(dt)
    print(mapped)
    print(len(mapped))

    print(len(dt))

    fr = []

    # Plot
    plt.imshow(image_grid)
    # plt.title('Color SOM')
    for i, m in enumerate(mapped):
        fr.append(m)
        count = Counter(map(tuple, fr))
        count = dict(count)
        # plt.text(m[1], m[0], v[i], ha='center', va='center', bbox=dict(facecolor='white', alpha=0.5, lw=0))

    print(count)
    plt.show()