# CSV Predictor Usage

The CSV predictor allows you to specify your own predictions for matches using a simple CSV file format.

## CSV File Format

Create a CSV file with the following columns:

```csv
home_team,away_team,home_goals,away_goals
Bayern München,Borussia Dortmund,2,1
RB Leipzig,Bayer Leverkusen,1,2
Eintracht Frankfurt,VfL Wolfsburg,1,1
```

### Column Descriptions:

- **home_team**: Name of the home team (must match team names on kicktipp.de)
- **away_team**: Name of the away team (must match team names on kicktipp.de)
- **home_goals**: Your predicted goals for the home team (integer)
- **away_goals**: Your predicted goals for the away team (integer)

## Usage

```bash
# Use CSV file for predictions
python kicktippbb.py --csv-file my_predictions.csv --dry-run ehonda-test

# Combine with other options
python kicktippbb.py --csv-file my_predictions.csv --override-bets ehonda-test
```

## Team Name Matching

The CSV predictor tries to match team names in the following order:

1. **Exact match**: Team names must match exactly (case-insensitive)
2. **Fuzzy match**: Partial substring matching for cases where team names might be slightly different

If no match is found for a team, the predictor will:
- Print a warning message
- Use a default prediction of 1:1

## Tips for Creating CSV Files

1. **Get team names**: Run a dry-run first to see the exact team names used on kicktipp.de
2. **Use Excel/Google Sheets**: Easy to create and edit the CSV format
3. **UTF-8 encoding**: Save the file with UTF-8 encoding to handle special characters
4. **Test first**: Always use `--dry-run` to test your CSV file before placing real bets

## Example Workflow

1. **Check upcoming matches:**
   ```bash
   python kicktippbb.py --dry-run ehonda-test
   ```

2. **Create CSV file with your predictions** (using the exact team names from step 1)

3. **Test your CSV file:**
   ```bash
   python kicktippbb.py --csv-file my_predictions.csv --dry-run ehonda-test
   ```

4. **Place bets:**
   ```bash
   python kicktippbb.py --csv-file my_predictions.csv ehonda-test
   ```
