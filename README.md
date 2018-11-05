# Hello! And Welcome to my Facebook Messenger Chat Parser!
This is a basic script, designed to allow a user who downloads their Facebook data the ability to see the stats of each user in the chat they choose to download.

## How to Use
**For simplicity, it is assumed the user understands what Python is.**

### Windows
#### Step One
Download the source code of this repository from releases
![image](https://image.ibb.co/jBP7k0/download.png)
*You may choose tar.gz, but for windows most users will recognize zip*
#### Step Two
Etc must edit on windows with this info

### Linux
#### Step One
Download the source code of this repository from releases
![image](https://image.ibb.co/jBP7k0/download.png)
*You can choose zip or tar.gz, your choice they are both the same*
#### Step Two
##### Part One
In Terminal navigate to the directory you have unzipped the file
![image](https://image.ibb.co/dwUjXf/step-One-Linux.png)
*Navigation command is cd. Use tab for autocompletion or if you do not understand the command, please learn it. It is a very commonly used command*
##### Part Two
Type `python3 main.py` (*Note the 3 is only necessary if you have two versions of python*) in the same directory as the directory you have chosen.
![image](https://image.ibb.co/mP74Xf/step-Two-Linux.png)
*Parsing of the file should take less than a minute for most individuals*
![image](https://image.ibb.co/no7tQ0/step-Three-Linux.png)

#### Step Three
Navigate to your directory and open the file
![image](https://image.ibb.co/m0CtQ0/linux-File.png)
*Distro shown in this tutorial is elementaryOS, but this should work for every Linux Distro*

# How to get Messenger Data
For this program it requires a message.html file to be in the directory with `main.py`. This file is available for download from Facebook through a certain set of steps.
## Step One - Login to Facebook
You can do this :)
## Step Two - Go to Settings
![image](https://image.ibb.co/daSGdL/facebook.png)\
#### Look at the Helpful Upper Bar
![image](https://image.ibb.co/ke4wdL/helpful-Bar.png)
#### Go to Your Facebook Information
Select `Download Your Information`
![image](https://image.ibb.co/mq3BCf/download-Info.png)
#### (Optional) Deselect All Items
Press `Deselect All` to only download messenger data in the next step
![image](https://image.ibb.co/jxddsf/deselect.png)
#### Download Messenger Data
Select Messenger Data's Check Mark
![image](https://image.ibb.co/e4BL50/select-This.png)
#### Select Create File
![image](https://image.ibb.co/f7XGdL/press-This.png)
#### Wait for your File
![image](https://image.ibb.co/gA2GdL/confirmation.png)

## Step Three - Get Your File
Once your file is done, you should receive an email from Facebook.

image

#### Download the Zip file from Facebook
(**Warning - It could be massive depending on how many images/videos you and your friends send on Messenger**)

image

#### Extract the Zip File somewhere
Anywhere will work. Just remember to navigate there using Console/Terminal.

image
#### Select Any One of Your Numerous Chats to Parse
I personally went with what I knew was my biggest chat. (>360k messages).

image 

Grab that HTML file, put it in the same directory as `main.py` and run that baby.

# Thank You
Thank you for reading everything! Many people don't read instructions and instantly come to the developers complaining, so thank you for being proactive.

If you would like to help, go ahead and fork it. I know this isn't complete, and there are plenty of other things I can continue to parse from the file that I have yet to implement.

***Have this Happy Fox for making it all the way down***
![image](http://i.imgur.com/WhZThdw.jpg)
