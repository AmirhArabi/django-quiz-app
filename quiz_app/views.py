import random

from django.contrib.auth.models import User
from django.db.models import Sum
from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from .email_module import send_email_result
from .models import Question, UserResult, Category
from .serializers import (QuestionsSerializer, ResultSerializer,
                          CategorysSerializer, QuestionSerializer)
from .utils import updatescore
from rest_framework.authtoken.models import Token


class StartGame(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, category_name):
        try:
            valid_list = Question.objects.filter(category=category_name).values_list('id', flat=True)
            random_list = random.sample(list(valid_list), min(len(valid_list), 3))
            query_set = Question.objects.filter(id__in=random_list)
            serializer = QuestionSerializer(query_set, many=True)
            return Response(serializer.data)
        except Category.DoesNotExist:
            return Response({"message": "دسته بندی مورد نظر یافت نشد."}, status=status.HTTP_404_NOT_FOUND)


class Quiz(View):
    def get(self, request):
        if request.user.is_authenticated:
            user_flag = True

            if UserResult.objects.filter(username=request.user).exists():
                user_flag = False

            questions = Question.objects.all()

            return render(request, 'index.html', {'questions': questions, 'flag': user_flag})
        else:
            return redirect('account:login_page')

    def post(self, request):
        print(request.POST)
        questions = Question.objects.filter(status=True)
        fullname = request.user
        totall = 0
        score = 0
        correct = 0
        wrong = 0
        for q in questions:
            totall += 1
            if q.answer == request.POST.get(q.question):
                score += 10
                correct += 1
            else:
                wrong += 1
        percent = score / (totall * 10) * 100

        UserResult.objects.create(
            username=fullname,
            total=totall,
            score=score,
            percent=percent,
            current=correct,
            wrong=wrong,
        )

        return redirect(reverse('quiz:result_page') + f'?fullname={fullname}')


class Result(View):
    def get(self, request):
        if request.user.is_authenticated:
            try:
                fullname = request.GET['fullname']
                user_object = UserResult.objects.get(username=fullname)
                return render(request, 'quiz_app/result.html', {'user': user_object})
            except:
                return redirect('quiz:quiz_page')
        else:
            return redirect('account:login_page')


def send_email(request):
    if request.user.is_authenticated and request.method == 'GET':
        if UserResult.objects.filter(fullname=request.user.username).exists():
            name = request.user.username
            user_result = UserResult.objects.get(fullname=name)

            send_email_result.delay(
                name=user_result.fullname,
                total=user_result.total,
                score=user_result.score,
                percent=user_result.percent,
                correct=user_result.correct,
                wrong=user_result.wrong,
                created_at=user_result.created_at,
                email=request.user.email,
            )
            return redirect('quiz:result_page')
        else:
            return redirect('quiz:quiz_page')
    else:
        return redirect('account:login_page')


# ----------------- API VIEWS--------------------


class CategoryListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        qategory_list = Category.objects.filter()
        if len(qategory_list) == 0:
            return Response('No Data', status=status.HTTP_204_NO_CONTENT)
        else:
            serializer = CategorysSerializer(instance=qategory_list, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


class QuestionListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        questions_list = Question.objects.filter(status=True)
        if len(questions_list) == 0:
            return Response('No Data', status=status.HTTP_204_NO_CONTENT)
        else:
            serializer = QuestionsSerializer(instance=questions_list, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


class ResultView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            instance = UserResult.objects.get(username=request.user)
        except:
            return Response({'Error': 'There is no result'}, status=status.HTTP_204_NO_CONTENT)
        serializer = ResultSerializer(instance=instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryQuestionList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, category_name):
        try:
            category = Category.objects.get(category_name=category_name)
            questions = Question.objects.filter(category=category)
            serializer = QuestionSerializer(questions, many=True)
            return Response(serializer.data)
        except Category.DoesNotExist:
            return Response({"message": "دسته بندی مورد نظر یافت نشد."}, status=status.HTTP_404_NOT_FOUND)


class LeaderBoard(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            users = User.objects.alias(total_score=Sum('userresult__score')).order_by('-total_score')[:5]
            print(users)
            data = {}
            for i in users:
                print(i)
                try:
                    user = UserResult.objects.get(username=i)
                    score = user.score
                    data[str(user.username)] = score
                except UserResult.DoesNotExist:
                    data[str(i.username)] = 0

            return Response(data)
        except Category.DoesNotExist:
            return Response({"message": "هیچ کاربری تا کنون در مسابقه شرکت نکرده است."},
                            status=status.HTTP_404_NOT_FOUND)


class AnswerView(APIView):
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            answers = request.data.get('answers', [])
            if not isinstance(answers, list):
                return Response({"error": "Invalid answers format"}, status=400)

            data = {
                'answers': answers,
                'username': str(request.user.username)
            }
            result = updatescore(data)
            return Response(result)
        except ValueError as e:
            return Response({"error": str(e)}, status=400)
        except Exception as e:
            return Response({"error": "An error occurred"}, status=500)

