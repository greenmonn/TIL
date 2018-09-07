# Babel User Guide

## Install babel

`npm install --save-dev @babel/core @babel/cli`

## Plugin/Presets

`npm install --save-dev @babel/preset-env`

## Babel Compile

`./node_modules/.bin/babel src --out-dir lib --presets=@babel/env`

`package.json`의 `scripts`에 추가하면 더 편하게 쓸 수 있다.

내 경우에는 path 치는 게 귀찮아서 `babel-cli`를 global로 깔아놓고 쓰고 있다.

## 추가할 것

gulp나 webpack 등과 연동해서 사용하는 방법도 익혀보자.

## Links

[Babel docs](https://babeljs.io/docs/en/next/usage)
