from django import forms
from .models import Relatorios_recrutamento
from users.models import CustomUser

def USERS_CHOICES():
    try:
        users = CustomUser.objects.all()
        escolhas = (('NADA','NADA'),)
        if users:
            for user in users:
                tuplo = ((user.username,user.first_name + ' ' + user.last_name),)
                try:
                    escolhas += tuplo
                except:
                    escolhas = tuplo
            return escolhas
    except:
        return (('NADA','NADA'),)
    return (('NADA','NADA'),)

class RecrutamentoForm(forms.Form):
    SEMESTRE_ESCOLHA = (("1º Semestre","1º Semestre"), ("2º Semestre","2º Semestre"))


    semestre = forms.ChoiceField(choices = SEMESTRE_ESCOLHA, label = 'Semestre')
    responsavel = forms.ChoiceField(choices = USERS_CHOICES())
    n_vagas_tec = forms.IntegerField(label = 'Nº vagas TEC:')
    n_vagas_ino = forms.IntegerField(label = 'Nº vagas INO:')
    n_vagas_int = forms.IntegerField(label = 'Nº vagas INT:')
    n_candidatos = forms.IntegerField(label = 'Nº de candidatos:')
    n_grupos = forms.IntegerField(label = 'Nº de grupos:')
    n_min_grupo = forms.IntegerField(label = 'Mínimo grupo:')
    n_max_grupo = forms.IntegerField(label = 'Máximo grupo:')
    n_individual = forms.IntegerField(label = 'Individual:')
    n_estagio = forms.IntegerField(label = 'Estagio:')
    n_admitidos = forms.IntegerField(label = 'Admitidos:')
