import media
import fresh_tomatoes

def print_all_movie_attributes(object):
    """
    When passed a Movie() object, prints all of its attributes
    """
    print("title: " + object.title +
    "\nplot summary: " + object.storyline +
    "\ntrailer url: " + object.trailer_youtube_url +
    "\nposter image url: " + object.poster_image_url +
    "\nduration: " + str(object.duration) + " minutes"
    "\nvalid ratings: ")
    print(object.VALID_RATINGS)


lady_bird = media.Movie("Lady Bird",
                        "A teenager (Saoirse Ronan) navigates a loving but turbulent relationship with her strong-willed mother (Laurie Metcalf) over the course of an eventful and poignant senior year of high school.",
                        "https://www.youtube.com/watch?v=cNi_HC839Wo",
                        "https://images-na.ssl-images-amazon.com/images/I/A1sU+Yf+V9L._RI_.jpg",
                        95)

coco = media.Movie("Coco",
                    "Despite his family's generations-old ban on music, young Miguel dreams of becoming an accomplished musician like his idol Ernesto de la Cruz. Desperate to prove his talent, Miguel finds himself in the stunning and colorful Land of the Dead. After meeting a charming trickster named Héctor, the two new friends embark on an extraordinary journey to unlock the real story behind Miguel's family history.",
                    "https://www.youtube.com/watch?v=xlnPHQ3TLX8",
                    "http://t3.gstatic.com/images?q=tbn:ANd9GcS3FGIsangc2iauB89mttkiBAvIDj_O952Ypk2p5QqABby--L6d",
                    109)

midnight_in_paris = media.Movie("Midnight in Paris",
                                "Gil Pender (Owen Wilson) is a screenwriter and aspiring novelist. Vacationing in Paris with his fiancee (Rachel McAdams), he has taken to touring the city alone. On one such late-night excursion, Gil encounters a group of strange -- yet familiar -- revelers, who sweep him along, apparently back in time, for a night with some of the Jazz Age's icons of art and literature. The more time Gil spends with these cultural heroes of the past, the more dissatisfied he becomes with the present.",
                                "https://www.youtube.com/watch?v=BYRWfS2s2v4",
                                "https://www.movieposter.com/posters/archive/main/145/MPW-72510",
                                100)

shape_of_water = media.Movie("The Shape of Water",
                            "Elisa is a mute, isolated woman who works as a cleaning lady in a hidden, high-security government laboratory in 1962 Baltimore. Her life changes forever when she discovers the lab's classified secret -- a mysterious, scaled creature from South America that lives in a water tank. As Elisa develops a unique bond with her new friend, she soon learns that its fate and very survival lies in the hands of a hostile government agent and a marine biologist.",
                            "https://www.youtube.com/watch?v=XFYWazblaUA",
                            "https://www.movieposter.com/posters/archive/main/242/MPW-121262",
                            123)

moonrise_kingdom = media.Movie("Moonrise Kingdom",
                                "The year is 1965, and the residents of New Penzance, an island off the coast of New England, inhabit a community that seems untouched by some of the bad things going on in the rest of the world. Twelve-year-olds Sam (Jared Gilman) and Suzy (Kara Hayward) have fallen in love and decide to run away. But a violent storm is approaching the island, forcing a group of quirky adults (Bruce Willis, Edward Norton, Bill Murray) to mobilize a search party and find the youths before calamity strikes.",
                                "https://www.youtube.com/watch?v=7N8wkVA4_8s",
                                "http://img.moviepostershop.com/moonrise-kingdom-movie-poster-2012-1020750674.jpg",
                                94)

movie_list = [lady_bird, coco, midnight_in_paris, shape_of_water, moonrise_kingdom]

fresh_tomatoes.open_media_page(movie_list)
