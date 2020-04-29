import gspread  ## access the gspread lib to interface with google sheets
import random  ## access random lib to use random integer method
from google.oauth2.service_account import Credentials   ## access credentials method
scopes = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
credentials = Credentials.from_service_account_file('TweetBot.json', scopes=scopes)
gc = gspread.authorize(credentials) ## this authorizes the program to access the sheet
wks = gc.open("Twitter_Bot").sheet1  ## this is the spread sheet to access
# print(wks.get('B3'))  ## this would print out contents of cell B3
tweet_list=[]
tweet_list = wks.col_values(2)  ## this gets the entire 2nd column data and stuffs it into a list
print("There are " ,len(tweet_list) - 1 , " entries in the twitter bot message database")
msg_num_to_tweet = random.randint(1,len(tweet_list)-1)  ## start random at 1 to eliminate the column header,
print("")
print(tweet_list[msg_num_to_tweet])

