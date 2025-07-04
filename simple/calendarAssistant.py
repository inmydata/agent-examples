import os

from datetime import date
from dotenv import load_dotenv
from inmydata.CalendarAssistant import CalendarAssistant

load_dotenv()

# Get today's date
today = date.today()

# Initialize the Calendar Assistant with tenant and calendar name
assistant = CalendarAssistant(os.environ['INMYDATA_TENANT'], os.environ['INMYDATA_CALENDAR'])

# Get the current financial year
print("The current financial year is:  " + str(assistant.get_financial_year(today)))
# Get the current financial quarter
print("The current financial quarter is: " + str(assistant.get_quarter(today)))
# Get the current financial month
print("The current financial month is: " + str(assistant.get_month(today)))
# Get the current financial week
print("The current financial week is: " + str(assistant.get_week_number(today)))
# Get the current financial periods
print("The current periods are:")
print(assistant.get_financial_periods(today))