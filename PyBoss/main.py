import os
import pandas as pd

employee_csv = os.path.join("Resources","employee_data.csv")

employee_csv_df = pd.read_csv(employee_csv)

employee_csv_df[['First Name','Last Name']] = employee_csv_df['Name'].loc[employee_csv_df['Name'].str.split().str.len() == 2].str.split(expand=True)

employee_csv_df["DOB"] = pd.to_datetime(employee_csv_df["DOB"]).dt.strftime('%m/%d/%Y')

employee_csv_df["SSN"] = employee_csv_df['SSN'].replace(r'^\d{3}-\d{2}', "***-**", regex=True)

employee_csv_df["State"]= employee_csv_df["State"].replace({
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
})

final_employee_csv = employee_csv_df[['Emp ID','First Name','Last Name','DOB','SSN','State']]
final_employee_csv.to_excel('Analysis/final_employee_list.xlsx', index=False,header =True)
