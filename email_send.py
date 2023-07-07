import smtplib
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def send_email(config, recipient, data, html, image):

	# Construindo a message do e-mail
	message = MIMEMultipart()
	message['Subject'] = 'Teste BOT [5]'  # Assunto do e-mail
	message['From'] = config['usuario']  # Remetente
	message['To'] = recipient  # Destinatário

	# Texto do e-mail
	# texto = f'Olá {data[0]}!\n\nSua chave de acesso é: {data[1]}\n\nAtenciosamente,\nSua Empresa'
	# message_texto = MIMEText(texto, 'plain')
	# message.attach(message_texto)

	# Anexando a imagem
	# with open('image.jpg', 'rb') as arquivo:
	# 	imagem = MIMEImage(arquivo.read())
	# 	print(type(imagem))
	# 	imagem.add_header('Content-ID', '<imagem>')
	message.attach(image)

	# with open('email_body.html', encoding='utf-8') as file:
	# 	conteudo_html = file.read().format(*data)
	# 	# print(conteudo_html)
	message_html = MIMEText(html.format(*data), 'html')
	message.attach(message_html)

	# Estabelecendo conexão com o servidor SMTP
	servidor = smtplib.SMTP(config['servidor_smtp'], config['porta_smtp'])
	servidor.starttls()
	servidor.login(config['usuario'], config['senha'])

	# Enviando o e-mail
	servidor.send_message(message)

	# Encerrando a conexão com o servidor SMTP
	servidor.quit()

config = {}
data = {}
image = None
html = ''

try:
	with open('email.config') as file:
		config = json.loads(file.read())
except:
	print('''
		Não foi encontrado o arquivo de configuração: "email.config"
		{
		"servidor_smtp": "smtp.gmail.com",
		"porta_smtp": 587,
		"usuario": "seu_email@gmail.com",
		"senha": "senha_de_app"
		}    
	''')
	quit()

try:
	with open('email.data') as file:
		data = json.loads(file.read())
except:
	print('''
		Não foi encontrado o arquivo de dados: "email.data"
		{
		"email_destinatario1": ["dados","do","destinatario"]
		"email_destinatario2": ["dados","do","destinatario"]
		"email_destinatario3": ["dados","do","destinatario"]
       		...
		}    
	''')
	quit()

with open('image.jpg', 'rb') as arquivo:
	image = MIMEImage(arquivo.read())
	image.add_header('Content-ID', '<imagem>')
	

with open('email_body.html', encoding='utf-8') as file:
	html = file.read()

# Enviando e-mails individuais

for recipient in data:
	send_email(config, recipient, data[recipient], html, image)

print('E-mails enviados com sucesso!')
