
"""
Artificial Neural Net Simulation
"""
# import math
import random
# import time
# from collections import defaultdict
# from collections import Counter

import comp130_nntests as nntests


#
# Things for students to modify:
# * To change computing environment, change the flags CODESKULPTOR and STEPPER here.
# * To change the output, change the flag SHOW_TESTS and VERBOSITY here.
# * To change what is modelled, change what "test" is assigned to (near bottom of file).
# * To change the number of training runs, redefine test["training_runs"] (near bottom of file).
# * To change the hidden layers, redefine test["hidden_layers"] (near bottom of file).

CODESKULPTOR = False       # Are you using CodeSkulptor vs. regular Python?
                           # Regular Python is recommended for speed.
STEPPER = False            # Do you want to use the CodeSkulptor's visual NN stepper?
                           # Stepper is meant primarily to understand the
                           # training process.

SHOW_TESTS = 1             # Controls verbosity of output
                           # 0 = Show no tests, 1 = Show missed tests, 2 = Show
                           # all tests
VERBOSITY = 2              # Controls how much to output about each test
                           # 0 = minimal, 1 = medium, 2 = maximum
#


if CODESKULPTOR:
    import simplegui


# Parameters for drawing neural nets
FRAME_WIDTH = 1000
FRAME_HEIGHT = 750
CONTROL_WIDTH = 150

BACKGROUND_COLOR = "black"
TEXT_COLOR = "yellow"
NODE_COLOR = "red"
EDGE_COLOR = "white"

TEXT_SIZE = 10
LINE_THICKNESS = 2


#


class Node:

    """
    Class that represents an artificial neural net node
    Has a value, and edges to previous and next layers
    Also has "input" and "error" values used during
    forward and backpropagation calculations.
    Holds a function and its derivative used in those
    calculations.
    """

    def __init__(self, value, fns):
        """
        Constructor for the class

        Arguments:
        value = the initial value for this node, usually a random number
        fns = a pair of a functions (f(x), df(x)/dx)

        Attributes:
        _value = same as above
        _edges_fwd = set of edges to next layer
        _edges_bwd = set of edges from previous layer
        _fn_fwd = f(x) is the forward propagation function and
        _fn_bwd = df(x)/dx is the backpropagation function, which is the
                  derivative of fn_fwd.
        _input = propagation value
        _error = error estimate in propagation
        """
        self._value = value
        self._edges_fwd = set()
        self._edges_bwd = set()
        self._fn_fwd = fns[0]
        self._fn_bwd = fns[1]
        self._input = 0.0
        self._error = 0.0

    def get_value(self):
        """
        Gets (returns) the current value of this node
        """
        return self._value

    def set_value(self, value):
        """
        Sets the current value of this node.
        """
        self._value = value

    def get_error(self):
        """
        Gets the current error value of this node
        """
        return self._error

    def set_error(self, expected_value):
        """
        Sets the current value of this node based on a given expected value.
        error = fn_bwd(expected_value - current_value)
        """
        self._error = self._fn_bwd(
            self._input) * (
                expected_value - self._value)

    def add_source(self, edge):
        """
        Adds the given edge, which links from a source node, to this (self) node.
        Thus, this (self) node is the target node of the given edge.
        """
        self._edges_bwd.add(edge)

    def add_target(self, edge):
        """
        Adds the given edge, which links to a target node, to this (self) node.
        Thus, this (self) node is the source node of the given edge.
        """
        self._edges_fwd.add(edge)

    def draw(self, canvas, x, y, size):
        """
        Draw a node with its value and error.
        (x,y) = Screen upper-left coordinates.
        size = Diameter of node.
        """
        canvas.draw_circle(
            (x + size * 0.5,
             y + size * 0.5),
            size / 2,
            LINE_THICKNESS,
            NODE_COLOR)
        canvas.draw_text(
            "V:" + str(round(self._value, 3)), (x, y + 20), TEXT_SIZE, TEXT_COLOR)
        canvas.draw_text(
            "E:" + str(round(self._error, 3)), (x, y + 30), TEXT_SIZE, TEXT_COLOR)

    def forwardpropagate(self):
        """
        Performs a forward propagation calculation from the connected nodes in
        the previous layer to this node.  Note that the contribution
        from each connected edge to the previous node, is not calculated
        here but rather in each connected edge itself.   Those contributions
        are simply accumulated and processed here.
        """
        self._input = sum([edge.propagate_fwd() for edge in self._edges_bwd])
        self._value = self._fn_fwd(self._input)
        return self._input, self._value

    def backpropagate(self):
        """
        Performs a backpropagation calculation from the connected nodes in
        the next layer back to this node. Note that the contribution
        from each connected edge to the next node, is not calculated
        here but rather in each connected edge itself.   Those contributions
        are simply accumulated and processed here.
        """
        err = sum([edge.propagate_bwd(self._value)
                  for edge in self._edges_fwd])
        self._error = self._fn_bwd(self._input) * err
        return err, self._error


class Edge:

    """
    Class that represents a weighted edge in the neural net graph.
    The weighted edge connects a "source" node to a "target" node,
    as defined by the direction of a forward propagation calculation
    in the node graph.
    """

    def __init__(self, weight, source, target, factor):
        """
        Constructor for the class.

        Arguments/Attributes:
        weight = the initial weight of the edge,
                 usually a small random number centered around zero
        source = the source node in the neural net graph
        target = the target node in the neural net graph
        factor = error scaling factor used in the backpropagation calculation.

        This constructor also asks the given source and target nodes to
        add this edge to its target and source lists, respectively.
        """

        self._weight = weight
        self._source = source
        self._target = target
        self._factor = factor

        # Add edge to each endpoint node
        source.add_target(self)
        target.add_source(self)

    def get_source(self):
        """
        Returns the source node endpoint of this edge.
        """
        return self._source

    def get_target(self):
        """
        Returs the target node endpoint of this edge.
        """
        return self._target

    def get_weight(self):
        """
        Returns the current weight of this edge.
        """
        return self._weight

    def set_weight(self, weight):
        """
        Sets the current weight of this edge.
        """
        self._weight = weight

    def propagate_fwd(self):
        """
        Returns this edge's contribution to a forward propagation calculation.
        """
        return self._source.get_value() * self._weight

    def propagate_bwd(self, source_value):
        """
        Performs this edge's contribution to a backpropagation calculation.
        Also, uses the given source_value to update the weight of the edge.
        source_value = the value of source node (relative to a
        forward calculation direction)
        """
        target_error = self._target.get_error()
        err = target_error * self._weight
        self._weight += self._factor * source_value * target_error
        return err


class Layer:

    """
    Represents a layer of nodes in an artificial neural net.
    Can create a fully connected set of edges with another layer

    Note:  get_nodes, get_values, set_values, get_errors and set_errors should
    all use/return lists whose indices all refer to the same nodes.   That is, these
    functions take/return data that is all in the same order.
    """

    def __init__(self, values, fns):
        """
        Constructor for the class.

        Arguments:
        values = List of initial values for the nodes.
                 Its length determines the number of nodes.
        fns = Pair of functions ( f(x), df/dx ) used in forward
                and backpropagation calculations.

        Attribute:
        _nodes = A list of nodes in this layer.
                 The ith node should use the ith given value and
                 the given pair of functions.
        It is assumed that the nodes and their corresponding values and
        and errors are always used in the same consistent order.
        """

        # Assign self._nodes to the list you construct.
        self._nodes = [Node(value, fns) for value in values]

    def get_nodes(self):
        """
        Returns a list of the nodes in this layer.  Does NOT return the actual
        internal data structure object used to hold the nodes!
        """

        return self._nodes

    def get_values(self):
        """
        Returns a list of the values of all the nodes in the layer.
        """
        return [node.get_value() for node in self.get_nodes()]

    def set_values(self, values):
        """
        Sets the value of each of the layer's nodes to the respective given values.
        values = List of values.  Its length must equal the number of nodes in the layer.
        """
        for value, node in zip(values, self.get_nodes()):
                node.set_value(value)
        # TO BE IMPLEMENTED IN ASSIGNMENT
        # Note: Same idea as set_errors().

    def get_errors(self):
        """
        Returns a list of the error values of all the nodes in the layer.
        """
        return [node.get_error() for node in self.get_nodes()]
        # TO BE IMPLEMENTED IN ASSIGNMENT

    def set_errors(self, expected_values):
        """
        Sets the error value of each of the layer's nodes to the respective given error value.
        expected_values = List of the expected values.  Its length must equal the
        number of nodes in the layer.
        """
        for value, node in zip(expected_values, self.get_nodes()):
            node.set_error(value)
        # TO BE IMPLEMENTED IN ASSIGNMENT
        # Note: Same idea as set_values().

    def draw(self, canvas, x, size):
        """
        Draw this layer of nodes.
        x = Screen x coordinate for left-hand side of layer.
        size = Diameter of each node.
        """
        y = 0
        for node in self._nodes:
            node.draw(canvas, x, y, size)
            y += FRAME_HEIGHT / len(self._nodes)

    def draw_edges(self, canvas, next_layer, x, size, x_step):
        """
        Draw all edges between nodes in this layer and nodes in next layer.
        next_layer = The next layer.
        x = Screen x coordinate for this layer.
        size = Diameter of a node.
        x_step = Screen x coordinate between layers.
        """

        # Put weight labels nearer the end with more nodes.
        if len(self._nodes) > len(next_layer.get_nodes()):
            label_weight = 0.7
        else:
            label_weight = 0.3

        y = 0
        for self_node in self._nodes:
            next_x = x + x_step
            next_y = 0
            for next_node in next_layer.get_nodes():
                # Calculate line endpoints
                x_from = x + size
                y_from = y + size * 0.5
                x_to = next_x
                y_to = next_y + size * 0.5

                canvas.draw_line((x_from, y_from), (x_to, y_to),
                                 LINE_THICKNESS, EDGE_COLOR)

                # Find appropriate edge and draw it with weight label
                for edge in self_node._edges_fwd:
                    if edge.get_target() == next_node:
                        canvas.draw_text(str(round(edge.get_weight(), 3)),
                                         (label_weight * x_from +
                                          (1 - label_weight) * x_to,
                                          label_weight * y_from +
                                          (1 - label_weight) * y_to),
                                         TEXT_SIZE, TEXT_COLOR)
                        break

                next_y += FRAME_HEIGHT / len(next_layer.get_nodes())

            y += FRAME_HEIGHT / len(self._nodes)

    def forwardpropagate(self):
        """
        Makes each node in the layer perform a forward propagation calculation.
        Returns a list of the values of the nodes.
        """
        for node in self._nodes:
            node.forwardpropagate()
        return self.get_values()

    def backpropagate(self):
        """
        Makes each node in the layer perform a backpropagation calculation.
        Returns a list of the error values of the nodes.
        """
        for node in self._nodes:
            node.backpropagate()
        return self.get_errors()

    def connect(self, next_layer, factor, random_range_fn, weight_range):
        """
        Connects each of the nodes in this layer to each of the nodes in the given
        next_layer by creating a Edge object for each such node pair.
        Each edge gets a random weight based upon the mean and width.

        next_layer = the layer to connect to.  next_layer is the next layer in the neural net w.r.t.
        the forward propagation direction.
        factor = the error scaling factor used by the edges' backpropagation calculation.

        random_range_fn = function returning a random value where
                            mean-width/2 <= x < mean+width/2

        weight_range = pair of mean and width of the random weights given to the edges.
        """
        weight = random_range_fn(weight_range)
        for node in self.get_nodes():
            for nextNode in next_layer.get_nodes():
                Edge(weight, node, nextNode, factor)
        # TO BE IMPLEMENTED IN ASSIGNMENT


class NeuralNet:

    """
    Represents an artificial neural net
    """

    def __init__(self, test):
        """
        Constructor for the class

        Argument:
        test = All the test parameters for this NN.
               See below for test dictionary structure definition.

        Attributes:
        _input_layer = a layer of the input nodes
        _output_layer = a layer of the output nodes
        _hidden_layers = list of hidden layers

        All layers are fully connected from one layer to the next layer,
        that is, every node in one layer connects to every node in the
        next layer, except the output layer which has no next layer.
        """

        input_vals = [test["random_range_fn"](test["value_range"])
                      for x in range(test["input_size"])]

        output_vals = [test["random_range_fn"](test["value_range"])
                       for x in range(test["output_size"])]

        hidden_vals_list = [[test["random_range_fn"](test["value_range"])
                            for x in range(num_hidden_nodes)]
                            for num_hidden_nodes in test["hidden_layers"]]

        # Make the layers
        self._input_layer = Layer(input_vals, test["fns"])
        self._output_layer = Layer(output_vals, test["fns"])
        self._hidden_layers = [Layer(hidden_vals, test["fns"])
                               for hidden_vals in hidden_vals_list]
        _factor = test["factor"]
        _rrf = test["random_range_fn"]
        _weight_range = test["weight_range"]

        prev_layer = self._input_layer
        for next_layer in self._hidden_layers:
            prev_layer.connect(next_layer, _factor, _rrf, _weight_range)
            prev_layer = next_layer
        prev_layer.connect(self._output_layer, _factor, _rrf, _weight_range)
        # self._input_layer.connect(self._hidden_layers[0],_factor,_rrf,_weight_range)
#
        # for _index in range(1,len(self._hidden_layers)-1):
            # self._hidden_layers[_index].connect(self._hidden_layers[_index+1],_factor,_rrf,_weight_range)
#
        # self._hidden_layers[-1].connect(self._output_layer,_factor,_rrf,_weight_range)
#
        # Connect the layers
        # TO BE IMPLEMENTED IN ASSIGNMENT
        # Hint:  Use Layer.connect() to connect pairs of layers,
        # i.e., the input layer to the first hidden layer,
        # each hidden layer to the next, and the last hidden layer
        # to the output layer.  One option is to structure this code
        # similar to the loop in NeuralNet.draw().

    def draw(self, canvas):
        """
        Draw the NeuralNet with the given maximum width and height.
        """

        # Scale the drawing to the available space.
        # Calculates the largest node size such that there is
        # at least "size" pixels space horizontally and vertically
        # between nodes.
        # x_step and y_step are the horizontal and vertical spacing
        # between nodes -- which includes space for a node.
        max_width = (FRAME_WIDTH / (len(self._hidden_layers) + 2)) / 2
        max_layer_nodes = max(len(self._input_layer.get_nodes()),
                              len(self._output_layer.get_nodes()),
                              max([len(layer.get_nodes()) for layer in self._hidden_layers]))
        max_height = (FRAME_HEIGHT / max_layer_nodes) / 2
        size = min(max_width, max_height)
        x_step = FRAME_WIDTH / (len(self._hidden_layers) + 2)

        # Draw each layer and each set of edges between layers
        prev_layer = self._input_layer
        x = 0
        prev_layer.draw(canvas, x, size)

        for next_layer in self._hidden_layers:
            prev_layer.draw_edges(canvas, next_layer, x, size, x_step)
            x += x_step
            next_layer.draw(canvas, x, size)
            prev_layer = next_layer

        prev_layer.draw_edges(canvas, self._output_layer, x, size, x_step)
        x += x_step
        self._output_layer.draw(canvas, x, size)

    def forwardpropagate(self, input_values):
        """
        Perform a forward propagation across all the layers, using the
        given input values.
        This method is used both for learning and for evaluating the
        output for a given input.

        The values of the output layer are returned.
        """

        self._input_layer.set_values(input_values)
        for layer in self._hidden_layers:
            layer.forwardpropagate()
        self._output_layer.forwardpropagate()
        return self._output_layer.get_values()

    def backpropagate(self, expected_values):
        """
        Perform a backward propagation across all the layers, using the
        given expected values.
        This is only used by the stepper version.
        """
        self._output_layer.set_errors(expected_values)

        for idx in range(len(self._hidden_layers) - 1, -1, -1):
            self._hidden_layers[idx].backpropagate()
        self._input_layer.backpropagate()

    def learn(self, input_values, expected_values):
        """
        Perform a forward propagation across all the layers
        using the given input values and then a perform a
        backpropagation across all the layers based on the
        given expected values.

        The values from the output layer are returned.
        """
        self.forwardpropagate(input_values)

        self._output_layer.set_errors(expected_values)

        for idx in range(len(self._hidden_layers) - 1, -1, -1):
            self._hidden_layers[idx].backpropagate()
        self._input_layer.backpropagate()
        return self._output_layer.get_values()

    def train(self, training_data, num_trials):
        """
        Perform num_trials repetitions of learning passes on the given
        training data.   The training data is in the form of a list of tuples
        (input values , expected values).   The training data order is randomized
        before each learning run.   The original traiing data is not mutated.
        """
        training_list = training_data[:]  # copy the training data
        for i in range(num_trials):
            random.shuffle(training_list)  # randomize the training data
            for input_values, expected_values in training_list:
                self.learn(input_values, expected_values)


class NNStepper:

    """
    Class that creates a GUI that steps through the training process
    of a neural net.
    """

    def __init__(self, neural_net):
        """
        Constructor for the class
        neural_net = the neural net to train
        """
        self._nn = neural_net
        self._labels = {True: "Fwd Propagation", False: "Backpropagation"}
        self._isFwdPropagate = True
        self._training_data = [([], [])]
        self._num_trials = 0
        self._count = 0
        self._idx = 0
        self._trial = 0
        self._data_len = 0

        self._frame = simplegui.create_frame(
            "NN Display",
            FRAME_WIDTH,
            FRAME_HEIGHT,
            CONTROL_WIDTH)
        self._frame.set_canvas_background(BACKGROUND_COLOR)
        self._frame.set_draw_handler(self.draw)
        self._label = self._frame.add_label(self._labels[self._isFwdPropagate])
        self._step_btn = self._frame.add_button("Step", self.click)
        self._num_trial_lbl = self._frame.add_label("")
        self._idx_lbl = self._frame.add_label("")
        self._frame.add_label("Input values:")
        self._input_vals_lbl = self._frame.add_label("")
        self._frame.add_label("Expected values:")
        self._expect_vals_lbl = self._frame.add_label("")
        self._done_lbl = self._frame.add_label("Running...")

    def draw(self, canvas):
        """
        Internally used draw handler for the frame.
        canvas = the GUI's drawing canvas.
        """
        self._nn.draw(canvas)
        if self._num_trials > self._trial:
            self._num_trial_lbl.set_text("Trial #" + str(self._trial))
            self._idx_lbl.set_text("idx = " + str(self._idx))
            self._input_vals_lbl.set_text(
                str(self._training_data[self._idx][0]))
            self._expect_vals_lbl.set_text(
                str(self._training_data[self._idx][1]))
        else:
            self._done_lbl.set_text("Done!")

        self._label.set_text(self._labels[self._isFwdPropagate])

    def train(self, training_data, num_trials):
        """
        Train the NN with the given training_data for the given number of trials.
        The training process starts right away.
        """
        self._training_data = training_data[:]
        random.shuffle(self._training_data)
        self._data_len = len(self._training_data)
        self._num_trials = num_trials
        self._input_vals_lbl.set_text(str(self._training_data[0][0]))
        self._expect_vals_lbl.set_text(str(self._training_data[0][1]))
        self._frame.start()

    def click(self):
        """
        Handler for the "Step" button.   Steps the NN through a single
        forward or backward propagation, alternating between the two and
        using the appropriate input and expected values as the process
        steps through the training data.
        """
        if self._num_trials > self._trial:
            if self._isFwdPropagate:
                self._nn.forwardpropagate(self._training_data[self._idx][0])
            else:
                self._nn.backpropagate(self._training_data[self._idx][1])
                self._count += 1
                self._trial = self._count // self._data_len
                self._idx = self._count % self._data_len
                if 0 == self._idx:
                    random.shuffle(self._training_data)
            self._isFwdPropagate = not self._isFwdPropagate


def draw_NN(nn):
    """
    Draws the given NN on the screen in a graphical manner
    """
    frame = simplegui.create_frame(
        "NN Display",
        FRAME_WIDTH,
     FRAME_HEIGHT,
     CONTROL_WIDTH)
    frame.set_canvas_background(BACKGROUND_COLOR)
    frame.set_draw_handler(nn.draw)
    frame.start()


#
# A Test is a dictionary of
# name: A text description
# random_range_fn: function to randomly generate numbers within a range
# value_range: pair of mean value and width
# weight_range: pair of mean weight and width
# input_size: Number of input bits
# output_size: Number of ouptut bits
# hidden_layers: List of sizes of each hidden layer
# training_runs: Number of times to run the training data
#     (larger for more accuracy, esp. on complicated functions)
# fns: sigmoid functions
# factor: error scaling factor in backpropagation
#     (smaller for more accuracy)
# training_data: list of input, output pairs to train against
# testing_data: list of input, output pairs to test against
#   Both Training and Testing data have the same format:
#   a list of pairs of tuple of input bits and tuple of output bits
#   Must be a list, since input patterns can repeat.


#---------------------------------------------------------
# FOR STUDENT TO CHANGE:

# Look at nntests.available_tests to see the options.
test = nntests.SEVEN_BIT_LED_TEST

# Can change the number of training runs, i.e., the number of times
# to train on the existing data.
# text["training_runs"] = ...

# Can change number and sizes of the hidden layers.
# test["hidden_layers"] = ...

#---------------------------------------------------------
# !!! When submitting to OwlTest, comment out the following code. !!!


# Define neural net.
nn = NeuralNet(test)

# Train and test neural net.  (No testing with STEPPER.)
# print "Training on",
# print len(test["training_data"]), "inputs, ",
# print "repeated", test["training_runs"], "times each ..."
# if CODESKULPTOR and STEPPER:
    # NNStepper(nn).train(test["training_data"], test["training_runs"])
# else:
    # start_time = time.time()
    # nn.train(test["training_data"], test["training_runs"])
    # nntests.test_NN(nn, test, SHOW_TESTS, VERBOSITY)
    # print
    # print "Elapsed time            :", nntests.time_formatter(time.time() - start_time)
#
# if CODESKULPTOR and not STEPPER:
    # draw_NN(nn)
