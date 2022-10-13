from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from passagens.classe_viagem import tipos_de_classes

class PassagemForms(forms.Form):
    origem = forms.CharField(label='Origem', max_length=100)
    destino = forms.CharField(label='Destino',  max_length=100)
    data_ida = forms.DateField(label='Ida', widget=DatePicker())
    data_volta = forms.DateField(label='Volta',  widget=DatePicker())
    data_pesquisa = forms.DateField(label='Data da pesquisa', disabled=True, initial=datetime.today)
    classes_viagem = forms.ChoiceField(label='Classe do vôo', choices=tipos_de_classes)
    informacoes = forms.CharField(
        label='Informações extras', 
        max_length=200,
        widget=forms.Textarea(),
        required=False
    )
    email = forms.EmailField(label='Email', max_length=150)

    def clean_origem(self):
        origem = self.cleaned_data.get('origem')
        if any(char.isdigit() for char in origem):
            raise forms.ValidationError('Origem inválida: Não inclua números')
        else:
            return origem
    
    def clean_destino(self):
        destino = self.cleaned_data.get('destino')
        if any(char.isdigit() for char in destino):
            raise forms.ValidationError('Destino inválida: Não inclua números')
        else:
            return destino
    
    def clean(self):
        origem = self.cleaned_data.get('origem')
        destino = self.cleaned_data.get('destino')
        
        return self.cleaned_data