from django.db import models

class MyappInstituicao(models.Model):
    codigocompensacao = models.IntegerField(db_column='CodigoCompensacao', primary_key=True)  # Field name made lowercase.
    nomeinstituicao = models.CharField(db_column='NomeInstituicao', max_length=255)  # Field name made lowercase.

    def __str__(self):
        return self.nomeinstituicao
    
    class Meta:
        managed = True
        db_table = 'myapp_instituicao'
