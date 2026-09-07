

import unittest
import movie_flix

class TestMovieFlix(unittest.TestCase):

    def setUp(self):
        movie_flix.movies.clear()

    def test_add_movie_success(self):
        result = movie_flix.add_movie("Inception")
        self.assertEqual(result, "Movie 'Inception' added!")
        self.assertIn("inception", movie_flix.movies)

    def test_add_empty_movie_name(self):
        result = movie_flix.add_movie("   ")
        self.assertEqual(result, "Movie name cannot be empty.")

    def test_add_duplicate_movie(self):
        movie_flix.add_movie("Inception")
        result = movie_flix.add_movie("inception")
        self.assertEqual(result, "'inception' is already in the system.")

    def test_rate_movie_success(self):
        movie_flix.add_movie("Inception")
        result = movie_flix.rate_movie("Inception", 5)
        self.assertEqual(result, "Rating 5 added!")
        self.assertEqual(movie_flix.movies["inception"]["ratings"], [5])

    def test_rate_movie_invalid_range(self):
        movie_flix.add_movie("Inception")
        result_high = movie_flix.rate_movie("Inception", 6)
        result_low = movie_flix.rate_movie("Inception", -1)
        self.assertEqual(result_high, "Rating must be between 1 and 5.")
        self.assertEqual(result_low, "Rating must be between 1 and 5.")

    def test_rate_movie_invalid_type(self):
        movie_flix.add_movie("Inception")
        result = movie_flix.rate_movie("Inception", "five")
        self.assertEqual(result, "Invalid input.")

    def test_calculate_average(self):
        movie_flix.add_movie("Inception")
        movie_flix.rate_movie("Inception", 4)
        movie_flix.rate_movie("Inception", 5)
        avg = movie_flix.calculate_average("Inception")
        self.assertEqual(avg, 4.5)

if __name__ == "__main__":
    unittest.main()
