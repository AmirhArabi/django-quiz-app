from .models import Question, UserResult
from django.forms.models import model_to_dict

from django.contrib.auth.models import User


def updatescore(data):
    username = data['username']
    user = User.objects.get(username=username)
    print(user)
    total = 0
    score = 0
    current = 0
    wrong = 0

    for i in data['answers']:
        print(i)
        try:
            id = int(i['qid'])  # تبدیل id به عدد صحیح
        except ValueError:
            raise ValueError(f"Invalid question id: {i['qid']}")

        answer = i['answer']
        question = Question.objects.filter(id=id).first()

        if question is not None:
            total += 1
            if question.answer == answer:
                score += 10
                current += 1
            else:
                wrong += 1

    percent = (score / (total * 10)) * 100 if total > 0 else 0
    print(percent)
    UserResult.objects.update_or_create(
        username=user,
        total=total,
        score=score,
        percent=percent,
        current=current,
        wrong=wrong,
        defaults={
            'total': total,
            'score': score,
            'percent': percent,
            'current': current,
            'wrong': wrong,
        },
    )
    print("score updatedd")
    result = UserResult.objects.filter(username=user).first()
    print("sasdasdasd", result)
    return model_to_dict(result)
