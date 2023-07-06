import smtplib
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def enviar_email(destinatario, nome, chave_acesso):
    # Configurações do servidor SMTP
    servidor_smtp = 'smtp.gmail.com'  # Servidor SMTP do Gmail
    porta_smtp = 587  # Porta do servidor SMTP do Gmail
    usuario = 'seu_email@gmail.com'  # Seu endereço de e-mail do Gmail
    senha = 'sua_senha_de_aplicativo'  # Senha de aplicativo gerada para o script Python

    # Construindo a mensagem do e-mail
    mensagem = MIMEMultipart()
    mensagem['Subject'] = 'Mensagem Importante'  # Assunto do e-mail
    mensagem['From'] = usuario  # Remetente
    mensagem['To'] = destinatario  # Destinatário

    # Texto do e-mail
    texto = f'Olá {nome}!\n\nSua chave de acesso é: {chave_acesso}\n\nAtenciosamente,\nSua Empresa'
    mensagem_texto = MIMEText(texto, 'plain')
    mensagem.attach(mensagem_texto)

    # Anexando a imagem
    with open('caminho_da_imagem.png', 'rb') as arquivo:
        imagem = MIMEImage(arquivo.read())
        imagem.add_header('Content-ID', '<imagem>')
        mensagem.attach(imagem)

    # Construindo o conteúdo HTML do e-mail
    conteudo_html = f'''
        <html>
            <body>
                <p>Olá {nome}!</p>
                <p>Aqui está a sua chave de acesso: {chave_acesso}</p>
                <p>Atenciosamente,<br>Sua Empresa</p>
                <p><img src="cid:imagem" alt="Imagem incorporada"></p>
            </body>
        </html>
    '''
    mensagem_html = MIMEText(conteudo_html, 'html')
    mensagem.attach(mensagem_html)

    # Estabelecendo conexão com o servidor SMTP
    servidor = smtplib.SMTP(servidor_smtp, porta_smtp)
    servidor.starttls()
    servidor.login(usuario, senha)

    # Enviando o e-mail
    servidor.send_message(mensagem)

    # Encerrando a conexão com o servidor SMTP
    servidor.quit()

# Lista de destinatários, nomes e chaves de acesso
destinatarios = ['email1@example.com', 'email2@example.com', 'email3@example.com']
nomes = ['João', 'Maria', 'José']
chaves_acesso = ['chave1', 'chave2', 'chave3']

# Enviando e-mails individuais
for destinatario, nome, chave_acesso in zip(destinatarios, nomes, chaves_acesso):
    enviar_email(destinatario, nome, chave_acesso)

print('E-mails enviados com sucesso!')
