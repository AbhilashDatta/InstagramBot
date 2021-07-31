from instabot import Bot 
# from credentials import username, password

def Upload_post(post_path, caption):
    bot = Bot()
    bot.login(username = 'instabot3228', password = 'igbot3228')
    bot.upload_photo(post_path, caption)
    bot.logout(username = username)

# Upload_post('Drive_downloads/instagrambot.jpg', 'igbot logo')