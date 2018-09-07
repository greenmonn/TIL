# Python bytecode

Python을 다루다 보면 pyc 파일을 종종 볼 수 있다. (나의 경우에는 \__pycache__ import된 파일에 대해 생성된 것을 볼 수 있었다)

## pyc 파일이란?

`.py` 파일을 bytecode로 컴파일한 코드. 이후 `.pyc` 파일은 VM에 의해 기계어로 interpret된다. Java와 유사한 방식으로, interpreter와 compiler를 함께 사용하게 된다.

#### bytecode 나온 김에 뜬금 WebAssembly와 비교
![](https://d2.naver.com/content/images/2017/04/helloworld-1570-1571-04.png)

LLVM 컴파일러로 WebAssembly 바이트 코드를 generate하고, Browser가 VM을 내장하고 있어 네이티브 어플리케이션에 근접한 속도로 코드를 실행하도록 한다. (원리는 결국 비슷하다)