import webapp2

class Index(webapp2.RequestHandler):

    def getRandomMovie(self):

        # TODO: make a list with at least 5 movie titles
        movies = ["The Big Lebowski", "Only Lovers Left Alive", "Interstellar", "The Wind Rises", "My Neighbor Totoro"]
        # TODO: randomly choose one of the movies, and return it
        randomSelection = random.randrange(len(movies))
        return movies[randomSelection]

        return "The Big Lebowski"

    def get(self):
        # choose a movie by invoking our new function
        movie = self.getRandomMovie()

        # build the response string
        content = "<h1>Movie of the Day</h1>"
        content += "<p>" + movie + "</p>"

        # TODO: pick a different random movie, and display it under
        # the heading "<h1>Tommorrow's Movie</h1>"

        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
