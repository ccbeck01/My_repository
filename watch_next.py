'''
watch_next.py
This program creates a function that reads movies from a text file, then returns the most similar
movie to a description, which will be entered by the user.
'''

import spacy
nlp = spacy.load('en_core_web_md')


movies = []                   # Creates a list container to read the movies from the text file into.
similar_f = []                # Creates a list to store the Similar values into
movie_similar_dict = {}       # Creates a dictionary to store the Movie / Similar values into


# This block reads the movies from the text file into a list.
def compare_movies(movie_to_compare):
    with open("movies.txt", "r")as f:
        for movie in f:
            movie = movie.strip("\n")
            movies.append(movie)

    # Creates an nlp object of the description entered.
    model_movie = nlp(movie_to_compare)

    # This block performs the similarity calculation and enters it with the corresponding
    # movie into the dictionary.
    for m_movie in movies:
        similarity = nlp(m_movie).similarity(model_movie)
        similar_f.append(similarity)
        movie_similar_dict[similarity] = m_movie

    print(movie_similar_dict)                         # Prints the movies and similarity index to the description.
    print(f"\nHighest similarity value to this description:\n{max(similar_f)}")  # Prints the highest similarity value
    print(f"\nThe most similar movie:\n{movie_similar_dict[max(similar_f)]}")    # Prints the movie with the highest similarity value.

    return {movie_similar_dict[max(similar_f)]}


# Calling the function
description = input("\nPlease enter the description of the move to be compared: ")
compare_movies(description)
