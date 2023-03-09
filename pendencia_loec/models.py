# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Abril(models.Model):
    mcu = models.CharField(max_length=10, blank=True, null=True)
    sro = models.CharField(db_column='SRO', max_length=8, blank=True, null=True)  # Field name made lowercase.
    nomeunidade = models.CharField(db_column='nomeUnidade', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gerencia = models.CharField(db_column='Gerencia', max_length=5, blank=True, null=True)  # Field name made lowercase.
    lista = models.CharField(db_column='Lista', max_length=4, blank=True, null=True)  # Field name made lowercase.
    lancado = models.CharField(max_length=18, blank=True, null=True)
    objeto = models.CharField(db_column='Objeto', max_length=13, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Abril'


class Agosto(models.Model):
    mcu = models.CharField(max_length=10, blank=True, null=True)
    sro = models.CharField(db_column='SRO', max_length=8, blank=True, null=True)  # Field name made lowercase.
    nomeunidade = models.CharField(db_column='nomeUnidade', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gerencia = models.CharField(db_column='Gerencia', max_length=5, blank=True, null=True)  # Field name made lowercase.
    lista = models.CharField(db_column='Lista', max_length=4, blank=True, null=True)  # Field name made lowercase.
    lancado = models.CharField(max_length=18, blank=True, null=True)
    objeto = models.CharField(db_column='Objeto', max_length=13, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Agosto'


class Dezembro(models.Model):
    mcu = models.CharField(max_length=10, blank=True, null=True)
    sro = models.CharField(db_column='SRO', max_length=8, blank=True, null=True)  # Field name made lowercase.
    nomeunidade = models.CharField(db_column='nomeUnidade', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gerencia = models.CharField(db_column='Gerencia', max_length=5, blank=True, null=True)  # Field name made lowercase.
    lista = models.CharField(db_column='Lista', max_length=4, blank=True, null=True)  # Field name made lowercase.
    lancado = models.CharField(max_length=18, blank=True, null=True)
    objeto = models.CharField(db_column='Objeto', max_length=13, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Dezembro'


class Fevereiro(models.Model):
    mcu = models.CharField(max_length=20, blank=True, null=True)
    sro = models.CharField(db_column='SRO', max_length=8, blank=True, null=True)  # Field name made lowercase.
    nomeunidade = models.CharField(db_column='nomeUnidade', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gerencia = models.CharField(db_column='Gerencia', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lancado = models.CharField(max_length=30, blank=True, null=True)
    objeto = models.CharField(db_column='Objeto', max_length=13, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Fevereiro'


class Janeiro(models.Model):
    mcu = models.CharField(max_length=10, blank=True, null=True)
    sro = models.CharField(db_column='SRO', max_length=8, blank=True, null=True)  # Field name made lowercase.
    nomeunidade = models.CharField(db_column='nomeUnidade', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gerencia = models.CharField(db_column='Gerencia', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lancado = models.CharField(max_length=30, blank=True, null=True)
    objeto = models.CharField(db_column='Objeto', max_length=13, blank=True, null=True)  # Field name made lowercase.
    prazo = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'Janeiro'


class Julho(models.Model):
    mcu = models.CharField(max_length=10, blank=True, null=True)
    sro = models.CharField(db_column='SRO', max_length=8, blank=True, null=True)  # Field name made lowercase.
    nomeunidade = models.CharField(db_column='nomeUnidade', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gerencia = models.CharField(db_column='Gerencia', max_length=5, blank=True, null=True)  # Field name made lowercase.
    lista = models.CharField(db_column='Lista', max_length=4, blank=True, null=True)  # Field name made lowercase.
    lancado = models.CharField(max_length=18, blank=True, null=True)
    objeto = models.CharField(db_column='Objeto', max_length=13, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Julho'


class Junho(models.Model):
    mcu = models.CharField(max_length=10, blank=True, null=True)
    sro = models.CharField(db_column='SRO', max_length=8, blank=True, null=True)  # Field name made lowercase.
    nomeunidade = models.CharField(db_column='nomeUnidade', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gerencia = models.CharField(db_column='Gerencia', max_length=5, blank=True, null=True)  # Field name made lowercase.
    lista = models.CharField(db_column='Lista', max_length=4, blank=True, null=True)  # Field name made lowercase.
    lancado = models.CharField(max_length=18, blank=True, null=True)
    objeto = models.CharField(db_column='Objeto', max_length=13, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Junho'


class Maio(models.Model):
    mcu = models.CharField(max_length=10, blank=True, null=True)
    sro = models.CharField(db_column='SRO', max_length=8, blank=True, null=True)  # Field name made lowercase.
    nomeunidade = models.CharField(db_column='nomeUnidade', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gerencia = models.CharField(db_column='Gerencia', max_length=5, blank=True, null=True)  # Field name made lowercase.
    lista = models.CharField(db_column='Lista', max_length=4, blank=True, null=True)  # Field name made lowercase.
    lancado = models.CharField(max_length=18, blank=True, null=True)
    objeto = models.CharField(db_column='Objeto', max_length=13, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Maio'


class Maro(models.Model):
    mcu = models.CharField(max_length=10)
    sro = models.CharField(db_column='SRO', max_length=8, blank=True, null=True)  # Field name made lowercase.
    nomeunidade = models.CharField(db_column='nomeUnidade', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gerencia = models.CharField(db_column='Gerencia', max_length=8, blank=True, null=True)  # Field name made lowercase.
    lista = models.CharField(db_column='Lista', max_length=4, blank=True, null=True)  # Field name made lowercase.
    lancado = models.CharField(max_length=20, blank=True, null=True)
    objeto = models.CharField(db_column='Objeto', max_length=13, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Março'


class Novembro(models.Model):
    mcu = models.CharField(max_length=10, blank=True, null=True)
    sro = models.CharField(db_column='SRO', max_length=8, blank=True, null=True)  # Field name made lowercase.
    nomeunidade = models.CharField(db_column='nomeUnidade', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gerencia = models.CharField(db_column='Gerencia', max_length=5, blank=True, null=True)  # Field name made lowercase.
    lista = models.CharField(db_column='Lista', max_length=4, blank=True, null=True)  # Field name made lowercase.
    lancado = models.CharField(max_length=18, blank=True, null=True)
    objeto = models.CharField(db_column='Objeto', max_length=13, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Novembro'


class Outubro(models.Model):
    mcu = models.CharField(max_length=10)
    sro = models.CharField(db_column='SRO', max_length=8, blank=True, null=True)  # Field name made lowercase.
    nomeunidade = models.CharField(db_column='nomeUnidade', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gerencia = models.CharField(db_column='Gerencia', max_length=5, blank=True, null=True)  # Field name made lowercase.
    lista = models.CharField(db_column='Lista', max_length=4, blank=True, null=True)  # Field name made lowercase.
    lancado = models.CharField(max_length=18, blank=True, null=True)
    objeto = models.CharField(db_column='Objeto', max_length=13, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Outubro'


class Setembro(models.Model):
    mcu = models.CharField(max_length=10)
    sro = models.CharField(db_column='SRO', max_length=8, blank=True, null=True)  # Field name made lowercase.
    nomeunidade = models.CharField(db_column='nomeUnidade', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gerencia = models.CharField(db_column='Gerencia', max_length=5, blank=True, null=True)  # Field name made lowercase.
    lista = models.CharField(db_column='Lista', max_length=4, blank=True, null=True)  # Field name made lowercase.
    lancado = models.CharField(max_length=18, blank=True, null=True)
    objeto = models.CharField(db_column='Objeto', max_length=13, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Setembro'
