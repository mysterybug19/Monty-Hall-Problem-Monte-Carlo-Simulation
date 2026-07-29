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
if "N" not in st.session_state:
    st.session_state.N = 0
if "stay_wins" not in st.session_state:
    st.session_state.stay_wins = 0
if "switch_wins" not in st.session_state:
    st.session_state.switch_wins = 0
    
#Intro
if st.session_state.page == "intro":
    st.title("Simulare Monty Hall")
    st.divider()
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
        st.session_state.page = "simulation_nr"
        st.rerun()

#Game
if st.session_state.page == "game":
    st.title("Jocul")
    st.divider()
    if st.button("Back"):
        st.session_state.page = "intro"
        st.rerun()
#Explenation
if st.session_state.page == "explenation":
    st.title("Explicație")
    st.divider()
    if st.button("Back"):
        st.session_state.page = "intro"
        st.rerun()

#Simulations
if st.session_state.page == "simulation_nr":
    st.title("Simulare Monty Hall")
    st.header("Alege numărul de simulări")
    st.session_state.N=st.number_input("Număr Simulări (1-10e6)", min_value=1, max_value=1000000)
    st.session_state.idx  = 0
    st.session_state.stay_wins = 0
    st.session_state.switch_wins = 0
    st.session_state.page = "simulation"
    
if st.session_state.page == "simulation":
    st.title("Simulare Monty Hall")
    st.divider()
    doors=[1,2,3]
    N=st.session_state.N
    idx=st.session_state.idx
    if idx<N
        car = random.choice(doors)
        player = random.choice(doors)
        possible = [d for d in doors if d != player and d != car]
        host = random.choice(possible)
        switch = [d for d in doors if d != player and d != host][0]
        if player == car:
            st.session_state.stay_wins += 1
        if switch == car:
            st.session_state.switch_wins += 1
        stay_wins=st.session_state.stay_wins
        switch_wins=st.session_state.switch_wins
        st.markdown("Victorii dacă nu schimb")
        st.progress(float(stay_wins)/float(N))
        st.caption(str(float(stay_wins)/float(N)))
        st.markdown("Victorii dacă schimb")
        st.progress(float(switch_wins)/float(N))
        st.caption(str(float(switch_wins)/float(N)))
        st.rerun()
    else:
        stay_wins=st.session_state.stay_wins
        switch_wins=st.session_state.switch_wins
        st.markdown("Victorii dacă nu schimb")
        st.progress(float(stay_wins)/float(N))
        st.caption(str(float(stay_wins)/float(N)))
        st.markdown("Victorii dacă schimb")
        st.progress(float(switch_wins)/float(N))
        st.caption(str(float(switch_wins)/float(N)))

    if st.button("Back"):
        st.session_state.page = "intro"
        st.rerun()
    
