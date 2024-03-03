from __future__ import annotations
from abc import ABC, abstractmethod

# 추상클래스
class Animal(ABC):
    # 추상 메소드는 반드시 구현 해야 함, 정형화 목적으로 사용
    @abstractmethod
    def speak(self):
        pass

# 추상클래스 - 동물 팩토리와 개/고양이 팩토리 연결
class AnimalFactory(ABC):
    # 추상 메소드는 반드시 구현 해야 함, 정형화 목적으로 사용
    @abstractmethod
    def create_animal(self):
        pass

# =========================================
# 객체 - 개
class Dog(Animal):
    add_steel = False
    def speak(self):
        print('Dog')

# 객체 - 고양이
class Cat(Animal):
    add_wing = False
    add_mustache = False

    def speak(self):
        print('Cat')

# 팩토리 - 개
class DogFactory(AnimalFactory): # DogCreator
    # 필수 - AnimalFactory
    def create_animal(self):
        return Dog()

    def add_steel(self, dog:Dog):
        dog.add_steel = True
        print('Dog Add Steel')

# 팩토리 - 고양이
class CatFactory(AnimalFactory): # CatCreator
    # 필수 - AnimalFactory
    def create_animal(self):
        return Cat()

    def add_wing(self, cat:Cat):
        cat.add_wing = True
        print('Cat Add Wings')

    def add_mustache(self, cat):
        cat.add_mustache = True
        print('Cat Add Mustache')

if __name__ == "__main__":
    # 팩토리 - 고양이
    cat_factory = CatFactory()

    # 고양이 (날개달린)
    cat1 = cat_factory.create_animal()
    cat_factory.add_wing(cat1)

    # 고양이 (수염달린)
    cat2 = cat_factory.create_animal()
    cat_factory.add_mustache(cat2)

