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
##### Extract Anywhere in Windows

![image](https://image.ibb.co/gwQmxf/save-Location.png)

*message.html should be placed here as well. Do not worry if most of the files above are not there, I have many test files in my directory*

##### Open PowerShell `Windows Key` + `X`, Press `I`.

![image](https://image.ibb.co/eqsAOL/windowsX.png)

##### Navigate to the directory you have selected (`cd <Directory>`)

![image](https://image.ibb.co/j8mFq0/cd-Directory.png)

##### Type into Shell `python main.py` (*Make sure you have message.html in the same directory!*)

![image](https://image.ibb.co/gfCYcf/runFile.png)

**If you get an error at this step, run this command to install beautifulsoup4:**

`python -m pip install beautifulsoup4`
#### Step Three
Navigate to the directory and open `messenger_stats.txt`

![image](https://image.ibb.co/e64PiL/stats.png)

#### Enjoy!

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

**If you get an error at this step, run this command to install beautifulsoup4:**

`python3 -m pip install beautifulsoup4`

![image](https://image.ibb.co/mP74Xf/step-Two-Linux.png)

*Parsing of the file should take less than a minute for most individuals*
![image](https://image.ibb.co/no7tQ0/step-Three-Linux.png)

#### Step Three
Navigate to your directory and open the file
![image](https://image.ibb.co/m0CtQ0/linux-File.png)

*Distro shown in this tutorial is elementaryOS, but this should work for every Linux Distro*

## MacOS
I don't have a mac, but I assume most of the steps I listed for Linux should 100% work for Mac. (Both use Terminal)

# How to get Messenger Data
For this program it requires a message.html file to be in the directory with `main.py`. This file is available for download from Facebook through a certain set of steps.
## Step One - Login to Facebook
You can do this :)
## Step Two - Go to Settings
![image](https://image.ibb.co/daSGdL/facebook.png)

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

#### Select Any One of Your Numerous Chats to Parse
I personally went with what I knew was my biggest chat. (>360k messages).

image

Grab that HTML file, put it in the same directory as `main.py` and run that baby.

image

# Example Output
An Example of the output to expect from the program

(Names were Redacted, replaced with AAA)

```
File Generated Using Nate's Messenger Parser (https://github.com/artyomos/messenger-parser)
Version 1.0.0

Messenger Chat: The Know Nothing Squad

Total Messages: 594
Word Count: 2753
Character Count: 9940
Images Sent: 82
Gifs Sent: 0
Videos Sent: 0
Audio Files Sent: 0
Links Sent: 4
Reactions Given: 13
	👍:7	👎:2	😢:2	😆:1	😠:1
The 50 Most Common Words:
	1. AAA (34x)	2. Do (31x)	3. AAA (31x)	4. Yeah (20x)	5. Can (20x)	6. What (20x)	7. Are (19x)	8. Guys (18x)	9. Lab (18x)	10. When (17x)	11. AAA (17x)	12. Ok (15x)	13. 8 (15x)	14. Did (15x)	15. No (14x)	16. Work (14x)	17. Have (13x)	18. Get (13x)	19. 7 (13x)	20. Your (12x)	21. Right (12x)	22. Yes (11x)	23. Now (11x)	24. Got (11x)	25. Or (10x)	26. There (10x)	27. Mean (10x)	28. How (10x)	29. Lol (9x)	30. Me (9x)	31. Wrong (9x)	32. Chem (9x)	33. Know (9x)	34. AAA (9x)	35. Send (8x)	36. Should (8x)	37. Not (8x)	38. Up (8x)	39. 5 (8x)	40. Idk (8x)	41. AAA (8x)	42. Then (8x)	43. 6 (8x)	44. Want (7x)	45. Answer (7x)	46. Oh (7x)	47. Same (7x)	48. 3 (7x)	49. Them (7x)	50. Literally (7x)

Stats by Member:

AAA

Total Messages: 206
Word Count: 853
Character Count: 3050
Images Sent: 28
Gifs Sent: 0
Videos Sent: 0
Audio Files Sent: 0
Links Sent: 0
Reactions Given: 0

Reactions Received: 5
	👍:2	👎:1	😆:1	😠:1
The 25 Most Common Words:
	1. AAA (28x)	2. Yeah (13x)	3. AAA (13x)	4. Do (11x)	5. Are (9x)	6. AAA (8x)	7. AAA (7x)	8. AAA (7x)	9. What (7x)	10. Guys (6x)	11. Ok (6x)	12. Cause (6x)	13. When (6x)	14. Can (6x)	15. Your (6x)	16. Have (5x)	17. Get (5x)	18. 8 (5x)	19. Wrong (5x)	20. No (4x)	21. Sure (4x)	22. Now (4x)	23. How (4x)	24. Work (4x)	25. Eating (4x)

AAA

Total Messages: 168
Word Count: 825
Character Count: 2995
Images Sent: 33
Gifs Sent: 0
Videos Sent: 0
Audio Files Sent: 0
Links Sent: 2
Reactions Given: 3
	👍:2	👎:1
Reactions Received: 8
	👍:5	😢:2	👎:1
The 25 Most Common Words:
	1. No (8x)	2. Have (6x)	3. Yes (6x)	4. Lol (5x)	5. 7 (5x)	6. What (5x)	7. Solution (5x)	8. When (4x)	9. 27 (4x)	10. Guess (4x)	11. One (4x)	12. 3 (4x)	13. As (4x)	14. Did (4x)	15. They (4x)	16. Guide (4x)	17. Guys (4x)	18. Or (3x)	19. 14 (3x)	20. Can (3x)	21. Thats (3x)	22. Got (3x)	23. Had (3x)	24. Question (3x)	25. Do (3x)

AAA

Total Messages: 220
Word Count: 1075
Character Count: 3895
Images Sent: 21
Gifs Sent: 0
Videos Sent: 0
Audio Files Sent: 0
Links Sent: 2
Reactions Given: 10
	👍:5	😢:2	👎:1	😆:1	😠:1
Reactions Received: 0

The 25 Most Common Words:
	1. AAA (23x)	2. Do (17x)	3. Lab (12x)	4. Can (11x)	5. Did (10x)	6. Work (9x)	7. What (8x)	8. Guys (8x)	9. Right (8x)	10. Yeah (7x)	11. 8 (7x)	12. When (7x)	13. Chem (7x)	14. Mean (7x)	15. Ok (7x)	16. Are (7x)	17. Me (7x)	18. Or (6x)	19. Get (6x)	20. Wait (5x)	21. There (5x)	22. Want (5x)	23. Answer (5x)	24. 5 (5x)	25. Up (5x)
```

# Thank You
Thank you for reading everything! Many people don't read instructions and instantly come to the developers complaining, so thank you for being proactive.

If you would like to help, go ahead and fork it. I know this isn't complete, and there are plenty of other things I can continue to parse from the file that I have yet to implement.

***Have this Happy Fox for making it all the way down***
![image](http://i.imgur.com/WhZThdw.jpg)
