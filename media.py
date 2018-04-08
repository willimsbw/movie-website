import webbrowser


class Movie():
    """
    This class lets you construct Movie objects containing a movie's:

    title: string
    trailer url: string
    poster url: string
    storyline summary: string
    duration: int. number of minutes long the movie is
    """

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, plot_summary, movie_trailer, poster_image,
                 movie_duration):
        self.title = movie_title
        self.duration = movie_duration
        self.trailer_youtube_url = movie_trailer
        self.poster_image_url = poster_image
        self.storyline = plot_summary

    def show_trailer(self):
        webbrowser.open(self.trailer_url)
