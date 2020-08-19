from rest_framework import serializers

from .models import Person,Reunion,Hobby

class PersonSerielizer(serializers.ModelSerializer):
    class Meta:
        model=Person
        fields=('__all__')
        # fields=(
        #     'id',
        #     'full_name',
        #     'job',
        #     'email',
        # )


#interacturar con serializadores
class PersonaSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    full_name = serializers.CharField()
    job = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()
    activo=serializers.BooleanField(required=False)


class PersonaSerializer2(serializers.ModelSerializer):
    activo=serializers.BooleanField(default=False)
    class Meta:
        model=Person
        fields=('__all__')


class ReunionSerializer(serializers.ModelSerializer):
    persona=PersonaSerializer()
    class Meta:
        model=Reunion
        fields=(
            'id',
            'fecha',
            'hora',
            'asunto',
            'persona',
        )


class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        model=Hobby
        fields=('__all__')


class PersonaSerializer3(serializers.ModelSerializer):
    hobbies=HobbySerializer(many=True)
    class Meta:
        model=Person
        fields=(
            'id',
            'full_name',
            'job',
            'email',
            'phone',
            'hobbies',
            'created'
        )
    
    
    
