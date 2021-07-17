# Instagram Bot
July 14, 2021

<p align="center">
  <img src="InstagramBot.jpg" />
</p>

## Overview
A multifunctionality automated instagram bot that can mass text users, receive and read a message and store it somewhere with user details and much more. Powered by Selenium.

<br>

## Get Started
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

## Multipurpose Bot


<br>

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
bot.follow_user('user')
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

* Retrieve the latest message from multiple user

<p><b> &nbsp &nbsp UPDATE THE IMAGES DIRECTORY WITH SCREENSHOTS TAKEN FROM YOUR COMPUTER</b></p>
    
```
from BOT import Bot
bot = Bot()
bot.login(username, password)
bot.retrieve_messages('user')
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
from __follow_user__ import Follow_user

Follow_user(driver, <username>)
```  
  </li>
  <li> Responding to a Single User: (Achieved) 
<p><b> &nbsp &nbsp UPDATE THE IMAGES DIRECTORY WITH SCREENSHOTS TAKEN FROM YOUR COMPUTER</b></p>
    
```
from __retrieve_messages__ import Retrieve_messages

Retrieve_messages(driver, <username>)
```  
  </li>
  <li> Texting to Multiple Users: (Achieved)

```
from __multiple_dm__ import Multiple_dm

Multiple_dm(driver, [users], <message>)
```  
  </li>
  <li> Creating Group and texting in it: (Achieved)

```
from __group_dm__ import Group_dm 

Group_dm(driver, [users], {message})
```  
  </li>
  <li> Downloading a number of posts with a keyword: (Achieved)

```
from __download_pics__ import Download_pics

Download_pics(driver, {keyword})
```
  </li>
  <li> Liking a number of posts of a user/hashtag: (Achieved)

```
from __like_by_keyword__ import Like_by_keyword

Like_by_keyword(driver, {keyword})
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

Platform: Python files. Virtual Environment using PIPENV.
Libraries: Selenium, Instabot, InstaPy, Time, Pyperclip, Pyautogui, OpenCv, os, wget
Softwares: Windows Chromedriver 
Low-Level Specs: Whole program is built in Object Oriented fashion and Modular structure is followed throughout.
    
