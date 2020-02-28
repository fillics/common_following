# Common Following
Find out which users are followed by the same ones.

## What is it?
Do you want to know who two users follow in common on Instagram? Do you want to know the username of that person who you've seen at a party, but you only know that that person is a friend of other two people? With this bot, developed with **Python** and **Selenium**, you could find out the name of that person, only typing the two Instagram's username that you know.
The bot will find out the users in common, followed by those two usernames.

## How does it work
First of all, you need to insert your *Instagram's credentials* into the file [credentials.py](credentials.py). After that, the bot goes to https://www.instagram.com/ and uses your credentials to log in. Once it's logged in, it asks you the first username to search with the command line : 

``` person = raw_input("Write username ") ```

(***if the person has a Private account, the bot doesn't work***)

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
