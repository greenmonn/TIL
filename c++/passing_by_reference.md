# Passing by reference

Pass-by-reference means to pass the *reference of an argument* in the calling function to the corresponding *formal parameter of the called function*.

The called function(callee) can modify the value of the argument by using its reference passed in.

The reference parameters are initialized with the actual arguments **when the function is called**.

```c++
#include <stdio.h>

void swapnum(int &i, int &j) {
  int temp = i;
  i = j;
  j = temp;
}

int main(void) {
  int a = 10;
  int b = 20;

  swapnum(a, b);
  printf("A is %d and B is %d\n", a, b);
  return 0;
}
```

To modify a reference that is qualified by the const qualifier, use `const_cast` operator to cast away its constness.

(Maybe it would be strange to change the value of const variable)

```c++
#include <iostream>
using namespace std;

void f(const int& x) {
  int& y = const_cast<int&>(x);
  ++y;
}

int main() {
  int a = 5;
  f(a);
  cout << a << endl;
}
```

## Compared to pass-by-value
- Pass-by-reference does not copy the arguments. (More efficient)
- Actual modification is made with pass-by-reference, while pass-by-value is not.

## Compared to pass-by-pointer
- Pointers can be NULL or reassigned whereas references cannot. 
- Use pass-by-pointer if NULL is a valid parameter value or if you want to reassign the pointer.
- Otherwise, use constant or non-constant references to pass arguments.

## My thought
- It would be generally better to use reference than value/pointer.
- Let's use const reference instead of value.
- Let's use reference instead of pointer when we definitely don't need NULL.

## See also
https://www.ibm.com/support/knowledgecenter/en/SSLTBW_2.3.0/com.ibm.zos.v2r3.cbclx01/cplr233.htm

