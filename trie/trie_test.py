import pytest

from trie import *

def test_find_child():
    key = [0x01]
    value = [1]

    node = BranchNode()
    node.children[key[0]] = LeafNode(value)

    assert value == node.Find(key).value

def test_find_self():
    value = [1]
    node = BranchNode(value)
    
    assert value == node.Find([]).value

def test_find_with_longer_key():
    key = [0x01, 0x02]
    value = [1]

    child = BranchNode()
    child.children[key[1]] = LeafNode(value)
    
    node = BranchNode()
    node.children[key[0]] = child

    assert value == node.Find(key).value

def test_put_value_to_self():
    value = [1]
    newValue = [2]

    node = BranchNode(value)

    node = node.Put([], newValue)

    assert newValue == node.value

def test_put_to_child():
    key = [0x01]
    value = [1]

    node = BranchNode()
    node = node.Put(key, value)

    assert value == node.Find(key).value
    
def test_put_and_find():
    key = [0x01, 0x02]
    value = [1]

    node = BranchNode()
    node = node.Put(key, value)

    assert value == node.Find(key).value

def test_put_longer_key():
    key = [0x01]
    longerKey = [0x01, 0x02]

    value1 = [1]
    value2 = [2]

    node = BranchNode()
    node = node.Put(key, value1)

    node = node.Put(longerKey, value2)

    assert value1 == node.Find(key).value
    assert value2 == node.Find(longerKey).value

def test_put_empty_value():
    key = [0x01, 0x02]

    node = BranchNode()
    node = node.Put(key, [])
    
    assert node == None

def test_type_of_nodes_by_depth():
    key = [0x01, 0x02]
    value = [1]

    node = BranchNode()
    node = node.Put(key, value)

    assert BranchNode == type(node.Find(key[:1]))
    assert LeafNode == type(node.Find(key))
    
def test_state_change():
    key = [0x01, 0x02]
    value = [1]
    
    state0 = Trie()
    state1 = state0.Put(key, value)

    node = state1.Find(key)
    
    assert value == node.value