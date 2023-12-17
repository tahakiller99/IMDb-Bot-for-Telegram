import requests
from Functions import Splitting
from Functions import IsSeries


class show:

    def __init__(self, ID):
        temp1 = []
        temp2 = []
        url = f"http://www.omdbapi.com/?i={ID}&apikey=[Your api key]"
        response = requests.get(url).json()
        for i in range(response['Ratings'].__len__()):
            temp1.append(response['Ratings'][i]['Source'])
            temp2.append(response['Ratings'][i]["Value"])

        self.Title = response['Title']
        self.ImdbID = ID
        self.Year = response['Year']
        self.Runtime = response['Runtime']
        self.Genre = Splitting(response['Genre'])
        self.Director = response['Director']
        self.Writer = response['Writer']
        self.Actors = response['Actors']
        self.Plot = response['Plot']
        self.Language = response['Language']
        self.Country = response['Country']
        self.DVD = response['DVD']
        self.Awards = response['Awards']
        self.BoxOffice = response['BoxOffice']
        self.PosterLink = response['Poster']
        self.ImdbRating = response['imdbRating']
        self.ImdbVotes = response['imdbVotes']
        self.Ratings = dict(zip(temp1, temp2))
        self.IsSeries = IsSeries(response['Type'])
        if self.IsSeries:
            self.TotalSeason = response['totalSeasons']

    def UpdateRatings(self, ID):
        temp1 = []
        temp2 = []
        url = f"http://www.omdbapi.com/?i={ID}&apikey=[Your api key]"
        response = requests.get(url).json()

        for i in range(response['Ratings'].__len__()):
            temp1.append(response['Ratings'][i]['Source'])
            temp2.append(response['Ratings'][i]["Value"])

        self.Ratings = dict(zip(temp1, temp2))
        if self.IsSeries:
            self.TotalSeason = response['totalSeasons']
