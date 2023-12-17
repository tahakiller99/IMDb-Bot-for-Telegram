from Show import show
from User import user


class database:

    def __init__(self):
        self.Movies = []
        self.Users = []
        pass

    def AddOrUpdateShow(self, ID):
        if self.GetShowByID(ID) is None:
            self.Movies.append(show(ID))
        else:
            self.GetShowByID(ID).UpdateRatings(ID)

    def AddORLoadUser(self, x):
        if self.GetUserByID(x) is None:
            self.Users.append(user(x))

    def GetShowByID(self, ID):
        for i in range(self.Movies.__len__()):
            if self.Movies[i].ImdbID == ID:
                return self.Movies[i]
        return None

    def GetUserByID(self, x):
        for i in range(self.Users.__len__()):
            if self.Users[i].ID == x:
                return self.Users[i]
            else:
                return None
