import telebot

description = "🎬 Explore the cinematic world with WikiMovieBot! Discover films, get details, " \
              "and make your movie nights epic.\n\n"\
              "🔍 Search Movies: Easily search for movies by title.\n\n" \
              "🎥 Movie Details: Get comprehensive details about movies, including plot summaries, " \
              "ratings, etc.\n\n" \
              "🔗 Connect with OMDb: Our bot is linked with OMDb, one of the most comprehensive movie databases.\n\n" \
              "🤖 Easy to Use: Navigate through the bot's user-friendly interface with simple " \
              "commands and interactive buttons.\n\n" \
              "Start exploring by typing /start" \

help = "Welcome to the WikiMovie Bot Help section! 🎬🤖\n\n"\
       "This bot is your ultimate companion for exploring the world of movies. " \
       "Whether you're a cinephile or just looking for a great film to watch, we've got you covered. " \
       "Here's how you can use our bot:\n\n"\
       "🔍 Search Movies: Use the /search command to find movies matching your query.\n\n"\
       "⚡️ Find by IMDb ID: If you know the IMDb ID of a movie, you can get its details directly. " \
       "For example, to find details about \"Inception\" use the IMDb ID like this: /tt1375666\n\n" \
       "🏆 IMDb Top 250: Explore the top-rated movies according to IMDb's ranking using the /top250 command.\n\n" \
       "ℹ️ About: To learn more about this bot and its creators, use the /about command.\n\n"\
       "Feel free to explore and have fun with our bot's features. If you ever need assistance, " \
       "just type /help to see this message again.\n\n" \
       "Lights, camera, action! 🍿🎥\n\n@[Your bot id]"

about = "🎥 WikiMovie Bot: Your one-stop destination for movie enthusiasts! Get ready to explore the fascinating" \
        " world of cinema with our bot. From movie details to ratings and cast information, we're here to provide you" \
        " with a cinematic journey like no other.\n\n"\
        "📱 Contact: If you have any questions, feedback or you just want to make your own Telegram bot," \
        "feel free to Contact us on Telegram at @[Admin id]\n\n" \
        "Stay tuned for updates and enjoy your movie discoveries!\n\n@[Your bot id]"

commands = [
        telebot.types.BotCommand("/help", "Get help"),
        telebot.types.BotCommand("/search", "Search a movie"),
        telebot.types.BotCommand("/top250", "Get IMDb top 250 movies"),
        telebot.types.BotCommand("/about", "About the bot"),
    ]
