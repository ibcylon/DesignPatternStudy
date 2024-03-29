# State

## 의도

State 패턴은 행동 패턴 중 하나로 내부 상태가 변경될 때 객체의 행동을 교체한다. 객체가 행동을 변경할 때 클래스를 변경한 것 처럼 보인다.

<img src="https://refactoring.guru/images/patterns/content/state/state-ko-2x.png?id=29bf5543c2e0818f7e6217f79beeb433" alt="intent" style="zoom:47%;" />

## 등장배경

유한 상태 머신 컨셉과 관련이 있다.

<img src="https://refactoring.guru/images/patterns/diagrams/state/problem1-2x.png" alt="state machine" style="zoom:33%;" />

주요 컨셉은 프로그램이 존재할 수 있는 유한한 갯수의 상태를 가지고 있다. 어떤 유일한 상태마다, 프로그램은 다르게 행동하고, 다른 상태로 즉각적으로 변경될 수 있다. 그러나, 현재 상태에 따라서 특정한 다른 상태로 변경될 수도 또는 변경할 수 없을 수도 있다. 이러한 트랜지션이라고 불리는 변경 원칙은 유한하고, 미리 결정되어야한다.

이러한 접근법을 객체에 적용할 수 있다. 초안, 검토, 출판본의 상태를 가진 문서 객체가 있다고 가정해보자. `publish` 메서드는 각 state 마다 다르게 작동할 것이다.

- 초안: 검토 상태로 변경한다.
- 검토: 공개 상태로 변경하는데 관리자일 때만 가능함
- 출판본: 아무것도 하지 않음

<img src="https://refactoring.guru/images/patterns/diagrams/state/problem2-en-2x.png" alt="pubilsh" title="a" style="zoom:67%;" />

상태 머신은 일반적으로 많은 조건문들로 구현된다.(if or switch) 이는 객체의 현재 상태에 따라 적절한 행동을 선택하게 한다. 일반적으로 "state"는 객체의 필드 집합일 뿐이다. 유한 상태 머신에 대해 들어본 적이 없더라도, 한번이라도 구현한 적이 있을 것이다. 

조건문을 베이스로한 상태 머신의 최대 취약점은 객체에 상태와 상태에 의존한 행위를 추가해야할 때 나타난다. 대부분의 메서드들이 현재 상태를 분기하기 위한 거대한 조건문들을 가지고 있다. 이런 코드는 유지보수하기 매우 어렵다. 왜냐하면, 트랜지션 로직을 수정하면 모든 메서드의 조건문을 수정해야 하기 때문이다.

프로젝트가 커질 수록 문제가 커지는 경향이 있다. 설계 시점에서는 상태의 경우 수를 예측하기 어렵다. 더욱이, 잘 빠진 상태 머신도 시간이 갈 수록 괴물이 되어간다.

## 해결책 

state 패턴은 객체의 가능한 모든 상태를 새 클래스로 만들고, 상태 관련 행위들을 추출해내 각 클래스에 옮기는 것이다.

각각의 모든 행위들을 구현하는 대신, 현재 상태를 나타내는 참조를 저장하는 `context`를 만들고, 상태 관련 일을 위임한다.

![클래스 다이어그램](https://refactoring.guru/images/patterns/diagrams/state/solution-en-2x.png)

컨텍스트를 다른 상태로 트랜지션하기 위해서는, 활성화된 상태 객체를 새로운 상태를 나타내는 다른 객체로 대체해야한다. 이는 **모든 상태 클래스가 같은 인터페이스를 공유**해야하고, **컨텍스트가 이 인터페이스를 통해** 동작해야 가능하다.

이 구조는 전략 패턴과 비슷해보이지만, 중요한 차이점이 있다. 상태 패턴에는 상태들간은 서로를 알고 있고, 한 상태에서 다른 상태로 **전이**된다. 반면에, 전략 패턴은 각 전략들 간 서로 **알지 못한다**.

## 리월월드

현재 상태에 따라 같은 버튼일지라도 다른 동작을 한다. 잠금 여부에 따라, 충전이 필요한지 여부에 따라 다른 화면을 띄운다.

## 구조

<img src="https://refactoring.guru/images/patterns/diagrams/state/structure-en-indexed-2x.png" alt="abstract diagram" style="zoom:80%;" />

1. **Context**: 상태 구현체 객체의 참조를 저장하고, 상태관련 동작을 위임한다. state 인터페이스를 통해  상태 객체와 커뮤니케이션한다. 새로운 상태 객체를 set하는 메서드를 가지고 있다.

2. **State Interface**: 상태관련 메서드를 선언한다. 이 메서드들은 모든 상태 객체와 호환돼야한다. 호출될 필요 없는 메서드가 인터페이스에 있을 필요가 없기 때문이다.

3. **Concrete States**: 상태 관련 행위들을 각각 구현한다. 여러 상태들간의 중복코드를 피하기 이ㅜ해서는 중간 추상 객체가 필요하다. 이 객체는 공통 행위들을 추상화하고 캡슐화하여 제공한다.

   상태 객체들은 컨텍스트를 역참조(backreference)를 저장한다. 이를 참조를 통해, 상태는 필요한 컨텍스트 정보를 불러올 뿐 아니라, 상태 트랜지션을 초기화할 수 있다.

4. 컨텍스트와 상태 구현체 둘 모두는 컨텍스트의 다음 상태를 설정할 수 있고, 컨텍스트와 연결된 객체를 교체함으로써 실제 상태 전이를 수행한다.

## 의사코드

<img src="https://refactoring.guru/images/patterns/diagrams/state/example-2x.png?id=cd81e3ffb8aba5883983a59c111b805f" alt="의사코드" style="zoom:60%;" />

미디어 플레이어의 컨트롤들은 playback 상태에 따라 다르게 동작한다. 플레이어 메인 객체는 플레이어 작업의 대부분을 수행하는 상태 객체와 연결되어 있다. 어떤 액션은 현재 상태를 다른 상태로 트랜지션하는데, 이는 유저 행위에 따라 플레이어가 동작하는 방식을 변경한다.

## 적용 

**현재 상태에 따라 다르게 동작해야할 때, 상태의 경우의 수가 많을 때, 상태 관련 코드들의 수정이 빈번할 때 사용하길 권장한다.**

각각의 클래스들로 상태 관련 코드들을 추출해서 옮긴다. 결과적으로 **새로운 상태를 추가하거나 수정할 때**(**OCP**), 각각으로부터 의존하지 않고 할 수 있어, 유지 보수 비용을 줄일 수 있다.

**클래스의 현재 필드에 따라, 클래스가 어떻게 동작할지 분기하는 거대한 조건문들로 클래스가 더러워졌을 때 권장한다.**(**SRP**)

상태 패턴은 조건문 분기들을 추출해내서 해당 상태 클래스의 메서드들로 옮길 수 있다. 이렇게 함으로써, 메인 클래스에서 상태 관련한 **임시 필드들과 헬퍼 메서드**들을 분리할 수 있다.

**중복코드가 많은 비슷한 상태들과 조건문으로 이루어진 트랜지션을 가진 상태머신일 때 권장한다.**

공통코드를 추상 클래스로 추출해서, 상태 클래스들의 계층을 **조합(compose)**할 수 있게 해주고, 중복을 줄여준다.

## 구현방법 

1. 어떤 클래스가 **컨텍스트**로서 동작해야하는지 결정한다. 기존에 이미 상태에 의존하는 클래스가 있을 것이다. 또는 상태 관련 코드가 여러 클래스에 분리되어 있을 경우 새로 만든다.

2. **상태 인터페이스**를 선언한다. 모든 메서드들이 컨텍스트에서 선언된 것을 복제하는 것일지라도, 상태 관련 행위를 포함하는 걸 목표로 해야한다.

3. 모든 실제 상태는 인터페이스를 따라서 클래스를 만들어야한다. 그런 다음 컨텐스트의 메서드를 살펴보고 새로 생성된 상태 클래스의 상태와 관련된 모든 코드를 추출한다.

   상태 클래스로 옮기는 과정동안, 컨텍스트의 private member에 의존하고 있다는 것을 발견할 것이다. 이 때, 다음과 같은 해결 방법들이 있다.

   - 이 멤버들(메서드, 필드)를 public화한다.
   - context의 public method로 추출하고, state class에서 호출한다.(backreference를 통해). 못생긴 코드가 되지만, 빠르게 해결할 수 있고 나중에 고치면 된다.
   - 컨텍스트 클래스안에 상태 클래스를 nesting한다. 지원할 때만 가능하다.

4. 컨텍스트 클래스에서, 상태 인터페이스 참조 필드와 이 필드를 오버라이딩 가능케 하는 public 설정 setter를 추가한다.

5. 컨텍스트의 메서드들을 살펴보고, 조건문들을 상태 메서드 호출들로 바꾼다.

6. 컨텍스트의 상태를 변경하기 위해, 상태 객체 인스턴스를 만들고 컨텍스트로 보낸다. 이 과정을 컨텍스트 내부에서 또는 스테이트 내부에서 또는 클라이언트 코드에서 할 수도 있다. 이 행위가 수행된 곳마다, 클래스는 상태 구현체들을 알게 되므로 이에 의존하게 된다.

## 장단점 

### 장점

- SRP. 여러 클래스에 각각의 상태 코드들을 분리할 수 있다.
- OCP. 기존 코드 변경 없이 새 상태를 추가할 수 있다.
- 컨텐스트 코드를 거대한 상태 머신 조건문들을 제거하여 단순화할 수 있다.

### 단점

- 상태가 별로 없을 때는 오버엔지니어링이다.

## 다른 패턴과의 관계 

- 브릿지, 상태, 전략(몇몇 관점에선느 어댑터)와 비슷한 구조를 가지고 있다. 사실 이 패턴들은 작업을 다른 객체에 위임하는 composition 패턴에 기반을 두고 있다. 그러나, 각자 다른 문제를 해결하기 위해 생겨났다. 패턴은 특정 방법으로 구조화하기 위한 레시피에 불과하다. 이 패턴으로 해결할 수 있는 문제를 겪고 있는 다른 개발자들과 소통할 수도 있다.
- 상태 패턴은 전략 패턴의 확장팩으로 여길 수 있다. 둘 모두 compositon에 기반을 두고 있다. 헬퍼 객체에 위임함으로써, 컨텍스트의 행위를 변경한다. 전략 패턴은 전략들간의 의존성을 제거하지만, 상태 패턴은 상태들간의 의존성을 제한하지 않고, 서로간에 필요에 따라 변경하게 만들 수 있다.

