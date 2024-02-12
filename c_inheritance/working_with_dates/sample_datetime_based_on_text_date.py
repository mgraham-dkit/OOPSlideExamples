import datetime as dt

# Create a date with specific year, month and date information
text_date = "20/10/2020"
# Specify the format of the date used in the text
# %d is days, %m is months, %Y is years (full version, i.e. 2020 and not 20)
date_format = "%d/%m/%Y"
# Extract the day, month and year data from the string and create a date out of it
date_one = dt.datetime.strptime(text_date, date_format)
# Create a date representing right now
date_now = dt.datetime.now()
# Get the difference between the two in days (i.e. the time that has passed between them)
num_days = (date_now - date_one).days
# Convert the number of days into whole years
num_years = int((num_days / 365))
print(num_years)