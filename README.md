# Instagram Bot :robot:
July 14, 2021

<p align="center">
  <img src="InstagramBot.jpg" />
</p>

## Overview 👍
A multifunctionality automated instagram bot that can mass text users, receive and read a message and store it somewhere with user details and much more. Powered by Selenium.

 [![](https://camo.githubusercontent.com/2fb0723ef80f8d87a51218680e209c66f213edf8/68747470733a2f2f666f7274686562616467652e636f6d2f696d616765732f6261646765732f6d6164652d776974682d707974686f6e2e737667)](https://python.org)




## Get Started 🤞
<li> PIPENV: For virtual environment </li>
<p><code>
  $  pip install pipenv
</code></p>
<br>
<li> Installing required libraries and versions </li>
<p><code>
  $  pipenv install
</code></p>
<br>
<li> Starting the PIP virtual environment </li>
<p><code>
  $  pipenv shell
</code></p>
<br>

## Multipurpose Bot 🛰️


* Login-out using credentials 
```
from BOT import Bot
bot = Bot()
bot.login(username, password)
bot.logout()
```

<br>

* Direct Message anyone
```
from BOT import Bot
bot = Bot()
bot.login(username, password)
bot.dm('user','Hi there')
bot.logout()
```

<br>

* Follow another user
```
from BOT import Bot
bot = Bot()
bot.login(username, password)
bot.follow_users(['user1','user2'])
bot.logout()
```

<br>

* Like a number of posts by a user/hashtag
```
from BOT import Bot
bot = Bot()
bot.login(username, password)
bot.like_by_keyword(keyword, numOfPosts)
bot.logout()
```

<br>

* Create a group and direct message in it
```
from BOT import Bot
bot = Bot()
bot.login(username, password)
bot.group_dm(['user1','user2', 'user3'],'Final Testing')
bot.logout()
```

<br>

* Direct Message multiple users
```
from BOT import Bot
bot = Bot()
bot.login(username, password)
bot.multiple_dm(['user1','user2', 'user3'],'Final Testing')
bot.logout()
```

<br>

* Direct Message multiple users from a csv file
```
from BOT import Bot
bot = Bot()
bot.login(username, password)
# if csv file doesn't contains message column
bot.multiple_dm_from_csv('path to csv file','general message')
# else
bot.multiple_dm_from_csv('path to csv file') 
bot.logout()
```

<br>

* Retrieve the latest message from multiple user

<p><b> &nbsp &nbsp UPDATE THE IMAGES DIRECTORY WITH SCREENSHOTS TAKEN FROM YOUR COMPUTER</b></p>
<p><b> &nbsp &nbsp UPDATE THE DATABASE CREDENTIALS IN db_credentials.py FILE</b></p>
```
from BOT import Bot
bot = Bot()
bot.login(username, password)
bot.retrieve_messages([users])
bot.logout()
```

<br>

* Retrieve the latest message from multiple user in a csv file

<p><b> &nbsp &nbsp UPDATE THE IMAGES DIRECTORY WITH SCREENSHOTS TAKEN FROM YOUR COMPUTER</b></p>
<p><b> &nbsp &nbsp UPDATE THE DATABASE CREDENTIALS IN db_credentials.py FILE</b></p>
    
```
from BOT import Bot
bot = Bot()
bot.login(username, password)
bot.retrieve_messages_from_csv('path to csv file')
bot.logout()
```

<br>

* Download posts by a keyword
```
from BOT import Bot
bot = Bot()
bot.login(username, password)
bot.download_pics(keyword)
bot.logout()
```

<br>

## Individual Functionalities:
<ul>
  <li> Login into Instagram: (Achieved)
    
```
from __login__ import Login

Login(driver, <username>, <password>)
```


  </li>
  <li> Texting to a Single User: (Achieved) 

```
from __dm__ import 

Dm(driver, <user>, <message>)
```

  </li>
  <li> Following Users: (Achieved) 

```
from __follow_users__ import Follow_users

Follow_users(driver, ['user1','user2'])
```  
  </li>
  <li> Retrieving messages from single/multiple user(s): (Achieved) 
<p><b> &nbsp &nbsp UPDATE THE IMAGES DIRECTORY WITH SCREENSHOTS TAKEN FROM YOUR COMPUTER</b></p>
    
```
from __retrieve_messages__ import Retrieve_messages

Retrieve_messages(driver, [users])
```  
  </li>
  <li> Retrieving messages from single/multiple user(s) with names in a csv file: (Achieved) 
<p><b> &nbsp &nbsp UPDATE THE IMAGES DIRECTORY WITH SCREENSHOTS TAKEN FROM YOUR COMPUTER</b></p>
    
```
from __retrieve_messages_from_csv__ import Retrieve_messages_from_csv

Retrieve_messages_from_csv(driver, 'path to csv file')
```  
  </li>
  <li> Texting to Multiple Users: (Achieved)

```
from __multiple_dm__ import Multiple_dm

Multiple_dm(driver, [users], <message>)
```  
  </li>
  <li> Texting to Multiple Users from a csv file: (Achieved)

```
from __multiple_dm_from_csv__ import Multiple_dm_from_csv

Multiple_dm_from_csv(driver, 'path to csv file', <general message (optional)>)
```  
  </li>
  <li> Creating Group and texting in it: (Achieved)

```
from __group_dm__ import Group_dm 

Group_dm(driver, [users], <message>)
```  
  </li>
  <li> Downloading a number of posts with a keyword: (Achieved)

```
from __download_pics__ import Download_pics

Download_pics(driver, <keyword>)
```
  </li>
  <li> Liking a number of posts of a user/hashtag: (Achieved)

```
from __like_by_keyword__ import Like_by_keyword

Like_by_keyword(driver, <keyword>)
```
  </li>
  <li> Logging Out: (Achieved) 

```
from __logout__ import Logout

Logout(driver)
```
  </li>
  <li> GUI app: (On the way)</li>
</ul>
<br>
    
<b> Platform:</b> Python files. Virtual Environment using PIPENV.
   
<b> Libraries:</b> Selenium, Instabot, InstaPy, Time, Pyperclip, Pyautogui, OpenCv, os, wget
    
<b> Softwares:</b> Windows Chromedriver 
    
<b> Low-Level Specs:</b> Whole program is built in Object Oriented fashion and Modular structure is followed throughout.
