# config.py

# Telegram Bot Configuration
TELEGRAM_BOT_TOKEN = 'your_telegram_bot_token'
TELEGRAM_CHAT_ID = 'your_chat_or_group_id_'

# Number of steps for predictions
NUM_OF_STEPS = 3

# Report template
REPORT_TEMPLATE = """
Report

We have made {num_observations} observations from tossing a coin: {tail_count} of them were tails and {head_count} of them were heads.
The probabilities are {tail_prob}% and {head_prob}%, respectively.
Our forecast is that in the next {num_forecasts} observations we will have: {forecast_tails} tail(s) and {forecast_heads} head(s).
"""
