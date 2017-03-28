import pandas as pd

def csv_col_is_numeric(filename, col=1, skiprows=1):
    # verifies a csv column is numerical by casting to float and returning the line on error
    with open(filename) as f:
        for line in f.readlines()[skiprows:]:
            vals = line.strip().split(',')
            #print(vals)
            try:
                x = float(vals[col])
            except:
                return line.strip()

def csv_col_duplicates(filename, col=1, skiprows=1):
    with open(filename) as f:
        existing_values = []
        for line in f.readlines()[skiprows:]:
            vals = line.strip().split(',')
            if vals[col] not in existing_values:
                existing_values.append(vals[col])
            else:
                return line.strip()

def csv_col_is_monotonic(filename, col=1, skiprows=1):
    with open(filename) as f:
        lines = f.readlines()[skiprows:]
        previous_line = lines[0]
        previous_value = previous_line.strip().split(',')[col]
        for line in lines[skiprows+1:]:
            current_value = line.strip().split(',')[col]
            if float(current_value) < float(previous_value):
                return previous_line.strip(), line.strip()
            previous_value = current_value
            previous_line = line

def csv_col_dates_valid(filename, col=0, skiprows=1):
    data = pd.read_csv(filename, parse_dates=True, index_col=col, skiprows=skiprows)
    if data.index.dtype == 'O':
        return 'invalid date'
    else:
        return 0

