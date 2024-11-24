class Anime:
    def __init__(self, name, type, episodes, status, aired, premiered, broadcast, producers, licensors, studios, source, genres, duration, rating, score, ranked, popularity, favorites):
        self.name = name
        self.type = type
        self.episodes = episodes
        self.status = status
        self.aired = aired
        self.premiered = premiered
        self.broadcast = broadcast
        self.producers = producers
        self.licensors = licensors
        self.studios = studios
        self.source = source
        self.genres = genres
        self.duration = duration
        self.rating = rating
        self.score = score
        self.ranked = ranked
        self.popularity = popularity
        self.favorites = favorites

# Sample data from the CSV file
data = [
    ["Sousou no Frieren", "TV", 28, "Finished Airing", "Sep 29, 2023 to Mar 22, 2024", "Fall 2023", "Fridays at 23:00 (JST)", "['Aniplex', 'Dentsu', 'Shogakukan-Shueisha Productions', 'Nippon Television Network', 'TOHO animation', 'Shogakukan']", "['add some']", "Madhouse", "Manga", "['Adventure', 'Drama', 'Fantasy']", "24 min. per ep.", "PG-13 - Teens 13 or older", 9.36, "#1", "#259", "43,524"],
    ["Steins;Gate", "TV", 24, "Finished Airing", "Apr 6, 2011 to Sep 14, 2011", "Spring 2011", "Wednesdays at 02:05 (JST)", "['Frontier Works', 'Media Factory', 'Kadokawa Shoten', 'Movic', 'AT-X', 'Kadokawa Pictures Japan', 'Nitroplus']", "['Funimation']", "White Fox", "", "['Drama', 'Sci-Fi', 'Suspense']", "24 min. per ep.", "PG-13 - Teens 13 or older", 9.07, "#3", "#13", "189,803"],
    # Add more data as needed
]

# Create Anime objects
anime_objects = []
for entry in data:
    anime = Anime(*entry)
    anime_objects.append(anime)

# Example usage
for anime in anime_objects:
    print(f"Name: {anime.name}, Score: {anime.score}")  