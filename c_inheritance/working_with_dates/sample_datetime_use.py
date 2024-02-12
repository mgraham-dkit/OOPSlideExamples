import datetime as dt

# Create a date with specific year, month and date information
date_one = dt.datetime(2020, 10, 20)
# Create a date representing right now
date_now = dt.datetime.now()
# Get the difference between the two in days (i.e. the time that has passed between them)
num_days = (date_now - date_one).days
# Convert the number of days into whole years
num_years = int((num_days / 365))
print(num_years)