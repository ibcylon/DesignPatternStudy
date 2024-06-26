# Mediator

## 의도

객체들 간의 복잡한 의존성들을 줄여준다. 객체들간의 직접 통신을 금지하고, 중재자 객체를 통한 통신을 강제시킨다.

![심플](https://refactoring.guru/images/patterns/content/mediator/mediator-2x.png)

## 등장배경

여러 컴포넌트로 이루어진 프로필을 만든다고 해보자.

![컴포넌트 프로필 화면](https://refactoring.guru/images/patterns/diagrams/mediator/problem1-en-2x.png)

다른 컴포넌트와 상호작용을 하는 컴포넌트가 있다고 해보자. 필드들의 값에 따라전송 버튼의 hidden 여부 등

이런 로직이 폼 객체 안에 있음으로, 재사용하기 어렵게 된다.

## 해결책 

이패턴은 컴포넌트의 의존성들을 제거하기 위해서 컴포넌트간의 직접 통신을 금지시킨다. 대신 간접적으로 통신하게 되는데, 적절한 컴포넌트에게 재요청해주는 중재자 객체를 통해서다. 결과적으로, 수십의 의존성이 생기는 대신, 컴포넌트들은 한 객체에만 의존하게 된다.

위 예시에서는 다이얼로그 객체가 이미 모든 컴포넌트를 알고 있으므로, 중재자 객체로 만들기 제격이다.

![변환](https://refactoring.guru/images/patterns/diagrams/mediator/solution1-en-2x.png)

이전에는 버튼을 클릭해서 모든 폼 요소에 대해서 체크를 했다면, 중재가 객체에게 알림 하나만 보내는 이만 하면 된다. 이 알림을 받으면, 값 체크를 하거나 해당 요소로 테스크를 넘긴다. 따라서, 수십의 요소들이 얽혀있기보다, 버튼이 다이얼로그 객체 하나만을 의존하는 것으로 변경된다.

모든 다이얼로그 타입에 대한 공통 인터페이스를 추출해내면, 더 의존성을 loose하게 만들 수 있다. 인터페이스는 알림 메서드를 정의해야하는데, 이는 모든 요소가 해당 요소들에게 일어나는 이벤트에 대한 다이얼로그에게 알리는데 사용할 수 있어야한다. 따라서, 버튼은 해당 인터페이스를 구현한 다이얼로그이면 사용 가능하게 된다.

이 방법을 통해, 중재자 패턴은 다양한 객체들간의 복잡한 관계를 한 곳에 캡슐화할 수 있다. 클래스가 더 적은 의존성을 가질 수록, 변경/확장/재사용에 수월해진다.

## 실사용 사례

![관제탑](https://refactoring.guru/images/patterns/diagrams/mediator/live-example-2x.png)

항공기들은 서로 직접 통신을 하지 않고 관제탑을 통해 주변 항공기들의 정보를 받는다.

## 구조

<img src="https://refactoring.guru/images/patterns/diagrams/mediator/structure-indexed-2x.png" alt="구조" style="zoom:67%;" />

1. **Components**는 비즈니스 로직을 가지고 있는 다양한 클래스이다. 각 컴포넌트는 중재자 인터페이스에 대한 참조를 가지고 있다. 컴포넌트는 중재자 구현체를 알지 못하므로, 다른 중재자 객체를 사용할 수 있게 된다. 즉, 재사용 가능하다.

2. **Mediator Interface**는 컴포넌트와 통신할 수 있는 메소드를 가지고 있는데, 일반적으로 하나의 알림 메소드를 포함한다. 컴포넌트는 어떤 Context라도 심지어 컴포넌트 그 자체도 이 메소드이 인자로 넘길 수 있다. 그러나 receiving 컴포넌트와 Sender 클래스 사이의 관계가 없을 때만 가능하다.

3. **Concrete Mediators**는 다양한 컴포넌트와의 관계를 캡슐화한다. 구현체는 종종 모든 컴포넌트의 참조를 유지하는데, 종종 컴포넌트의 라이프사이클도 관리한다.

4. 컴포넌트는 반드시 다른 컴포넌트를 알지 못해야 한다. 중요한 일이 일어난다면, 반드시 중재자에게 알려야한다. 중재자가 알림을 받을 떄, 센더를 쉽게 알 수 있는데, 어떤 컴포넌트가 실행되어야 하는지 알기 충분하다.

   컴포넌트 관점에서 보면, 블랙박스를 보는 것과 같다. Sender는 누가 이 요청을 처리하는지 모른다. 그래서 리시버는 누가 처음에 요청을 보냈는지 알 수 없다.

## 의사코드

![예제](https://refactoring.guru/images/patterns/diagrams/mediator/example-2x.png)

이 예제에서 다이얼로그는 중재자 구현체이며, 모든 이벤트를 처리한다. 알림을 받으면, 어떤 요소에서 알림이 왔으며, 어떤 요소에게 재전송할지 결정한다.

## 적용 

**다른 클래스들과 복잡하고 가깝게 얽혀있어, 수정이 힘든 경우**

클래스들간의 관계를 추출해서 하나의 클래스로 옮긴다. 나머지 컴포넌트로부터 특정 컴포넌트에 대한 어떤 변화라도 분리시킨다.

**다른 컴포넌트에 지나치게 의존해서 재사용이 힘든 경우**

중재자 적용 후, 각 컴포넌트는 다른 컴포넌트를 모르게된다. 그들은 여전히 간접적이기는 하지만, 중재자 객체를 통해서  서로 통신할수 있다. 다른 앱에서 재사용하기 위해서, 새로운 중재자 클래스를 만들면 된다.

**다양한 상황에서 간단한 동작을 재사용하기 위해서 많은 서브클래싱을 하고 있는 자신을 발견한 경우**

모든 컴포넌트간의 관계는 중재자 안에 있으므로, 컴포넌트 수정없이, 새로운 중재자 클래스의 도입을 통해서,  새로운 방식으로 컴포넌트간의 관계를 정의할 수 있다.

## 구현방법 

1. 타이트하게 묶인 클래스들간에서 어떤 클래스가 더 독립적인게 이득인지 식별한다.(재사용성과 우지보수를 위해서)

2. 중재자 인터페이스를 정의하고, 중재자와 컴포넌트들간의 의도된 통신 프로토콜을 묘사한다. 대부분의 경우 알림을 받기위한 단 하나의 메소드만으로 충분하다.

   다른 문맥에서 해당 컴포넌트를 재사용하기 위해서 이 인터페이스가 매우 중요하다. 인터페이스를 통한 중재자와 통신을 하는한, 다른 중재자로 구현해도 연결시킬 수 있다.

3. 중재자를 구현한다. 중재자 내부에 모든 컴포넌트 참조를 저장하는 걸 고려해라. 이를 통해, 중재자 메소드를 통해 모든 컴포넌트를 호출할 수 있다.;

4. 컴포넌트 객체의 라이프사이클을 관장하도록 중재자 객체를 발전시킬 수도 있다. 이 경우, 팩토리 또는 파사드와 비슷해진다.

5. 컴포넌트는 중재자를 참조해야한다. 이 관계는 일반적으로 생성자에서 만들어지는데, 중재자 객체가 인자로 보내진다.

6. 컴포넌트 코드를 바꿔서, 다른 컴포넌트의 메소드를 호출하는 대신, 중재자 알림 메소드를 호출한다. 다른 컴포넌트의 메소드를 호출하는 코드를 추출해서 중재자 클래스로 옮긴다. 중재자가 알림을 받으면 해당 코드를 실행한다.

## 장단점 

### 장점

- SRP. 이해하기 쉽고, 유지보수하기 쉬운 컴포넌트를 만들 수 있다.
- OCP. 컴포넌트  수정 없이, 새로운 중재자를 만들 수 있다.
- 컴포넌트들간의 의존성을 줄일 수 있다.
- 각각의 컴포넌트를 재사용하기 쉬워진다.

### 단점

- 시간이 지날 수록 중재자가 갓 오브젝트가 될 수 있다.

## 다른 패턴과의 관계 

- **vs 책임연쇄, 커맨드, 중재자, 옵저버 패턴**
  Sender와 Receiver 사이의 관계를 표현하는 다양한 방법이 있다.

  - 책임연쇄는 요청을 순차적으로 동적인 잠재 리시버들의 체이닝에게 보낸다. 그들 중 하나가 핸들링 할 때 까지
  - 커맨드는 Sender와 Receiver사이의 단방향 연결을 구축한다.
  - 중재자는 직접 연결을 제거하고, 중재자 객체를 통한 간접 연결을 강제한다.
  - 옵저버는 리시버들이 동적으로 구독/구독취소하게 만든다.

- **vs Facade**
  비슷한 일을 한다. 강하게 결합된 클래스들간의 조직적인 협응을 위한 일을 한다.

  - 파사드는 간단하게 바꾼 인터페이스를 사용하지만, 새로운 기능을 추가하지 않는다. 서브시스템 그 자체는 파사드를 알 수 없다. 서브시스템의 객체들은 직접적으로 통신한다.
  - 중재자는 시스템의 컴포넌트들간의 통신을 중앙집중화한다. 컴포넌트는 중재자 밖에 모르며, 직접적으로 통신하지 않는다.

- **vs Observer**
  둘의 차이점은 종종 알기 힘들다. 대부분의 경우, 둘 중에 하나를 구현하게 되지만, 가끔, 동시에 적용할 수도 있다.

  중재자의 주요 목적은 컴포넌트간의 의존성들을 제거하는 것이다. 대신, 이들은 중재자에 대한 의존성 하나만을 가지게 된다. 옵저버의 목적은 특정 객체가  다른 객체의 하위 객체처럼 행동하는 곳에서 객체들간의 단방향 동적 연결을 구축하는 것이다.

  이런 중재자 구현 방식은 옵저버 패턴을 따른다. 중재자는 publisher역할을 하고, 컴포넌트는 subscriber역할을 한다. 중재자의 이벤트에 따라 구독/구독 취소를 한다. 중재자가 이런 방식으로 구현된다면 옵저버 패턴과 매우 흡사해진다.

  헷갈린다면, 다른 방식으로 중재자 패턴을 구현할 수 있다. 모든 컴포넌트들을 같은 중재자에게 영구적으로 연결시킬 수 있다. 이 구현 방법은 구독취소를 할 수 있는 Observer와 다르다.

  모든 컴포넌트가 publisher가 되어, 그들 끼리 동적 연결을 허용한다고 생각해보자. 거기에는 중앙 집중화된 중재자 객체가 없다. 오직 옵저버들만이 있다.

