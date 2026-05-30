from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

similarity = pickle.load(open("../models/recommender.pkl", "rb"))
movies = pickle.load(open("../models/movies.pkl", "rb"))

movie_titles = movies["title"].tolist()

def recommend(movie_name):

    try:
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

    except:
        return []


@app.route("/", methods=["GET", "POST"])
def home():

    recommendations = []

    if request.method == "POST":

        movie = request.form["movie"]

        recommendations = recommend(movie)

    return render_template(
        "index.html",
        movies=movie_titles,
        recommendations=recommendations
    )


if __name__ == "__main__":
    app.run(debug=True)
