
"""cleaning logic"""
def load_csv(filepath):
    """Load a CSV file into memory.
    Args:

        filepath (str): Path to the CSV.

    Returns:

        dict: Rows as list of dicts.

    """

    import csv
    with open(filepath,'r') as file:
        reader = csv.DictReader(file)
        data = list(reader)
    return data


def validate_row(row,schema):
    errors= []
    for col,col_type in schema.items():
        if col not in row:
            errors.append(f"Missing Col:{col}")
        elif row[col].strip() == "":
            errors.append(f"Empty string")
        
    return len(errors)==0,errors
        

