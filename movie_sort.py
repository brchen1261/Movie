import csv
import matplotlib.pyplot as plt
import numpy as np
from math import floor

class Movie:
    def __init__(self, title, year, genre, duration, country, language, avg_vote):
        self.title = title
        self.year = year
        self.genre = genre.split(', ')
        self.duration = duration
        self.country = country
        self.language = language
        self.avg_vote = float(avg_vote)

class Movie_data:
    def __init__(self):
        self.data = []
        self._is_sorted = False

    def load_data(self, file_path):
        with open(file_path, encoding ='windows=1252') as a:
            reader = csv.reader(a)  

            for entry in list(reader):
                self.data.append(Movie(entry[0], entry[1], entry[2], entry[3], entry[4], entry[5], entry[6]))

    def insertion_sort(self):
        for index in range(1, len(self.data)):
            current_value = self.data[index]
            current_position = index

            while current_position > 0 and self.data[current_position - 1].title > current_value.title:
                tmp = self.data[current_position]
                self.data[current_position] = self.data[current_position - 1]
                self.data[current_position - 1] = tmp
                current_position = current_position - 1

        self._is_sorted = True

    # remember to search on a sorted list
    def _binary_search(self, element, start, end):
        if self._is_sorted:
            if start > end:
                return -1
            
            mid = (start + end) // 2
            if element == self.data[mid].title:
                return mid
            if element < self.data[mid].title:
                return self._binary_search(element, start, mid - 1)
            else:
                return self._binary_search(element, mid + 1, end)    

    def search(self, element):
        self._binary_search('Atlantis', 0, len(movie_data.data))

    def genre_search(self, genre):
        result = []
        for movie in self.data:
            if genre in movie.genre:
                result.append(movie)

        return result

    def plot_rating_year(self):
        result = {}
        min = 9999
        max = 0

        for movie in self.data:

            if int(movie.year) > max:
                max = int(movie.year)
            
            if int(movie.year) < min:
                min = int(movie.year)

            if movie.year in result:
                result[movie.year][0] += movie.avg_vote
                result[movie.year][1] += 1
            else:
                result[movie.year] = [movie.avg_vote, 1]

        x_axis = np.array(range(min, max + 1))
        y_axis = []

        for i in range(min, max + 1):
            if str(i) in result:
                y_axis.append(result[str(i)][0] / result[str(i)][1])
            else:
                y_axis.append(0)

        y_axis = np.array(y_axis)
        plt.plot(x_axis, y_axis)
        plt.show()

    def plot_rating(self):
        rating = [0] * 10

        for movie in self.data:
            rating[floor(movie.avg_vote)] += 1

        xpoints = np.array(['0-1', '1-2', '2-3','3-4','4-5','5-6','6-7','7-8','8-9','9-10'])
        rating_array = np.array(rating)

        print(rating)
        plt.bar(xpoints, rating_array)
        plt.show()


    def plot_genre(self):
        result = {}

        for movie in self.data:
            for genre in movie.genre:
                if genre in result:
                    result[genre] += 1
                else:
                    result[genre] = 1


        values = []
        lables = []
        for (key, value) in result.items():
            values.append(value)
            lables.append(key)

        values = np.array(values)

        print(lables)
        print(values)

        plt.pie(values, labels=lables, autopct='%1.2f%%')
        plt.show()



movie_data = Movie_data()
movie_data.load_data('IMDb_movies.csv')
movie_data.plot_genre()