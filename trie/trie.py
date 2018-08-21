from abc import *

class Trie:
    def __init__(self):
        self.rootNode = BranchNode()

    def Put(self, key, value):
        newRoot = Trie()

        newRoot.rootNode = self.rootNode.Put(key, value)

        return newRoot
    
    def Find(self, key):
        return self.rootNode.Find(key)

class Node(metaclass=ABCMeta):
    @abstractmethod
    def Find(self, key):
        pass
    
    @abstractmethod
    def Put(self, key, value):
        pass

class BranchNode(Node):
    def __init__(self, value = []):
        self.value = value
        self.children = [None]*16

    def Find(self, key):
        if not key:
            return self
        
        return self.children[key[0]].Find(key[1:])

    def Put(self, key, value):
        newNode = BranchNode()
        newNode.children = self.children
        
        if not key:
            return newNode.setValue(value)
        
        child = newNode.children[key[0]]

        if child is None:
            child = BranchNode()

        newNode.children[key[0]] = child.Put(key[1:], value)
        return newNode.setValue(self.value)

    def setValue(self, value):
        for child in self.children:
            if child is not None:
                self.value = value
                return self

        if not value:
            return None

        return LeafNode(value)
        
        

class LeafNode(Node):
    def __init__(self, value = []):
        self.value = value
    
    def Find(self, key):
        if not key:
            return self

    def Put(self, key, value):
        if not key:
            return LeafNode(value)
        
        return BranchNode(self.value).Put(key, value)