from django.db import models
from django.conf import settings  # Usamos settings para obtener AUTH_USER_MODEL
from django.utils import timezone
from django.urls import reverse

# Modelo Post
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Usamos settings.AUTH_USER_MODEL

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        # Devuelve la URL de detalle del post
        return reverse('post_detail', kwargs={'pk': self.pk})

# Modelo Comment
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Usamos settings.AUTH_USER_MODEL
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comentario de {self.author} sobre {self.post.title}'

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.post.pk})
