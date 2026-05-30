import pickle

similarity = pickle.load(open("../models/recommender.pkl", "rb"))
movies = pickle.load(open("../models/movies.pkl", "rb"))

def recommend(movie_name):

    movie_index = movies[movies["title"] == movie_name].index[0]

    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommendations = []

    for movie in movie_list:
        recommendations.append(
            movies.iloc[movie[0]].title
        )

    return recommendations


print(recommend("Toy Story"))
