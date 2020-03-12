from rest_framework.serializers import ModelSerializer
from core_learn_race.models import Race, Player, Question

class PlayerSerializer(ModelSerializer):

    class Meta:
        model = Player
        fields = '__all__'

class RaceSerializer(ModelSerializer):
    players = PlayerSerializer(many=True, read_only=True)
    class Meta:
        model = Race
        fields = ['id', 'group', 'state', 'subjects', 'categories', 'players']

class QuestionSerializer(ModelSerializer):

    class Meta:
        model = Question
        fields = '__all__'
