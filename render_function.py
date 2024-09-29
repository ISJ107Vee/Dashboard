import streamlit as st

def render(rating_type, rating, total_entries, star_rating):
    
    # three colums to display the parameter of the function
    left_column, middle_column, right_column = st.columns(3)

    # TUT slogan on left column
    with left_column:
        st.subheader("TUT Slogan")
        st.subheader("We Empower People")
    
    # rating parameters
    with middle_column:
        st.subheader(rating_type)
        st.subheader(f"{rating} {star_rating}")
    
    # total number of respondents
    with right_column:
        st.subheader("Survey Entries")
        st.subheader(f"Entries: {total_entries}")
        
    st.markdown("---")