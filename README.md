<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">PYTHON MUSIC BOT</h3>
  <p align="center">
    A music bot for you and your friends :)
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

This is an in progress python music bot that will stream music onto a group chatting platform known as discord. 
This project was written fully in python and by my self that I will be updating as I go.

Here's why:
* Personal use
* Allows me and my friends to listen to music together
* Many of the popular music bots that work with youtube are being taken down
* Project experience (duh)
* Learning experience 

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

This is an guide on how to set up the bot on your local machine.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is a list things you need to use the bot and how to install them.

* [Making a bot, getting its unique token and inviting it to your server.
  Refer to this link (click me) if you know how to make a discord bot](https://discordpy.readthedocs.io/en/stable/discord.html)
* After you have your bot created go to your developer portal and go to the bot section and enable *SERVER MEMBERS INTENT* and *MESSAGE CONTENT INTENT*.
* This git repo has a requirements.txt file becasue the bots uses a fair amount of libaries. If your not a beginner you will know what to do with this file.
* For the beginners I will show you how to manually install all the libaries. 
* Open up your terminal (cmd) and type in these commands:
 
  ```sh
  pip install yt_dlp
  pip install validators
  pip install discord
  pip install youtube_search
  pip install PyNaCl
  ```

### Installation

This is a quick guide on how to get the bot running on your own device. Note that once done these steps
the bot will only run while your pc or laptop is on unless you are using a server to host it.
One more thing as mentioned above it's still a work in progress and does not work perfectly. I am
Aware of most of the bugs and I am updating it as often as I can.

1. Have a bot on discord that is ready to use along with its unique token
2. Clone the repo
   ```sh
   git clone https://github.com/Adib-Nasreddine/Python-Music-Bot
   ```
3. Put in your unique bot token which will be at the bottom of the code
4. Finally just run the code on your pc or laptop

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage

The bot has a few commands that are common with any music bot

1. play: This will play a song and it takes youtube links or just a name of a song
  ```sh
  $play <song>
  ```
2. skip: This will skip the current song if there is a song next in queue
  ```sh
  $skip
  ```
3. pause: will pause the music
  ```sh
  $pause
  ```
4. resume: will resume the music
  ```sh
  $resume
  ```
5. stop: will stop the bot (disconnect) and reset the queue
  ```sh
  $stop
  ```
6. queue: will display the song queue
  ```sh
  $queue
  ```


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Volume mixing (All sounds have the same respective volume)
- [ ] Error handling (more)
- [ ] Youtube Playlists 
- [ ] Spotify & Sounds cloud Integeration
- [ ] Clean up code (in progress)
- [ ] fix youtube links embeds showing the wrong song
- [ ] allow bot to be dragged while playing and continue to play 
  

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

Id prefer not accept contributions becasue this is a solo project but I dont mind users sending me unique bugs they have found.

If you have a new bug or glitch that you have found feel free to contact me with the bug and why it's happening 

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Email - eddynasreddine@hotmail.com

Project Link: [Python Music Bot](https://github.com/Adib-Nasreddine/Python-Music-Bot)

Linkdin: [Adib-Nasreddine](https://www.linkedin.com/in/adib-nasreddine-938466233/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<p align="right">(<a href="#readme-top">back to top</a>)</p>
