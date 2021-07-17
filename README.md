# Instagram Bot
July 14, 2021

<p align="center">
  <img src="InstagramBot.jpg" />
</p>

## Overview
An instagram bot that can mass text users, receive and read a text back and store it somewhere with user details and much more. Exploring options like selenium driver (python API) etc.

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

* Import the bot
```
from BOT import Bot
```

<br>

* Initialize the bot
```
bot = Bot()
```

<br>

* Login using credentials 
```
bot.login(username, password)
```

<br>

* Direct Message anyone
```
bot.dm('user','Hi there')
```

<br>

* Follow another user
```
bot.follow_user('user')
```

<br>

* Like a number of posts by a user/hashtag
```
bot.like_by_keyword(keyword, numOfPosts)
```

<br>

* Create a group and direct message in it
```
bot.group_dm(['user1','user2', 'user3'],'Final Testing')
```

<br>

* Direct Message multiple users
```
bot.multiple_dm(['user1','user2', 'user3'],'Final Testing')
```

<br>

* Retrieve the latest message from a user
```
bot.retrieve_message('user')
```

<br>

* Download posts by a keyword
```
bot.download_pics(keyword)
```

<br>

* Finally Logout
```
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

```
from __retrieve_message__ import Retrieve_message 

Retrieve_message(driver, <username>)
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
