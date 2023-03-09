# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Abril(models.Model):
    data = models.CharField(max_length=12, blank=True, null=True)
    siglase = models.CharField(db_column='siglaSE', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cargalancada = models.CharField(db_column='cargaLancada', max_length=12, blank=True, null=True)  # Field name made lowercase.
    cargabaixada = models.CharField(db_column='cargaBaixada', max_length=12, blank=True, null=True)  # Field name made lowercase.
    percentual = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Abril'


class Agosto(models.Model):
    data = models.CharField(max_length=12, blank=True, null=True)
    siglase = models.CharField(db_column='siglaSE', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cargalancada = models.CharField(db_column='cargaLancada', max_length=12, blank=True, null=True)  # Field name made lowercase.
    cargabaixada = models.CharField(db_column='cargaBaixada', max_length=12, blank=True, null=True)  # Field name made lowercase.
    percentual = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Agosto'


class Dezembro(models.Model):
    data = models.CharField(max_length=12, blank=True, null=True)
    siglase = models.CharField(db_column='siglaSE', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cargalancada = models.CharField(db_column='cargaLancada', max_length=12, blank=True, null=True)  # Field name made lowercase.
    cargabaixada = models.CharField(db_column='cargaBaixada', max_length=12, blank=True, null=True)  # Field name made lowercase.
    percentual = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Dezembro'


class Fevereiro(models.Model):
    data = models.CharField(max_length=12, blank=True, null=True)
    siglase = models.CharField(db_column='siglaSE', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cargalancada = models.CharField(db_column='cargaLancada', max_length=12, blank=True, null=True)  # Field name made lowercase.
    cargabaixada = models.CharField(db_column='cargaBaixada', max_length=12, blank=True, null=True)  # Field name made lowercase.
    percentual = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Fevereiro'


class Janeiro(models.Model):
    data = models.CharField(max_length=12, blank=True, null=True)
    siglase = models.CharField(db_column='siglaSE', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cargalancada = models.CharField(db_column='cargaLancada', max_length=12, blank=True, null=True)  # Field name made lowercase.
    cargabaixada = models.CharField(db_column='cargaBaixada', max_length=12, blank=True, null=True)  # Field name made lowercase.
    percentual = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Janeiro'


class Julho(models.Model):
    data = models.CharField(max_length=12, blank=True, null=True)
    siglase = models.CharField(db_column='siglaSE', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cargalancada = models.CharField(db_column='cargaLancada', max_length=12, blank=True, null=True)  # Field name made lowercase.
    cargabaixada = models.CharField(db_column='cargaBaixada', max_length=12, blank=True, null=True)  # Field name made lowercase.
    percentual = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Julho'


class Junho(models.Model):
    data = models.CharField(max_length=12, blank=True, null=True)
    siglase = models.CharField(db_column='siglaSE', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cargalancada = models.CharField(db_column='cargaLancada', max_length=12, blank=True, null=True)  # Field name made lowercase.
    cargabaixada = models.CharField(db_column='cargaBaixada', max_length=12, blank=True, null=True)  # Field name made lowercase.
    percentual = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Junho'


class Maio(models.Model):
    data = models.CharField(max_length=12, blank=True, null=True)
    siglase = models.CharField(db_column='siglaSE', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cargalancada = models.CharField(db_column='cargaLancada', max_length=12, blank=True, null=True)  # Field name made lowercase.
    cargabaixada = models.CharField(db_column='cargaBaixada', max_length=12, blank=True, null=True)  # Field name made lowercase.
    percentual = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Maio'


class Março(models.Model):
    data = models.CharField(max_length=12, blank=True, null=True)
    siglase = models.CharField(db_column='siglaSE', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cargalancada = models.CharField(db_column='cargaLancada', max_length=12, blank=True, null=True)  # Field name made lowercase.
    cargabaixada = models.CharField(db_column='cargaBaixada', max_length=12, blank=True, null=True)  # Field name made lowercase.
    percentual = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Março'


class Novembro(models.Model):
    data = models.CharField(max_length=12, blank=True, null=True)
    siglase = models.CharField(db_column='siglaSE', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cargalancada = models.CharField(db_column='cargaLancada', max_length=12, blank=True, null=True)  # Field name made lowercase.
    cargabaixada = models.CharField(db_column='cargaBaixada', max_length=12, blank=True, null=True)  # Field name made lowercase.
    percentual = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Novembro'


class Outubro(models.Model):
    data = models.CharField(max_length=12, blank=True, null=True)
    siglase = models.CharField(db_column='siglaSE', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cargalancada = models.CharField(db_column='cargaLancada', max_length=12, blank=True, null=True)  # Field name made lowercase.
    cargabaixada = models.CharField(db_column='cargaBaixada', max_length=12, blank=True, null=True)  # Field name made lowercase.
    percentual = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Outubro'


class Setembro(models.Model):
    data = models.CharField(max_length=12, blank=True, null=True)
    siglase = models.CharField(db_column='siglaSE', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cargalancada = models.CharField(db_column='cargaLancada', max_length=12, blank=True, null=True)  # Field name made lowercase.
    cargabaixada = models.CharField(db_column='cargaBaixada', max_length=12, blank=True, null=True)  # Field name made lowercase.
    percentual = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Setembro'
