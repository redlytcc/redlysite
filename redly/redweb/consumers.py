from channels import Group
import ast
from .models import Chat

def ws_add(message):
	print('recibida')
	message.reply_channel.send({'accept':True})
	Group('chat').add(message.reply_channel)

def ws_message(message):
	to_model=ast.literal_eval(message.content['text'])
	print(to_model)
	md=Chat(nome=to_model['nome'],text=to_model['msm'])
	md.save()
	Group('chat').send({'text': message.content['text']})

def ws_disconnect(message):
	print('fim')
	Group('chat').discard(message.reply_channel)
