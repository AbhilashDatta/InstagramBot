from bot import Bot
from credentials import username, password

if __name__ == '__main__':
    bot = Bot()
    bot.login(username, password)
    bot.dm('abhilash_datta','Hi there')
    bot.follow_user('avi_1.5')
    bot.like_by_keyword('kartik_murthy', 20)
    bot.group_dm(['abhilash.datta','kartik_murthy', 'divyangnasharma23'],'Final Testing')
    bot.multiple_dm(['abhilash.datta','kartik_murthy', 'divyangnasharma23'],'Final Testing')
    bot.retrieve_message('abhilash.datta')
    bot.download_pics('#dog')
    bot.logout()