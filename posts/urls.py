from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostIndex.as_view(), name="index"),
    path('categoria/<str:categoria>', views.PostCategoria.as_view(), name="post_categoria"),
    path('busca/', views.PostBusca.as_view(), name="post_busca"),
    #Nota: Herdando a classe UpdateView do django, o nome do valor inteiro que será recebido
    # na view deve ser PK
    path('post/<int:pk>', views.PostDetalhes.as_view(), name="post_detalhes"),

]