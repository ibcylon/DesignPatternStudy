from __future__ import annotations
from abc import ABC, abstractmethod

# 추상클래스
class Animal(ABC):
    # 추상 메소드는 반드시 구현 해야 함, 정형화 목적으로 사용
    @abstractmethod
    def speak(self):
        pass

# 객체1
class Dog(Animal):
    def speak(self):
        print('Dog')

# 객체2
class Cat(Animal):
    def speak(self):
        print('Cat')

# 객체1과 객체2를 중간에서 생성해주는 팩토리
class AnimalFactory():
    def create_animal(self, type:str):
        if type=='Dog':
            return Dog()
        elif type=='Cat':
            return Cat()


if __name__ == "__main__":
    # 강아지와 고양이를 하나씩 만들어서 짖게함.
    dog = Dog()
    dog.speak()

    cat = Cat()
    cat.speak()

    # 같은 클래스의 인자만 조절하고 싶다.
    animal_factory = AnimalFactory()
    animal_factory.create_animal(type='Cat').speak()

