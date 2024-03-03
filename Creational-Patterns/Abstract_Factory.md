# Abstract Factory

## 의도

추상 팩토리 패턴은 생성 패턴으로, 관련 객체들의 구현체 클래스를 지정하지 않고,  관련된 객체들의 패밀리를 생성한다.

![팩토리 패턴](https://refactoring.guru/images/patterns/content/abstract-factory/abstract-factory-ko-2x.png)

## 등장배경

예를 들어, 가구 판매점을 상상해보자. 코드는 다음의 클래스들로 구성되어질 것이다.

1. 관련 제품들의 패밀리: Chair + Sofa + Coffeetable
2. 이 패밀리들의 여러 변형들. 예를 들어, 제품 Chair + Sofa + CoffeeTable은 다음의 변형이 가능함: Modern, Victorian, ArtDeco

![variants families](https://refactoring.guru/images/patterns/diagrams/abstract-factory/problem-en-2x.png?id=7de667bc24583c3ac03ccb80f3613cfe)

개별 가구 객체를 만들어서, 같은 패밀리군의 다른 제품과 매칭시킬 필요가 있습니다. 고객은 매칭되지 않는 가구를 받았을 때 매우 화낼 것입니다.

![Customer get mad](https://refactoring.guru/images/patterns/content/abstract-factory/abstract-factory-comic-1-en-2x.png?id=e2d4e7bbdd41899a3a85ebefa88bca3e)

도한, 새 제품 또는 패밀리를 새로 추가할 때 기존의 코드를 수정하길 원하지 않는다. 벤더들은 카탈로그를 자주 바꾸는데 그 때마다 매번 코드를 변경할 순 없다.

## 해결책 

추상 팩토리 패턴을 도입하기 위해 첫번째로, 각각의  제품 패밀리 제품들에 대한 개별적인 인터페이스를 명시적으로 선언할 필요가 있다. 예를 들어, chair, sofa or coffeeTable 그런 다음, 모든 제품군들을 이 인터페이스를 따르게 하면 된다. 예를 들어, 의자 변형 제품들은 Chair 인터페이스를 따라야한다; 모든 커피 테이블 변형들은 CoffeeTable 인터페이스를 따라야한다. 나머지도 같다.

![인터페이스](https://refactoring.guru/images/patterns/diagrams/abstract-factory/solution1-2x.png?id=eacec286153e058db9255d26541c0529)

다음 스텝은 추상 팩토리를 선언하는 것이다. - 제품 패밀리들의 모든 부분이 되는 모든 제품군을 생성하는 메서드들의 리스트 인터페이스이다. 이 메서드들은 반드시 이전에 추출한 인터페이스에 나타난 추상 제품 타입을 리턴해야한다. Chiar, Sofa, CoffeeTable 등

![추상 팩토리 인터페이스](https://refactoring.guru/images/patterns/diagrams/abstract-factory/solution2-2x.png?id=b21557081f75ac7b4110427e89a10378)

제품 변형군들은 어떻게 해야할까? 가각의 변형 제품군들에, 추상 팩토리 메서드 인터페이스를 베이스로한 개별 팩토리 클래스들을 만들어야 한다 팩토리 클래스는 특별한 종류의 프로덕틀르 리턴한다. 예를 들어, `ModernFunitureFactory` 는 오직 `ModernChair, ModernSofa and ModernCoffeeTable`만 생성할 수 있다.

클라이언트 코드는 반드시 자신에 해당하는 추상 인터페이스를 통헤 제품과 팩토리들과 작동해야한다. 그래야 클라이언트 코드로 보내는 팩토리 타입 뿐 아니라, 클라이언트 코드가 받는 제품 변형군들을 클라이언트 코드 변경없이, 변경하게 해준다.

![client don't care about factories it work with](https://refactoring.guru/images/patterns/content/abstract-factory/abstract-factory-comic-2-en-2x.png?id=824023e4cfdc6f4d2457e6dc3e51ccfb)

클라이언트가 의자를 만드는 공장이 필요하다고 생각해보자. 클라이언트는 팩토리 클래스를 알필요도, 또한, 어떤 종류의 의자를 받게 될지 상관하지 않는다. 현대적인 의자인지 빅토리안 의자이던지, 클라이언트는 반드시 모든 의자를 interface `Chair`을 통해 같은 취급을 해야한다. 이런 접근으로, 의자에 대해 유일하게 알아야할 것은 `sitOn`메서드를 confirm했는지 여부이다. 또한, 어떤 의자 타입이 리턴되던지, 같은 팩토리에서 만든 소파나 커피테이블과 같은 가구들과 매치되어야 한다.

명확히 해야할 것이 하나 더 남았다. 만약 클라이언트가 인터페이스만을 알고 있다면, 무엇이 실제 팩토리들을 생성하는가? 일반적으로, 앱이 초기화 단계에서 팩토리 구현체 객체를 생성한다. 그 직전에, 앱은 반드시 팩토리가 의존하는 환결 또는 구성 설정에 따라 팩토리 유형을 선택해야 한다.

## 구조

![클래스 다이어그램](https://refactoring.guru/images/patterns/diagrams/abstract-factory/structure-2x.png?id=c4d3634ec2e74e02a0fe1a83ce9b50f6)



## 구조

## 의사코드

아래 예시는 어떻게 추상 팩토리 패턴이 크로스 플랫폼 UI 요소를 생성하는지이다. 클라이언트 코드는 UI 구현체에 의존하지 않고, 모든 생성된 UI 요소는 선택된 OS에 맞게 생성된다.

![Cross platform UI](https://refactoring.guru/images/patterns/diagrams/abstract-factory/example-2x.png)

크로스 플랫폼 내의 같은 UI 요소는 같은 동작을 하길 기대하지만, OS에 따라 약간 다르게 생길 것으로 기대된다. 게다가, OS의 스타일에 맞게 UI 요소를 만드는게 당신의 목적이라면, 당신은 윈도우 시스템에 매OS UI 요소를 원치 않을 것이다.

추상 팩토리 인터페이스는 클라이언트 코드가 다른 타입의 UI 요소를 생성하기 위해 사용할 수 있는 여러 생성 메서드들의 집합이다. 팩토리 구현체는 OS에 맞게 생성되어야 하며, OS에 맞는 UI 객체를 생성해야한다.

다음과 같이 동작한다. 앱이 켜지면, 최근의 OS를 체크한다. 앱은 이 정보를 이용해서 OS에 맞는 팩토리 객체를 생성한다. 나머지 코드는 이 팩토리르 사용하여 UI 요소를 만드는데 사용된다. 이는 잘못된 객체가 생성되는 것을 방지한다.

이런 접근방법으로, 클라이언트 코드는 추상 인터페이스에를 통해 동작하는 한, 팩토리와 UI 구현체들에 의존하지 않는다. 이는 앞으로 추가될 UI와 팩토리들을 유지보수하기 편하게한다.

결과적으로, 앱에 새로운 팩토리와 UI객체를 추가할 대마다 클라이언트 코드를 변경할 필요 없다.(OCP 법칙). 단지, 이런 요소들을 만드는 새로운 팩토리를 만들고, 앱의 초기화 코드를 약간 수정해서, 적절한 클래스를 선택하게 만들기만하면 된다.

## 적용 

**관련 제품들의 다양한 패밀리들과 일할 필요가 있지만, 제품들의 구현체들에 의존하고 싶지 않을 때, 추상 팩토리 패턴을 사용하자** - 미리 알 수 없거나, 단순하게 미래 확장성을 고려하기 위해

추상 팩토리 패턴은 제품 패밀리의 각 클래스로부터 객체를 생성하기 위한 인터페이스를 제공해준다. 인터페이스를 통해 객체를 생성하는 한, 객체들과 매치되지 않을까봐 걱정할 필요가 없다.

**기본 책임(Primary Responsibility)이 불투명해진 팩토리 메서드들을 가진 클래스가 있다면 추상 팩토리 패턴을 고려하자 SRP**

잘 만든 앱은 각 클래스가 하나의 책임만을 가진다. 한 클래스가 여러 제품 타입을 다루게 될 때, 기존 팩토리 메서드들을 단독 모델(Stand-alone) 팩토리 클래스 또는 추상 팩토리로 추출한다면  더 나아질 것이다.

## 구현방법 

1. 고유한 제품 유형과 이 제품에 대한 변형 제품들을 매핑
2. 모든 제품 타입에 대한 추상 제품 인터페이스를 선언, 그리고 모둔 제품 구현체들이 인터페이스를 confirm
3. 모든 추상 제품들의 생성 메서드를 가진 추상 팩토리 인터페이스 선언
4. 제품 변형군 마다 하나씩 추상 팩토리 인터페이스를 confirm한 팩토리 구현체 생성.
5. 앱 어딘가에 팩토리 초기화 코드 작성. 최근 환경이나 앱 구성 설정에 관련된 팩토리 구현체를 반드시 인스턴스해야함. 제품을 생성하는 클래스들에 이 팩토리를 전달한다.
6. 코드를 스캔해서, 직접적으로 제품 생성자를 호출하는 코드를 모두 검색. 팩토리 오브젝트에서 적절한 생성 메소드로 대체한다.

## 장단점 

### 장점

- 팩토리에서 만든 제품과 다른 제품들끼리 상호호환을 보장할 수 있다.
- 클라이언트 코드와 구현체의 강한 결합을 피할 수 있음
- SRP. 제품 생성 코드를 추출해서 한 곳으로 옮길 수 있다. 유지보수에 좋음
- OCP. 기존 클라이언트 코드를 break하지 않고, 추가할 수 있다.

### 단점

- 패턴 구현을 위해, 많은 클래스와 인터페이스들이 필요하기 때문에, 복잡도가 올라감

## 다른 패턴과의 관계 

- 많은 디자인들이 Factory Method에서 출발해, Builder, Abstract Factory, Prototype 으로 발전해감
- Builder가 복잡한 객체 생성하는데 단계적인데 중점을 둔다면, Abstract Factory는 관련 객체들의 패밀리를 생성하는데 특화되어있다. Abstract Factory는 제품을 바로 리턴하는 반면, Builder는 리턴 전에 몇가지 추가적인 생성 과정을 가질 수 있다.
- Abstract Factory 클래스들은 종종 Factory Method 집합으로 이루어져 있지만, Prototype 을 이용해 이 메서드들을 조합(compose)할 수 있다.
- 단순히 하위 시스템 객체들이 클라이언트 코드로부터 생성되는 방식만을 숨기고 싶다면, Facade대신 Abstract Factory를 사용할 수 있다.
- Bridge와 함께 Abstract Factory를 사용할 수 있다. 이 조합은 Bridge에 의해 정의된 어떤 추상화들이 특정 구현들과만 작동할 수 있을 때 유용합니다.
  이런 경우에 Abstract Factory는 이런 관계들을 캡슐화하고, 클라이언트 코드로부터 복잡성을 숨길 수 있다.
- Singletone으로 구현 가능하다.

---

### 팩토리 패턴 - 정의
- 팩토리 안에 각 객체를 생성 해주는 로직들을 숨겨놓고, argument를 통해 가독성을 높인다?
- 팩토리 패턴은 원하는 '객체'를 리턴해 주는 것이 핵심
- 중간 메소드 느낌. 리얼 공장 느낌
- 클래스의 생성자의 로직이 복잡해졌을 때 
- 추상 클래스 팩토리 패턴 으로 올리는 경우 (의존성을 기준으로 볼 수도 있음)

## Abstract Factory Patterns 

### 추상 팩토리 패턴 - 정의
- 추상 팩토리 (Abstract Factory)는 공통 테마를 갖는 개별 팩토리 그룹을 캡슐화 하여, 관련 객체의 패밀리를 생성하는 방법의 디자인 패턴

### Factory Pattern vs Abstract Factory Pattern
- 한 종류의 객체를 위해 사용되느냐 마느냐 차이
- 팩토리 패턴은 인터페이스를 구현하여 하나의 객체를 생성하는데 사용됨
- 추상 팩토리 패턴은 여러 객체(다양한)를 생성하기 위해 사용
- Animal-Cat-Dog
  - AnimalFactory
    - 다양한 동물
    - AnimalFactory 에서 분기하여 사용

- Animal-Cat-Dog
  - AnimalFactory
    - CatFactory, DogFactory
      - 다양한 개, 고양이
      - CatFactory, DogFactory 에서 분기()하여 사용
      - CatCreator, DogCreator 로도 많이 네이밍