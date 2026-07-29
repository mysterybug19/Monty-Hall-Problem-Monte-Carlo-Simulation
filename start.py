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

#Simulations
if st.session_state.page == "simulation_nr":
    st.title("Simulare Monty Hall")
    st.header("Alege numărul de simulări")
    st.session_state.N=st.number_input("Număr Simulări (1-10e8)", min_value=1, max_value=100000000)
    col1, col2 = st.columns(2)
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
    fig.update_layout(title="Monty Hall Convergence",xaxis_title="Number of simulations",yaxis_title="Probability",)
    fig.update_xaxes(type="log")
    fig.add_hline(y=1/3, line_dash="dash")
    fig.add_hline(y=2/3, line_dash="dash")
    
    st.headline("Procente finale:")
    st.markdown("Victorii dacă nu schimb")
    st.progress(stay_rate[-1]/100.00)
    st.caption(f"{stay_rate[-1]:.1f}%")
    st.markdown("Victorii dacă schimb")
    st.progress(switch_rate[-1]/100.00)
    st.caption(f"{switch_rate[-1]:.1f}%")
    st.divider()
    st.headline("Grafic:")
    st.plotly_chart(fig, use_container_width=True)
    
    if st.button("Înapoi"):
        st.session_state.page = "intro"
        st.rerun()
    
