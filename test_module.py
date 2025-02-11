import unittest
import demographic_data_analyzer

class DemographicAnalyzerTestCase(unittest.TestCase):
    def setUp(self):
        # Run the function and store the results
        self.results = demographic_data_analyzer.calculate_demographic_data(print_data=False)

    def test_race_count(self):
        expected = {
            'White': 27816,
            'Black': 3124,
            'Asian-Pac-Islander': 1039,
            'Amer-Indian-Eskimo': 311,
            'Other': 271
        }
        self.assertEqual(self.results["race_count"].to_dict(), expected)

    def test_average_age_men(self):
        self.assertAlmostEqual(self.results["average_age_men"], 39.4, places=1)

    def test_percentage_bachelors(self):
        self.assertAlmostEqual(self.results["percentage_bachelors"], 16.4, places=1)

    def test_higher_education_rich(self):
        self.assertAlmostEqual(self.results["higher_education_rich"], 46.5, places=1)

    def test_lower_education_rich(self):
        self.assertAlmostEqual(self.results["lower_education_rich"], 17.4, places=1)

    def test_min_work_hours(self):
        self.assertEqual(self.results["min_work_hours"], 1)

    def test_rich_percentage(self):
        self.assertAlmostEqual(self.results["rich_percentage"], 10.0, places=1)

    def test_highest_earning_country(self):
        self.assertEqual(self.results["highest_earning_country"], "Iran")

    def test_highest_earning_country_percentage(self):
        self.assertAlmostEqual(self.results["highest_earning_country_percentage"], 41.9, places=1)

    def test_top_IN_occupation(self):
        self.assertEqual(self.results["top_IN_occupation"], "Prof-specialty")

if __name__ == "__main__":
    unittest.main()
