import streamlit as st
import random as rnd

st.set_page_config(
    "Guessing Game"
)

if 'number' not in st.session_state:
    st.session_state.number = None
if 'number_from' not in st.session_state:
    st.session_state.number_from = None
if 'number_to' not in st.session_state:
    st.session_state.number_to = None
if 'number_of_guesses' not in st.session_state:
    st.session_state.number_of_guesses = None
if 'passed1' not in st.session_state:
    st.session_state.passed1 = False
if 'end' not in st.session_state:
    st.session_state.end = False
if 'name' not in st.session_state:
    st.session_state.name = False


if not st.session_state.name:
    st.session_state.name = st.text_input("Hello! What is your name?")

if st.session_state.name and (not st.session_state.passed1):
    with st.form("form1"):
        st.session_state.number_of_guesses = st.number_input(
            f'{st.session_state.name.capitalize()} how lucky do you think you\
                 are? How many guesses do you want?',
            min_value=1,
            max_value=10,
            value=5
        )
        st.session_state.number_from = st.number_input(
            'Pick your smallest number for the range, what would you like it to\
                 be?',
            min_value=1,
            max_value=100
        )
        st.session_state.number_to = st.number_input(
            'Pick your largest number for the range, what would you like it to\
                 be?',
            min_value=2,
            max_value=100
        )
        submitted1 = st.form_submit_button("Submit")

    # need to validate user inputs
    if submitted1:
        if not (st.session_state.number_to > st.session_state.number_from):
            st.error('Sorry, the largest number must be larger than\
                    smallest!')
        else:
            st.session_state.passed1 = True
            # the number generation has to be outside of guessing form,
            # otherwise it keeps generating a new number
            st.session_state.number = rnd.randint(
                st.session_state.number_from, st.session_state.number_to)

if st.session_state.passed1 and (not st.session_state.end):
    f'Well, {st.session_state.name} I am thinking of a number\
         between {st.session_state.number_from} and\
              {st.session_state.number_to}.'

    with st.form("form2"):
        guess = st.number_input(
            '',
            min_value=1,
            max_value=100
        )
        submitted2 = st.form_submit_button("Submit")

    if submitted2:
        st.session_state.number_of_guesses -= 1
        st.info(f"You have {st.session_state.number_of_guesses} chances left")
        if guess < st.session_state.number_from \
                or guess > st.session_state.number_to:
            st.warning("That is out of range, FOOL!")
        elif guess < st.session_state.number:
            st.warning("That is less than my number!")
        elif guess > st.session_state.number:
            st.warning("That is bigger than my number!")
        else:
            st.success("You won!")
            st.session_state.end = True

        if st.session_state.number_of_guesses == 0:
            st.error(f"You lost! The number I was thinking was\
                 {st.session_state.number}")
            st.session_state.end = True

if st.session_state.end:
    '''
    # Thanks for playing!
    ## Refresh the page if you wish to play again!
    '''
