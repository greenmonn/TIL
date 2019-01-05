# Pow.cx

- [Pow.cx](http://pow.cx)는 Mac OS에서 Rack Server를 쉽게 생성할 수 있도록 해주는 도구다.

Rails app에서만 되는 줄 알고 안 쓰고 있었는데 Port forwarding 기능이 있다는 것을 알게 되었다.

```echo 8080 > ~/.pow/myapp```

이렇게 포트 번호만 지정해주면 localhost:8080에 띄운 앱을 `myapp.test` 테스트 도메인으로 접속할 수 있다.

라고 하는데 `SERVER_CONNECTION_ERROR`만 뜨고 나는 접속이 되지 않았다.

아래의 커맨드 입력으로 해결 가능하다.
```sudo pfctl -f /etc/pf.conf; sudo pfctl -e```

아래 링크된 이슈에서 찾았다.

- https://github.com/basecamp/pow/issues/525
- https://github.com/basecamp/pow/issues/172

Mac Yosemite 이후에는 ipfw 대신 pf 커맨드를 사용하는데, pow에서 이를 지원하지 않아서 생긴 문제로 보인다. 그러므로 수동으로 위의 커맨드를 입력해 줘야 하는 듯 하다. 현재 github의 pow repository는 아카이빙되어 수정 불가하다 (ㅠㅠ)

- pfctl 명령어 설명: https://donghwi-kim.github.io/jekyll/update/2015/04/12/Mac%20Yosemite%20port%20forwarding.html