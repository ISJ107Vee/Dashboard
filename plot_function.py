# import external functions and libraries
import plotly_express as px
from data_cleansing import cleanse
import streamlit as st

# function to plot two bar charts side by side
def plot(column1,title1,column2,title2,pos1,pos2,df = cleanse()):
    
    # setting up the first plot
    fig1 = px.bar(
        df[column1].value_counts(), 
        title=title1, 
        orientation = pos1
    )
    
    fig1.update_layout(
        plot_bgcolor = "rgba(0,0,0,0)",
        xaxis = (dict(showgrid=False))
    )
    
    # setting up the second plot
    fig2 = px.bar(
        df[column2].value_counts(), 
        title=title2, 
        orientation = pos2
    )

    fig2.update_layout(
        plot_bgcolor = "rgba(0,0,0,0)",
        xaxis = (dict(showgrid=False))
    )
    
    # plotting charts side by side
    left_column, right_column = st.columns(2)
    left_column.plotly_chart(fig1, use_container_width=True)
    right_column.plotly_chart(fig2, use_container_width=True)