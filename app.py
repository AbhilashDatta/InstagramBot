from flask import Flask, render_template, request
from BOT import Bot
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    req = request.args  
    credentials_in = False
        
        
    if 'username' in req.keys() and 'password' in req.keys() and 'dm' in req.keys() and 'message' in req.keys():
        username = req['username']
        password = req['password']
        
        bot = Bot()
        bot.driver.maximize_window()
        bot.login(username, password)
        bot.multiple_dm_followers(req['message'])
        bot.logout()

    if 'username' in req.keys() and 'password' in req.keys() and 'retrieve' in req.keys():
        username = req['username']
        password = req['password']
        
        bot = Bot()
        bot.driver.maximize_window()
        bot.login(username, password)
        bot.retrieve_messages_from_inbox(tolerance=2)
        bot.logout()

    if 'username' in req.keys() and 'password' in req.keys() and 'share' in req.keys():
        username = req['username']
        password = req['password']
        
        bot = Bot()
        bot.driver.maximize_window()
        bot.login(username, password)
        bot.share_latest_post()
        bot.logout()

    # print(req)
    return render_template("index.html")