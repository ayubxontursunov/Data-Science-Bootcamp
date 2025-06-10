# make_report.py
import sys
from analytics import Research
import config

def generate_report():
    # Load data from file
    research = Research(sys.argv[1])
    data = research.file_reader()

    # Perform calculations
    calculations = research.Calculations()
    heads, tails = calculations.counts(data)
    head_frac, tail_frac = calculations.fractions(heads, tails)

    # Forecast predictions
    analytics = research.Analytics()
    forecast = analytics.predict_random(config.NUM_OF_STEPS)
    forecast_heads = sum([1 for x in forecast if x[0] == 1])
    forecast_tails = sum([1 for x in forecast if x[1] == 1])

    # Prepare report data using the template from config
    report = config.REPORT_TEMPLATE.format(
        num_observations=len(data),
        tail_count=tails,
        head_count=heads,
        tail_prob=tail_frac,
        head_prob=head_frac,
        num_forecasts=config.NUM_OF_STEPS,
        forecast_tails=forecast_tails,
        forecast_heads=forecast_heads
    )

    # Print the report to the console
    print(report)

    # Save the report to a text file
    analytics.save_file([report], 'report', 'txt')




if __name__ == "__main__":
    research = Research(sys.argv[1])
    analytics = research.Analytics()
    if len(sys.argv) != 2:
        print("Usage: python3 make_report.py <path_to_csv_file>")
        sys.exit(1)

    try:
        generate_report()
        analytics.send_telegram_message("The report has been successfully created.")
    except Exception as e:
        print(f"Error: {e}")
        analytics.send_telegram_message("The report hasn’t been created due to an error")
        sys.exit(1)
