# UK exports after Brexit visualization with Streamlit

Hi, I will try to explain the process of building a visualization using Python and **Streamlit**.  The visualization we are trying to build is about UK exports after Brexit.

## Dataset

The original dataset can be found at:
[ONS (UK trade: goods and services publication table 14)](https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/datasets/uktradegoodsandservicespublicationtables)

For the sake of this visualization, I've made a few changes and saved it in google spreadsheet format, you can find it at:
[Google spreadsheet](https://docs.google.com/spreadsheets/d/1jUxkeyYX2D9Xss-ojTAcKVrkXalrCHEVQeDM0PfNb8E/)

The dataset itself displays the value of UK exports and imports from 1997 to January 2021.

## The Anatomy

![enter image description here](https://github.com/RFirmansyah/streamlit-uk-exports/blob/0e5ac4dec1f3de565ce7d2f2f58b3ed462a72240/media/anatomy.png) 

 - Orange color shows the title of the visualization, 
 - Blue color shows a short explanation of the impact of Brexit, 
 - Purple color shows the line chart of the comparison of UK exports and imports from 1997 to 2021, 
 - Green one shows the export and import comparison chart area presented in the form of small multiple.
 - Pink color for footer

## Code Explanation

### Prelude | load required libraries/packages

<pre>
import streamlit as st  
import altair as alt

import pandas as pd
import numpy as np

from gsheetsdb import connect
</pre>

### Prelude | load dataset

<pre>
query = """
        SELECT
            month,
            category,
            exports,        
            imports,
            balance,
            split_month,
            split_year
        FROM
            "https://docs.google.com/spreadsheets/d/1jUxkeyYX2D9Xss-ojTAcKVrkXalrCHEVQeDM0PfNb8E/"  
    """ 
 
conn = connect()
result = conn.execute(query, headers=1)

df = pd.DataFrame(result)
</pre>

### Prelude | setup width and add necessary styling

<pre>
st.set_page_config(layout="wide")

st.markdown('<style>.css-18e3th9{width: 75% !important; padding: 1rem;} .css-fg4pbf{background: azure none repeat scroll 0% 0%}</style>', unsafe_allow_html=True)
</pre>

### Header | title & short text

<pre>

</pre>
