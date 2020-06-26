from rest_framework import serializers


class MessageSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    link = serializers.URLField(max_length = 200)
    creation_date = serializers.CharField(max_length=120)
    amount_of_upvotes = serializers.IntegerField(default = 0)
    author_name = serializers.CharField(max_length=20)

    def create(self, validated_data):
        return Message.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.link = validated_data.get('link', instance.link)
        instance.amount_of_upvotes = validated_data.get('amount_of_upvotes', instance.amount_of_upvotes)
        instance.author_id = validated_data.get('author_id', instance.author_id)
        instance.save()
        return instance