from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class ProcessImage(APIView):

    def get(self, request):
        return Response(data={'hello': 1}, status=status.HTTP_200_OK)