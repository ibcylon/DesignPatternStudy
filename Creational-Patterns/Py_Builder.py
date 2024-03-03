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

    def set_username(self, username):
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


if __name__ == "__main__":
    user = UserBuilder() \
        .set_username('smkim') \
        .set_password('1234') \
        .set_email('john@example.com') \
        .build()
    print(user)