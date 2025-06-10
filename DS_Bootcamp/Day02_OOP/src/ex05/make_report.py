# make_report.py
import sys
from analytics import Research
import config

def generate_report():
    # Load data from file
    research = Research(sys.argv[1])
    data = research.file_reader()
    print(data)

    # Perform calculations
    calculations = research.Calculations()
    heads, tails = calculations.counts(data)
    head_frac, tail_frac = calculations.fractions(heads, tails)
    print(heads,tails)
    print(head_frac,tail_frac)

    # Forecast predictions
    analytics = research.Analytics()
    forecast = analytics.predict_random(config.num_of_steps)
    forecast_heads = sum([1 for x in forecast if x[0] == 1])
    forecast_tails = sum([1 for x in forecast if x[1] == 1])

    # Prepare report data using the template from config
    report = config.report_template.format(
        num_observations=len(data),
        tail_count=tails,
        head_count=heads,
        tail_prob=tail_frac,
        head_prob=head_frac,
        num_forecasts=config.num_of_steps,
        forecast_tails=forecast_tails,
        forecast_heads=forecast_heads
    )


    print(report)

    # Save the report to a text file
    analytics.save_file([report], 'report', 'txt')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 make_report.py <path_to_csv_file>")
        sys.exit(1)

    try:
        generate_report()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
