import os
from dotenv import load_dotenv
from inmydata.StructuredData import StructuredDataDriver, AIDataSimpleFilter, AIDataFilter, LogicalOperator, ConditionOperator
load_dotenv()

driver = StructuredDataDriver(os.environ['INMYDATA_TENANT'])

# -- Use get_data_simple when your filter is simple (only equality filters, no bracketing, no ORs, etc.)

# Build our simple filter
filter = []
filter.append(
    AIDataSimpleFilter(
        "Store", # Field to filter on
        "Edinburgh") # Value to filter by
    ) 
df = driver.get_data_simple(
    "Inmystore Sales", # Name of the subject we want to extract data from
    ["Financial Year","Sales Value"], # List of fields we want to extract
    filter, # Filters to apply
    False) # Whether filters are case sensitive

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
        False # Whether the filter is case sensitiv
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
        False # Whether the filter is case sensitiv
    )
)
df = driver.get_data(
    "Inmystore Sales", # Name of the subject we want to extract data from
    ["Financial Year","Store","Sales Value"], # List of fields we want to extract
    filter) # Filters to apply

print(df)

