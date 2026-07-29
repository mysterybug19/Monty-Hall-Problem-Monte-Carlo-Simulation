import random
import pandas as pd
import numpy as np
import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="Simulare Monty Hall")

if "page" not in st.session_state:
    st.session_state.page = "intro"
if "N" not in st.session_state:
    st.session_state.N = 0
if "player_door" not in st.session_state:
    st.session_state.player_door=0
    
#Intro
if st.session_state.page == "intro":
    st.title("Simulare Monty Hall")
    st.divider()
    st.markdown("""Platforma ce explică acestă problemă clasică de statistică și efectuază simulări pe baza acestor rezultate.""")

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
    st.markdown("""Regulile jocului: Regulile Problemei lui Monty Hall presupun trei uși închise, o mașină ascunsă și două capre. Jucătorul alege o ușă, prezentatorul deschide altă ușă cu o capră, iar jucătorul decide dacă păstrează sau schimbă ușa.""")
    col1, col2, col3= st.columns(3)
    with col1:
        if st.button("Ușa 1", use_container_width=True):
            st.session_state.player_door=1
            st.session_state.page = "game1"
            st.rerun()
    with col2:
        if st.button("Ușa 2", use_container_width=True):
            st.session_state.player_door=2
            st.session_state.page = "game1"
            st.rerun()
    with col3:
        if st.button("Ușa 3", use_container_width=True):
            st.session_state.player_door=3
            st.session_state.page = "game1"
            st.rerun()
    if st.button("Înapoi"):
        st.session_state.page = "intro"
        st.rerun()
#Explenation
if st.session_state.page == "explenation":
    st.title("Explicație")
    st.divider()
    if st.button("Înapoi"):
        st.session_state.page = "intro"
        st.rerun()

if st.session_state.page == "game1":
    st.title("Jocul")
    st.divider()
    doors=[1,2,3]
    car_door = random.choice(doors)
    player_door=st.session_state.player_door
    possible_door = [d for d in doors if d != player_door and d != car_door]
    host_door = random.choice(possible_door)
    ch_host=str(host_door)
    st.markdown("Ușa "+ ch_host+ "ascundea o capră. Ce alegi, păstrezi decizia sau o schimbi?")
    col1, col2= st.columns(2)
    with col1:
        if st.button("Păstrez", use_container_width=True):
            if player_door==car_door:
                st.session_state.page = "winner"
                st.rerun()
            else:
                st.session_state.page = "losser"
                st.rerun()
    with col2:
        if st.button("Schimb", use_container_width=True):
            if player_door==car_door:
                st.session_state.page = "losser"
                st.rerun()
            else:
                st.session_state.page = "winner"
                st.rerun()
    if st.button("Înapoi"):
        st.session_state.page = "game"
        st.rerun()
#Winner
if st.session_state.page == "winner":
    st.title("Ai câiștigat")
    st.ballons()
    if st.button("Înapoi"):
        st.session_state.page = "intro"
        st.rerun()
if st.session_state.page == "loser":
    st.title("Ai pierdut")
    if st.button("Înapoi"):
        st.session_state.page = "intro"
        st.rerun()
    
#Simulations
if st.session_state.page == "simulation_nr":
    st.title("Simulare Monty Hall")
    st.header("Alege numărul de simulări")
    st.session_state.N=st.number_input("Număr Simulări (1-10e7)", min_value=1, max_value=10000000)
    col1, col2= st.columns(2)
    with col1:
        if st.button("Înapoi", use_container_width=True):
            st.session_state.page = "intro"
            st.rerun()

    with col2:
        if st.button("Rulează simularea", use_container_width=True):
            st.session_state.page = "simulation"
            st.rerun()
    
if st.session_state.page == "simulation":
    st.title("Simulare Monty Hall")
    st.divider()
    doors=[1,2,3]
    N=st.session_state.N
    
    car=np.random.randint(0,3,N)
    player=np.random.randint(0,3,N)
    
    stay_win=(player==car)
    switch_win=~stay_win

    stay_rate=100*np.cumsum(stay_win)/np.arange(1,N+1)
    switch_rate=100*np.cumsum(switch_win)/np.arange(1,N +1)

    idx=np.unique(np.logspace(0,np.log10(N),min(5000,N),dtype=int)-1)

    x=idx+1
    stay_plot=stay_rate[idx]
    switch_plot=switch_rate[idx]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x,y=stay_plot,mode="lines",name="Stay"))
    fig.add_trace(go.Scatter(x=x,y=switch_plot,mode="lines",name="Switch"))
    fig.update_layout(title="Convergența Monty Hall",xaxis_title="Number of simulations",yaxis_title="Probability",)
    fig.update_xaxes(type="log")
    fig.add_hline(y=1/3, line_dash="dash")
    fig.add_hline(y=2/3, line_dash="dash")
    
    st.header("Procente finale:")
    st.markdown("Victorii dacă nu schimb")
    st.progress(stay_rate[-1]/100.00)
    st.caption(f"{stay_rate[-1]:.1f}%")
    st.markdown("Victorii dacă schimb")
    st.progress(switch_rate[-1]/100.00)
    st.caption(f"{switch_rate[-1]:.1f}%")
    st.divider()
    st.header("Grafic:")
    st.plotly_chart(fig, use_container_width=True)
    
    if st.button("Înapoi"):
        st.session_state.page = "intro"
        st.rerun()
    
