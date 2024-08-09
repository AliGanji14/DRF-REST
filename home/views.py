from itertools import repeat

from rest_framework.views import APIView
from rest_framework.response import Response


class Home(APIView):
    def get(self, request):
        return Response({'name': 'Ali'})

    def post(self, request):
        print(request.data)
        name = request.data['name']
        return Response({'name': name})
