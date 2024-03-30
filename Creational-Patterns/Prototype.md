# Prototype

## 의도
- Prototype은 코드를 **클래스** 만의 관계 에만 종속 시키지 않고 **객체**를 복사 하여 사용하는 디자인 패턴
- 목적 : 객체를 복제 = 객체를 복사+붙여넣기

## 등장 배경
- 왼쪽 사진의 비행기를 그대로 **복제** 해서 똑같이 만들고 싶어함
- 왼쪽 사진 -> 오른쪽 사진으로 복사함
- 오른쪽 사진 : 이것은 형태(클래스)를 복사한 것이지 **객체**를 그대로 복사한 것이 아님
- 클래스를 상속 받으면서 해당 클래스로 만들어진 객체 또한 복사하는 것
![프로토타입1](https://refactoring.guru/images/patterns/content/prototype/prototype-comic-1-en-2x.png)

## 해결책
- ConfigA 객체가 초기화 되면, ConfigA 객체에 clone() 함수를 둠
- clone() 함수 : **현재 상태의 객체를 리턴**
- ConfigB 객체는 ConfigA 객체의 clone() 함수를 호출해서 생성함
- ..ConfigC, ConfigD .. 반복하여 생성
- 자 여까진 병렬임. 동등한 관계 주의

![프로토 타입2](https://refactoring.guru/images/patterns/content/prototype/prototype-comic-2-en-2x.png)

## 추가 (부모 - 자식 관계 추가. 상속의 관점)
- 정석 : ConfigA **클래스**를 상속 받아서 ConfigB **클래스**에서 **객체**를 초기화 함
- 근데 이 클래스가 만약 필드가 뒤지게 많다. (수십개 필드, 수백개의 가능 구성) 등 이럴 땐, 일단 필드는 상속 받고.. 
- 상위 객체의 초기화 되어 있는 값을 같이 받아서(clone) 사용.
- 만약 상위 객체 상속 안받고, 그냥 선언 후 객체 값 만 받아서 (clone) 직접 초기화 해도 됨. (=상속은 선택임)
- 결론 : **복제(clone 메소드)를 지원하는 개체를 프로토타입** 이라고 합니다 .
  - 해당 관계가 병렬일 수도 있고,
  - 부모-자식간 일 수도 있음. 어쨋든 객체 가지고 복제한다!

## 구조 
1) Prototype 인터페이스 생성 (clone() 함수 가짐)
2) ConcretePrototype 생성자는 그냥 SubclassPrototype 다형성을 위해 **그냥 기본으로 존재하는 것**
3) SubclassPrototype 생성자 : super(prototype) -> 부모의 값을 다 받아서 초기화를 다 해줘 (field1, field2를 가짐)

![프로토 타입3](https://refactoring.guru/images/patterns/diagrams/prototype/structure-2x.png)

## 의사 코드
- 다음 에서 
![프로토 타입4](https://refactoring.guru/images/patterns/diagrams/prototype/example-2x.png)

``` shell
// Base prototype.
abstract class Shape is
    field X: int
    field Y: int

    // The prototype constructor
    constructor Shape(X, Y, color) is
        this()
        this.X = X
        this.Y = Y

    // The clone operation returns one of the Shape subclasses.
    abstract method clone():
        return new Shape(this) 
        
class Circle extend Shape is => 상속은 선택임, 
    field radius: int

    constructor Circle(source: Circle) is
        super(source) # <- 부모, 자식 (상속 관점 / 
        this.radius = source.radius

    method clone():
        return new Circle(this)

// Somewhere in the client code.
class Application is
    field circles : Array

    constructor Application() is
        # 복제 - 병렬형
        Circle circle = new Circle()
        circle.X = 10
        circle.Y = 10
        circle.radius = 20
        circles.add(circle)

        Circle anotherCircle = circle.clone()
        circles.add(anotherCircle)
        
        # 사실 anotherCircle = circle.deepcopy() 도 가능.. => 패턴 화
```


## 장단점
- 장점 : 미리 빌드된 프로토타입을 복제하기 위해 반복되는 초기화 코드를 제거 가능
- 장점 : 복잡한 객체를 보다 편리하게 제작할 수 있습니다.
- 장점 : 복잡한 개체에 대한 구성 사전 설정을 처리할 때 상속에 대한 대안으로도 가능.
- 단점 : '순환 참조가 있는 복잡한 개체'를 복제하는 것은 매우 까다로울 수 있습니다.

## 다른 패턴과의 관계 
- 일반적으로 많은 생성 패턴의 흐름은 팩토리 메서드 (덜 복잡하고 서브클래스를 통해 사용자 정의 가능한) 에서 시작해 => Abstract Factory, Prototype, Builder (더 유연하지만 더 복잡함) 로 발전된다.
- at 추상 팩토리 클래스
  - 추상 팩토리 클래스에서 이러한 니즈 수행이 **팩토리 메소드**로도  가능하지만 **프로토타입**을 사용해서도 구성 가능
- with Command 
  - Prototype은 Command 패턴을 기록에 저장해야 할 때 도움이 될 수 있다.
- with Composite, Decorator
  - Composite 와 Decorator 를 많이 사용하는 디자인은 Prototype을 사용하면 종종 이점을 얻을 수 있음
  - 해당 패턴을 적용하면 처음부터 다시 구성하는 대신 복잡한 구조를 복제하여 사용 가능
- vs 상속이 선택임
  - 상속이 필수는 아님
  - 단, Prototype은 복제된 객체가 필드가 많다면, 복잡한 초기화가 필요 할 것임
- vs Memento 
  - Prototype이 Memento 보다 더 간단한 대안이 될 수도 있음
- at 싱글톤
  - 추상 팩토리, 빌더 및 프로토타입은 모두 싱글톤 으로 구현될 수 있음