from django import forms
from django.core.mail.message import EmailMessage

class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=120)
    mensagem = forms.CharField(label='Menssagem', widget=forms.Textarea())
    
    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']
        
        conteudo = f'Nome:{nome}\n, E-mail:{email}\n, Assunto: {assunto}\n, Mensagem: {mensagem}'
        
        mail = EmailMessage(
            subject=assunto,
            body=conteudo,
            from_email='teste@teste.com.br',
            to=['contato@contato.com.br'],
            headers={'Reply-To': email}
            )
        mail.send()