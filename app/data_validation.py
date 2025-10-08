from pydantic import BaseModel, ValidationError

class CSVData(BaseModel):
    column: str
    value: float

def validate_csv_data(df):
    """Validate CSV data using Pydantic model."""
    errors = []
    for index, row in df.iterrows():
        try:
            CSVData(column=row.iloc[0], value=row.iloc[1])
        except ValidationError as e:
            errors.append(f"Row {index + 1}: {e}")
    return errors
