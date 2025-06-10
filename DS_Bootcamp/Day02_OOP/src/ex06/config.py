# config.py

# Telegram Bot Configuration
TELEGRAM_BOT_TOKEN = '7019160856:AAE14iTC5a1O5i6g_2VqLEqDV2WDimuSvyw'
TELEGRAM_CHAT_ID = '-1002089728025'

# Number of steps for predictions
NUM_OF_STEPS = 3

# Report template
REPORT_TEMPLATE = """
Report

We have made {num_observations} observations from tossing a coin: {tail_count} of them were tails and {head_count} of them were heads.
The probabilities are {tail_prob}% and {head_prob}%, respectively.
Our forecast is that in the next {num_forecasts} observations we will have: {forecast_tails} tail(s) and {forecast_heads} head(s).
"""
