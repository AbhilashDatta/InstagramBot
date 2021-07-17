from BOT import Bot
from credentials import username, password

if __name__ == '__main__':
    ''' Feed the program your required data'''

    bot = Bot()
    bot.login('user1', 'pw1')
    bot.dm('abhilash.datta','Hi There')
    bot.follow_user('abhilash.datta')
    bot.like_by_keyword('abhilash.datta', 20)
    bot.group_dm(['abhilash.datta','user2'],'Testing')
    bot.multiple_dm(['abhilash.datta','user2'],'Final Testing')
    bot.retrieve_messages(['abhilash.datta','user2'])
    bot.download_pics('#dog')
    bot.logout()
