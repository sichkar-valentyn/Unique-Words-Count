#!/usr/bin/python

"""
Description:  Program counts unique words in the given txt files

File: words-count-Python.py
"""


# Counting unique words in the given txt files
#
# Algorithm:
# Defining class for Binary Search Tree -->
# --> Parsing argument with full path to the directory with txt fies -->
# --> Reading txt files and counting needed features -->
# --> Printing results -->
# --> Plotting results -->
# --> Saving results in txt and png files
#
# Result:
# Files result.txt and plot.png with results


# Importing needed libraries
import os
import argparse
import string


# Defining class for nodes to use in Binary Search Tree
class Node:
    def __init__(self, word, left=None, right=None):
        self.word = word
        self.left = left
        self.right = right
        self.freq = 1


# Defining class for Binary Search Tree
class BinarySearchTree:

    # Constructor of the class
    def __init__(self):
        self.root = None  # Initializing root node
        self.d = {}  # Defining dictionary to collect words and frequencies

    # Defining function for checking if Binary Search Tree is empty
    def empty(self):
        return self.root is None

    # Defining function for searching specific word
    def search(self, word):
        # Traversing Binary Search Tree and checking if word exists
        current = self.root
        while current is not None:
            # If word is found
            if word == current.word:
                # Returning word itself and its frequency
                return current.word, current.freq

            # Going left
            elif word < current.word:
                # Getting left child
                current = current.left

            # Going right
            else:
                # Getting right child
                current = current.right

        # If not found
        return False, False

    # Defining function for printing Binary Search Tree
    # Checking if root node is not empty
    def travers(self):
        if self.root is not None:
            # Adding node to the dictionary
            self.d[self.root.word] = self.root.freq
            # Traversing rest of the Binary Search Tree
            self._travers(self.root)

    # Traversing rest of the Binary Search Tree
    def _travers(self, current_node):
        # Checking if current node is not empty
        if current_node is not None:
            # Traversing left
            self._travers(current_node.left)

            # Adding current node to the dictionary
            self.d[current_node.word] = current_node.freq

            # Traversing right
            self._travers(current_node.right)

    # Defining function for adding new word
    # or increasing frequency counter if it exists already
    def add(self, word):
        if self.empty():
            self.root = Node(word)
            return

        # Keeping track of parent to use when adding
        parent = None

        # Traversing Binary Tree and checking if word exists
        current = self.root
        while current is not None:
            # Going left
            if word < current.word:
                # Before going to child, saving parent
                parent = current
                # Getting left child
                current = current.left

            # Going right
            elif word > current.word:
                # Before going to child, saving parent
                parent = current
                # Getting right child
                current = current.right

            # Increasing frequency if word exists already
            else:
                current.freq += 1
                return

        # Adding new word
        # New word will be a left child
        if word < parent.word:
            parent.left = Node(word)
        # New word will be a right child
        else:
            parent.right = Node(word)


# Defining main function for calculations
def main():
    """
    Start of:
    Setting up full path to needed directory with txt files to test
    """

    # Setting full path by parsing argument
    # Constructing argument parser
    ap = argparse.ArgumentParser()
    ap.add_argument('-p', '--path', required=False,
                    default='tests',
                    help='full or absolute path to directory')

    # Parsing arguments
    # Option 1 might have mistake if importing file as utility in jupyter notebook
    # https://stackoverflow.com/questions/48796169/how-to-fix-ipykernel-launcher-py-error-unrecognized-arguments-in-jupyter
    # args = vars(ap.parse_args())

    # Parsing arguments
    # Option 2
    args = vars(ap.parse_known_args()[0])

    # Parsing path to needed directory into variable
    full_path_to_tests = args['path']

    # Setting full path manually
    # Checking if after parsing path is defined as default
    if args['path'] == 'tests':
        # Find it with Py file getting-full-path.py
        # Pay attention! If you're using Windows, yours path might looks like:
        # r'\home\my_name\Downloads\tests'
        # or:
        # '\\home\\my_name\\Downloads\\tests'
        full_path_to_tests = 'tests'  # define you path here manually

    """
    End of:
    Setting up full path to needed directory with txt files to test
    """

    """
    Start of:
    Counting words in the given txt files
    """

    # Getting the current directory with main Python file
    directory = os.path.dirname(os.path.abspath(__file__))

    # Check point
    # print(directory)

    # Changing the current working directory to one with given txt files to test
    os.chdir(full_path_to_tests)

    # Check point
    # Getting the current working directory
    # print(os.getcwd())

    # Defining counters
    counter_lines = 0         # for lines
    counter_symbols = 0       # for symbols
    counter_words = 0         # for words
    counter_unique_words = 0  # for unique words

    # Initializing instance of the Binary Search Tree class
    bst = BinarySearchTree()

    # Using os.walk for going through all directories
    # and files in them from the current directory
    # Fullstop in os.walk('.') means the current directory
    for current_dir, dirs, files in os.walk('.'):
        # Going through all files
        for f in files:
            # Checking if filename ends with '.txt'
            if f.endswith('.txt'):
                # Opening current txt file for reading
                with open(f, 'r') as txt:
                    # Going through all lines in txt file
                    for line in txt:
                        # Increasing counter for lines
                        counter_lines += 1

                        # Removing left-right spaces and newline character
                        line = line.strip()

                        # Removing punctuations from the line
                        line = line.translate(line.maketrans('', '', string.punctuation))

                        # Converting all characters in line to lowercase
                        # in order to avoid case mismatch
                        line = line.lower()

                        # Splitting all elements in the current line and creating list
                        temp = line.split()

                        # Going through all elements of the list
                        # Counting number of symbols in every element
                        # Adding words in Binary Search Tree
                        for e in temp:
                            # Increasing counter for symbols
                            counter_symbols += len(e)

                            # Adding word into the Binary Search Tree
                            # If it already exists, then frequency counter will be updated
                            bst.add(e)

                        # Increasing counter for words
                        counter_words += len(temp)

    # Traversing Binary Search Tree and getting resulted dictionary
    # with unique words and their frequencies
    bst.travers()
    r_words = bst.d

    # Updating counter for unique words
    counter_unique_words += len(r_words)

    """
    End of:
    Counting words in the given txt files
    """

    # Printing final results
    print('Total lines = {}'.format(counter_lines))
    print('Total symbols = {}'.format(counter_symbols))
    print('Total words = {}'.format(counter_words))
    print('Total unique words = {}'.format(counter_unique_words))

    # Defining list and writing counted numbers
    r_keys = [counter_lines, counter_symbols, counter_words, counter_unique_words]

    # Defining dictionary and writing counted numbers
    results = {'lines': counter_lines,
               'symbols': counter_symbols,
               'words': counter_words,
               'unique words': counter_unique_words}

    # Creating file results.txt and saving found numbers for keys and unique words
    with open(os.path.sep.join([directory, 'results.txt']), 'w') as txt:
        # Writing description line
        txt.write('Counted numbers for keys are shown below.\n')
        # Going through all elements of the dictionary with keys
        for k, v in results.items():
            # Writing current element at the end of the file
            # We use here '\n' to move to the next line
            # when writing lines into txt files
            txt.write(k + ' : ' + str(v) + '\n')

        # Writing description line
        txt.write('\nFound unique words and their frequencies are shown below.\n')
        # Going through all elements of the dictionary with unique words
        for k, v in r_words.items():
            # Writing current element at the end of the file
            # We use here '\n' to move to the next line
            # when writing lines into txt files
            txt.write(k + ' : ' + str(v) + '\n')

    # Returning resulted list and directory with main Py file
    return r_keys, r_words, directory


# Defining function for plotting results
# Passing list with counted values, dictionary with unique words
# and directory full path where to save results
def plot_results(r_k, r_w, d):
    # Importing library for plotting score results
    import numpy as np
    import matplotlib.pyplot as plt

    plt.rcParams['figure.figsize'] = (6.0, 6.0)  # Setting default size of plots
    plt.rcParams['image.interpolation'] = 'nearest'

    # Initialization instance of object figure
    fig = plt.figure()

    # Defining labels of ticks for keys
    labels = ['lines', 'symbols', 'words', 'unique words']

    # Plotting subplot bar chart for keys
    plt.subplot(2, 1, 1)
    x_positions = np.arange(len(labels))
    bar_list = plt.bar(x_positions, r_k, align='center', alpha=0.6)
    bar_list[np.argmax(r_k)].set_color('red')
    plt.xticks(x_positions, labels, fontsize=15)
    plt.ylabel('Value', fontsize=15)
    plt.title('Counted keys in given txt files', fontsize=20)

    # Defining labels of ticks for unique words
    unique = list(r_w.keys())
    # Getting list with frequencies of unique words
    freq = list(r_w.values())

    # Plotting subplot bar chart for unique words
    plt.subplot(2, 1, 2)
    x_positions = np.arange(len(unique))
    bar_list = plt.barh(x_positions, freq, align='center', alpha=0.6)
    bar_list[np.argmax(freq)].set_color('red')
    plt.yticks(x_positions, unique, fontsize=8)
    plt.xlabel('Frequency of unique words', fontsize=15)

    # Showing plot
    plt.show()

    # Saving plot in the same directory where
    fig.savefig(os.path.sep.join([d, 'plot.png']))
    plt.close()


# Checking if current namespace is main, that is file is not imported
if __name__ == '__main__':
    # Implementing firstly main() function
    # Unpacking arguments with * and passing them to second function
    plot_results(*main())
