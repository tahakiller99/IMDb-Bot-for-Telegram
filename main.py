import requests
import Functions
import Keyboards
import Strings

from Database import database
from telebot import *
from telebot.types import *
from Functions import SendToAll
from Functions import SaveData
from Functions import LoadData

# Replace 'YOUR_API_TOKEN' with the API token you obtained from the BotFather
TOKEN = 'Type your bot token here!'
# Enable Logging
logging.basicConfig(level=logging.ERROR)

bot = telebot.TeleBot(TOKEN)

try:
    data = LoadData()
    print("Data Loaded")
except FileNotFoundError:
    data = database()
    print("Database created")

Functions.CustomizeBot(bot)


@bot.message_handler(commands=["start"])
def Start(message):
    data.AddORLoadUser(message.chat.id)
    bot.send_message(message.chat.id, Strings.help)
    SaveData(data)


@bot.message_handler(commands=["help"])
def Help(message):
    bot.send_message(message.chat.id, Strings.help)


@bot.message_handler(commands=["about"])
def About(message):
    bot.send_message(message.chat.id, Strings.about)


@bot.message_handler(func=lambda message: message.text[0:3] == "/tt")
def MovieID(message):
    temp = bot.send_message(message.chat.id, "Loading ...")
    x = message.text[1:]
    url = f"http://www.omdbapi.com/?i={x}&apikey=[Your api key]"
    response = requests.get(url).json()
    page = 1
    if response["Response"] == "True" and response["Type"] == "movie":
        data.AddOrUpdateShow(x)
        SaveData(data)
        found = data.GetShowByID(x)
        poster = found.PosterLink
        if poster == "N/A":
            bot.delete_message(temp.chat.id, temp.id)
            bot.send_photo(message.chat.id, photo=open("NoPoster.jpg", 'rb'),
                           caption=Functions.AboutMovie(found), reply_markup=Keyboards.MovieKeyboard(page, x))
        else:
            bot.delete_message(temp.chat.id, temp.id)
            bot.send_photo(message.chat.id, photo=found.PosterLink, caption=Functions.AboutMovie(found),
                           reply_markup=Keyboards.MovieKeyboard(page, x))
    else:
        bot.delete_message(temp.chat.id, temp.id)
        bot.send_message(message.chat.id, "Incorrect IMDb ID.")


@bot.message_handler(commands=["search"])
def Search(message):
    bot.send_message(message.chat.id, "Send the movie title you want to search.")
    bot.register_next_step_handler(message, ShowResults)


@bot.message_handler(commands=["top250"])
def Top250(message):
    temp = bot.send_message(message.chat.id, "Loading...")
    bot.edit_message_text(chat_id=message.chat.id, text=Functions.Top250(), message_id=temp.id)
    bot.edit_message_reply_markup(chat_id=message.chat.id, message_id=temp.id,
                                  reply_markup=Keyboards.ChangePageTop250Keyboard())


def ShowResults(message):
    temp = bot.send_message(message.chat.id, "Searching ...")
    title = message.text
    if Functions.CheckPage(Functions.SearchByPage(1, title)):
        bot.delete_message(temp.chat.id, temp.id)
        bot.send_message(message.chat.id, Functions.SearchResults(title, 1),
                         reply_markup=Keyboards.ChangePageSearchKeyboard(1, title))
    else:
        bot.delete_message(temp.chat.id, temp.id)
        bot.send_message(message.chat.id, Functions.SearchResults(title, 1))


# Server
# Sending messages with this [/admin_@(command)] format
@bot.message_handler(func=lambda message: "/admin" in message.text)
def StopServer(message):
    command = Functions.ExtractCommand(message.text)
    if command == "stop":
        SendToAll(bot, data.Users, "The server has stopped for a few minutes to update.")
        SaveData(data)
        bot.stop_polling()
    elif command == "save":
        SaveData(data)
    elif command == "users":
        bot.send_message(message.chat.id, f"{data.Users.__len__()}")
    elif command == "movies":
        bot.send_message(message.chat.id, f"{data.Movies.__len__()}")


@bot.callback_query_handler(func=lambda call: "Crew & Ratings" in call.data or "About movie" in call.data or
                                              call.data == "None1" or call.data == "None2")
def MovieCallBack(call):
    temp = call.message
    x = Functions.ExtractID(call.data)
    if call.data == f"Crew & Ratings /{x}":
        bot.edit_message_caption(message_id=temp.id, chat_id=temp.chat.id,
                                 caption=Functions.CrewAndRatings(data.GetShowByID(x)),
                                 reply_markup=Keyboards.MovieKeyboard(2, x))
    elif call.data == f"About movie /{x}":
        bot.edit_message_caption(message_id=temp.id, chat_id=temp.chat.id,
                                 caption=Functions.AboutMovie(data.GetShowByID(x)),
                                 reply_markup=Keyboards.MovieKeyboard(1, x))
    elif call.data == "None1":
        bot.answer_callback_query(call.id, "You are already in \"About movie\" page!")
    elif call.data == "None2":
        bot.answer_callback_query(call.id, "You are already in \"Crew & Ratings\" page!")


@bot.callback_query_handler(func=lambda call: "Next" in call.data or "Then" in call.data or
                                              "Page" in call.data or "Close" in call.data)
def SearchCallBack(call):
    temp = call.message
    if "Next" in call.data:
        page = int(Functions.ExtractPage(call.data))
        text = Functions.ExtractText(call.data)
        if Functions.CheckPage(Functions.SearchByPage(page, text)):
            bot.edit_message_text(message_id=temp.id, chat_id=temp.chat.id,
                                  text=Functions.SearchResults(text, page))
            bot.edit_message_reply_markup(message_id=temp.id, chat_id=temp.chat.id,
                                          reply_markup=Keyboards.ChangePageSearchKeyboard(page, text))
        else:
            bot.answer_callback_query(callback_query_id=call.id, text="This is the last page!", show_alert=True)
    elif "Then" in call.data:
        page = int(Functions.ExtractPage(call.data))
        text = Functions.ExtractText(call.data)
        if Functions.CheckPage(Functions.SearchByPage(page, text)):
            bot.edit_message_text(message_id=temp.id, chat_id=temp.chat.id,
                                  text=Functions.SearchResults(text, page))
            bot.edit_message_reply_markup(message_id=temp.id, chat_id=temp.chat.id,
                                          reply_markup=Keyboards.ChangePageSearchKeyboard(page, text))
        else:
            bot.answer_callback_query(callback_query_id=call.id, text="This is the first page!", show_alert=True)
    elif call.data == "Close":
        bot.edit_message_text(message_id=temp.id, chat_id=temp.chat.id, text="You have closed results.")
    else:
        bot.answer_callback_query(callback_query_id=call.id, text="This key just shows you the current page.",
                                  show_alert=True)


@bot.callback_query_handler(func=lambda call: "Top N" in call.data or "Top T" in call.data or
                                              "Top P" in call.data or "Top C" in call.data)
def Top250CallBack(call):
    temp = call.message
    if "Top N" in call.data:
        page = int(Functions.ExtractPage(call.data))
        if page <= 25:
            bot.edit_message_text(chat_id=temp.chat.id, message_id=temp.id, text=Functions.Top250(page))
            bot.edit_message_reply_markup(message_id=temp.id, chat_id=temp.chat.id,
                                          reply_markup=Keyboards.ChangePageTop250Keyboard(page))
        else:
            bot.answer_callback_query(callback_query_id=call.id, text="This is the last page!", show_alert=True)
    elif "Top T" in call.data:
        page = int(Functions.ExtractPage(call.data))
        if page >= 1:
            bot.edit_message_text(chat_id=temp.chat.id, message_id=temp.id, text=Functions.Top250(page))
            bot.edit_message_reply_markup(message_id=temp.id, chat_id=temp.chat.id,
                                          reply_markup=Keyboards.ChangePageTop250Keyboard(page))
        else:
            bot.answer_callback_query(callback_query_id=call.id, text="This is the first page!", show_alert=True)
    elif call.data == "Top C":
        bot.edit_message_text(message_id=temp.id, chat_id=temp.chat.id, text="You have closed this message.")
    else:
        bot.answer_callback_query(callback_query_id=call.id, text="This key just shows you the current page.",
                                  show_alert=True)


try:
    bot.polling(none_stop=True)
except Exception as e:
    logging.error(e)
    print("An error occurred:", e)
