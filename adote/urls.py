# adote/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static

# URLs de Autenticação
auth_patterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registro/', views.registro, name='registro'),
    path('deslogado/', views.deslogado, name='deslogado'),  # Página após logout
]
# URLs para Animais
animal_patterns = [
    path('', views.pagina_inicial, name='pagina_inicial'),  # Página inicial
    path('lista-animais/', views.lista_animais, name='lista_animais'),
    path('animal/<int:animal_id>/', views.detalhes_animal, name='detalhes_animal'),
    path('adotar/<int:animal_id>/', views.adotar_animal, name='adotar_animal'),  # Adoção
    path('doar/', views.doar_animal, name='doar_animal'),  # Doação
    path('marcar-adotado/', views.marcar_adotado, name='marcar_adotado'),  # Marcar como adotado
]
# URLs para Administração
admin_patterns = [
    path('admin-area/', views.area_admin, name='area_admin'),  # Área administrativa
    path('adicionar-pet/', views.adicionar_pet, name='adicionar_pet'),  # Adicionar novo pet
]
# Combinação dos padrões de rota
urlpatterns = auth_patterns + animal_patterns + admin_patterns

# Configuração para servir arquivos de mídia em modo DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
