# UK exports after Brexit visualization with Streamlit

Hi, I will try to explain the process of building a visualization using Python and **Streamlit**.  The visualization we are trying to build is about UK exports after Brexit.

## Dataset

The original dataset can be found at:
[ONS (UK trade: goods and services publication table 14)](https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/datasets/uktradegoodsandservicespublicationtables)

For the sake of this visualization, I've made a few changes and saved it in google spreadsheet format, you can find it at:
[Google spreadsheet](https://docs.google.com/spreadsheets/d/1jUxkeyYX2D9Xss-ojTAcKVrkXalrCHEVQeDM0PfNb8E/)

The dataset itself displays the value of UK exports and imports from 1997 to January 2021.

## The Anatomy

![enter image description here](https://github.com/RFirmansyah/streamlit-uk-exports/blob/c3e350b11f9f2a79f46d77b93e72140452bfe8f7/media/anatomy.png) 

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
st.markdown('<h1`><b style="color: #547eac;">Exports</b> to EU plunge by 40% in first month since Brexit</h1`>', unsafe_allow_html=True)

st.markdown('<p`>With the United Kingdom leaving the European Union at the end of January 2020, as well as the start of an 11 month transition period, it will have quite a negative impact on the UK economy.</p`><p`>In the trade sector, especially exports and imports, there was a sharp decline in the first quarter of 2020. Although during the transition period the United Kingdom remained subject to European Union law, it remained part of the EU Customs Union and the European Single Market.</p`>', unsafe_allow_html=True)
</pre>

### Content | line chart displaying UK exports & imports

<pre>
with st.container():             
    df_temp = df[['split_year','exports','imports']]
    
    df_melt = pd.melt(df_temp,id_vars=['split_year'],var_name='Trade Type', value_name='Trade Values')
    df_export_import = pd.DataFrame(df_melt.groupby(['split_year','Trade Type'])['Trade Values'].sum()).reset_index()  
    df_export_import.rename(columns={'split_year':'Year'}, inplace=True)
    
    chart_data = alt.Chart(df_export_import).mark_line().encode(
        x='Year',
        y='Trade Values',
        color='Trade Type',               
        tooltip=['Year','Trade Values']
    ).configure(
        background='azure'
    ).configure_axis(
        labelAngle=0
    ) 
    
    st.altair_chart(chart_data, use_container_width=True)
</pre>

### Content | small multiple area chart

<pre>
with st.container():
    row2_col1, row2_col2, row2_col3 = st.columns([1,2,2])
    
    with row2_col1:
        st.markdown("<h5`>Food & live animals</h5`>", unsafe_allow_html=True)            
    
    with row2_col2:         
        df_temp_cat1 = df[df['category'] == 'Food & live animals'][['split_year','exports']]
        df_export_cat1 = pd.DataFrame(df_temp_cat1.groupby('split_year')['exports'].sum()).reset_index()
        df_export_cat1.rename(columns={'split_year':'Year'}, inplace=True)
        df_export_cat1.rename(columns={'exports':'Exports Values'}, inplace=True)
        
        chart_data_export_cat1 = alt.Chart(df_export_cat1).mark_area(
            line={'color':'#547eac'},
            color=alt.Gradient(
                gradient='linear',
                stops=[alt.GradientStop(color='white', offset=0),
                       alt.GradientStop(color='#547eac', offset=1)],
                x1=1,
                x2=1,
                y1=1,
                y2=0
            )
        ).encode(
            x='Year',
            y='Exports Values',
            tooltip=['Year','Exports Values']
        ).properties(
            height=150
        ).configure(
            background='azure'
        )  
        
        st.altair_chart(chart_data_export_cat1, use_container_width=True)
        
    with row2_col3:
        df_temp_cat1 = df[df['category'] == 'Food & live animals'][['split_year','imports']]
        df_import_cat1 = pd.DataFrame(df_temp_cat1.groupby('split_year')['imports'].sum()).reset_index()
        df_import_cat1.rename(columns={'split_year':'Year'}, inplace=True)
        df_import_cat1.rename(columns={'imports':'Imports Values'}, inplace=True)
        
        chart_data_import_cat1 = alt.Chart(df_import_cat1).mark_area(
            line={'color':'darkorange'},
            color=alt.Gradient(
                gradient='linear',
                stops=[alt.GradientStop(color='white', offset=0),
                       alt.GradientStop(color='darkorange', offset=1)],
                x1=1,
                x2=1,
                y1=1,
                y2=0
            )
        ).encode(
            x='Year',
            y='Imports Values',
            tooltip=['Year','Imports Values']
        ).properties(
            height=150
        ).configure(
            background='azure'
        ) 
        
        st.altair_chart(chart_data_import_cat1, use_container_width=True)
</pre>

### Footer

<pre>
with st.container():
    row3_col1, row3_col2 = st.columns(2)
    
    with row3_col1:
        st.markdown('<div` style="text-align: left;">Design by: <a` href="https://www.linkedin.com/in/rahman-firmansyah-79283512b" target="_blank">Rahman Firmansyah</a`></div`>', unsafe_allow_html=True)
        
    with row3_col2:
        st.markdown('<div` style="text-align: right;">Data source: <a` href="https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/datasets/uktradegoodsandservicespublicationtables">ONS (UK trade: goods and services publication table 14)</a`></div`>', unsafe_allow_html=True)
</pre>
