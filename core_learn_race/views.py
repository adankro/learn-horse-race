from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from core_learn_race.serializers import RaceSerializer, PlayerSerializer, QuestionSerializer
from core_learn_race.models import Race, Player, Question


class RaceViewSet(ViewSet):

    def list(self, request):
        queryset = Race.objects.order_by('pk')
        serializer = RaceSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = RaceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Race.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = RaceSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Race.objects.get(pk=pk)
        except Race.DoesNotExist:
            return Response(status=404)
        serializer = RaceSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Race.objects.get(pk=pk)
        except Race.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class PlayerViewSet(ViewSet):

    def list(self, request):
        queryset = Player.objects.order_by('pk')
        serializer = PlayerSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = PlayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Player.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = PlayerSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Player.objects.get(pk=pk)
        except Player.DoesNotExist:
            return Response(status=404)
        serializer = PlayerSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Player.objects.get(pk=pk)
        except Player.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class QuestionViewSet(ViewSet):

    def list(self, request):
        queryset = Question.objects.order_by('pk')
        serializer = QuestionSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Question.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = QuestionSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            return Response(status=404)
        serializer = QuestionSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)
