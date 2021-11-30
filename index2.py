import streamlit as st  
import altair as alt

import pandas as pd
import numpy as np

import datastream as ds
import vizopt as vo

df = pd.DataFrame(ds.data_stream())

st.set_page_config(layout="wide")

st.markdown('<style>.css-18e3th9{width: 75% !important; padding: 1rem;} .css-fg4pbf{background: azure none repeat scroll 0% 0%}</style>', unsafe_allow_html=True)

st.markdown('<h1><b style="color: #547eac;">Exports</b> to EU plunge by 40% in first month since Brexit</h1>', unsafe_allow_html=True)
st.markdown('<p>With the United Kingdom leaving the European Union at the end of January 2020, as well as the start of an 11 month transition period, it will have quite a negative impact on the UK economy.</p><p>In the trade sector, especially exports and imports, there was a sharp decline in the first quarter of 2020. Although during the transition period the United Kingdom remained subject to European Union law, it remained part of the EU Customs Union and the European Single Market.</p>', unsafe_allow_html=True)
    
with st.container():             
    df_temp = df[['split_year','exports','imports']]
    
    df_melt = pd.melt(df_temp,id_vars=['split_year'],var_name='Trade Type', value_name='Trade Values')
    df_export_import = pd.DataFrame(df_melt.groupby(['split_year','Trade Type'])['Trade Values'].sum()).reset_index()  
    df_export_import.rename(columns={'split_year':'Year'}, inplace=True)
    
    axisList = ['Year','Trade Values','Trade Type']
    chart_data = vo.set_chart_option('line',df_export_import,axisList)   
    
    st.altair_chart(chart_data, use_container_width=True)

categoryList = list(df['category'].unique())

for category in categoryList:  
    with st.container():
        x_col1, x_col2, x_col3 = st.columns([1,2,2])
        
        with x_col1:
            st.markdown("<h5>"+category+"</h5>", unsafe_allow_html=True)
            
        with x_col2:         
            exportAxisList = ['Year','Exports Values']
            
            df_temp_export = df[df['category'] == category][['split_year','exports']]
            df_export = pd.DataFrame(df_temp_export.groupby('split_year')['exports'].sum()).reset_index()
            df_export.rename(columns={'split_year':'Year'}, inplace=True)
            df_export.rename(columns={'exports':'Exports Values'}, inplace=True)
            
            chart_data_export = vo.set_chart_option('area',df_export,exportAxisList) 
            
            st.altair_chart(chart_data_export, use_container_width=True)              
        
        with x_col3:
            importAxisList = ['Year','Imports Values']
            
            df_temp_import = df[df['category'] == category][['split_year','imports']]
            df_import = pd.DataFrame(df_temp_import.groupby('split_year')['imports'].sum()).reset_index()
            df_import.rename(columns={'split_year':'Year'}, inplace=True)
            df_import.rename(columns={'imports':'Imports Values'}, inplace=True)
            
            chart_data_import = vo.set_chart_option('area',df_import,importAxisList) 
            
            st.altair_chart(chart_data_import, use_container_width=True)
        
with st.container():
    footer_col1, footer_col2 = st.columns(2)
    
    with footer_col1:
        st.markdown('<div style="text-align: left;">Design by: <a href="https://www.linkedin.com/in/rahman-firmansyah-79283512b" target="_blank">Rahman Firmansyah</a></div>', unsafe_allow_html=True)
        
    with footer_col2:
        st.markdown('<div style="text-align: right;">Data source: <a href="https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/datasets/uktradegoodsandservicespublicationtables">ONS (UK trade: goods and services publication table 14)</a></div>', unsafe_allow_html=True)                                                                        