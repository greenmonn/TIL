# Copying Objects

When creating copies of arrays or objects one can make a deep copy or a shallow copy.

## Shallow Copy
![](https://cdncontribute.geeksforgeeks.org/wp-content/uploads/shallow-copy.jpg)

![](https://www.cs.utexas.edu/~scottm/images/deep_v1.gif)

In case of shallow copy, a reference of object is copied in other object. It means that any changes made to a copy of object do reflect in the original object.

### Shallow Copy Example in Go

```golang
original = &MyObject{"hello"}
copied = new(MyObject)

*copied = *original
```

## Deep Copy
![](https://cdncontribute.geeksforgeeks.org/wp-content/uploads/deep-copy.jpg)

![](https://www.cs.utexas.edu/~scottm/images/deep_v3.gif)

In case of deep copy, a copy of object is copied in other object. It means that any changes made to a copy of object do not reflect in the original object.


> The difference between shallow and deep copying is only relevant for **compound objects** (objects that contain other objects, like lists or class instances).
A shallow copy constructs a new compound object and then (to the extent possible) inserts references into it to the objects found in the original.
A deep copy constructs a new compound object and then, **recursively**, inserts copies into it of the objects found in the original.

# Reference
- https://www.cs.utexas.edu/~scottm/cs307/handouts/deepCopying.htm
- https://www.geeksforgeeks.org/copy-python-deep-copy-shallow-copy/ (It's Python but I thought the fundamental is the same... maybe not?)