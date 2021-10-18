from django.db import models
from categorias.models import Categoria
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image
from django.conf import settings
import os



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

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        self.resize_image(self.imagem.name, 800)


    @staticmethod
    def resize_image(image_name, new_width):
        image_path = os.path.join(settings.MEDIA_ROOT, image_name)

        with Image.open(image_path) as img:
            width, height = img.size
            if width > new_width:
                new_height = round((new_width * height) / width)


                new_image = img.resize((new_width, new_height), Image.ANTIALIAS)
                new_image.save(
                    image_path,
                    optimize=True,
                    quality=60
                )
            else:
                pass



