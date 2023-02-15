# Python Virtualenv 설정

- pyenv: https://github.com/pyenv/pyenv
- virtualenv: https://virtualenv.pypa.io/en/stable/

## virtualenv 설치
```
$ pip install virtualenv
```
permission 문제 발생 시 `--user` flag를 사용한다. (이 경우 `bin` path를 따로 잡아줘야 할 수도 있다)

## pyenv 사용
python 프로젝트 폴더 내에 `.python-version` 파일을 생성하고 사용하고자 하는 버전을 기재한다. 이 상태에서 virtualenv로 가상환경 생성 시 원하는 버전의 가상환경이 만들어진다.

또는 `pyenv local` 옵션을 사용해도 된다.