import hashlib
import datetime
import uuid


class User:
    def __init__(self, name, password, age, gender):
        self.id = uuid.uuid1().hex
        self.name = name
        self.password = str(hashlib.md5(password.encode('utf-8')))
        self.age = age
        self.gender = gender

    def password_check(self, password):
        return str(hashlib.md5(password.encode('utf-8'))) == self.password


class Answer:
    def __init__(self, answer, question, user=None, date=datetime.datetime.now()):
        self.id = uuid.uuid1().hex
        self.answer = answer
        self.question = question
        self.user = user
        self.date = date

class Question:
    def __init__(self, question, user, date=datetime.datetime.now()):
        self.id = uuid.uuid1().hex
        self.question = question
        self.user = user
        self.date = date
        self.answers = list()

    def add_answer(self, answer):
        self.answers.append(answer)


user = User(name='John Smith', password='testpassword', age=45, gender='M')

print(user)
print(user.password_check('suvalinepassword'))
print(user.password_check('testpassword'))