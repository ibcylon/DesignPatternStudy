# Adapter Pattern

## 의도
어댑터는 호환되지 않는 인터페이스를 가진 객체가 협업할 수 있도록 하는 구조적 디자인 패턴 

ex) 차를 어댑터를 붙여 철도 레일에서 달릴 수 있도록 함

![어댑터 패턴](https://refactoring.guru/images/patterns/content/adapter/adapter-en-2x.png)

## 등장배경
ex) 얻은 데이터(xml)을 json 데이터로만 동작하는 분석툴에 넣고 싶을 때
![어댑터 패턴2](https://refactoring.guru/images/patterns/diagrams/adapter/solution-en-2x.png)

## 구조
- 객체 기반 구조
![어댑터 패턴3](https://refactoring.guru/images/patterns/diagrams/adapter/structure-object-adapter-2x.png)

1. specialData를 인풋으로 작동 하는 서비스 클래스의 serviceMethod가 존재
2. data도 인풋으로 활용하고 싶었고, data를 받아 specialData로 만들어 주는 convertToServiceFormat() 함수와
3. 변환 된 specialData를 최종 serviceMethod에 넣어 결과를 리턴 해주는 method() 함수를 설계 
4. 해당 Adapter(method() 함수 포함)를 Client에게 Interface로 제공
5. Client는 해당 Interface를 구현하여 사용

---

## 장단점 
### 장점 
- 단일 책임 원칙(SRP) : 인터페이스나 데이터 변환 코드를 분리(어댑터로)한 것이므로, 기존의 클래스 객체의 책임이 보존
- 개방/폐쇄 원칙(OCP) : 어댑터를 통해 확장(Open)은 적극적, 수정(폐쇄)도 필요 없음 (어댑터가 해주니까)

### 단점
- 새로운 인터페이스와 클래스 세트를 도입
- 변환해주는 비즈니스 로직.. 코드.. 복잡성 증가 (억지스러운 면도 있지)
- 가끔은 어댑터 늘리기 보다는 서비스 클래스의 코드를 스윽, 확장성있게 스윽.. 변경 하는 것이 간단할 수도 있음

---

## 다른 패턴과의 관계 (구조적 패턴)
- Adapter는 기존 앱과 함께 사용되어 호환되지 않는 일부 클래스가 함께 잘 작동 하도록 만드는 것 (유지 보수의 목적 느낌???)
  - vs Bridge: 일반적으로 사전에 설계 애플리케이션 일부를 서로 독립적으로 개발.
- Adapter는 기존 개체에 액세스하기 위해 완전히 다른 인터페이스를 제공
  - vs Decorator : 인터페이스가 동일하게 유지되거나 확장, Adapter에서 불가능한 재귀 구성을 활용 => 향상된 인터페이스를 통해 객체에 액세스
  - vs Proxy : Proxy를 사용하면 인터페이스가 동일하게 유지
- Adapter는 일반적으로 하나의 객체만 래핑한다.
  - vs Facade : 객체의 전체 하위 시스템과 함께 작동합
  - vs Facade : 기존 객체에 대한 새로운 인터페이스를 정의

---