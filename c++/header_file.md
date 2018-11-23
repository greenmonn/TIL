# Header file in C/C++

## Purpose?
- To hold declarations for other files to use.
- Typically only contain declarations, do not define how something is *implemented*.

## Standard library header files
- Standard libary function is implemented in the C++ runtime support library, which is automatically linked into the program during the link phase.

![iostream-library-linking](http://www.learncpp.com/images/CppTutorial/Section1/IncludeLibrary.png)

## Use header file instead of forward declaration

- We need a forward declaration so that the compiler would know about the function (even it is implemented in the another file) when compiling. 
- However, writing forward declarations for every function that lives in another file can is tedious.
- A header file only has to be written once, and it can be included in as many files as needed.

## Header guard

- Header guards prevent a given header file from being #included more than once in the same file.

```c++
#ifndef ADD_H   // can be any unique name
#define ADD_H

int add(int x, int y);

#endif
```

## How Compiler work with header files?

When the compiler compiles the `#include "some_header.h"`, It simply copies the contents of `some_header.h` into the current file at that point. Consequently, program will compile and link correctly.

![compile-and-linking-with-header](http://www.learncpp.com/images/CppTutorial/Section1/IncludeHeader.png)

## `<header.h>` vs `"header.h"`

- Angled brackets(`<>`): compiler looks for the header in the system directories.

- Double-quotes(`""`): compiler looks for the header file in the current directory containing the source code. If not found, it will check any other include paths specified in compiler/IDE settings. That failing, it will fall back to checking the system directories.

## Best practices

- Always include header guards.

- Do not define variables in header files unless they are constants. Header files should generally only be used for declarations.

- Do not define functions in header files.

- Each header file should have a specific job, and be as independent as possible. For example, you might put all your declarations related to functionality A in A.h and all your declarations related to functionality B in B.h. That way if you only care about A later, you can just include A.h and not get any of the stuff related to B.

- Give your header files the same name as the source files they’re associated with (e.g. grades.h goes with grades.cpp).

- Try to minimize the number of other header files you #include in your header files. Only #include what is necessary.
Do not #include .cpp files.


## See also

Referred from: https://www.learncpp.com/cpp-tutorial/19-header-files/