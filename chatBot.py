import time,datetime
import telepot
from telepot.loop import MessageLoop
import os

step = 0
answer_dict = {}
bot = telepot.Bot('Token')
greetings = ['Ola','Oi','Oie','Hi','Hello']
phrase = ''

def getAnswer(chat_id, msg):
    F = open('ans_quest.txt', 'r')
    for line in F:
        col = line.split("\" ")
        phrase = col[0]
        answer = col[1]
        answer_dict[phrase] = answer
    F.close()
    a = answer_dict.keys()
    if msg in a:
        bot.sendMessage(chat_id,  answer_dict[msg])
    else:
        bot.sendMessage(chat_id, 'Eu ainda nao sei como responder a essa pergunta, voce poderia me ajudar? Digite S ou N.')
     

def addAnswer(phrase, answer):
    F = open('ans_quest.txt', 'a')
    F.write('{}" {}\n'.format(phrase, answer))
    F.flush()
    F.close()

def action(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print('Received: %s' % command)
    global step
    global phrase

    if command == '/start':
        bot.sendMessage(chat_id,str("Obrigado por me utilizar, pergunte o que quiser! E quando eu nao puder responder, por favor, me ajude! Ainda estou em fase de desenvolvimento, meu criador se chama Leonardo Waite. :D"))

    elif command == '/time':
        now = datetime.datetime.now()
        bot.sendMessage(chat_id, now.strftime("%H:%M"))

    elif command in greetings:
        bot.sendMessage(chat_id, str("Ola!!"))

    elif command == 'S':
        bot.sendMessage(chat_id, 'Por favor, digite sua resposta.')
        step = 1
   
    elif step == 1 and command != None:
        addAnswer(phrase, command)
        bot.sendMessage(chat_id, 'Obrigado, sua resposta foi salva!')
        step = 0
        phrase = ''
  
    elif command == 'N':
        bot.sendMessage(chat_id, 'Que pena, adoraria ler sua resposta :(')

    else:
        getAnswer(chat_id, command)
      #  phrase = bot.getUpdates()[-1]['message']['text']
        phrase = command 

def main():
    MessageLoop(bot, action).run_as_thread()
    while 1:
        time.sleep(10)

if __name__ == '__main__':
    main()
