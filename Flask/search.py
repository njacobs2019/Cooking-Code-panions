#Search payload-object

from DBAccess import DBAccess
class Search:
    def __init__(self, txtSearch):
        self.text = txtSearch
        self.words = txtSearch.split(' ')
        self.tags = ()

    # Full text search, just searches by title for now
    def search_fullText(self):
        print(self.text)
        #Was thinking of Flux, but its going to take some reworking to make things conform to it
        #db = DBAccess()
        #db.get_with_title(self.text)

    #setters
    def setTags(self, givenTags):
        self.tags += givenTags