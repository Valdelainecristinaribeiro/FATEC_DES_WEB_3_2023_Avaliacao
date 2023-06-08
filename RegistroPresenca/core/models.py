from django.db import models

class RegistroModel(models.Model):
    nome = models.CharField('Nome Aluno', max_length=100)
    OPCOES_PROFESSOR = (
        ('Orlando Saraiva Jr', 'Orlando Saraiva Jr'),
        ('Thiago Mendes', 'Thiago Mendes'),
        ('Esdras Silva', 'Esdras Silva'),
        ('Ana Celia Portes', 'Ana Celia Portes'),
    )
    professor = models.CharField('Nome Professor', max_length=100, choices=OPCOES_PROFESSOR)

    def __str__(self):
        return self.nome