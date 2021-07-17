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
    pip install pipenv
</code></p>
<br>
<li> Installing required libraries and versions </li>
<p><code>
    pipenv install
</code></p>
<br>
<li> Starting the PIP virtual environment </li>
<p><code>
    pipenv shell
</code></p>
<br>


## Functionalities:
<ul>
  <li> Login into Instagram: (Achieved)
    <p><code>
    from __login__ import Login <br>
    Login(driver, {username}, {password})
    </code></p>
    <br>
  </li>
  <li> Texting to a Single User: (Achieved) 
  <p><code>
    from __dm__ import Dm <br>
    Dm(driver, {user}, {message})
    </code></p>
    <br>
  </li>
  <li> Following Users: (Achieved) 
  <p><code>
    from __follow_user__ import Follow_user <br>
    Follow_user(driver, {username})
    </code></p>
    <br></li>
  <li> Responding to a Single User: (Achieved) <p><code>
    from __retrieve_message__ import Retrieve_message <br>
    Retrieve_message(driver, {username})
    </code></p>
    <br></li>
  <li> Texting to Multiple Users: (Achieved)
  <p><code>
    from __multiple_dm__ import Multiple_dm <br>
    Multiple_dm(driver, [users], {message})
    </code></p>
    <br></li>
  <li> Creating Group and texting in it: (Achieved)
  <p><code>
    from __group_dm__ import Group_dm <br>
    Group_dm(driver, [users], {message})
    </code></p>
    <br></li>
  <li> Downloading a number of posts with a keyword: (Achieved)
  <p><code>
    from __download_pics__ import Download_pics <br>
    Download_pics(driver, {keyword})
    </code></p>
    <br></li>
  <li> Liking a number of posts of a user/hashtag: (Achieved)
  <p><code>
    from __like_by_keyword__ import Like_by_keyword <br>
    Like_by_keyword(driver, {keyword})
    </code></p>
    <br></li>
  <li> Logging Out: (Achieved) 
  <p><code>
    from __logout__ import Logout <br>
    Logout(driver)
    </code></p>
    <br></li>
  <li> GUI app: (On the way)</li>
</ul>
