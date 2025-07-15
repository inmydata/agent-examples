import os
from dotenv import load_dotenv
from inmydata.StructuredData import (
    StructuredDataDriver, 
    AIDataSimpleFilter, 
    AIDataFilter, 
    LogicalOperator, 
    ConditionOperator, 
    TopNOption, 
    ChartType
)

load_dotenv()

driver = StructuredDataDriver(os.environ['INMYDATA_TENANT'])
driver.user = "demo" # Events to display charts will be available to the user specified here
driver.session_id = "test-session" # Session ID passed in the event to display charts. Can optionnally be used to only show charts for the current session

# -- Use get_data_simple when your filter is simple (only equality filters, no bracketing, no ORs, etc.)

# Build our simple filter
filter = []
filter.append(
    AIDataSimpleFilter(
        "Store", # Field to filter on
        "Edinburgh") # Value to filter by
    ) 

# Build a TopN filter to only show the Top 10 Sales People based on Sales Value
TopN = TopNOption("Sales Value", 10) # Field to order by and number of records to return (Positive for TopN, negative for BottomN)
TopNOptions = {}
TopNOptions["Sales Person"] = TopN # Apply the Top N option to the Sales Person field

df = driver.get_data_simple(
    "Inmystore Sales", # Name of the subject we want to extract data from
    ["Sales Person","Sales Value"], # List of fields we want to extract
    filter, # Filters to apply
    False, # Whether filters are case sensitive
    TopNOptions) # Apply the Top 10 Sales People based on Sales Value filter

print(df)

# -- Use get_data when your filter more complex (non-equality matches, bracketing, ORs, etc.) --

# Build our filter
filter = [] 
filter.append(
    AIDataFilter(
        "Store",
        ConditionOperator.Equals, # Condition to use in the filter
        LogicalOperator.And, # Logical operator to use in the filter
        "Edinburgh", # Value to filter by
        0, # Number of brackets before this condition
        0, # Number of brackets after this condition
        False # Whether the filter is case sensitive
    )
)
filter.append(
    AIDataFilter(
        "Store",
        ConditionOperator.Equals, # Condition to use in the filter
        LogicalOperator.Or, # Logical operator to use in the filter
        "London", # Value to filter by
        0, # Number of brackets before this condition
        0, # Number of brackets after this condition
        False # Whether the filter is case sensitive
    )
)
df = driver.get_data(
    "Inmystore Sales", # Name of the subject we want to extract data from
    ["Financial Year","Store","Sales Value"], # List of fields we want to extract
    filter, # Filters to apply
    {}) # Apply no TopN options

print(df)

# -- Use get_chart to generate a chart based on the data -- see https://developer.inmydata.com/support/solutions/articles/36000577995-displaying-charts-generated-by-agentic-ai-workflows

# Build our filter
filter = [] 
filter.append(
    AIDataFilter(
        "Store",
        ConditionOperator.Equals, # Condition to use in the filter
        LogicalOperator.And, # Logical operator to use in the filter
        "Edinburgh", # Value to filter by
        0, # Number of brackets before this condition
        0, # Number of brackets after this condition
        False # Whether the filter is case sensitive
    )
)
filter.append(
    AIDataFilter(
        "Financial Year",
        ConditionOperator.Equals, # Condition to use in the filter
        LogicalOperator.And, # Logical operator to use in the filter
        "2025", # Value to filter by
        0, # Number of brackets before this condition
        0, # Number of brackets after this condition
        False # Whether the filter is case sensitive
    )
)

# Build a TopN filter to only show the Top 10 Sales People based on Sales Value
TopN = TopNOption("Sales Value", 10) # Field to order by and number of records to return (Positive for TopN, negative for BottomN)
TopNOptions = {}
TopNOptions["Sales Person"] = TopN # Apply the Top N option to the Sales Person field

chartId = driver.get_chart(
    "Inmystore Sales", # Name of the subject we want to extract data from
    ["Sales Person"], # Chart row fields
    [], # Chart Column Fields
    ["Sales Value"], # Chart value fields
    filter, # Filters to apply
    ChartType.Bar, # Type of chart to generate
    "Top 10 Sales People in Edinburgh for 2025", # Title of the chart
    TopNOptions, # Apply the Top 10 Sales People based on Sales Value filter
)

