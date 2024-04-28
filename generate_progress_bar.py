import datetime


def generate_progress_bar():
    # Get current date and total days in the current year
    today = datetime.datetime.now()
    start_of_year = datetime.datetime(today.year, 1, 1)
    end_of_year = datetime.datetime(today.year, 12, 31)
    total_days = (end_of_year - start_of_year).days + 1

    progress_bar_length = 50

    # Calculate progress percentage
    progress_percentage = round((today - start_of_year).days / total_days * 100, 2)

    # Generate progress bar
    filled_length = int((progress_percentage) / 100 * progress_bar_length)
    empty_length = progress_bar_length - filled_length
    progress_bar = f"{today.year} [{'#' * filled_length}{' ' * empty_length}] {progress_percentage}%"

    return progress_bar


if __name__ == "__main__":
    progress_bar = generate_progress_bar()

    readme = f"""
### Hi there :wave:

:hourglass_flowing_sand: **Year progress**

```txt
{progress_bar}
```
""".strip()

    print(readme)
