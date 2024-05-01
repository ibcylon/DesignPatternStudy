# Iterator

## 의도
- Iterator는 컬렉션의 요소(리스트, 스택, 트리) 등 를 탐색할 수 있는 동작 디자인 패턴
- 내부적으로 복잡한 컬렉션 데이터 관계 구조가 있지만 클라이언트로 부터 그 복잡성을 숨기려는 경우 또는 편의성/보안상의 이유

## 문제
- 다양한 유형의 컬렉션들을 효율적으로 순회하고 싶다..

![반복자1](https://refactoring.guru/images/patterns/diagrams/iterator/problem1.png)

## 해결책
- 컬렉션의 순회 동작을 iterator라는 별도의 객체로 추출
- 단. 알고리즘 자체를 구현하는 것 외에도
- 반복자 개체는 현재 위치 / 남은 요소 수와 같은 **순회 간 발생하는 세부 정보** 기록

![반복자2](https://refactoring.guru/images/patterns/diagrams/iterator/solution1.png)

## RealWorld
- 순회라는 것 자체가 좀 특이..
- 로마에서 효율적인 탐색 경로 찾기...
![반복자3](https://refactoring.guru/images/patterns/content/iterator/iterator-comic-1-en.png)

## 구조
- iterator 인터페이스와 iterator 구현체
- concrete 화
- 클라는 가진 객체를 순회시킴.
![반복자4](https://refactoring.guru/images/patterns/diagrams/iterator/structure.png)

```shell
class FacebookIterator is
    method hasMore() is        
    method getNext() is
      if (hasMore())
          result = cache[currentPosition]
          currentPosition++
          return result
  
class SocialSpammer is
    method send(iterator: FacebookIterator, message: string) is
        while (iterator.hasMore())
            profile = iterator.getNext()
            System.sendEmail(profile.getEmail(), message)

class Application is
    field network: SocialNetwork
    field spammer: SocialSpammer

    method config() is
        this.network = new Facebook()
        this.spammer = new SocialSpammer()

    method sendSpamToFriends(profile) is
        iterator = network.createFriendsIterator(profile.getId())
        spammer.send(iterator, "Very important message")

    method sendSpamToCoworkers(profile) is
        iterator = network.createCoworkersIterator(profile.getId())
        spammer.send(iterator, "Very important message")
```

## 적용 가능성
- **다양한 종류의 요청**을 **다양한 방식으로 처리**해야 하는 경우
- 여러 핸들러를 특정 순서로 실행해야 하는 경우
- 체인의 핸들러를 어떤 순서로든 연결 가능. 
- 런타임 시 핸들러 순서가 변경 되어야 하는 경우 도 가능 (클래스 내부에 필드를 두고 런타임 간 동적으로 핸들러에 부여)

---
## 장단점 
### 장점
- 단일 책임 원칙(SRP) : 대용량 순회 알고리즘을 별도의 클래스로 추출하여 위임 가능
- 개방/폐쇄 원칙(OCP) : 새로운 유형의 컬렉션과 반복자를 구현하고 이를 중단하지 않고 기존 코드에 전달

### 단점 
- 앱이 단순한 컬렉션에 패턴을 적용하는 것은 과잉
- 반복자를 사용하는 것은 일부 특수 컬렉션의 요소를 직접 통과하는 것보다 덜 효율적일 수 있습니다.

---

## 다른 패턴과의 관계
- with 복합자 (Composite)
  - Iterator 를 같이 사용 복합자(트리) 순회 가능
- with 팩토리 메소드 (FactoryMethods)
  - 팩토리 메소드 화 하여, 다양한 유형의 반복자를 반환 가능 
- with 메멘토(Memento) 
  - 현재 반복 상태를 캡처하고 필요한 경우 롤백 기능 구현 가능
- with Visitor
  - Iterator 와 함께 Visitor를 사용하여 복잡한 데이터 구조를 탐색 가능
