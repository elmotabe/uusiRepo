import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_finds_existing_player(self):
        result = self.stats.search("Semenko")
        self.assertIsNotNone(result)
        self.assertEqual(result.name, "Semenko")

    def test_search_finds_player_with_partial_name(self):
        result = self.stats.search("Kurr")
        self.assertIsNotNone(result)
        self.assertEqual(result.name, "Kurri")

    def test_search_returns_none_for_nonexistent_player(self):
        result = self.stats.search("Nonexistent")
        self.assertIsNone(result)

    def test_team_returns_players_from_specific_team(self):
        result = self.stats.team("EDM")
        self.assertEqual(len(result), 3)
        team_names = [player.name for player in result]
        self.assertIn("Semenko", team_names)
        self.assertIn("Kurri", team_names)
        self.assertIn("Gretzky", team_names)

    def test_team_returns_empty_list_for_nonexistent_team(self):
        result = self.stats.team("NYR")
        self.assertEqual(len(result), 0)

    def test_top_returns_correct_number_of_players(self):
        result = self.stats.top(2)
        self.assertEqual(len(result), 3)  # how_many + 1 pelaajaa (0 <= i <= how_many)

    def test_top_returns_players_sorted_by_points(self):
        result = self.stats.top(4)
        # Gretzky (124p), Yzerman (98p), Lemieux (99p), Kurri (90p), Semenko (16p)
        self.assertEqual(result[0].name, "Gretzky")
        self.assertEqual(result[1].name, "Lemieux")
        self.assertEqual(result[2].name, "Yzerman")
        self.assertEqual(result[3].name, "Kurri")
        self.assertEqual(result[4].name, "Semenko")

    def test_top_with_zero_returns_one_player(self):
        result = self.stats.top(0)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].name, "Gretzky")