# Asserting Equivalence

`ACTUAL` and `EXPECTED` should not be nil. Use `BeNil` instead.

## Equal(expected interface{})
uses `reflect.DeepEqual` inside.
It's strict about comparing types.
For comparing different type(if used sort of type alias), use `BeEquivalentTo` instead.

## BeEquivalentTo(expected interface{})
## BeIdenticalTo(expected interface{})
uses `==` to compare values. 
to assert that two pointers point to the exact same location in memory.

## BeAssignableToTypeOf(expected interface)
To check type is equivalent.



[Full reference](https://onsi.github.io/gomega/#asserting-equivalence)