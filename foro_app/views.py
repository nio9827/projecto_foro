from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Post,Comment
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
# Create your views here.


def Plantilla(request):
    return render (request, 'plantilla.html')

def home(request):
    return render (request, 'Home.html')



@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  # Crea el objeto Post pero no lo guarda aún
            post.author = request.user  # Asigna el autor al usuario autenticado
            post.save()  # Guarda el objeto en la base de datos
            return redirect('Home')  # Redirige a la lista de posts (o donde prefieras)
    else:
        form = PostForm()

    return render(request, 'crear_post.html', {'form': form})


def post_list(request):
    query = request.GET.get('search', '')  # Obtiene el término de búsqueda desde el parámetro 'search' en la URL
    
    if query:
        posts = Post.objects.filter(title__icontains=query)  # Filtra los posts cuyo título contiene el término de búsqueda
    else:
        posts = Post.objects.all()  # Si no hay término de búsqueda, muestra todos los posts
    
    return render(request, 'Ver_post.html', {'posts': posts, 'query': query})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    # Crear comentario si el formulario es enviado
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post  # Asociar el comentario al post
            comment.author = request.user  # Asociar el comentario al usuario
            comment.save()
            return redirect(post.get_absolute_url())  # Redirige a la misma página del post
    else:
        comment_form = CommentForm()

    comments = post.comments.all()  # Obtiene todos los comentarios del post

    return render(request, 'detalle_post.html', {
        'post': post,
        'comment_form': comment_form,
        'comments': comments
    })