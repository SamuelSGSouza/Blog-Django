from django.db import models
from categorias.models import Categoria
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    titulo = models.CharField(max_length=50, verbose_name='Título')
    autor = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="Autor")
    data = models.DateTimeField(default=timezone.now, verbose_name='Data')
    conteudo = models.TextField(verbose_name='Conteudo')
    excerto = models.TextField(verbose_name='Excerto')
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, blank=True,null=True, verbose_name='Categoria')
    imagem = models.ImageField(upload_to='post_img/%Y/%m/%d', blank=True, null=True, verbose_name='Imagem')
    publicado = models.BooleanField(default=False, verbose_name='Publicado')

    def __str__(self):
        return self.titulo


