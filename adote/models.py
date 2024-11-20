from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    DOADOR = 'doador'
    ADOTANTE = 'adotante'
    TIPOS_USUARIO = [
        (DOADOR, 'Doador'),
        (ADOTANTE, 'Adotante'),
    ]

    tipo_usuario = models.CharField(max_length=10, choices=TIPOS_USUARIO)
    telefone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return f"{self.username} ({self.get_tipo_usuario_display()})"

class TipoAnimal(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome

class Local(models.Model):
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.cidade} - {self.estado}"

class Animal(models.Model):
    SEXO_CHOICES = [
        ('M', 'Macho'),
        ('F', 'Fêmea'),
    ]

    nome = models.CharField(max_length=100)
    idade_anos = models.PositiveIntegerField(blank=True, null=True, help_text="Preencha apenas se a idade estiver em anos.")
    idade_meses = models.PositiveIntegerField(blank=True, null=True, help_text="Preencha apenas se a idade estiver em meses.")
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, default='M')
    tipo = models.ForeignKey(TipoAnimal, on_delete=models.CASCADE, related_name="animais")
    descricao = models.TextField(blank=True)
    local = models.ForeignKey(Local, on_delete=models.CASCADE, related_name="animais")
    doador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="animais_doadores")
    adotado = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

    def idade_formatada(self):
        if self.idade_anos:
            return f"{self.idade_anos} anos"
        elif self.idade_meses:
            return f"{self.idade_meses} meses"
        return "Idade não especificada"


class Adocao(models.Model):
    animal = models.OneToOneField(Animal, on_delete=models.CASCADE, related_name="adocao")
    adotante = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="adocoes")
    data_adocao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.adotante.username} adotou {self.animal.nome}"

class HistoriaAnimal(models.Model):
    animal = models.OneToOneField(Animal, on_delete=models.CASCADE, related_name="historia")
    historia = models.TextField()

    def __str__(self):
        return f"História de {self.animal.nome}"