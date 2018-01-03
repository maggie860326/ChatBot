import sys
from io import BytesIO

import telegram

from flask import Flask, request, send_file

from fsm import TocMachine


API_TOKEN = '545806002:AAHu7X4MaqyXGY5A-GhD4n4Gjdj6ShATEEs'
WEBHOOK_URL = 'https://9abede3c.ngrok.io/hook'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)

machine = TocMachine(
    states=[
        'S','intro','Q1','Q2','Q3','Q4','Q5','Q6','Q7','Q8','Q9','Q10','Q11','Q12','Q13','Q14','Q15','Q16','Q17','Q18','Q19','Q20','Q21','finish'
    ],
    transitions=[
        {
            'trigger': 'next',
            'source': 'S',
            'dest': 'intro'
        },
        {
            'trigger': 'next',
            'source': 'intro',
            'dest': 'Q1',
            'conditions': 'start_question'
        },
        {
            'trigger': 'next',
            'source': 'Q1',
            'dest': 'Q2',
            'conditions': 'answer'
        },
        {
            'trigger': 'next',
            'source': 'Q2',
            'dest': 'Q3',
            'conditions': 'answer'
        },
        {
            'trigger': 'next',
            'source': 'Q3',
            'dest': 'Q4',
            'conditions': 'answer'
        },
        {
            'trigger': 'next',
            'source': 'Q4',
            'dest': 'Q5',
            'conditions': 'answer'
        },
        {
            'trigger': 'next',
            'source': 'Q5',
            'dest': 'Q6',
            'conditions': 'answer'
        },
        {
            'trigger': 'next',
            'source': 'Q6',
            'dest': 'Q7',
            'conditions': 'answer'
        },
        {
            'trigger': 'next',
            'source': 'Q7',
            'dest': 'Q8',
            'conditions': 'answer'
        },
        {
            'trigger': 'next',
            'source': 'Q8',
            'dest': 'Q9',
            'conditions': 'answer'
        },
        {
            'trigger': 'next',
            'source': 'Q9',
            'dest': 'Q10',
            'conditions': 'answer'
        },
        {
            'trigger': 'next',
            'source': 'Q10',
            'dest': 'Q11',
            'conditions': 'answer'
        },
        {
            'trigger': 'next',
            'source': 'Q11',
            'dest': 'Q12',
            'conditions': 'answer'
        },
        {
            'trigger': 'next',
            'source': 'Q12',
            'dest': 'Q13',
            'conditions': 'answer'
        },
        {
            'trigger': 'next',
            'source': 'Q13',
            'dest': 'Q14',
            'conditions': 'answer'
        },
        {
            'trigger': 'next',
            'source': 'Q14',
            'dest': 'Q15',
            'conditions': 'answer'
        },
        {
            'trigger': 'next',
            'source': 'Q15',
            'dest': 'Q16',
            'conditions': 'answer'
        },
        {
            'trigger': 'next',
            'source': 'Q16',
            'dest': 'Q17',
            'conditions': 'answer'
        },
        {
            'trigger': 'next',
            'source': 'Q17',
            'dest': 'Q18',
            'conditions': 'answer'
        },
        {
            'trigger': 'next',
            'source': 'Q18',
            'dest': 'Q19',
            'conditions': 'answer'
        },
        {
            'trigger': 'next',
            'source': 'Q19',
            'dest': 'Q20',
            'conditions': 'answer'
        },
        {
            'trigger': 'next',
            'source': 'Q20',
            'dest': 'Q21',
            'conditions': 'answer'
        },
        {
            'trigger': 'next',
            'source': 'Q21',
            'dest': 'finish',
            'conditions': 'answer'
        },
        {
            'trigger': 'next',
            'source': ['Q1','Q21','finish'],
            'dest': 'intro',
            'conditions': 'restart'
        }
    ],
    initial='S',
    auto_transitions=False,
    show_conditions=True
)



def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    machine.next(update)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')


if __name__ == "__main__":
    _set_webhook()
    app.run()
