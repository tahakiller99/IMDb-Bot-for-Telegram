from telebot.types import *


def MovieKeyboard(page, ID):
    keyboard = InlineKeyboardMarkup()
    if page == 1:
        keyboard.row(InlineKeyboardButton("🔹 About Movie 🔹", callback_data=f"None1"))
        keyboard.row(InlineKeyboardButton("Crew & Ratings", callback_data=f"Crew & Ratings /{ID}"))
    elif page == 2:
        keyboard.row(InlineKeyboardButton("About Movie", callback_data=f"About movie /{ID}"))
        keyboard.row(InlineKeyboardButton("🔹 Crew & Ratings 🔹", callback_data=f"None2"))
    return keyboard


def ChangePageSearchKeyboard(page, text):
    keyboard = InlineKeyboardMarkup()
    keyboard.row(InlineKeyboardButton("<<", callback_data=f"Then /{page - 1} #{text}"),
                 InlineKeyboardButton(f"Page : {page}", callback_data=f"Page #{text}"),
                 InlineKeyboardButton(">>", callback_data=f"Next /{page + 1} #{text}"))
    keyboard.row(InlineKeyboardButton("Close results", callback_data="Close"))
    return keyboard


def ChangePageTop250Keyboard(page=1):
    keyboard = InlineKeyboardMarkup()
    keyboard.row(InlineKeyboardButton("<<", callback_data=f"Top T /{page - 1} #"),
                 InlineKeyboardButton(f"Page : {page}", callback_data=f"Top P #"),
                 InlineKeyboardButton(">>", callback_data=f"Top N /{page + 1} #"))
    keyboard.row(InlineKeyboardButton("Close", callback_data="Top C"))
    return keyboard
