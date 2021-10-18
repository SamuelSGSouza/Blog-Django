from django.forms import ModelForm
from .models import Comentario
import requests

class FormComentario(ModelForm):
    def clean(self):
        raw_data = self.data
        recaptch_response = raw_data.get('g-recaptcha-response')
        recaptch_request = requests.post(
            'https://www.google.com/recaptcha/api/siteverify',
            data={
                'secret': '6LfCFtwcAAAAAB3qJQRsRhnTjdakSv0Z9PkVTrW0',
                'response': recaptch_response
            }
        )

        recaptch_result = recaptch_request.json()
        if not recaptch_result.get('success'):
            self.add_error(
                'comentario',
                'Desculpe, MR. Robot.'
            )

        #https://www.google.com/recaptcha/api/siteverify
        #secret
        #response



        print(raw_data)
        data = self.cleaned_data
        nome = data.get('nome_comentario')
        email = data.get('email_comentario')

        if len(nome) < 5:
            self.add_error(
                'nome_comentario',
                'Nome precisa ter mais que 5 caracteres'
            )


    class Meta:
        model = Comentario
        fields = ('nome_comentario', 'email_comentario', 'comentario')