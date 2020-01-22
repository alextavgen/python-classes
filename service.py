from model import User, Question

class UserService:
    def __init__(self, repo):
        self.repo = repo

    def add_user_from_request(self, user):
        new_user = User(name=user['name'], password=user['password'], age=user['age'], gender=user['gender'])
        self.repo.add_user(new_user)

    def get_users(self):
        return self.repo.get_users()


class QuestionService:
    def __init__(self, repo):
        self.repo = repo

    def add_question_for_user(self, question):
        user = self.repo.get_user_for_name(question['user'])
        new_question = Question(question=question['question'], user=user)
        self.repo.add_question(new_question)

    def get_questions_for_user(self, user):
        return self.repo.get_questions_for_user_name(user)

    def get_users(self):
        return self.repo.get_users()