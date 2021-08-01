from BOT import Bot
from time import sleep
from credentials import username, password


if __name__ == '__main__':
    ''' Feed the program your required data'''

    bot = Bot()
    bot.login(username, password)

    ''' Direct Messaging functions '''
    # bot.dm('abhilash.datta', 'hi there')
    # bot.group_dm(['abhilash.datta','user2'],'Testing')
    # bot.multiple_dm(['abhilash.datta','user2'],'Final Testing')
    # bot.multiple_dm_from_db(general_message='db testing')
    # bot.multiple_dm_followers('what category of posts do you like?: \n political \n social \n activism \n history')
    # bot.multiple_dm_followers_of_epicenter('hi')

    ''' Message Retrieval functions '''
    # bot.retrieve_messages(['abhilash.datta','user2'])
    # bot.retrieve_messages_from_csv('users.csv')
    # bot.retrieve_messages_from_inbox(tolerance= 2)

    ''' Utility functions '''
    # bot.follow_users('abhilash.datta')
    # bot.like_by_keyword('abhilash.datta', 20)
    # bot.download_pics('#dog')
    # bot.share_latest_post()
    # bot.share_latest_post_of_epicenter()

    bot.logout()

    