# Generated by Django 3.2.7 on 2021-10-09 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='email_comentario',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='nome_comentario',
            field=models.CharField(max_length=150, verbose_name='Nome'),
        ),
    ]