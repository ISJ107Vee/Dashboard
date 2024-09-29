# import external functions and python libraries 
from data_cleansing import cleanse
from render_function import render
import webbrowser
from streamlit_option_menu import option_menu
import streamlit as st
from plot_function import plot
import plotly_express as px
from faculties import faculty
import os

# setting up the page
st.set_page_config(page_title="TUT Feedback Dashboard",
                   page_icon=":bar_chart",
                   layout="wide"
)

#getting dataframe
factors_df = cleanse()

#--------------------------Sidebar----------------------------------

# creating side bar menu
with st.sidebar:

    # creating selection options with radio buttons
    selected = option_menu(

        menu_title = "Dashboard Menu",
        options = ['Home', 'Faculty', 'Support', 'Career Outcomes','Logout'],
        menu_icon = "cast",
        default_index = 0,
    )

    st.image("TUT-Logo1.jpg")


#-------------------------Main Page-----------------------------------

st.title(":bar_chart: TUT Student Feedback Dashboard")
st.markdown("##")

rating_type = "TUT Rating"

# Tut average rating
rating = int(round(factors_df['TUT Rating'].mean(),0))

# tut average rating in stars
star_rating = ":star:"*rating

# number of total respondents
total_entries = factors_df.shape[0]

# creating options for pages based on selected options
if selected == "Home":

    # setting up the main page
    render(rating_type, rating, total_entries, star_rating)    

    plot(
        
        'TUT Rating','TUT Rating Distribution','Lecture Ratings',
        'Lecture Rating Distribution','h','v'
    )

    plot(

        'Challenges With Lecturers','Challenges With Lecturers',
        'Recommendations','Respondents Recommendations','h','h'
    )

elif selected == "Faculty":

    faculty()

elif selected == "Support":

    # NSFAS Rating
    NSFAS_Rating = factors_df[factors_df['NSFAS Process Rating'] != 0]['NSFAS Process Rating'].mean()

    NSFAS_Rating = int(round(NSFAS_Rating,0))

    star_rating = ":star:"*NSFAS_Rating

    # NSFAS Funded Students
    NSFAS_Count = factors_df[factors_df['NSFAS Process Rating'] != 0]['NSFAS Process Rating'].count()

    render("NSFAS Process Rating", NSFAS_Rating, NSFAS_Count, star_rating)

    plot(

        'Support','Support Outside Lectures','Funding',
        'Student Funding Distribution','v','h'
    )

    plot(

        'Residence','Student Residence Distribution',
        'Reason for Off Campus Stay','Reason for Off Campus Stay','v','h'
    )

    plot(

        'NSFAS Application Process','NSFAS Application Process Challenges',
        'Recommendations On NSFAS Process',
        'Recommendations On NSFAS Application Process','v','h'
    )

elif selected == "Career Outcomes":

    # setting up the main page
    render(rating_type, rating, total_entries, star_rating)

    plot(

        'Employment Status','Are You Currently Employed',
        'Employed In Field Of Study','Employed In Field Of Study','v','h'
    )

    plot(

        'Period Spent Looking For Work','Period Spent Looking For Work',
        'Was It Easy Applying Undergrad Knowledge','Was It Easy Applying Undergrad Knowledge',
        'h','h'
    )

    figure = px.bar(
        factors_df['Career Aspirations'].value_counts(), 
        title='Student Career Aspirations During Undergrad', 
        orientation = 'h'
    )

    figure.update_layout(
        plot_bgcolor = "rgba(0,0,0,0)",
        xaxis = (dict(showgrid=False))
    )

    st.plotly_chart(figure)

elif selected == "Logout":

    os.system("taskkill /im firefox.exe /f")
    os.system("taskkill /im chrome.exe /f")
    os.system("taskkill /im brave.exe /f")

    webbrowser.open("https://www.lucyheresy.com/")

#----------------------------------Styling-----------------------------------
hide_st_style = """
       
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """

st.markdown(hide_st_style, unsafe_allow_html=True)