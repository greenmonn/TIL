# Golang BDD Testing Framework

# Getting Ginkgo
```
$ go get github.com/onsi/ginkgo/ginkgo
$ go get github.com/onsi/gomega/...
```

This fetches ginkgo and installs the `ginkgo` executable under `$GOPATH/bin`.

Also installs the entire gomega library.

# Bootstrapping a Suite

```
$ cd path/to/<package_name>
$ ginkgo bootstrap
```

This will generate a file named <package_name>_suite_test


```
$ ginkgo generate <file_name>
```

This adds a test file for <file_name> specified.

# IDE support
`ginkgo watch` command reruns tests whenever changes are detected.

Set of completions available for `Sublime Text` and `VSCode`.

# Reference

![https://onsi.github.io/ginkgo/](https://onsi.github.io/ginkgo/)

# Playground code

![https://github.com/greenmonn/golang-playground/tree/master/books](https://github.com/greenmonn/golang-playground/tree/master/books)