
from flask import Flask, render_template, request
from flask_socketio import SocketIO, send
from bs4 import BeautifulSoup
from write import write_csv
import requests, time

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')

@app.route('/', methods=['GET', 'POST'])
def home():
    '''
    Home page of our app
    '''
    return render_template('index.html')

@socketio.on('message')
def handle_message(data):

    '''
    This function receives necessary data from our HTML search input then sends new data via socket...
    ...to the main JavaScript file 
    '''

    pages = 0
    while pages <= 20:

        web = requests.get(f'https://www.google.com/search?q={data}&rlz=1C1CHZN_enRS961RS961&ei=ZCwTY6T1LIGdkwWfoaewAg&start={pages}&sa=N&ved=2ahUKEwikt5CBtfj5AhWBzqQKHZ_QCSYQ8tMDegQIAhA7&biw=1722&bih=871&dpr=1')

        soup = BeautifulSoup(web.text, 'lxml')

        all_text = soup.select('h3')
        all_web = soup.find_all('div', class_='BNeawe UPmit AP7Wnd')

        for (t, w) in zip(all_text, all_web):
            all_data = t.text + '+' + w.text
            write_csv((t.text, w.text))
            send(all_data)
            time.sleep(2)
            
        pages += 10

if __name__ == '__main__':
    socketio.run(app)