import requests
import pickle
import Strings
import json


def Splitting(text):
    text = text.replace(" ", "")
    text = text.replace("-", "")
    temp = text.split(",")
    return temp


def IsSeries(text):
    if text == "Movie":
        return False
    elif text == "Series":
        return True


def GenreToText(genre):
    if genre[0] == "N/A":
        return genre[0]
    else:
        text = ""
        for i in range(genre.__len__()):
            text = text + "#" + genre[i] + " "
        return text


def AboutMovie(movie):
    text = f"Title : {movie.Title}\n" \
           f"IMDb ID : /{movie.ImdbID} \n" \
           f"Year : {movie.Year}\n" \
           f"Genre : {GenreToText(movie.Genre)} \n" \
           f"-------------------------\n" \
           f"Plot : {movie.Plot}\n" \
           f"-------------------------\n" \
           f"Language : {movie.Language}\n" \
           f"Country : {movie.Country}\n" \
           f"Runtime : {movie.Runtime}\n" \
           f"DVD : {movie.DVD}\n" \
           f"BoxOffice : {movie.BoxOffice}\n" \
           f"\n@[Your bot id]"
    return text


def CrewAndRatings(movie):
    text = f"Actors : {movie.Actors}\n" \
           f"Director : {movie.Director}\n" \
           f"Writer : {movie.Writer}\n" \
           f"--------------------\n" \
           f"Awards : {movie.Awards}\n" \
           f"IMDb Rating : {movie.ImdbRating}\n" \
           f"IMDb Votes : {movie.ImdbVotes}\n"
    text = text + RatingToText(movie) + f"\n@[Your bot id]"
    return text


def RatingToText(movie):
    text = ""
    temp = list(movie.Ratings.keys())
    for i in range(movie.Ratings.__len__()):
        text = text + f"{temp[i]} : {movie.Ratings[temp[i]]}\n"
    return text


def ExtractID(text):
    index1 = text.find("/") + 1
    x = text[index1:]
    return x


def ExtractPage(text):
    index1 = text.find("/") + 1
    index2 = text.find("#")
    page = text[index1:index2]
    return page


def ExtractText(text):
    index1 = text.find("#") + 1
    page = text[index1:]
    return page


def ExtractTitle(text):
    index1 = text.find("_") + 1
    title = text[index1:]
    return title


def ExtractCommand(text):
    index1 = text.find("@") + 1
    title = text[index1:]
    return title


def SearchResults(title, page):
    url = f"http://www.omdbapi.com/?s={title}&page={page}&apikey=[Your api key]"
    response = requests.get(url).json()
    if response["Response"] == "True":
        resultsnumber = response["totalResults"]
        text = f"Results for \"{title}\"\n"
        text = text + f"Total results : {resultsnumber} \n--------------------\n"
        for x in response["Search"]:
            title = x["Title"]
            year = x["Year"]
            imdbid = x["imdbID"]
            text = text + f"Title : {title}\n" \
                          f"Year : {year}\n" \
                          f"IMDb ID : /{imdbid}\n--------------------\n"
        text = text + "\n@[Your bot id]"
    else:
        text = response["Error"]
    return text


def SearchByPage(page, text):
    if page == 1:
        url = f"http://www.omdbapi.com/?s={text}&apikey=[Your api key]"
    else:
        url = f"http://www.omdbapi.com/?s={text}&page={page}&apikey=[Your api key]"
    response = requests.get(url).json()
    return response


def CheckPage(jsonobject):
    if jsonobject["Response"] == "False":
        return False
    else:
        return True


def SaveData(obj):
    with open('data.pickle', 'wb') as file:
        pickle.dump(obj, file)
    print("Data saved")


def LoadData():
    with open('data.pickle', 'rb') as file:
        data = pickle.load(file)
    return data


def CustomizeBot(bot):
    bot.set_my_description(Strings.description)
    bot.set_my_commands(Strings.commands)


def SendToAll(bot, users, text):
    for x in users:
        bot.send_message(x.ID, text)


def Top250(page=1):
    text = "IMDb top 250 movies\n" \
           "@[Your bot id]\n--------------------\n"
    with open("Top250.json", 'r') as file:
        data = json.load(file)
    temp = data['Movies'][(page - 1) * 10: (page * 10)]
    for x in temp:
        title = x["Title"]
        year = x["Year"]
        imdbid = x["imdbID"]
        imdbrating = x["imdbRating"]
        text = text + f"Title : {title}\n" \
                      f"Year : {year}\n" \
                      f"IMDb Rating: {imdbrating}\n" \
                      f"IMDb ID : /{imdbid}\n--------------------\n"
    return text
