import media
import fresh_tomatoes

#my favorite movies, in no particular order

#Hidden Figures
hidden_figures = media.Movie("Hidden Figures",
"The incredible untold story of Katherine G. Johnson, Dorothy Vaughan and Mary Jackson - brilliant African-American women working at NASA.",
"http://t1.gstatic.com/images?q=tbn:ANd9GcRqU2FbN7Zp0ELl-sX4lO8XO0pTjpmdJcpos_fnP9wM9DQHYgFq",
"https://www.youtube.com/watch?v=5wfrDhgUMGI")

#Split
split = media.Movie("Split",
"Chris reads his girlfriend's family's overly accommodating behavior as nervous attempts to deal with their daughter's interracial relationship, but as the weekend progresses, a series of increasingly disturbing discoveries lead him to a truth that he never could have imagined.",
"http://t0.gstatic.com/images?q=tbn:ANd9GcQxZKPueKzPFNEc1Un4x2TecYop4yrTVArVtfgrNzktMqbfehfv",
"https://www.youtube.com/watch?v=84TouqfIsiI")

#Get Out
get_out = media.Movie("Get Out",
"When mysterious spacecrafts touch down across the globe, an elite team - lead by expert linguist Louise Banks - is brought together to investigate.",
"https://images-na.ssl-images-amazon.com/images/M/MV5BNTE2Nzg1NjkzNV5BMl5BanBnXkFtZTgwOTgyODMyMTI@._V1_SY1000_CR0,0,631,1000_AL_.jpg",
"https://www.youtube.com/watch?v=sRfnevzM9kQ")

#Pride and Prejudice
pride_and_prejudice = media.Movie("Pride and Prejudice",
"Pride & Prejudice is a romantic drama based on Jane Austen's 1813 novel of the same name.",
"http://img.moviepostershop.com/pride-and-prejudice-movie-poster-2005-1020293519.jpg",
"https://www.youtube.com/watch?v=1dYv5u6v55Y")

#Black Swan
black_swan = media.Movie("Black Swan",
"Swan Lake requires a dancer who can play both the White Swan with innocence and grace, and the Black Swan, who represents guile and sensuality. Nina fits the White Swan role perfectly but Lily is the personification of the Black Swan.",
"http://t0.gstatic.com/images?q=tbn:ANd9GcQTEDENWuG9VwlAT8yRL_IkTYABMMmGmrQKcN8qjBLZYVkMOgWy",
"https://www.youtube.com/watch?v=5jaI1XOB-bs")

#Pineapple Express
pineapple_express = media.Movie("Pineapple Express",
"Lazy stoner Dale Denton has only one reason to visit his equally lazy dealer Saul Silver: to purchase weed, specifically, a rare new strain called Pineapple Express.",
"https://images-na.ssl-images-amazon.com/images/M/MV5BMTY1MTE4NzAwM15BMl5BanBnXkFtZTcwNzg3Mjg2MQ@@._V1_.jpg",
"https://www.youtube.com/watch?v=sW67OiY7xVw")

#array of the movies above, used for open_movies_page method
movies = [hidden_figures, split, get_out, pride_and_prejudice, black_swan, pineapple_express]

#displays my favorite movies on the web browser
fresh_tomatoes.open_movies_page(movies)
