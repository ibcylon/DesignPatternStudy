# Observer

## 의도
- Observer 패턴은 관찰 중인 개체에 발생하는 이벤트를, 다른 개체에 알리는 메커니즘
- 이러한 메커니즘을 구독 메커니즘이라고도 함

![옵저버1](https://refactoring.guru/images/patterns/content/state/state-ko-2x.png?id=29bf5543c2e0818f7e6217f79beeb433)

## 등장배경
- 왼쪽 사진 -> 매일 매장을 방문하여 제품 재고를 확인
- 오른쪽 사진 -> 새 제품이 출시될 때마다 모든 고객에게 수많은 이메일(스팸으로 간주될 수 있음)을 보냄

![옵저버2](https://refactoring.guru/images/patterns/content/observer/observer-comic-1-en-2x.png)

## 해결책
- 개념(클래스)으로는 Subscriber(구독자)와 Publisher(게시자) 가 있음
- Subscriber(구독자)는 Publisher(게시자)의 모든 상태, 변경 사항을 추적하고 싶어함
![옵저버3](https://refactoring.guru/images/patterns/diagrams/observer/solution1-en-2x.png)
- 즉 관찰자 패턴이란. 게시자(Publisher) 클래스에 구독자(Subscriber) 관리 메커니즘을 추가 하여, 구독자(Subscriber)가 게시자(Publisher)로부터 오는 이벤트 스트림을 연결해 정보를 알려주는 것
![옵저버4](https://refactoring.guru/images/patterns/diagrams/observer/solution2-en-2x.png)

## 리월월드
- 동일한 Publisher 클래스 + 서로 다른(다양한 요구조건의) 구독자 클래스 가 존재가 가능  
- 모든 구독자가 동일한 인터페이스로 할 수 있게 하거나, 확장성을 열어둠
- 확장성을 열 경우 해당 인터페이스는 어떤 경우(상황)인지 알 수 있게, 매개변수 집합(1개)과 알림 방법(1개) 필드 등을 같이 설계

## 구조
![옵저버5](https://refactoring.guru/images/patterns/diagrams/observer/structure-2x.png)

## 의사코드
![옵저버6](https://refactoring.guru/images/patterns/diagrams/observer/example-2x.png)

## 적용 가능성
- ![GUI 관련 언급](https://refactoring.guru/design-patterns/observer#:~:text=%2C%20emailAlerts%20)-,%EC%A0%81%EC%9A%A9%20%EA%B0%80%EB%8A%A5%EC%84%B1,-%ED%95%9C%20%EA%B0%9C%EC%B2%B4%EC%9D%98%20%EC%83%81%ED%83%9C%EB%A5%BC)

## 장점
- 장점 : OCP 원칙 지킴. Publisher의 코드를 변경하지 않고도 새 Subscriber 클래스 도입 가능
- 장점 : 런타임 시 관계 설정할 수 있습니다. (런타임 때 추가한다?)
- 단점 : 구독자 에게 순서 보장이 안될 수 있음. (무작위)

## 다른 패턴과의 관계 
- vs 행동 패턴들
- (공통) 책임 체인(Chain of Responsibility), 명령(command), 중재자(Mediator)들은 요청의 발신자와 수신자를 연결하는 방법들을 다룸
- vs 책임 사슬(Chain of Responsibility)
  - 체인을 통한 수신자들의 순차적 요청 전달 
- vs 명령(Command)
  - 발신자 -> 수신자 단방향 연결
- vs 중재자(Mediator)
  - 송/수신자 간의 직접적인 연결 없이, 중재자 개체를 통해 간접적 통신 
  - 송신자 -> 중재자 -> 수신자
- vs Observer
  - 송신자 -> 수신자 / 수신자가 요청 자체에 대한 동적 구독 및 구독 취소 가능