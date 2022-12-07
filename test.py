import unittest
from game_stamps import get_score, offset


class TestCaseGetScore(unittest.TestCase):
    """Тесты для функции get_score """

    def setUp(self):
        self.game_stamps = [
            {'offset': 99892, 'score': {'away': 1, 'home': 4}},
            {'offset': 99895, 'score': {'away': 2, 'home': 5}},
            {'offset': 99896, 'score': {'away': 3, 'home': 6}},
            {'offset': 99899, 'score': {'away': 4, 'home': 7}},
            {'offset': 99901, 'score': {'away': 5, 'home': 8}},
            {'offset': 99902, 'score': {'away': 6, 'home': 9}},
            {'offset': 99905, 'score': {'away': 7, 'home': 10}},
            {'offset': 99908, 'score': {'away': 8, 'home': 11}},
            {'offset': 99911, 'score': {'away': 9, 'home': 12}}
        ]

    def test_first_place(self):
        """Проверка корректности ответа первого момента в списке"""
        answer = get_score(self.game_stamps, offset)
        self.assertEqual(answer, (4, 1))

    def test_last_place(self):
        """Проверка корректности ответа последнего момента в списке"""
        answer = get_score(self.game_stamps, 99911)
        self.assertEqual(answer, (12, 9))

    def test_no_offset_first(self):
        """Проверка корректности ответа отсутствующего момента в начале списка"""
        answer = get_score(self.game_stamps, 99891)
        self.assertEqual(answer, ("Момент отсутствует в таблице", ""))

    def test_no_offset_last(self):
        """Проверка корректности ответа отсутствующего момента в конце списка"""
        answer = get_score(self.game_stamps, 99912)
        self.assertEqual(answer, ("Момент отсутствует в таблице", ""))

    def test_average_place(self):
        """Проверка корректности ответа среднего момента в списке"""
        answer = get_score(self.game_stamps, 99901)
        self.assertEqual(answer, (8, 5))


if __name__ == "__main__":
    unittest.main()
