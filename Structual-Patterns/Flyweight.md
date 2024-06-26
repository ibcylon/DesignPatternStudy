# Flyweight

## 요약

RAM 소모를 줄이기 위한 최적화 패턴 이 외 용도로는 사용되지 않음

## 의도
RAM을 효율적으로 사용하기 위해서 모든 데이터를 가지고 있는 대신에 공통 부분을 공유하는 패턴이다.

<img src="https://refactoring.guru/images/patterns/content/flyweight/flyweight-2x.png" alt="이미지" style="zoom:80%;" />

## 해결책

![image](https://refactoring.guru/images/patterns/diagrams/flyweight/problem-en-2x.png)

파티클 시스템을 잘 들여다보면, 색상과 스프라이트 필드가 다른 필드보다 많은 메모리를 잡아먹고 있다는 것을 알 수 있다. 더 최악인 것은 거의 동일한 데이터를 파티클들이 가지고 있다는 점이다.

![pattern](https://refactoring.guru/images/patterns/diagrams/flyweight/solution1-en-2x.png)

다른 파티클 상태의 부분들을 보면, 예를 들어, 이동 벡터, 코디네이트 속도 등, 파티클마다 다르다. 시간이 지남에 따라 이 값들은 모두 변화한다. 파티클이 존재하는 한 항상 변화하는 값들을 나타내지만, 반면에 색상과 스프라이트는 생명주기 동안 동일하다.

이런 상수들은 "***intrinsic state***"라고 불린다. 객체 안에 존재한다. 변하지 않고, 읽을 수만 있다. 다른 객체의 상태들은 종종 "외부 요인에 의해" 변하는데 이를 "***extrinsic state***"라고 부른다.

flyweight패턴은 외부 상태를 객체 내부에 저장하는 대신, 관련있는 메서드로 보내야한다. 오직 내부 상태만 내부에 있으므로, 다른 문맥안에서 재사용할 수 있다. 결과적으로, 이러한 객체들은 공유한 상태보다 변형이 훨씬 적은 고유한 상태에서만 달라지므로 훨씬 더 적은 수의 객체만 있으면 된다.

<img src="https://refactoring.guru/images/patterns/diagrams/flyweight/solution3-ko-2x.png?id=5003b23e27ce9b6b73514b0e7c69e8c9" alt="적용 후" style="zoom:50%;" />

공유한 상태를 추출하면, 총알, 미사일, 파편의 세가지 다른 객체만으로 모든 입자를 표현할 수 있다. 이러한 고유한 상태만 저장하는 객체를 플라이웨이트라고 한다.

### 공유한 상태 스토리지

공유한 상태는 **컨테이너** 객체로 이동되어 저장된다. 게임 예시에서는 "Game"객체가 모든 파티클들을 저장한다. 모든 외부 상태를 이 클래스로 옮기면, 각 입자들의 코디네이트, 벡터, 스피드를 저장할 어레이 필드가 필요하다. 파티클을 나타낼 특별한 플라이웨이트 참조를 저장할 어레이도 필요하다. 이 어레이는 동기화가 되어야하며, 그래야 같은 인덱스를 이용해 접근가능해지기 때문이다.

![](https://refactoring.guru/images/patterns/diagrams/flyweight/solution2-en-2x.png)

더 우아한 방법은 플라이웨이트 객체에 대한 참조와 공유된 상태를 저장할 별도의 콘텍스트 클래스를 만드는 것이다.

### 플라이웨이트의 불변성

플라이웨이트 객체가 다른 콘텍스트들에서 재사용될 수 있으므로, state가 바뀌지 않는 다는 것을 보장해여 한다. 플라이웨이트는 생성 시점에 생성자를 통해서 한 번만 초기화되어야한다. setter나 다른 객체의 public 필드를 가져선 안된다.

### 플라이웨이트 팩토리

다양한 플라이웨이트에 대한 접근성을 위해서, 플라이웨이트 풀을 관리하는 팩토리 메서드를 만들 수 있다. 이 메서드는 클라이언트로부터 intrinsic state를 받아서, pool에 일치하는 state를 가진 플라이웨이트를 찾는다. 없으면 풀에 생성해 더해주고, 있으면 리턴한다.

이 메서드가 어디에 존재할 수 있는지는 여러 옵션이 있다. 가장 obvious한 위치는

- flyweight container
- 새로운 팩토리 클래스를 만드는 것이다.
- flyweight class의 static method로 만드는 것이다.

## 구조

<img src="https://refactoring.guru/images/patterns/diagrams/flyweight/structure-2x.png" alt="구조" style="zoom:67%;" />

1. 이 패턴은 최적화 방법이기 때문에 적용하기 전에 *많은 수의 동일한 객체 사용*으로 이한 RAM 이슈가 있는지 체크할 것. 이 문제가 다른 의미 있는 방법으로 해결 될 수 있는지 체크할 것.
2. 플라이웨이트 객체는 원본 객체의 부분의 공통적으로 사용되는 부분을 포함하고 있다. 같은 플라이웨이트 객체가 여러개의 다른 컨텍스트 객체에서 사용될 수 있다. 플라이웨이트 객체가 가지고 있는 state를 `intrinsic state`라고 한다. 플라이웨이트의 메서드로 보내지는 state를 `extrinsic state`라고 한다.
3. **Context**클래스는 extrinsic sate을 가지고 있는데 모든 원본 객체를 통틀어서 유일하다. 컨텍스트가 플라이웨이트 객체와 한 짝을 이룬 상태라면, 원본 객체의 모든 상태를 표현할 수 있다.
4. 일반적으로는, 원본 객체의 행위는 플라이웨이트 객체 안에 남아있다. 이 경우, 플라이웨이트 메서드를 호출하려면, 적절한 extrinsic state를 파라미터로 보내야한다. 또 한편으로는, context 클래스로 이동할 수 있수도 있는데, 이 때는 플라이웨이트 클래스를 거의 data 객체로만 사용한다.
5.  **Client**는 extrinsic state를 계산하거나 저장한다. 클라이언트 입장에서는, 플라이웨이트 객체는 단지, 런타임에 설정되는 템플릿 설정값일 뿐이다. 
6. 플라이웨이트 팩토리는 플라이웨이트 pool을 관리한다. 팩토리를 통해 클라이언트는 직접적으로 객체를 생성하지 않는다. 대신, 팩토리를 호출한다. 팩토리는 이전에 생성된 플라이웨이트를 검색하고 있으면 리턴 없으면 새로 생성한다.

## 의사코드

![수도](https://refactoring.guru/images/patterns/diagrams/flyweight/example-2x.png)

Tree에서 공통된 intrinsic state를 추출해서, flyweight인 TreeType으로 옮긴다.

다음으로, 중복된 데이터를 여러 객체에 중복 저장하는 대신, context로 flyweight 객체를 저장하고, Tree에 연결한다. 클라이언트 코드는 플라이웨이트 팩토리를 통해 Tree를 생선한다. 이 팩토리 안에서 적절한 객체를 찾는 복잡성과 재사용하는 코드를 캡슐화한다.

## 적용 

**많은 객체를 사용하고, RAM을 최적화하기 위해서만 이 패턴을 사용**

- 비슷한 객체를 많이 사용할 필요가 있을 때
- 이 객체들이 RAM 소모를 많이 할 때
- 중복된 state를 가지고 있을 때, 이 상태가 추출될 수 있고, 여러 객체들에 공유된 상태일 때

## 구현방법 

1. 플라이웨이트로 만들 원본 클래스의 필드를 두 파트로 나눈다.
   - intrinsic state: 여러 객체들에 사용된 바뀌지 않는 값들
   - extrinsic state: 각 개체들만의 유일한 값들
2. intrinsic field는 클래스에 남겨둔다. 하지만, 불변성을 보장해야한다. 생성자를 통해서만 값을 가져야한다. ()
3. extrinsic state를 사용하는 메서드를 체크(Go Over). 메서드에 사용된 각 필드에 대해 새 매개 변수를 도입하고, 필드 대신 사용해야 함(즉, 클래스 필드를 사용하는 대신 파미리터로 받아서 사용)
4. 옵션으로, 풀 관리 팩토리 메서드를 생성. 중복 생성을 막기 위해, 생성 여부 체크해야 한다.
5. Client는 flyweight 메서드를 사용하기 위해서 extrinsic state를 저장하거나 계산할 수 있어야 한다. 이 들은 별도의 context class로 이동할 수 있다.

## 장단점 

### 장점

이 패턴을 통해 RAM을 절약할 수 있다.

### 단점

- 플라이웨이트 메서드 호출 할 때 마다 계산을 다시 해야 한다면 RAM을 절약하는 대신 CPU를 낭비하게 되는 것일 수도 있다.
- 복잡성이 올라가서, 새로운 멤버가 팀에 들어올 때, 이해하기 힘들 가능성이 크다.

## 다른 패턴과의 관계 

- **with Composite**
  composite 패턴의 leaf노드를 flyweight로 구현할 수 있다. leaf 노드들은 공통점이 있기 때문
- **vs Facade**
  flyweight 패턴은 작은 객체들을 많이 만든느 방법을 보여준느 반면, facade패턴은 하위 시스템을 단일 객체로 만든느 방법
- **vs Singleton**
  분리된 flyweight가 단 한개라면 singleton과 유사해진다. 하지만 아래 2가지 차이점이 있다.
  1. 싱글턴은 인스턴스가 하나만 존재. 반면에 flyweight는 여러 인스턴스가 가능
  2. 싱글턴 객체는 mutable, fllyweight는 immutable

