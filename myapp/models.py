from django.db import models

class MyappInstituicao(models.Model):
    codigocompensacao = models.IntegerField(db_column='CodigoCompensacao', primary_key=True)
    nomeinstituicao = models.CharField(db_column='NomeInstituicao', max_length=255)

    def __str__(self):
        return self.nomeinstituicao
    
    class Meta:
        managed = True
        db_table = 'myapp_instituicao'
