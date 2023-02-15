# Go Closure

Go supports **anonymous function** (also known as **function literal**, **lambda abstraction**, or **lambda expression**), which can form **closures**.

> *Anonymous function* is a function definition that is not bound to an *identifier*

> *Closure* is a function value that references variables from outside its body

## Example: ginkgo

Ginkgo makes extensive use of clousres to allow building descriptive test suites.

In order to share state between a `BeforeEach` and `It`, use closure variables, typically defined at the top of the most relevant `Describe` or `Context` container.

The `BeforeEach` is run before each spec thereby ensuring that each spec has a pristine copy of the state. Common state is shared using **closure variables** (`var book Book` in this case). You can also perform clean up in `AfterEach` blocks.

The important thing is:

> It is also a mistake to initialize a closure variable in a container block. If one of your `It`s mutates that variable, subsequent `It`s will receive the mutated value. This is a case of test pollution and can be hard to track down. Always initialize your variables in `BeforeEach` blocks.

## 5 Userful Ways to Use Closures in Go
[Link](https://www.calhoun.io/5-useful-ways-to-use-closures-in-go/)