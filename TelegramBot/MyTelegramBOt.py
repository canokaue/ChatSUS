#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to send timed Telegram messages.
This Bot uses the Updater class to handle the bot and the JobQueue to send
timed messages.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Alarm Bot example, sends a message after a set time.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging

from telegram.ext import Updater, CommandHandler , PrefixHandler

import json
import requests
import datetime
from collections import defaultdict
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)



##----------------------------------------------------------------------------------------------------------------------------------------------------##
##-----------------------This part of the code is meant to get the information from the database for processing it------------------------------------##
##----------------------------------------------------------------------------------------------------------------------------------------------------##
def FormatDate(date):
    #2018-04-30T11:30:45.148Z
    date_time_obj = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%fZ')
    
    return date_time_obj

def FormatDateText(date):
    #2018-04-30T11:30:45.148Z
    date_time_obj = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%fZ')
    
    return date_time_obj

def GetUserListaEspera(documento, tipo):
    if tipo == 'cpf':
        _tipo = 0
    else:
        _tipo = 1
        
    url = 'https://listadeespera.saude.sc.gov.br/filas/fila/usuarios/hackathon/doc/{_tipo}/byDocumento/{documento}'.format(**locals())
    PessoaReq = requests.get(url=url)
    if PessoaReq.status_code == 200:
        #print(PessoaReq.json())
        #print(len(PessoaReq.json()))
        procedimentos = []
        for item in PessoaReq.json():
            procedimentos.append(item['dataEntrada'])
        print("Agendados em", procedimentos)
    else:
        print("Erro get Centrais {0}".format(PessoaReq.status_code))

def GetUserAgendado(documento, tipo):
    url = 'https://listadeespera.saude.sc.gov.br/agendados/byCnes/6003044/fila/0701010/usuarios/byTipoFila/0/byIbge/4208203'
    resp = requests.get(url=url)
    #print(resp.status_code)
    UserAgendado = resp.json()
    for item in data3:
        if item[tipo] == documento:
            print("encontrei a pessoa")
            print(item.keys())
            print("Expedido em {0}".format(item['dataExecucao']))

def GetAllUser(documento, tipo):
    if tipo == 'cpf':
        _tipo = 0
    else:
        _tipo = 1
        
    url = 'https://listadeespera.saude.sc.gov.br/filas/all/usuarios/hackathon/{_tipo}/byDocumento/{documento}'.format(**locals())
    resp = requests.get(url=url)
    status_code = resp.status_code
    if status_code == 200:
        j = resp.json()
        data = defaultdict(list)
        for item in j:
            k = item.keys()
            #print(k)
            
            #print(item)
            if 'posicao' in k:
                data['lista_espera'].append({'dataEntrada': item['dataEntrada'],
                                            'procedimento' : item['descricaoFila'],
                                             'solicitante' : item['nomeEstabSolicitante'],
                                            'posicao' : item['posicao']})
                #Coisas na fila de espera
            elif 'confirmado' in k and item['confirmado'] == 0:
                #Coisas agendadas
                AgendationDate = FormatDate(item['dataExecucao'])
                if AgendationDate < datetime.datetime.now():
                    data['faltou'].append({'dataExecucao': item['dataExecucao'],
                                            'procedimento' : item['descricaoFila'],
                                             'solicitante' : item['descricaoEstabelecimentoSolicitante']})
                    #print("faltou")
                else:
                    data['agendado'].append({'dataExecucao': item['dataExecucao'],
                                            'procedimento' : item['descricaoFila'],
                                             'solicitante' : item['descricaoEstabelecimentoSolicitante']})
                #if item['dataExecucao'] < datetime.now():
                    #faltou
            elif 'confirmado' in k and item['confirmado'] == 1:
                data['feito'].append({'dataExecucao': item['dataExecucao'],
                                            'procedimento' : item['descricaoFila'],
                                             'solicitante' : item['descricaoEstabelecimentoSolicitante']})
                #Executado
            else:
                print("epaaaaa")
        print(data)
    else:
        print("Erro get {0}".format(status_code))

    return data


##----------------------------------------------------------------------------------------------------------------------------------------------------##
##-----------------------End DataBase Processing----------------------------------------------------------------------------------------------------------##
##----------------------------------------------------------------------------------------------------------------------------------------------------##



##----------------------------------------------------------------------------------------------------------------------------------------------------##
##-----------------------Logical Paths for Chatboot---------------------------------------------------------------------------------------------------##
##----------------------------------------------------------------------------------------------------------------------------------------------------##

def ListaEspera(update,context,TheList):
    #Just message body to be defined
    SizeofList = len(TheList)
    update.message.reply_text('Voce esta inserido em {SizeofList} listas de espera.'.format(**locals()))
    for itens in TheList:
        DataPaciente = FormatDate(itens['dataEntrada']).strftime("%d/%m/%Y %H:%M")
        Nafila = itens['posicao']
        procedimento = itens['procedimento'].upper()
        solicitante = itens['solicitante'].upper()
        t = "Processo marcado em {DataPaciente} para o procedimento {procedimento} ".format(**locals())+\
                "no posto de saúde {solicitante}. Sua posição na fila é {Nafila}".format(**locals())
        
        update.message.reply_text(t)
    #Get Feedback -- a dor ainda lhe incomoda ? Piorou ? Teve alguma recomendação?

def ListaAgendamentos(update,context,TheList):
    #Concientization part first messages 
    NumbSchedule = len(TheList)
    update.message.reply_text("Você esta agendado em {NumbSchedule}".format(**locals()))
    update.message.reply_text(TheList)


    #TimerFunc and options

def Faltas(TheList):
    #Message body messages 


    #TimerFunc and options



    pass
def Feito(TheList):
    #Congratulations
    pass

def Mockup():


    Tempo = datetime.datetime.now() + datetime.timedelta(days=1)
    DadosAgendados = defaultdict(list)

    DadosAgendados['agendado'].append({'dataExecucao': Tempo.strftime("%d/%m/%Y %H:%M"),
                            'procedimento' : 'PROCEDIMENTO MOCKUP ',
                            'solicitante' : 'MOCKUPSOLICITANTE'})
    return DadosAgendados

##----------------------------------------------------------------------------------------------------------------------------------------------------##
##-----------------------End Logical Paths Processing----------------------------------------------------------------------------------------------------------##
##----------------------------------------------------------------------------------------------------------------------------------------------------##
# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    update.message.reply_text('Insira seu dado  /cpf ou /cns')


def alarm(context):
    """Send the alarm message."""
    job = context.job
    context.bot.send_message(job.context, text='Beep!')


def set_timer(update, context):
    """Add a job to the queue."""
    chat_id = update.message.chat_id
    try:
        # args[0] should contain the time for the timer in seconds
        due = int(context.args[0])
        if due < 0:
            update.message.reply_text('Sorry we can not go back to future!')
            return

        # Add job to queue and stop current one if there is a timer already
        if 'job' in context.chat_data:
            old_job = context.chat_data['job']
            old_job.schedule_removal()
        new_job = context.job_queue.run_once(alarm, due, context=chat_id)
        context.chat_data['job'] = new_job

        update.message.reply_text('Timer successfully set!')

    except (IndexError, ValueError):
        update.message.reply_text('Usage: /set <seconds>')


def unset(update, context):
    """Remove the job if the user changed their mind."""
    if 'job' not in context.chat_data:
        update.message.reply_text('You have no active timer')
        return

    job = context.chat_data['job']
    job.schedule_removal()
    del context.chat_data['job']

    update.message.reply_text('Timer successfully unset!')


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)



def getCPF(update,context):
    cpf = context.args[0]
    #update.message.reply_text('Your custom callback youngpadawan ' + cpf)
    UserInfo = GetAllUser(cpf,'cpf')
    update.message.reply_text(UserInfo['lista_espera']) 

def getCNS(update,context):
    cns = context.args[0]
    #update.message.reply_text('Your custom callback youngpadawan ' + cns)
    DadosAgendados = Mockup()
    UserInfo = GetAllUser(cns,'cns')
    if UserInfo['lista_espera']:
        ListaEspera(update,context,UserInfo['lista_espera'])
    if DadosAgendados:
         ListaAgendamentos(update,context,DadosAgendados)
    # if UserInfo['faltou']:
    #      pass
    # #     #Faltas(UserInfo['agendado'])
    # if UserInfo['feito']:
    #      Feito(Userinfo['feito'])



    #Getmock();

# MESSAGE BOT


def main():
    """Run bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary

    updater = Updater("949664089:AAG2nEofCePbJo2n6y08_MOySrsUPEU3wCw", use_context=True)
    documento = {
       'cpf': '34',
       'cns': '234'
    }

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    #Defining handler for cpf and cns
    PrefixHandler(['/','/'], ['cpf','cns'], getCPF)

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", start))
    dp.add_handler(CommandHandler("set", set_timer,
                                  pass_args=True,
                                  pass_job_queue=True,
                                  pass_chat_data=True))
    dp.add_handler(CommandHandler("unset", unset, pass_chat_data=True))
    dp.add_handler(CommandHandler("cpf",getCPF))
    dp.add_handler(CommandHandler("cns",getCNS))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Block until you press Ctrl-C or the process receives SIGINT, SIGTERM or
    # SIGABRT. This should be used most of the time, since start_polling() is
    # non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()