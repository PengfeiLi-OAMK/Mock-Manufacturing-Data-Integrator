import pandas as pd

def load_data(file_path):
	"""
	   Load data from factories' files.
	   Handle FileNotFoundError and formatting issues gracefully.
	"""
	try:
		df=pd.read_excel(file_path)
		return df
	except FileNotFoundError:
		print(f"Error: The file at {file_path} was not found.")
		return None
	except Exception as e:
		print(f"CRITICAL ERROR: Failed to read or parse the report file '{file_path}'.")
		print(f"Exception details: {e}")
		return None
	
def transform_data(df):
    """
    convert non-standard test data from factories into into a standardizeds format.
    """
    clean_df = df[['Prod_ID', 'Test_Volt', 'Result', 'Temperature', 'Test_Time']].copy()
    clean_df = clean_df.rename(columns={
        'Prod_ID': 'product_id',
        'Test_Volt': 'voltage',
        'Result': 'result',
        'Temperature': 'temperature',
        'Test_Time': 'timestamp'
    })
    clean_df=clean_df.dropna(how='all')
    clean_df=clean_df.dropna(subset=['product_id'])

    for col in['voltage','temperature']:
        clean_df[col]=clean_df[col].astype(str).str.replace(r'[^\d.-]','', regex=True)
        clean_df[col]=pd.to_numeric(clean_df[col],errors='coerce')
    clean_df = clean_df.dropna(subset=['voltage', 'temperature'])

    status_map = {
        "OK": "PASS", "ok": "PASS", "Pass": "PASS", "pass": "PASS",
        "FAIL": "FAIL", "Error": "FAIL"
    }
    clean_df['result'] = clean_df['result'].map(status_map).fillna('FAIL')
	
    clean_df['timestamp']=pd.to_datetime(clean_df['timestamp'], errors='coerce') 
    clean_df = clean_df.dropna(subset=['timestamp'])
    clean_df['timestamp'] = clean_df['timestamp'].dt.strftime('%Y-%m-%dT%H:%M:%S')
    
    return clean_df.to_dict(orient='records')

