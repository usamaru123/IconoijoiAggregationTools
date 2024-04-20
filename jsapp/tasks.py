import json
import requests
from django.core.mail import  send_mail
from django.template.loader import get_template

import jsproject.settings as settings


def send_email(message):
    subject = 'データ更新'
    from_address = 'usamaru.server@gmail.com'
    to_address = ['usamaru.server@gmail.com']
    send_mail(subject,message,from_address,to_address)

def send_slack_message(message):
    requests.post(settings.SLACK_WEBHOOK_ENDPOINT,
                  data=json.dumps({
                      'text':message,
                      'username':u'me',
                      'icon_emoji':u':ghost',
                      'link_names':1,
                  }))
    
def get_message(item,action):
    template = get_template('app/message.txt')
    context = {
        "item":item,"action":action,
    }
    message = template.render(context)
    return message

def send_notification(item,action):
    message = get_message(item,action)
    send_slack_message(message)
    send_email(message)

    