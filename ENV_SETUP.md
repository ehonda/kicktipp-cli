# Using .env file for login token

To avoid having to enter your credentials every time or pass the login token as a command line argument, you can store your login token in a `.env` file.

## Setup

1. **Get your login token:**
   ```bash
   python kicktippbb.py --get-login-token
   ```
   Enter your username and password when prompted. The tool will print your login token.

2. **Create a .env file:**
   Copy the `.env.example` file to `.env`:
   ```bash
   cp .env.example .env
   ```

3. **Add your token to the .env file:**
   Edit the `.env` file and replace `your_login_token_here` with your actual token:
   ```
   KICKTIPP_LOGIN_TOKEN=your_actual_token_here
   ```

## Usage

Once you have the `.env` file set up, you can run the tool without any login arguments:

```bash
# This will automatically use the token from .env
python kicktippbb.py --dry-run mycommunity

# You can still override with a specific token if needed
python kicktippbb.py --use-login-token other_token --dry-run mycommunity
```

## Security

- The `.env` file is already included in `.gitignore` so it won't be committed to version control
- Keep your login token secure and don't share it with others
- According to kicktipp.de, login tokens are valid for approximately one year
