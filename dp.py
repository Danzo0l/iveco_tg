from sqlalchemy.orm import sessionmaker

from settings import Question, engine


def push(username, obj):
    session = sessionmaker(bind=engine)
    session = session()
    user = session.query(Question).filter_by(username=username).first()

    user.answer_2 = obj["question2"]
    user.answer_3 = obj["question3"]
    user.answer_4 = obj["question4"]
    user.answer_5 = obj["question5"]
    user.answer_6 = obj["question6"]
    user.answer_7 = obj["question7"]
    user.answer_8 = obj["question8"]
    user.answer_9 = obj["question9"]
    user.answer_10 = obj["question10"]
    user.answer_11 = obj["question11"]
    user.answer_12 = obj["question12"]
    user.answer_13 = obj["question13"]
    user.answer_14 = obj["question14"]
    user.answer_15 = obj["question15"]
    user.answer_16 = obj["question16"]
    user.answer_17 = obj["question17"]
    user.answer_18 = obj["question18"]

    session.commit()
    session.close()


def push_only(username, obj):
    session = sessionmaker(bind=engine)
    session = session()
    new_question = Question(
        username=username,
        phone=obj["question19"],
        answer_1=obj["question1"],
    )
    session.add(new_question)
    session.commit()
    session.close()


def check_user_existence(username):
    session = sessionmaker(bind=engine)
    session = session()
    user = session.query(Question).filter_by(username=username).first()
    session.close()
    if user:
        return True
    else:
        return False
