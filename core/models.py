from django.db import models
from stdimage.models import StdImageField
import uuid


# Gera o nome do arquivo / Evitar duplicidade de nome
def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


# Base para Armazenar dados especificos
class Base(models.Model):
    created_at = models.DateField('Criação', auto_now_add=True)
    modified_at = models.DateField('Modificado', auto_now=True)
    activated = models.BooleanField('Ativado?', default=True)

    class Meta:
        # especificando que será um dado abstrato
        abstract = True


class PhrasesModel(Base):
    # campos, nome/frase
    name = models.CharField('Nome', max_length=100)
    phrase = models.TextField('Frase')
    imagem = StdImageField('Imagem',
                           # nome do arquivo
                           upload_to=get_file_path,
                           # cria um novo arquivo redimencionado 600x300
                           variations={'thumb': {'width': 400, 'height': 400, 'crop': True}})

    class Meta:
        # nome em singular e plural
        verbose_name = 'Phrase'
        verbose_name_plural = 'Phrases'

    def __str__(self):
        # nome que será retornado para o dado especifico
        return f'{self.name}_{self.id}'
