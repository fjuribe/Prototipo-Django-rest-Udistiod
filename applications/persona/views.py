from django.shortcuts import render
from django.views.generic import ListView,TemplateView
#
from rest_framework.generics import(
     ListAPIView,
     CreateAPIView,
     RetrieveAPIView,
     DestroyAPIView,
     UpdateAPIView,
     RetrieveUpdateAPIView,
)
from .models import Person,Reunion
from .serializers import(
     PersonSerielizer,
     PersonaSerializer,
     PersonaSerializer2,
     ReunionSerializer,
     PersonaSerializer3,
)

class ListaPersona(ListView):    
    context_object_name='personas'
    template_name="persona/persona.html"
    def get_queryset(self):
        return Person.objects.all()


class PersonListView(TemplateView):
    template_name='persona/lista.html'

class PersonSearchApiView(ListAPIView):
    serializer_class=PersonSerielizer
    def get_queryset(self):

        #filtrado
        kword=self.kworgs['kword']

        return Person.objects.filter(
            full_name_icontains=kword
        )
##################################################


#list
class PersonListApiView(ListAPIView):
    serializer_class=PersonSerielizer
    def get_queryset(self):
        return Person.objects.all()

#create
class PersonCreateView(CreateAPIView):
    serializer_class=PersonSerielizer


#show
class PersonDetailView(RetrieveAPIView):
    serializer_class=PersonSerielizer
    queryset=Person.objects.filter()

#delete
class PersonDeleteView(DestroyAPIView):
    serializer_class=PersonSerielizer
    queryset=Person.objects.all()
    
#update
class PersonUpdateView(RetrieveAPIView):
    serializer_class=PersonSerielizer
    queryset=Person.objects.all()


#edit
class PersonRetriveUpdateView(RetrieveUpdateAPIView):
    serializer_class=PersonSerielizer
    queryset=Person.objects.all()


class PersonApiLista(ListAPIView):
    """
      vista para interacturar con serializadores
    """
    # serializer_class=PersonaSerializer
    serializer_class=PersonaSerializer2
    def get_queryset(self):
        return Person.objects.all()



class ReunionApiLista(ListAPIView):
    """
      vista para interacturar con serializadores
    """
    # serializer_class=PersonaSerializer
    serializer_class=ReunionSerializer
    def get_queryset(self):
        return Reunion.objects.all()


class PersonApiLista2(ListAPIView):
    """
      vista para interacturar con serializadores
    """
    # serializer_class=PersonaSerializer
    serializer_class=PersonaSerializer3
    def get_queryset(self):
        return Person.objects.all()