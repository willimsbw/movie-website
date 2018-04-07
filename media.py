import webbrowser

class Video():
    """
    This class lets you construct Video objects containing the video's:

    title: string
    duration: int. number of minutes long the video is
    """

    def __init__(self, video_title, video_duration):
        self.title = video_title
        self.duration = video_duration

class Movie(Video):
    """
    This class lets you construct Movie objects containing the movie's:

    title: string
    trailer url: string
    poster url: string
    storyline summary: string
    duration: int. number of minutes long the movie is
    """

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, plot_summary, movie_trailer, poster_image, movie_duration):
        Video.__init__(self, movie_title, movie_duration)
        self.trailer_youtube_url = movie_trailer
        self.poster_image_url = poster_image
        self.storyline = plot_summary

    def show_trailer(self):
        webbrowser.open(self.trailer_url)

class TvShow(Video):
    """
    This class lets you construct TvShow objects for individual episodes,
    containing the episode's

    title: string
    season: int
    episode: int
    tv_station: string
    duration: int. number of minutes long the episode is
    """

    def __init__(self, show_title, episode_season, episode_number, show_station, episode_duration):
        Video.__init__(self, show_title, episode_duration)
        self.season = episode_season
        self.episode = episode_number
        self.tv_station = show_station
