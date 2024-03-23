"""
Generates a CSV table with a date/time column,
with each row incrementing by one hour.
"""

import csv
from argparse import ArgumentParser
from datetime import datetime, timedelta
from pathlib import Path
from sys import stderr

if __name__ == "__main__":
    # Define the command line arguments.
    arg_parser = ArgumentParser(description=__doc__)
    arg_parser.add_argument("output_file", type=Path, help="The output CSV file.")
    arg_parser.add_argument(
        "start_date",
        type=datetime.fromisoformat,
        help=f"The start date. E.g., {datetime(1900, 1, 1).date()}",
    )
    arg_parser.add_argument(
        "end_date",
        type=datetime.fromisoformat,
        help=f"The end date. E.g., {datetime.now().date()}",
    )
    args = arg_parser.parse_args()

    start_date: datetime = args.start_date
    end_date: datetime = args.end_date
    output_file: Path = args.output_file

    row_count = 0

    if output_file.exists():
        stderr.write(
            f'A file named "{output_file}" already exists. Please choose a different filename or delete the existing file.'
        )
        exit(1)

    stderr.write(
        f"Creating a table of dates between {start_date} and {end_date} called {args.output_file}…\n"
    )
    # Open the output file.
    with open(args.output_file, "tw", encoding="utf-8", newline="") as f:
        writer = csv.writer(
            f,
            dialect=csv.excel,
        )
        writer.writerow(["Date"])

        current_date = start_date
        while current_date < end_date:
            writer.writerow([current_date])
            current_date += timedelta(hours=1)
            row_count += 1

    stderr.write(f"Completed. Created {row_count} rows.")
