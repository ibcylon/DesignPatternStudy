## Factory Patterns

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
