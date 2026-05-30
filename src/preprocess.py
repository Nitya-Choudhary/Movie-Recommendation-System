import pandas as pd

movies = pd.read_csv("../data/movies.csv")

movies["genres"] = movies["genres"].str.replace("|", " ", regex=False)

movies.to_csv("../data/processed_movies.csv", index=False)

print("Preprocessing Complete")
