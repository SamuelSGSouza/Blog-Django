from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from .models import Post
from django.db.models import Count, Q, When, Case
from comentarios.forms import FormComentario
from comentarios.models import Comentario
from django.contrib import messages
from django.shortcuts import redirect


class PostIndex(ListView):
    model = Post
    template_name = 'posts/index.html'
    paginate_by = 6
    context_object_name = 'posts'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.select_related('categoria')
        qs = qs.order_by('-id').filter(publicado=True)
        qs = qs.annotate(
            numero_comentarios=Count(
                Case(
                    When(comentario__publicado_comentario=True, then=1)
                )
            )
        )
        return qs


class PostBusca(PostIndex):
    template_name = 'posts/post_busca.html'

    def get_queryset(self):
        qs = super().get_queryset()
        termo = self.request.GET.get('termo')

        if not termo:
            return qs

        qs = qs.filter(
            Q(titulo__icontains=termo) |
            Q(autor__first_name__iexact=termo) |
            Q(conteudo__icontains=termo) |
            Q(excerto__icontains=termo) |
            Q(categoria__nome_categoria__iexact=termo)

        )
        return qs

class PostCategoria(PostIndex):
    template_name = 'posts/post_categoria.html'


    def get_queryset(self):
        qs = super().get_queryset()
        categoria = self.kwargs.get('categoria', None)

        if not categoria:
            return qs

        qs = qs.filter(categoria__nome_categoria__iexact=categoria)

        return qs


class PostDetalhes(UpdateView):
    template_name = 'posts/post_detalhes.html'
    model = Post
    form_class = FormComentario
    context_object_name = 'post'


    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        post = self.get_object()
        comentarios = Comentario.objects.filter(publicado_comentario=True,
                                                post_comentario=post.id)
        contexto['comentarios'] = comentarios

        return contexto


    def form_valid(self, form):
        post = self.get_object()
        comentario = Comentario(**form.cleaned_data)
        comentario.post_comentario = post

        if self.request.user.is_authenticated:
            comentario.usuario_comentario = self.request.user

        comentario.save()
        messages.success(self.request, 'Comentário Enviado com Sucesso')
        return redirect('post_detalhes', pk=post.id)



