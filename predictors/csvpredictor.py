"""
CSV file predictor for kicktipp bet bot.
Loads predictions from a CSV file instead of calculating them.
"""
from helper.match import Match
from .base import PredictorBase
import csv
import os.path


class CSVPredictor(PredictorBase):
    def __init__(self, csv_file_path):
        self.csv_file_path = csv_file_path
        self.predictions = self._load_predictions()

    def _load_predictions(self):
        """Load predictions from CSV file"""
        if not os.path.exists(self.csv_file_path):
            raise FileNotFoundError(f"CSV file not found: {self.csv_file_path}")
        
        predictions = {}
        try:
            with open(self.csv_file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Use team names as key for matching
                    home_team = row['home_team'].strip()
                    away_team = row['away_team'].strip()
                    home_goals = int(row['home_goals'])
                    away_goals = int(row['away_goals'])
                    
                    key = self._create_match_key(home_team, away_team)
                    predictions[key] = (home_goals, away_goals)
        except UnicodeDecodeError:
            # Try with different encoding if UTF-8 fails
            with open(self.csv_file_path, 'r', encoding='iso-8859-1') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Use team names as key for matching
                    home_team = row['home_team'].strip()
                    away_team = row['away_team'].strip()
                    home_goals = int(row['home_goals'])
                    away_goals = int(row['away_goals'])
                    
                    key = self._create_match_key(home_team, away_team)
                    predictions[key] = (home_goals, away_goals)
        
        return predictions

    def _create_match_key(self, home_team, away_team):
        """Create a normalized key for team matching"""
        return f"{home_team.lower().strip()} vs {away_team.lower().strip()}"

    def _find_prediction(self, match: Match):
        """Find prediction for a given match"""
        # Try exact match first
        key = self._create_match_key(match.hometeam, match.roadteam)
        if key in self.predictions:
            return self.predictions[key]
        
        # Try fuzzy matching (basic substring matching)
        home_lower = match.hometeam.lower().strip()
        away_lower = match.roadteam.lower().strip()
        
        for pred_key, prediction in self.predictions.items():
            pred_home, pred_away = pred_key.split(' vs ')
            
            # Check if team names contain each other (for partial matches)
            if (home_lower in pred_home or pred_home in home_lower) and \
               (away_lower in pred_away or pred_away in away_lower):
                return prediction
        
        return None

    def predict(self, match: Match):
        """Get prediction for a match from CSV data"""
        prediction = self._find_prediction(match)
        
        if prediction is None:
            print(f"Warning: No prediction found for {match.hometeam} vs {match.roadteam}")
            # Return a default prediction (1:1)
            return (1, 1)
        
        return prediction
