# Javascript Event 전파 중단

## event.preventDefault
현재 이벤트의 기본 동작을 중단한다.


## event.stopPropagation
현재 이벤트가 상위로 전파되지 않도록 중단한다.


## event.stopImmediatePropagation
현재 이벤트가 상위뿐 아니라 현재 레벨에 걸린 다른 이벤트도 동작하지 않도록 중단한다.
같은 DOM에 두 개 이상의 이벤트가 걸려있을 때, 이 함수를 호출한 하나의 이벤트만 실행된다.

## return false
`event.preventDefault`와 같은 의미.
`jQuery`의 경우에는 `event.stopPropagation`도 함께 실행된다.