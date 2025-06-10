# config.py

# Number of steps for predictions
num_of_steps = 4

# Report template
report_template = """
Report

We have made {num_observations} observations from tossing a coin: {tail_count} of them were tails and {head_count} of them were heads.
The probabilities are {tail_prob}% and {head_prob}%, respectively.
Our forecast is that in the next {num_forecasts} observations we will have: {forecast_tails} tail(s) and {forecast_heads} head(s).
"""
