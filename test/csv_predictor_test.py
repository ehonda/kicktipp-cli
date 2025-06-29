import pytest
import os
import tempfile
from predictors.csvpredictor import CSVPredictor
from helper.match import Match


def test_csv_predictor_load():
    # Create a temporary CSV file for testing
    csv_content = """home_team,away_team,home_goals,away_goals
Bayern Munich,Borussia Dortmund,2,1
RB Leipzig,Bayer Leverkusen,1,2
"""
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
        f.write(csv_content)
        csv_file = f.name
    
    try:
        predictor = CSVPredictor(csv_file)
        
        # Test exact match
        match = Match("Bayern Munich", "Borussia Dortmund", "01.01.24 15:30", "1.5", "3.0", "6.0")
        prediction = predictor.predict(match)
        assert prediction == (2, 1)
        
        # Test fuzzy match
        match2 = Match("bayern munich", "borussia dortmund", "01.01.24 15:30", "1.5", "3.0", "6.0")
        prediction2 = predictor.predict(match2)
        assert prediction2 == (2, 1)
        
        # Test no match (should return default 1:1)
        match3 = Match("Unknown Team", "Another Team", "01.01.24 15:30", "1.5", "3.0", "6.0")
        prediction3 = predictor.predict(match3)
        assert prediction3 == (1, 1)
        
    finally:
        os.unlink(csv_file)


def test_csv_predictor_file_not_found():
    with pytest.raises(FileNotFoundError):
        CSVPredictor("nonexistent_file.csv")
