# Joanna Li
# Homework 5
# Bintree
#

# import regular expression
import re

# read the data in the file, split by line into individual words
def getData():
    data = input("Enter a File:")
    file = open(data, "r")
    wordList = []
    for line in file.readlines():
        # regular expression removes special characters
        removeChar = re.split(r"[^A-Za-z0-9_]", line)
        # append each cleaned up word to a list to be stored
        # called later on in the class
        for word in removeChar:
            wordList.append(word)
    return wordList

# create the class "Node"
# will build the tree of words recursively
class Node:
# construct class with attributes
    def __init__(self, val, count = 1):
        self.val = val
        self.count = count
        self.left = None
        self.right = None

# creating the tree
# root is new word from wordList
# node is word in tree
def insert(root, node):
    # if there is not already the word, then the word becomes the node
    if root is None:
        root = node
    # else depending on word will either attach to the left or right of node
    # if left of right node does not already exist, root becomes that node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                # if the root already has a right node
                # move down to next level and compare and insert
                # keep moving down until find empty region
                insert(root.right, node)

        if root.val > node.val:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)
        # if there is already a node with that word,
        # then increase the count of the word
        if root.val == node.val:
            root.count += 1

# format the printing of the tree
# level is how much indented the word should be
# the indent represents how far down into the tree it is
def indentRoot(root, level=0):
    if root is None:
        return
    # go to left-most node and levels up each time until reach first word
    indentRoot(root.left, level+1)
    print("  " * level + str(root.val) + " (" + str(root.count) + ")")
    # go to right-most node and levels up until reach first word
    indentRoot(root.right, level+1)

# calls functions and class
def main():
    # hold data
    wl = getData()
    # set object
    root = Node(wl[0])
    # calls the words from the text file into the class
    # will run recursively until all words used up in wordList
    for idx, val in enumerate(wl):
        if idx > 0 and val != "":
            newNode = Node(val)
            insert(root, newNode)
    indentRoot(root)

main()
   
