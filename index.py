import streamlit as st  
import altair as alt

import pandas as pd
import numpy as np

from gsheetsdb import connect

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

st.set_page_config(layout="wide")

st.markdown('<style>.css-18e3th9{width: 75% !important; padding: 1rem;} .css-fg4pbf{background: azure none repeat scroll 0% 0%}</style>', unsafe_allow_html=True)

st.markdown('<h1>UK <b style="color: #547eac;">Exports</b> to EU plunge by 40% in first month since Brexit</h1>', unsafe_allow_html=True)                

st.markdown('<p>After several delays, United Kingdom will leaving the European Union at the end of January 2020, as well as the start of an 11 month transition period, it will have quite a negative impact on the UK economy.</p><p>In the trade sector, especially exports and imports, there was a sharp decline in the first quarter of 2020. Although during the transition period the United Kingdom remained subject to European Union law, it remained part of the EU Customs Union and the European Single Market.</p>', unsafe_allow_html=True)
    
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

with st.container():
    row2_col1, row2_col2, row2_col3 = st.columns([1,2,2])
    
    with row2_col1:
        st.markdown("<h5>Food & live animals</h5>", unsafe_allow_html=True)            
    
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

with st.container():
    row3_col1, row3_col2, row3_col3 = st.columns([1,2,2])
    
    with row3_col1:
        st.markdown("<h5>Beverages & tobacco</h5>", unsafe_allow_html=True)
    
    with row3_col2:         
        df_temp_cat2 = df[df['category'] == 'Beverages & tobacco'][['split_year','exports']]
        df_export_cat2 = pd.DataFrame(df_temp_cat2.groupby('split_year')['exports'].sum()).reset_index()
        df_export_cat2.rename(columns={'split_year':'Year'}, inplace=True)
        df_export_cat2.rename(columns={'exports':'Exports Values'}, inplace=True)
        
        df_temp_cat1 = df[df['category'] == 'Food & live animals'][['split_year','exports']]
        df_export_cat1 = pd.DataFrame(df_temp_cat1.groupby('split_year')['exports'].sum()).reset_index()
        df_export_cat1.rename(columns={'split_year':'Year'}, inplace=True)
        df_export_cat1.rename(columns={'exports':'Exports Values'}, inplace=True)
        
        chart_data_export_cat2 = alt.Chart(df_export_cat2).mark_area(
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
        
        st.altair_chart(chart_data_export_cat2, use_container_width=True)
        
    with row3_col3:
        df_temp_cat2 = df[df['category'] == 'Beverages & tobacco'][['split_year','imports']]
        df_import_cat2 = pd.DataFrame(df_temp_cat2.groupby('split_year')['imports'].sum()).reset_index()
        df_import_cat2.rename(columns={'split_year':'Year'}, inplace=True)
        df_import_cat2.rename(columns={'imports':'Imports Values'}, inplace=True) 
        
        chart_data_import_cat2 = alt.Chart(df_import_cat2).mark_area(
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
        
        st.altair_chart(chart_data_import_cat2, use_container_width=True)
        
with st.container():
    row4_col1, row4_col2, row4_col3 = st.columns([1,2,2])
    
    with row4_col1:
        st.markdown("<h5>Chemicals</h5>", unsafe_allow_html=True)
    
    with row4_col2:         
        df_temp_cat3 = df[df['category'] == 'Chemicals'][['split_year','exports']]
        df_export_cat3 = pd.DataFrame(df_temp_cat3.groupby('split_year')['exports'].sum()).reset_index()
        df_export_cat3.rename(columns={'split_year':'Year'}, inplace=True)
        df_export_cat3.rename(columns={'exports':'Exports Values'}, inplace=True)
        
        chart_data_export_cat3 = alt.Chart(df_export_cat3).mark_area(
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
        
        st.altair_chart(chart_data_export_cat3, use_container_width=True)
        
    with row4_col3:
        df_temp_cat3 = df[df['category'] == 'Chemicals'][['split_year','imports']]
        df_import_cat3 = pd.DataFrame(df_temp_cat3.groupby('split_year')['imports'].sum()).reset_index()
        df_import_cat3.rename(columns={'split_year':'Year'}, inplace=True)
        df_import_cat3.rename(columns={'imports':'Imports Values'}, inplace=True) 
        
        chart_data_import_cat3 = alt.Chart(df_import_cat3).mark_area(
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
        
        st.altair_chart(chart_data_import_cat3, use_container_width=True)
        
with st.container():
    row5_col1, row5_col2, row5_col3 = st.columns([1,2,2])
    
    with row5_col1:
        st.markdown("<h5>Crude materials</h5>", unsafe_allow_html=True)
    
    with row5_col2:         
        df_temp_cat4 = df[df['category'] == 'Crude materials'][['split_year','exports']]
        df_export_cat4 = pd.DataFrame(df_temp_cat4.groupby('split_year')['exports'].sum()).reset_index()
        df_export_cat4.rename(columns={'split_year':'Year'}, inplace=True)
        df_export_cat4.rename(columns={'exports':'Exports Values'}, inplace=True)      
        
        chart_data_export_cat4 = alt.Chart(df_export_cat4).mark_area(
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
        
        st.altair_chart(chart_data_export_cat4, use_container_width=True)
        
    with row5_col3:
        df_temp_cat4 = df[df['category'] == 'Crude materials'][['split_year','imports']]
        df_import_cat4 = pd.DataFrame(df_temp_cat4.groupby('split_year')['imports'].sum()).reset_index()
        df_import_cat4.rename(columns={'split_year':'Year'}, inplace=True)
        df_import_cat4.rename(columns={'imports':'Imports Values'}, inplace=True)
        
        chart_data_import_cat4 = alt.Chart(df_import_cat4).mark_area(
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
        
        st.altair_chart(chart_data_import_cat4, use_container_width=True)
        
with st.container():
    row6_col1, row6_col2, row6_col3 = st.columns([1,2,2])
    
    with row6_col1:
        st.markdown("<h5>Fuels</h5>", unsafe_allow_html=True)
    
    with row6_col2:         
        df_temp_cat5 = df[df['category'] == 'Fuels'][['split_year','exports']]
        df_export_cat5 = pd.DataFrame(df_temp_cat5.groupby('split_year')['exports'].sum()).reset_index()
        df_export_cat5.rename(columns={'split_year':'Year'}, inplace=True)
        df_export_cat5.rename(columns={'exports':'Exports Values'}, inplace=True)    
        
        chart_data_export_cat5 = alt.Chart(df_export_cat5).mark_area(
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
        
        st.altair_chart(chart_data_export_cat5, use_container_width=True)
        
    with row6_col3:
        df_temp_cat5 = df[df['category'] == 'Fuels'][['split_year','imports']]
        df_import_cat5 = pd.DataFrame(df_temp_cat5.groupby('split_year')['imports'].sum()).reset_index()
        df_import_cat5.rename(columns={'split_year':'Year'}, inplace=True)
        df_import_cat5.rename(columns={'imports':'Imports Values'}, inplace=True)
        
        chart_data_import_cat5 = alt.Chart(df_import_cat5).mark_area(
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
        
        st.altair_chart(chart_data_import_cat5, use_container_width=True)
        
with st.container():
    row7_col1, row7_col2, row7_col3 = st.columns([1,2,2])
    
    with row7_col1:
        st.markdown("<h5>Machinery & transport equipment</h5>", unsafe_allow_html=True)
    
    with row7_col2:         
        df_temp_cat6 = df[df['category'] == 'Machinery & transport equipment'][['split_year','exports']]
        df_export_cat6 = pd.DataFrame(df_temp_cat6.groupby('split_year')['exports'].sum()).reset_index()
        df_export_cat6.rename(columns={'split_year':'Year'}, inplace=True)
        df_export_cat6.rename(columns={'exports':'Exports Values'}, inplace=True)     
        
        chart_data_export_cat6 = alt.Chart(df_export_cat6).mark_area(
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
        
        st.altair_chart(chart_data_export_cat6, use_container_width=True)
        
    with row7_col3:
        df_temp_cat6 = df[df['category'] == 'Machinery & transport equipment'][['split_year','imports']]
        df_import_cat6 = pd.DataFrame(df_temp_cat6.groupby('split_year')['imports'].sum()).reset_index()
        df_import_cat6.rename(columns={'split_year':'Year'}, inplace=True)
        df_import_cat6.rename(columns={'imports':'Imports Values'}, inplace=True)
        
        chart_data_import_cat6 = alt.Chart(df_import_cat6).mark_area(
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
        
        st.altair_chart(chart_data_import_cat6, use_container_width=True)
        
with st.container():
    row8_col1, row8_col2, row8_col3 = st.columns([1,2,2])
    
    with row8_col1:
        st.markdown("<h5>Animal & vegetable oils & fats</h5>", unsafe_allow_html=True)
    
    with row8_col2:         
        df_temp_cat7 = df[df['category'] == 'Animal & vegetable oils & fats'][['split_year','exports']]
        df_export_cat7 = pd.DataFrame(df_temp_cat7.groupby('split_year')['exports'].sum()).reset_index()
        df_export_cat7.rename(columns={'split_year':'Year'}, inplace=True)
        df_export_cat7.rename(columns={'exports':'Exports Values'}, inplace=True)     
        
        chart_data_export_cat7 = alt.Chart(df_export_cat7).mark_area(
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
        
        st.altair_chart(chart_data_export_cat7, use_container_width=True)
        
    with row8_col3:
        df_temp_cat7 = df[df['category'] == 'Animal & vegetable oils & fats'][['split_year','imports']]
        df_import_cat7 = pd.DataFrame(df_temp_cat7.groupby('split_year')['imports'].sum()).reset_index()
        df_import_cat7.rename(columns={'split_year':'Year'}, inplace=True)
        df_import_cat7.rename(columns={'imports':'Imports Values'}, inplace=True)
        
        chart_data_import_cat7 = alt.Chart(df_import_cat7).mark_area(
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
        
        st.altair_chart(chart_data_import_cat7, use_container_width=True)
        
with st.container():
    row9_col1, row9_col2, row9_col3 = st.columns([1,2,2])
    
    with row9_col1:
        st.markdown("<h5>Material manufactures</h5>", unsafe_allow_html=True)
    
    with row9_col2:         
        df_temp_cat8 = df[df['category'] == 'Material manufactures'][['split_year','exports']]
        df_export_cat8 = pd.DataFrame(df_temp_cat8.groupby('split_year')['exports'].sum()).reset_index()
        df_export_cat8.rename(columns={'split_year':'Year'}, inplace=True)
        df_export_cat8.rename(columns={'exports':'Exports Values'}, inplace=True)      
        
        chart_data_export_cat8 = alt.Chart(df_export_cat8).mark_area(
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
        
        st.altair_chart(chart_data_export_cat8, use_container_width=True)
        
    with row9_col3:
        df_temp_cat8 = df[df['category'] == 'Material manufactures'][['split_year','imports']]
        df_import_cat8 = pd.DataFrame(df_temp_cat8.groupby('split_year')['imports'].sum()).reset_index()
        df_import_cat8.rename(columns={'split_year':'Year'}, inplace=True)
        df_import_cat8.rename(columns={'imports':'Imports Values'}, inplace=True)
        
        chart_data_import_cat8 = alt.Chart(df_import_cat8).mark_area(
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
        
        st.altair_chart(chart_data_import_cat8, use_container_width=True)
        
with st.container():
    row10_col1, row10_col2, row10_col3 = st.columns([1,2,2])
    
    with row10_col1:
        st.markdown("<h5>Miscellaneous manufactures</h5>", unsafe_allow_html=True)
    
    with row10_col2:         
        df_temp_cat9 = df[df['category'] == 'Miscellaneous manufactures'][['split_year','exports']]
        df_export_cat9 = pd.DataFrame(df_temp_cat9.groupby('split_year')['exports'].sum()).reset_index()
        df_export_cat9.rename(columns={'split_year':'Year'}, inplace=True)
        df_export_cat9.rename(columns={'exports':'Exports Values'}, inplace=True)       
        
        chart_data_export_cat9 = alt.Chart(df_export_cat9).mark_area(
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
        
        st.altair_chart(chart_data_export_cat9, use_container_width=True)
        
    with row10_col3:
        df_temp_cat9 = df[df['category'] == 'Miscellaneous manufactures'][['split_year','imports']]
        df_import_cat9 = pd.DataFrame(df_temp_cat9.groupby('split_year')['imports'].sum()).reset_index()
        df_import_cat9.rename(columns={'split_year':'Year'}, inplace=True)
        df_import_cat9.rename(columns={'imports':'Imports Values'}, inplace=True)
        
        chart_data_import_cat9 = alt.Chart(df_import_cat9).mark_area(
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
        
        st.altair_chart(chart_data_import_cat9, use_container_width=True)
        
with st.container():
    row11_col1, row11_col2, row11_col3 = st.columns([1,2,2])
    
    with row11_col1:
        st.markdown("<h5>Unspecified goods</h5>", unsafe_allow_html=True)
    
    with row11_col2:         
        df_temp_cat10 = df[df['category'] == 'Unspecified goods'][['split_year','exports']]
        df_export_cat10 = pd.DataFrame(df_temp_cat10.groupby('split_year')['exports'].sum()).reset_index()
        df_export_cat10.rename(columns={'split_year':'Year'}, inplace=True)
        df_export_cat10.rename(columns={'exports':'Exports Values'}, inplace=True)       
        
        chart_data_export_cat10 = alt.Chart(df_export_cat10).mark_area(
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
        
        st.altair_chart(chart_data_export_cat10, use_container_width=True)
        
    with row11_col3:
        df_temp_cat10 = df[df['category'] == 'Unspecified goods'][['split_year','imports']]
        df_import_cat10 = pd.DataFrame(df_temp_cat10.groupby('split_year')['imports'].sum()).reset_index()
        df_import_cat10.rename(columns={'split_year':'Year'}, inplace=True)
        df_import_cat10.rename(columns={'imports':'Imports Values'}, inplace=True)
        
        chart_data_import_cat10 = alt.Chart(df_import_cat10).mark_area(
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
        
        st.altair_chart(chart_data_import_cat10, use_container_width=True)
        
with st.container():
    row3_col1, row3_col2 = st.columns(2)
    
    with row3_col1:
        st.markdown('<div style="text-align: left;">Design by: <a href="https://www.linkedin.com/in/rahman-firmansyah-79283512b" target="_blank">Rahman Firmansyah</a></div>', unsafe_allow_html=True)
        
    with row3_col2:
        st.markdown('<div style="text-align: right;">Data source: <a href="https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/datasets/uktradegoodsandservicespublicationtables">ONS (UK trade: goods and services publication table 14)</a></div>', unsafe_allow_html=True)                                                                        