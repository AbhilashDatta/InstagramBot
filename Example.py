from BOT import Bot
from credentials import username, password

if __name__ == '__main__':
    ''' Feed the program your required data'''

    bot = Bot()
    bot.login(username, password)
    bot.dm('abhilash.datta','Hi there')
    bot.follow_user('user')
    bot.like_by_keyword('user', 20)
    bot.group_dm(['abhilash.datta','xxx', 'xxx'],'Testing')
    bot.multiple_dm(['abhilash.datta','xxx', 'xxx'],'Final Testing')
    bot.retrieve_message('abhilash.datta')
    bot.download_pics('#dog')
    bot.logout()
