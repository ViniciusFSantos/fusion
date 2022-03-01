from distutils.command.upload import upload
from fileinput import filename
from tkinter import CASCADE
from django.db import models
from stdimage.models import StdImageField
import uuid

class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualizado em:', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)
    
    class Meta:
        abstract = True
        
def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

class Servicos(Base):
    icon_choices = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Gráfico'),
        ('lni-users', 'Usuários'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
    )
    servico = models.CharField('Serviço', max_length=100)
    descricao = models.TextField('Descrção', max_length=200)
    icon = models.CharField('Icone', max_length=12, choices=icon_choices)
    
    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'
    
    def __str__(self):
        return self.servico

class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'
    
    def __str__(self):
        return self.cargo

class Colaborador(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=200)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {"width": 480, "height": 480, "crop": True}})
    facebook = models.CharField('Facebook', max_length=150, default='#')
    twitter = models.CharField('Twitter', max_length=150, default='#')
    instagram = models.CharField('Instagram', max_length=150, default='#')
    
    class Meta():
        verbose_name = 'Colaborador'
        verbose_name_plural = 'Colaboradores'
    
    def __str__(self):
        return self.nome