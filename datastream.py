import sys
import subprocess

#subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'gsheetsdb'])

from gsheetsdb import connect

source = "https://docs.google.com/spreadsheets/d/1jUxkeyYX2D9Xss-ojTAcKVrkXalrCHEVQeDM0PfNb8E/"

template = """
        SELECT
            month,
            category,
            exports,        
            imports,
            balance,
            split_month,
            split_year
        FROM
            "{0}"
    """

def data_stream():
    query = template.format(source)
    
    conn = connect()
    result = conn.execute(query, headers=1)
    
    return result 