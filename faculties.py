import pandas as pd
import numpy as np
from render_function import render
from plot_function import plot
from data_cleansing import cleanse
from streamlit_option_menu import option_menu

# dataframe
factors_df = cleanse()

# old faculties
faculties = list(factors_df['Faculty'].unique())

# Shortening faculty names
new_faculties = ['ICT','The Arts','EBE','Humanities','Ecos & Finance','Management Sci','Science']

factors_df['Faculty'] = factors_df['Faculty'].replace(faculties,new_faculties)

def faculty():

    selected = option_menu(
        menu_title = None,
        options = list(factors_df['Faculty'].unique()),
        menu_icon = 'cast',
        default_index = 0,
        orientation = 'horizontal'
    )

    if selected == 'ICT':

        # filtering by faculty
        Faculty_df = factors_df[factors_df['Faculty'] == 'ICT']

        rating_type = 'Lecturer Rating' # lecture rating
        
        # rating value
        rating = int(round(Faculty_df['Lecture Ratings'].mean(),0))

        star_rating = ":star:"*rating # getting star rating

        total_entries =  Faculty_df.shape[0] # getting number of respondents

        # setting up the main page
        render(rating_type, rating, total_entries, star_rating)

        plot(
            
            'Registration Year','Student Registrations By Year','Graduation Status',
            'Stundent Graduation Stats','v','h', df=Faculty_df
        )

        plot(
            
            'Completion Period','Graduation On Record Time','Challenges With Lecturers',
            'Challenges With Lecturers','h','v', df=Faculty_df
        )

        plot(
            
            'Lecture Ratings','Faculty Lecturer Rating','Reason For Rating',
            'Reason For Faculty Lecturer Rating','h','v', df=Faculty_df
        )
    
    elif selected == 'The Arts':

        # filtering by faculty
        Faculty_df = factors_df[factors_df['Faculty'] == 'The Arts']

        rating_type = 'Lecturer Rating' # lecture rating
        
        # rating value
        rating = int(round(Faculty_df['Lecture Ratings'].mean(),0))

        star_rating = ":star:"*rating # getting star rating

        total_entries =  Faculty_df.shape[0] # getting number of respondents

        # setting up the main page
        render(rating_type, rating, total_entries, star_rating)

        plot(
            
            'Registration Year','Student Registrations By Year','Graduation Status',
            'Stundent Graduation Stats','v','h', df=Faculty_df
        )

        plot(
            
            'Completion Period','Graduation On Record Time','Challenges With Lecturers',
            'Challenges With Lecturers','h','v', df=Faculty_df
        )

        plot(
            
            'Lecture Ratings','Faculty Lecturer Rating','Reason For Rating',
            'Reason For Faculty Lecturer Rating','h','v', df=Faculty_df
        )
    
    elif selected == 'EBE':
        
        # filtering by faculty
        Faculty_df = factors_df[factors_df['Faculty'] == 'EBE']

        rating_type = 'Lecturer Rating' # lecture rating
        
        # rating value
        rating = int(round(Faculty_df['Lecture Ratings'].mean(),0))

        star_rating = ":star:"*rating # getting star rating

        total_entries =  Faculty_df.shape[0] # getting number of respondents

        # setting up the main page
        render(rating_type, rating, total_entries, star_rating)

        plot(
            
            'Registration Year','Student Registrations By Year','Graduation Status',
            'Stundent Graduation Stats','v','h', df=Faculty_df
        )

        plot(
            
            'Completion Period','Graduation On Record Time','Challenges With Lecturers',
            'Challenges With Lecturers','h','v', df=Faculty_df
        )

        plot(
            
            'Lecture Ratings','Faculty Lecturer Rating','Reason For Rating',
            'Reason For Faculty Lecturer Rating','h','v', df=Faculty_df
        )
    
    elif selected == 'Humanities':

        # filtering by faculty
        Faculty_df = factors_df[factors_df['Faculty'] == 'Humanities']

        rating_type = 'Lecturer Rating' # lecture rating
        
        # rating value
        rating = int(round(Faculty_df['Lecture Ratings'].mean(),0))

        star_rating = ":star:"*rating # getting star rating

        total_entries =  Faculty_df.shape[0] # getting number of respondents

        # setting up the main page
        render(rating_type, rating, total_entries, star_rating)

        plot(
            
            'Registration Year','Student Registrations By Year','Graduation Status',
            'Stundent Graduation Stats','v','h', df=Faculty_df
        )

        plot(
            
            'Completion Period','Graduation On Record Time','Challenges With Lecturers',
            'Challenges With Lecturers','h','v', df=Faculty_df
        )

        plot(
            
            'Lecture Ratings','Faculty Lecturer Rating','Reason For Rating',
            'Reason For Faculty Lecturer Rating','h','v', df=Faculty_df
        )
    
    elif selected == 'Ecos & Finance':

        # filtering by faculty
        Faculty_df = factors_df[factors_df['Faculty'] == 'Ecos & Finance']

        rating_type = 'Lecturer Rating' # lecture rating
        
        # rating value
        rating = int(round(Faculty_df['Lecture Ratings'].mean(),0))

        star_rating = ":star:"*rating # getting star rating

        total_entries =  Faculty_df.shape[0] # getting number of respondents

        # setting up the main page
        render(rating_type, rating, total_entries, star_rating)

        plot(
            
            'Registration Year','Student Registrations By Year','Graduation Status',
            'Stundent Graduation Stats','v','h', df=Faculty_df
        )

        plot(
            
            'Completion Period','Graduation On Record Time','Challenges With Lecturers',
            'Challenges With Lecturers','h','v', df=Faculty_df
        )

        plot(
            
            'Lecture Ratings','Faculty Lecturer Rating','Reason For Rating',
            'Reason For Faculty Lecturer Rating','h','v', df=Faculty_df
        )
    
    elif selected == 'Management Sci':

        # filtering by faculty
        Faculty_df = factors_df[factors_df['Faculty'] == 'Management Sci']

        rating_type = 'Lecturer Rating' # lecture rating
        
        # rating value
        rating = int(round(Faculty_df['Lecture Ratings'].mean(),0))

        star_rating = ":star:"*rating # getting star rating

        total_entries =  Faculty_df.shape[0] # getting number of respondents

        # setting up the main page
        render(rating_type, rating, total_entries, star_rating)

        plot(
            
            'Registration Year','Student Registrations By Year','Graduation Status',
            'Stundent Graduation Stats','v','h', df=Faculty_df
        )

        plot(
            
            'Completion Period','Graduation On Record Time','Challenges With Lecturers',
            'Challenges With Lecturers','h','v', df=Faculty_df
        )

        plot(
            
            'Lecture Ratings','Faculty Lecturer Rating','Reason For Rating',
            'Reason For Faculty Lecturer Rating','h','v', df=Faculty_df
        )
    
    elif selected == 'Science':

        # filtering by faculty
        Faculty_df = factors_df[factors_df['Faculty'] == 'Science']

        rating_type = 'Lecturer Rating' # lecture rating
        
        # rating value
        rating = int(round(Faculty_df['Lecture Ratings'].mean(),0))

        star_rating = ":star:"*rating # getting star rating

        total_entries =  Faculty_df.shape[0] # getting number of respondents

        # setting up the main page
        render(rating_type, rating, total_entries, star_rating)

        plot(
            
            'Registration Year','Student Registrations By Year','Graduation Status',
            'Stundent Graduation Stats','v','h', df=Faculty_df
        )

        plot(
            
            'Completion Period','Graduation On Record Time','Challenges With Lecturers',
            'Challenges With Lecturers','h','v', df=Faculty_df
        )

        plot(
            
            'Lecture Ratings','Faculty Lecturer Rating','Reason For Rating',
            'Reason For Faculty Lecturer Rating','h','v', df=Faculty_df
        )
    
    else:

        pass