from django.urls import path
from .import views

app_name='persona_app'
urlpatterns = [
    path('personas/',views.ListaPersona.as_view(),name="personas"),   
    path('lista/',views.PersonListView.as_view(),name="personas_template"),
    path('api/persona/search/<kword>/',views.PersonSearchApiView.as_view(),name="personas_template"),
    #rutas de api
    path('api/persona/lista/',views.PersonListApiView.as_view(),name="personas_list"),
    path('api/persona/create/',views.PersonCreateView.as_view(),name="personas_create"),
    path('api/persona/detail/<pk>',views.PersonDetailView.as_view(),name="personas_detail"),
    path('api/persona/delete/<pk>',views.PersonDeleteView.as_view(),name="personas_delete"),
    path('api/persona/update/<pk>',views.PersonUpdateView.as_view(),name="personas_update"),
    path('api/persona/edit/<pk>',views.PersonRetriveUpdateView.as_view(),name="personas_edit"),


    #ruta que interactura con un serializador
    path('api/personas/',views.PersonApiLista2.as_view(),name="api_personas"),
    path('api/reuniones/',views.ReunionApiLista.as_view(),name="api_reuniones"),
]
