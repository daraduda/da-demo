from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Car
from .serializers import CarSerializer

class CarAPIView(APIView):
    def get(self, request):
        cars = Car.objects.all()
        return Response({'cars': CarSerializer(cars, many=True).data}, status=200)

    def post(self, request):
        serializer = CarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data}, status=201)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method PUT not allowed.'}, status=405)

        try:
            instance = Car.objects.get(pk=pk)
        except:
            return Response({'error': 'Object does not exist.'}, status=404)

        serializer = CarSerializer(instance=instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'put': serializer.data}, status=200)

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method DELETE not allowed.'}, status=405)

        try:
            instance = Car.objects.get(pk=pk)
        except:
            return Response({'error': 'Object does not exist.'}, status=404)

        instance.delete()
        return Response({'delete id': pk, 'status': 'success'}, status=200)

# class CarAPIView(generics.ListAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer
