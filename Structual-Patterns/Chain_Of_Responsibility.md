# Chain of Responsibility (CoR)

## 의도
- CoR 패턴 (Chain of Responsibility) 는 **핸들러 체인**을 따라 요청을 전달 하는 동작(Behavial) 디자인 패턴
- 한 줄 요약 : 연쇄적인 작업을 핸들러 단위로 작게 나누고 종속성 없이 작업을 나누어 처리 하는 것

## 문제
- 온라인 주문 시스템
- 처음에는 인증 기능만..
- 나중에는 인가, 검증, 캐싱 등등.. 필요해지면서 추가되어감
- 어쩔때는 캐싱만 해야되는데 코드(기능)가 얽혀 있음

![책임체인패턴1](https://refactoring.guru/images/patterns/diagrams/chain-of-responsibility/problem1-en.png)
![책임체인패턴2](https://refactoring.guru/images/patterns/diagrams/chain-of-responsibility/problem2-en.png)

## 해결책
- 특정 행동을 하는 **핸들러 (독립형 객체)로 변환** 
- 요청이 헨들러1을 거친 후 **결과 데이터에 따라 혹은 요청에 따라 다음 핸들러2의 인수로 전달 여부**를 결정

![책임체인패턴3](https://refactoring.guru/images/patterns/diagrams/chain-of-responsibility/solution1-en.png)

- GUI 와 같은 구조에 유리
![책임체인패턴4](https://refactoring.guru/images/patterns/diagrams/chain-of-responsibility/solution2-en.png)

## 구조
- h1, h2, h3 핸들러 만들고 h1, h2 연결 시켜놓음
- 최초 h1 을 호출하는 순간 쭉쭉쭉

![책임체인패턴5](https://refactoring.guru/images/patterns/diagrams/chain-of-responsibility/structure-indexed.png)

- 구조는 뭐 Hnadler 클래스1, Handler 클래스2... 등 클라이언트만 보면

```shell
class Application is
    // Every application configures the chain differently.
    method createUI() is
        dialog = new Dialog("Budget Reports")
        dialog.wikiPageURL = "http://..."
        panel = new Panel(0, 0, 400, 800)
        panel.modalHelpText = "This panel does..."
        ok = new Button(250, 760, 50, 20, "OK")
        ok.tooltipText = "This is an OK button that..."
        cancel = new Button(320, 760, 50, 20, "Cancel")
        // ...
        panel.add(ok)
        panel.add(cancel)
        dialog.add(panel)

    // Imagine what happens here.
    method onF1KeyPress() is
        component = this.getComponentAtMouseCoords()
        component.showHelp()
```

## 적용 가능성
- **다양한 종류의 요청**을 **다양한 방식으로 처리**해야 하는 경우
- 여러 핸들러를 특정 순서로 실행해야 하는 경우
- 체인의 핸들러를 어떤 순서로든 연결 가능. 
- 런타임 시 핸들러 순서가 변경 되어야 하는 경우 도 가능 (클래스 내부에 필드를 두고 런타임 간 동적으로 핸들러에 부여)

---
## 장단점 
### 장점
- 단일 책임 원칙(SRP) : 작업을 수행하는 클래스에서 작업을 호출하는 클래스를 분리
- 개방/폐쇄 원칙(OCP) : 기존 클라이언트 코드를 수정 없이 새 핸들러 도입 가능

---

## 다른 패턴과의 관계
- 공통 (특징 비교)
  - 책임 체인(CoR), 명령(Command), 중재자(Mediator) 및 관찰자(Observer) 등은 요청의 **발신자와 수신자를 연결**하는 다양한 방법을 다룸
  - 책임 사슬(CoR)은 동적 수신자 체인을 따라 순차적으로 요청을 전달
  - 명령 (Command)은 발신자와 수신자 간의 단방향 연결을 설정
  - 중재자 (Mediator)는 송신자와 수신자 간의 직접적인 연결 x / 중재자 개체를 통해 간접적으로 통신
  - Observer를 사용하면 수신자가 수신 요청을 동적으로 구독 / 구독 취소
- with 명령 (Command) 
  - 책임 체인 의 핸들러는 명령 으로도 구현 가능. (어쨋든 단방향이니까?) 
  - 이 경우 요청으로 표시되는 동일한 컨텍스트 개체에 대해 다양한 작업을 실행할 수 있습니다.
  - 요청 자체가 Command 개체인 또 다른 접근 방식이 있습니다. 이 경우 체인으로 연결된 일련의 서로 다른 컨텍스트에서 동일한 작업을 실행할 수 있습니다.
- with Composite 
  - 책임 사슬은 Composite 와 함께 사용되는 경우가 많음. 리프(Leaft) 구성 요소가 요청을 받으면 모든 상위 구성 요소의 체인을 통해 개체 트리의 루트까지 이를 전달
- with Decorator 
  - 클래스 구조가 매우 유사. 두 패턴 모두 일련의 개체를 통해 실행을 전달 (순서대로 실행)하기 위해 재귀적 구성에 의존
- vs Decorator
  - CoR의 핸들러는 서로 독립적으로 **임의의 작업을 실행 가능 하며(병렬)**, 또한 언제든지 요청 **전달을 중지도 가능**
  - 데코레이터는 기본 인터페이스와 일관성을 유지하면서 **객체의 동작을 확장**. 또한 데코레이터는 요청 **전달을 중단 불가**
- 추가)
  - 행동 패턴들에 대해서 송->수 에 대한 차이점으로 기억할 필요가 있겠다?
  - CoR, Decorator, Composite 은 같이 이해하고 생각해도 좋겠다?