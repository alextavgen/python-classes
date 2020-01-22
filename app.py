from flask import Flask, request, render_template
import json
from service import UserService, QuestionService
from persistence import ModelsRepo, InMemoryStorage

import os


app = Flask(__name__, template_folder='template')

storage = InMemoryStorage()
models_repo = ModelsRepo(storage)
user_service = UserService(models_repo)
question_service = QuestionService(models_repo)

@app.route('/user',methods = ['POST'])
def user_add():
    user = request.get_json()
    user_service.add_user_from_request(user)
    return user

@app.route('/question',methods = ['POST'])
def question_add():
    question = request.get_json()
    question_service.add_question_for_user(question)
    return question

@app.route('/question/<user>',methods = ['GET'])
def questions_for_user(user):
    questions = question_service.get_questions_for_user(user)
    return render_template("questions.html", questions=questions)

@app.route('/users',methods = ['GET'])
def users_get():
    users = user_service.get_users()
    return render_template("users.html", users=users)


app.run()