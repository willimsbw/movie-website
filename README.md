# Static Movie Webpage

entertainment_center.py generates a file called fresh_tomatoes.html, which
opens a static webpage displaying my favorite movies' poster art. When a piece
of poster art is clicked, it will play the movie's trailer.

## Getting Started

If you meet all of the prerequisites, download entertainment_center.py and
fresh_tomatoes.py. Run fresh_tomatoes.py while connected to the internet, and
it will generate fresh_tomatoes.html. Open the new html file to view a webpage
of my favorite movies.

### Prerequisites

To run fresh_tomatoes.py, you'll need to install [Python 3](https://www.python.org/ftp/python/3.6.5/python-3.6.5.exe)

Then you'll need to install the [requests library](http://docs.python-requests.org/en/latest/user/install/#install)

Finally, you'll need to get your own api key for [The Movie Database](https://www.themoviedb.org/settings/api) and store it as a string in the variable: "key" in "api_key.py":
```
key = "<<<your api key here>>>"
```

To view the fresh_tomatoes.html file generated when entertainment_center.py is run, you'll need a web browser installed.

## Built With

* [Python 3](https://docs.python.org/3/)
* [The Movie Database](https://www.themoviedb.org)
-- This product uses the TMDb API but is not endorsed or certified by TMDb. --
* [The requests library for Python 3](http://docs.python-requests.org/en/latest/user/quickstart/)


## Contributing

If you find an issue or have a feature you think I should add, feel free to submit an issue or pull request!

## Authors

* **Bryan Williams** - *Initial work* - [willimsbw](https://github.com/willimsbw)
* Udacity's team, who provided the original version of fresh_tomatoes.py

See also the list of [contributors](https://github.com/willimsbw/movie-website/graphs/contributors)
who participated in this project.

## Acknowledgments

* Thanks to Udacity for their nanodegree programs
* Thanks to Free Code Camp, for getting me started and whose projects provided me with some previous experience using REST api's and an idea for how to approach this type of site
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2), for providing this really great readme template
