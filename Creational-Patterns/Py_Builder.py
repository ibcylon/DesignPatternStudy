# 유저 객체
class User:
    def __init__(self):
        self.username = None
        self.password = None
        self.email = None

    def __str__(self):
        return f"username: {self.username}, password: {self.password}, email: {self.email}"

# 유저 빌더
class UserBuilder:
    def __init__(self):
        self.user = User()

    def set_user_name(self, username):
        self.user.username = username
        return self

    def set_password(self, password):
        self.user.password = password
        return self

    def set_email(self, email):
        self.user.email = email
        return self

    def build(self):
        return self.user


# Builder vs Constructor
class User:
    def __init__(self, user_type, user_name):
        # username에 대한 복잡한 비즈니스 로직이 추가됨
        if user_type == 'admin':
            self.user_name = '관리자' + user_name
        else:
            self.user_name = '일반' + user_name


# Builder vs Constructor
class User:
    def __init__(self):
        self.user_type = None
        self.user_name = None

class UserBuilder:
    def __init__(self):
        self.user=User()

    def set_user_type(self, user_type):
        self.user.user_type = user_type

    def set_user_name(self, user_name):
        if self.user.user_type == 'admin':
            self.user.user_name = '관리자' + user_name
        else:
            self.user.user_name = '일반' + user_name
        return self



if __name__ == "__main__":
    # 빌더 호출 방식
    user = UserBuilder() \
        .set_user_name('smkim') \
        .set_password('1234') \
        .set_email('smkim@naver.com') \
        .build()
    print(user)

    # 생성자 vs 빌더 - 생성자
    user = User(user_type='Admin', user_name='smkim')

    user = User(user_type='Admin')
    user.set_user_name(user_name='smkim')

    # 빌더 호출 방식
    user = UserBuilder() \
        .set_user_type('Admin') \
        .set_user_name('smkim') \
        .build()