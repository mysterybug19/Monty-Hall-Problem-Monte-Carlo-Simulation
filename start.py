import random
import pandas as pd
import numpy as np
import streamlit as st
import os

st.set_page_config(page_title="Simulare Monty Hall")

if "page" not in st.session_state:
    st.session_state.page = "intro"
if "idx" not in st.session_state:
    st.session_state.idx = 0
if "answers" not in st.session_state:
    st.session_state.answers = {}

@st.cache_resource

#Intro
if st.session_state.page == "intro":
    st.title("Simulare Monty Hall")
    st.markdown("""
    Platforma ce explică acestă problemă clasică de statistică și efectuază simulări pe baza acestor rezultate.
    """)

    if st.button("Jocul", use_container_width=True):
        st.session_state.page = "game"
        st.rerun()

    if st.button("Explicație", use_container_width=True):
        st.session_state.page = "explenation"
        st.rerun()

    if st.button("Simulare", use_container_width=True):
        st.session_state.page = "simulation"
        st.rerun()

#Game
if st.session_state.page == "game":
    st.title("Simulare Monty Hall")

    if st.button("Back"):
        st.session_state.page = "intro"
        st.rerun()
    
