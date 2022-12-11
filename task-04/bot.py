import os
import telebot
import requests
import json
import csv
from dotenv import load_dotenv,find_dotenv

load_dotenv(find_dotenv())

# TODO: 1.1 Get your environment variables 
yourkey = os.getenv('KEY')
bot_id = os.getenv('ID')
token = os.getenv('TOKEN')

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'hello'])
def greet(message):
    global botRunning
    botRunning = True
    bot.reply_to(
        message, 'Hello there! I am a bot that will show movie information for you and export it in a CSV file.\n\n')
    
@bot.message_handler(commands=['stop', 'bye'])
def goodbye(message):
    global botRunning
    botRunning = False
    bot.reply_to(message, 'Bye!\nHave a good time')
    


@bot.message_handler(func=lambda message: botRunning, commands=['help'])
def helpProvider(message):
    bot.reply_to(message, '1.0 You can use \"/movie MOVIE_NAME\" command to get the details of a particular movie. For eg: \"/movie The Shawshank Redemption\"\n\n2.0. You can use \"/export\" command to export all the movie data in CSV format.\n\n3.0. You can use \"/stop\" or the command \"/bye\" to stop the bot.')


@bot.message_handler(func=lambda message: botRunning, commands=['movie'])
def getMovie(message):
    bot.reply_to(message, 'Getting movie info...')
   
    # TODO: 1.2 Get movie information from the API

    movieName = message.text.split(' ', 1)[1]
    movieName = movieName.replace(' ', '+')
    url = 'http://www.omdbapi.com/?apikey=' + str(yourkey) + '&t=' + str(movieName)
    
    response = requests.get(url)
    data = response.json()
   

    # TODO: 1.3 Show the movie information in the chat window
    if data['Response'] == 'False':
        bot.reply_to(message, 'Movie not found')
        return
    else:
        if(data['Poster'] != 'N/A'):
            poster = data['Poster']
            bot.send_message(message.chat.id,'Movie Found')
            bot.send_photo(message.chat.id,poster)
        bot.send_message(message.chat.id, 'Title: ' + data['Title'] + '\nYear: ' + data['Year'] + '\nIMDB: ' + data['imdbRating'] + '\nReleased: ' + data['Released'] )
        

    # TODO: 2.1 Create a CSV file and dump the movie information in it
    with open('movies.csv', 'w') as csvfile:
        fieldnames = ['Title', 'Year', 'imdbRating', 'Released']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'Title': data['Title'], 'Year': data['Year'], 'imdbRating': data['imdbRating'], 'Released': data['Released']})
    

  
@bot.message_handler(func=lambda message: botRunning, commands=['export'])
def getList(message):
    bot.reply_to(message, 'Generating file...')
    #TODO: 2.2 Send downlodable CSV file to telegram chat
    csv = open('movies.csv', 'rb')
    bot.send_document(message.chat.id, csv)
    return
    

@bot.message_handler(func=lambda message: botRunning)
def default(message):
    bot.reply_to(message, 'I did not understand '+'\N{confused face}')
    
bot.infinity_polling()
