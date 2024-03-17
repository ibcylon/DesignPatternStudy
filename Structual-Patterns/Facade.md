# Facade Pattern

## 의도
- 복잡한 클래스 세트/하위 시스템에 대해 클리이언트 에게 단순화 된 인터페이스를 제공하는 구조적 디자인 패턴

![파서드 패턴1](https://refactoring.guru/images/patterns/content/facade/facade-2x.png)

## 등장배경
- 외부 라이브러리나 프레임워크에 속하는 광범위한 객체들을 사용하는 경우, 해당 개체를 모두 초기화 하고, 종속성을 추적해야 됨.
- 종속성을 추적하다 : 올바른 순서로 메서드를 실행해서, 라이브러리 코드 실행 간 논리상 문제가 없는 지 등 

## 구조
![파서드 패턴2](https://refactoring.guru/images/patterns/diagrams/facade/structure-2x.png)

## PseudoCode
![파서드 패턴3](https://refactoring.guru/images/patterns/diagrams/facade/example-2x.png)
```python
class VideoFile
class OggCompressionCodec
class MPEG4CompressionCodec
class CodecFactory
class BitrateReader
class AudioMixer

class VideoConverter
    method convertVideo(filename, format)
        file = new VideoFile(filename)
        if (format == "mp4")
            destinationCodec = new MPEG4CompressionCodec()
        buffer = BitrateReader.read(filename, sourceCodec)
        result = (new AudioMixer()).fix(result)
        return new File(result)

class Application is
    method main() is
        convertor = new VideoConverter()
        mp4 = convertor.convertVideo("funny-cats-video.ogg", "mp4")
        mp4.save()
```

## 적용
- 복잡한 하위 시스템에 대한 제한적이지만 간단한 인터페이스가 필요한 경우
- 하위 시스템을 레이어로 구성하려고 할 때, Facade를 사용

## 장단점 
### 장점 
- 하위 시스템의 복잡성으로부터 코드를 분리

### 단점
- 파사드는 하나 둘 엮다 보면, 앱의 모든 클래스와 결합된 신(god) 객체가 될 수 있습니다.

---

## 다른 패턴과의 관계
vs Adapter
- Facade : 기존 객체에 대한 새로운 인터페이스를 정의 (1, 1, N(1+1))
- Adapter : 기존 인터페이스를 사용 가능하게 (1 -> adapter) 
- Adapter : 일반적으로 하나의 객체만 래핑
- Facade : 객체의 전체 하위 시스템과 함께 작동

vs Abstract Factory
- 하위 시스템 개체가 생성되는 방식만 숨기려는 경우 Facade 의 대안으로 사용 가능

vs Flyweight
- Flyweight : 작은 개체를 많이 만드는 방법을 보여주는 반면
- Facade : 전체 하위 시스템을 나타내는 단일 객체를 만드는 방법

vs Mediator
- Facade와 Mediator는 비슷한 역할
- (공통) 밀접하게 결합된 많은 (서브)클래스 간의 협업을 조직하는 역할
- Facade : 하위 시스템 내의 개체는 직접 통신할 수 있습니다.
- Mediator : 시스템 구성 요소 간의 통신을 중앙 집중화 (구성 요소는 중재자 개체에 대해서만 알고 있으며 직접 통신 X)

vs Proxy
- 하위 시스템의 복잡한 엔터티를 자체적으로(늘리든, 줄이든) 초기화한다는 점에서 Proxy 와 유사
---