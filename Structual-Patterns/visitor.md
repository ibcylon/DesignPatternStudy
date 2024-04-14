# Visitor

## 의도
- Visitor는 알고리즘이 작동하는 개체에서 알고리즘을 분리할 수 있게 해주는 동작 디자인 패턴
- 핵심은 데이터 구조(트리든, 그래프든..)와 연산(기능)을 분리하는 것

## 문제
- graph 형의 정보를 xml로 저장하고자 함
- 내보내고서 정보를 읽을 때 각 노드들 (점들) 에서 재귀적으로 하려고 했으나 유지보수간 객체 구조를 변경해야 되거나 (캡슐화 깨지거나)
- 하여간 OOP 에 잘 맞지 않았다고 함

![방문자1](https://refactoring.guru/images/patterns/diagrams/visitor/problem1.png)

## 해결책
- Visitor(연산 기능) 와 Node(데이터 구조) 로 정보를 나누어 저장

### 1차적
- node 들이 돌면서 visotry들이 직접 행하게 함 (동작을)
- visitor의 함수에 node 인자를 던짐

```shell
class ExportVisitor implements Visitor is
    method doForCity(City c) { ... }
    method doForIndustry(Industry f) { ... }
    method doForSightSeeing(SightSeeing ss) { ... }
    // ...

// Client code
foreach (Node node in graph)
    if (node instanceof City)
        exportVisitor.doForCity((City) node)
    if (node instanceof Industry)
        exportVisitor.doForIndustry((Industry) node)
    // ...
}
```

### double dispatch
- double dispatch 라는 개념을 통해 클라이언트가 호출할 적절한 버전의 메소드를 선택하는 대신,
- 방문자에게 인수로 전달하는 객체에 이 선택을 위임하는 것
- 클라이언트는 node에게 방문자를 던짐
- 그래서 결론적으로 OOP에 이점이 생겼다고 함

```shell
// Client code
foreach (Node node in graph)
    node.accept(exportVisitor)

// City
class City is
    method accept(Visitor v) is
        v.doForCity(this)
    // ...

// Industry
class Industry is
    method accept(Visitor v) is
        v.doForIndustry(this)
    // ...
```

## 구조
- 클라이언트는 Visotr와 Element 라는 node를 만들어서 
- node(Element)에 accept 함수에 visitor를 던져 수행하게 함
![방문자2](https://refactoring.guru/images/patterns/diagrams/visitor/structure-en.png)

## 적용 가능성
- 복잡한 구조(예: 개체 트리)의 **모든 요소에 대해 작업을 수행해야 하는 경우** 방문자를 사용
- 방문자 개체가 (ex. 그래프를 지나며) 여러 변형 기능 작업 가능.
- 방문자를 사용하여 보조 동작의 비즈니스 논리를 정리

---
## 장단점 
### 장점

- 단일 책임 원칙(SRP) : 동일한 동작의 여러 버전을 동일한 클래스로 이동 (방문자가 보기에 각 노드 방문시 각 노드 작업 수행이 잘 나뉘어져 있다의 뜻??, 이동만 하면 된다?)
- 개방/폐쇄 원칙(OCP) : 이러한 클래스(아마 노드인듯)를 변경하지 않고도 다양한 클래스의 개체에 대해 작업할 수 있는 새로운 동작을 도입

### 단점 
- 앱이 단순한 컬렉션에 패턴을 적용하는 것은 과잉
- 반복자를 사용하는 것은 일부 특수 컬렉션의 요소를 직접 통과하는 것보다 덜 효율적일 수 있습니다.
- 방문자 개체는 다양한 개체로 방문하면 작업 하는 동안 몇 가지 유용한 정보를 축적 가능.
  - 개체 트리와 같은 복잡한 개체 구조를 탐색(방문)하고 각 개체에 방문자를 적용하려는 경우 유용
---

## 다른 패턴과의 관계
with 명령 
- 방문자를 명령 패턴 의 강력한 버전으로 처리 가능. (visit 순서 강제한다?? A->B->C??)
- 해당 객체는 다양한 클래스의 다양한 객체에 대해 작업을 실행 가능

with Compositie
- 방문자를 사용하여 전체 복합(Composite) 트리 에 대해 작업을 실행 가능

with Iteraotr
- Iterator 와 함께 Visitor를 사용 하여 복잡한 데이터 구조를 탐색 및 해당 요소에 대해 일부 작업을 수행 가능
