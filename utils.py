import pandas as pd
def transform_df_percentage(df):
 
  # Assuming 'df' is your DataFrame
  df_percentage = df.copy()

  # Exclude 'Empresa' column from the calculation
  columns_to_convert = df.columns.drop('Empresa')

  # Calculate the percentage for each column
  for column in columns_to_convert:
      total = df[column].sum()
      df_percentage[column] = df[column] / total

  # Multiply by 100 to get percentages
  df_percentage[columns_to_convert] *= 100
  return df_percentage