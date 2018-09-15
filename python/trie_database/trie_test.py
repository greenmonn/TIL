import pytest

from trie import *

database = {}

# def test_load_and_save_leaf_node():
#     node = LeafNode([1])

#     key = node.Hash()
#     value = node.Encode()

#     database[key] = value

#     decoded = Decode(database[key])

#     assert decoded.value == [1]

def test_hash_node():
    node = LeafNode([1])
    node2 = LeafNode([1])

    hash1 = node.Hash()
    hash2 = node.Hash()
    hash3 = node2.Hash()

    assert hash1 == hash2

    assert hash2 != hash3