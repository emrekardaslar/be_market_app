from rest_framework.serializers import ModelSerializer

from .models import Question


class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"

    def create(self, validated_data):
        print(validated_data)
        q = Question(question_text=validated_data['question_text'],
                     pub_date=validated_data['pub_date'])
        q.save()
        return q
