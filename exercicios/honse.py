class Horse():
    def __init__(self, breed, rider):
        self.breed = breed
        self.rider = rider

class Rider():
    def __init__(self, name, competition):
        self.name = name
        self.competition = competition

r = Rider("Sinistro", "Barretoscore")
h = Horse("Mangalarga", r)

print("Rider: {}\nCompetition: {}\nHorse Breed: {}".format(h.breed,
                                                           h.rider.name,
                                                           h.rider.competition))
