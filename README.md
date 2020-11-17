# Common Following
Find out which Instagram users are followed by the same ones.

## What is it?
Do you want to know who two users follow in common on Instagram? Do you want to know the username of that person who you've seen at a party, but you only know that that person is a friend of other two people? With this bot, developed with **Python** and **Selenium**, you could find out the name of that person, only typing the two Instagram's username that you know.
The bot will find out the users in common, followed by those two usernames.

## Getting Started
I suggest you to use **Linux** and **[Sublime Text](https://www.sublimetext.com/)** as text editor. You can easy install it, typing in the Terminal, the following lines:

```
wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list
sudo apt-get update
sudo apt-get install sublime-text
```
To open Sublime Text, type in the Terminal: ```subl```.

At least, to install *Selenium Library*, click [here](https://askubuntu.com/questions/937770/how-to-install-and-set-up-selenium-webdriver-on-ubuntu-16-04). 

## How does it work?
First of all, you need to insert your *Instagram's credentials* into the file [credentials.py](credentials.py). After that, the bot goes to https://www.instagram.com/ and uses your credentials to log in. Once it's logged in, it asks you the first username to search with the command line : 

``` person = raw_input("Write username ") ```

(***if the person has a Private Account, the bot doesn't work***)

The bot reads and saves all of the following users of that person. 

```
links = scroll_box.find_elements_by_tag_name('a')
names = [name.text for name in links if name.text != '']
```

After that, you need to type another account and the bot does the same thing than before, saving all of the following users of the other account.
At least, it checks the two lists and prints the common users, with the code: 

```
common = (set(list1).intersection(list2))
print('\n'.join(common))
```

If you want, you can also save the users in a file.txt, called in this case *common.txt*,  with: 

```
with open("common.txt", "w") as outfile:
outfile.write("\n".join(common))
```
