import pickle

class InMemoryStorage:
    def __init__(self):
        self.users_storage = dict()
        self.questions_storage = dict()
        self.answers_storage = dict()
        self.filename_prefix = 'STORAGE_'
        try:
            self.users_storage = pickle.load(open(self.filename_prefix + "users", "rb"))
            self.answers_storage = pickle.load(open(self.filename_prefix + "answers", "rb"))
            self.questions_storage = pickle.load(open(self.filename_prefix + "questions", "rb"))
        except:
            pass


    def add_user(self, user):
        self.users_storage[user.id] = user
        pickle.dump(self.users_storage, open(self.filename_prefix+'users', "wb"))

    def get_users(self):
        return self.users_storage

    def get_user_for_name(self, name):
        for user in self.users_storage.values():
            if user.name == name:
                return user

    def add_question(self, question):
        self.questions_storage[question.id] = question
        pickle.dump(self.questions_storage, open(self.filename_prefix + 'question', "wb"))

    def add_answer_to_question(self, answer, question):
        self.answers_storage[answer.id] = answer
        self.questions_storage[question.id] = question
        pickle.dump(self.answers_storage, open(self.filename_prefix + 'answers', "wb"))
        pickle.dump(self.questions_storage, open(self.filename_prefix + 'question', "wb"))

    def get_questions_for_user_id(self, id):
        return [question for question in self.questions_storage.values() if question.user.id == id]

    def get_questions_for_user_name(self, name):
        return [question for question in self.questions_storage.values() if question.user.name == name]


class ModelsRepo:
    def __init__(self, storage):
        self.storage = storage

    def add_user(self, user):
        self.storage.add_user(user)

    def get_users(self):
        return self.storage.get_users()

    def get_user_for_name(self, name):
        return self.storage.get_user_for_name(name)

    def add_question(self, question):
        self.storage.add_question(question)

    def add_answer_to_question(self, answer, question):
        question.add_answer(answer)
        self.storage.add_answer_to_question(answer, question)

    def get_questions_for_user(self, user):
        self.storage.get_questions_for_user(user)

    def get_questions_for_user_name(self, name):
        return self.storage.get_questions_for_user_name(name)
