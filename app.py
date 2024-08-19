from pyneet import diabetes
from pyneet import analysis
import streamlit as st
import seaborn as sns
import base64
import numpy as np


## optiopns


options = ['Diabetes', 'Datasets', 'Analysis']
selected_options = st.sidebar.selectbox("Menu", options=options)


### ---------dataframe-----------

data = analysis.dataFrame()


## -------- diabetes prediction ------------


if selected_options == 'Diabetes':
	dbts = diabetes.diabetes_prediction()
	

	

		
elif  selected_options == 'Analysis':
	st.title("")
	## heat map
	st.dataframe(analysis.dataFrame(), hide_index=True)
	analysis.heatMap()
	analysis.boxPlot()
	analysis.num_dist_plot()
	
else:
    df = analysis.dataFrame()
    st.dataframe(df, hide_index=True)
    st.markdown("<h4>Download the Datsets from Github</h4>", unsafe_allow_html=True)
    st.markdown("<a style=font-size:20px; href='https://github.com/kamaljit12'>Clock Here...</a>", unsafe_allow_html=True)
