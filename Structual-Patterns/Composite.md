# Composite Pattern

## 의도
Composite 는 객체를 트리 구조로 구성하여, 이러한 구조를 하나의 객체인 것처럼 작업할 수 있는 구조적 디자인 패턴

## 등장배경
ex) 어떤 주문 요청 (망치, (폰, 이어폰), 충전기, 주문서)에 대해 따로 포장에 포장을 해야 되는 현실 객체가 존재.

이것들을 포장을 해서 주문 요청에 대해 완료 하고 싶어.

![콤보짓 패턴1](https://refactoring.guru/images/patterns/diagrams/composite/problem-en-2x.png)

## 해결책
- 코드로 치면, 생성된 객체들의 hammer(), (phone(), earphone()), charger() 들의 execute()를 n번 호출해서 더함
- 만약 이걸 box().execute()으로만 해결 할 수 있다면? 
- 해당 메소드를 호출하여 알아서 하위 트리들에 전파 되게 하는 것 -> 콤포짓패턴
- [youtube 영상(~02:47)](https://www.youtube.com/watch?v=XXvrHAsfTso)
![콤보짓 패턴2](https://refactoring.guru/images/patterns/content/composite/composite-comic-1-en-2x.png)

## 구조

![콤보짓 패턴3](https://refactoring.guru/images/patterns/diagrams/composite/structure-en-2x.png)

1. Leaf와 Composite(=Leaf Group) 클래스를 설계
2. Leaf, Composite는 모두 execute() box 포장 함수를 가짐
3. 이 둘(Leaf, Composite)을 같은 객체로 취급하므로 -> 공통의 Component 인터페이스를 만듬 (Compoent는 execute()라는 추상메소드 가짐)
4. Leaf Group은 children 리스트 (=즉 Leaf 리스트)를 가지고 이들에 add, remove함
5. execute() 함수는 기본적으로 내 children들에 대해 확인함
6. Client가 Component Interface를 구현하여 execute() 함수를 호출
7. Copmosite의 execute() 실행 -> 자기 children 뒤지면서 Leaf들 execute() 실행

---

## 장단점 
### 장점 
- 복잡한 트리 구조를 보다 편리하게 작업 가능. (다형성과 재귀)
- 개방/폐쇄 원칙(OCP) : 트리에 대한 연결만 해두면 새로운 포장품이 추가 될 때, 확장(Open)이 쉬워지고, 수정(폐쇄)도 필요 없음

### 단점
- 기능이 너무 많이 다른 클래스에 대해 공통 인터페이스를 제공할 때 난해할 수 있음
- 특정 시나리오에서는 공통 인터페이스를 과도한 일반화가 필요할지도. 

---

## 다른 패턴과의 관계
- 재귀적 프로그래밍 (execute 함수)
  - 복잡한 복합 트리를 생성할 때 Builder(return 자기자신..) 등을 사용할 수 있음
  - with. 행동 패턴 - 반복자(iterator), 방문자(visitor) 를 사용하여 복합 트리 순회 가능
  - with. 구조 패턴 - Flyweight 활용하여 리프 노드를 Flyweight 로 구현 -> 일부 RAM 절약 가능
- 재귀적 구성 (vs Decorator)
  - (공통) 둘 다 재귀적 구성을 사용 (유사한 다이어그램 구조)
  - (공통) 무제한의 개체 수를 구성 할 수 있음.
  - (차이점) Decorator 는 하위 구성 요소가 하나만 있음
  - (차이점) Decorator 는 래핑된 객체에 추가 책임을 부여 하는 반면, Composite는 하위 항목들의 정보를 가짐? 요약?해놓음
- with Prototype
  - Composite 와 Decorator를 많이 사용하는 디자인은 Prototype을 사용하면 좋음
  - 패턴 적용시 처음부터 다시 구성하는 대신 복잡한 구조를 복제 가능

---