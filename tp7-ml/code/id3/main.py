import math
import pandas as pd
from collections import deque

class Tree:
    def __init__(self, attribute=None, value=None, classification=None, parent=None):
        self.attribute = attribute  # Attribute to test at this node
        self.value = value  # Value of the attribute for this branch (None for leaf nodes)
        self.classification = classification  # Classification result for leaf nodes
        self.parent = parent
        self.children = {}  # Dictionary to store branches (key = attribute value, value = subtree)
    
    # def get_parent_info(self):
        # Aquí devuelve la información que deseas mostrar del nodo padre
        # Por ejemplo, si el nodo padre tiene un atributo 'name':
        # return f"{self.parent.attribute} = {self.value}" if self.parent else None


def pluralityValue(examples): # more ocurrencys in last column
    return examples[examples.iloc[0, -1]].value_counts().idxmax() 


def sameClassification(examples): # all examples have the same classification
    # verificar si todas las filas de la última columna son iguales a la primera fila y última columna.
    # si todos los valores de esa columna son iguales
    if len(examples[examples.iloc[:, -1] == examples.iloc[0, -1]]) == len(examples):
        return True
    else:
        return False

def remainder(attribute, examples): # Entropy of the variable from attributes
    len_example = len(examples)
    total_remainder = 0
    # print("aa ",attribute)
    # attribute = examples[attribute]
    for value in examples[attribute].unique():
        # print(value)
        subset = examples[examples[attribute] == value]
        len_subset = len(subset)
        
        if len_subset == 0:
            continue  # Avoid 0 divisions
            
        probability = len_subset / len_example
        entropy = b(probability)
        
        total_remainder += probability * entropy
    
    return total_remainder


def b(q): # Entropy of the variable from attributes
    if q == 0 or q == 1:
        return 0
    else:
        return -q*math.log(q,2)-(1-q)*math.log((1-q),2)
    

def importance(attribute,examples): # Entropy of the variable

    # filtra las filas donde los valores en la última columna son iguales al valor en la primera fila y última columna.
    q = len(examples[examples.iloc[:, -1] == examples.iloc[0, -1]]) / len(examples)
    if q == 0 or q == 1:
        return 0
    return b(q) - remainder(attribute, examples)  


def decisionTreeLearning(examples: pd.DataFrame, attributes, parentExamples=None, parent=None):
    if examples.empty:
        return Tree(classification=pluralityValue(parentExamples), parent=parent)
    elif sameClassification(examples):
        return Tree(classification=examples.iloc[0, -1], parent=parent)
    elif not attributes:
        return Tree(classification=pluralityValue(examples), parent=parent)
    else:
        bestAttribute = max(attributes, key=lambda x: importance(x, examples))
        tree = Tree(attribute=bestAttribute, parent=parent)
        for value in examples[bestAttribute].unique():
            exs = examples[examples[bestAttribute] == value]
            subtree = decisionTreeLearning(exs, [a for a in attributes if a != bestAttribute], examples, str(tree.attribute) + " = " + str(value))
            tree.children[value] = subtree
            # print(value)
        return tree

def treeBFS(root_node):
    if not root_node:
        return

    queue = deque([root_node])

    while queue:
        node = queue.popleft()
        if node.attribute is not None:
            print(f"Test {node.attribute}:")
            print(f"Parent: {node.parent}")
            for value, child_node in node.children.items():
                print(f"  {node.attribute} = {value}")
                queue.append(child_node)
        else:
            print(f"Classify as {node.classification} (Parent: {node.parent})")



if __name__ == '__main__':
    examples = pd.read_csv('./tp7-ml/code/id3/tennis.csv')
    attributes = ['outlook', 'temp', 'humidity', 'windy']
    target = 'play'
    tree = decisionTreeLearning(examples, attributes)
    treeBFS(tree)
