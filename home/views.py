from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import Person, Question
from .serializers import PersonSerializer, QuestionSerializer
from permissions import IsOwnerOrReadOnly


class Home(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        person = Person.objects.all()
        ser_data = PersonSerializer(instance=person, many=True)
        return Response(data=ser_data.data)


class QuestionListView(APIView):
    def get(self, request):
        questions = Question.objects.all()
        ser_data = QuestionSerializer(instance=questions, many=True).data
        return Response(ser_data, status=status.HTTP_200_OK)


class QuestionCreateView(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        srz_data = QuestionSerializer(data=request.data)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_201_CREATED)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionUpdateView(APIView):
    permission_classes = [IsOwnerOrReadOnly, ]

    def put(self, request, pk):
        question = Question.objects.get(pk=pk)
        self.check_object_permissions(request, question)
        srz_data = QuestionSerializer(instance=question, data=request.data, partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_200_OK)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDeleteView(APIView):
    permission_classes = [IsOwnerOrReadOnly, ]

    def delete(self, request, pk):
        question = Question.objects.get(pk=pk)
        self.check_object_permissions(request, question)
        question.delete()
        return Response({'messages': 'question deleted successfully'}, status=status.HTTP_200_OK)
