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

if st.session_state.page == "game1":
    st.title("Jocul")
    st.divider()
    doors=[1,2,3]
    car_door = random.choice(doors)
    player_door=st.session_state.player_door
    possible_door = [d for d in doors if d != player_door and d != car_door]
    host_door = random.choice(possible_door)
    ch_host=str(host_door)
    st.markdown("Ușa "+ ch_host+ " ascundea o capră. Ce alegi, păstrezi decizia sau o schimbi?")
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
    st.markdown("Ai câiștigat o mașină nouă!!!")
    st.balloons()
    if st.button("Înapoi"):
        st.session_state.page = "intro"
        st.rerun()
if st.session_state.page == "losser":
    st.title("Ai pierdut")
    st.markdown("Privește partea bună, acum ai o capră :)")
    if st.button("Înapoi"):
        st.session_state.page = "intro"
        st.rerun()
#Explenation
if st.session_state.page == "explenation":
    st.title("Explicație")
    st.divider()
    st.markdown("""
# The Monty Hall Problem

The Monty Hall problem is a famous probability puzzle. There are **three closed doors**:

- 🚗 Behind one door is a **car**.
- 🐐 Behind the other two doors are **goats**.

The game works as follows:

1. You choose one of the three doors.
2. The host, who **knows where the car is**, opens one of the remaining doors, always revealing a goat.
3. You are then given a choice:
   - **Stay** with your original door.
   - **Switch** to the other unopened door.

At first glance it seems that, after one goat is revealed, each remaining door should have a 50% chance of hiding the car. However, this intuition is incorrect because the host never reveals the car.

---

# Why does switching work?

Without loss of generality, assume the **car is behind Door A**.

Initially, every door is equally likely to be chosen.

| Your initial choice | Probability |
|---------------------|------------:|
| Door A (car) | 1/3 |
| Door B (goat) | 1/3 |
| Door C (goat) | 1/3 |

Now consider each possible case.

### Case 1: You choose Door A (probability = 1/3)

The host can reveal either Door B or Door C.

- **Stay** → Win
- **Switch** → Lose

Since each host choice is equally likely:

| Host opens | Probability |
|------------|------------:|
| Door B | 1/6 |
| Door C | 1/6 |

---

### Case 2: You choose Door B (probability = 1/3)

The host **must** reveal Door C.

- **Stay** → Lose
- **Switch** → Win

---

### Case 3: You choose Door C (probability = 1/3)

The host **must** reveal Door B.

- **Stay** → Lose
- **Switch** → Win

---

# Combining the probabilities

| Initial choice | Host opens | Probability | Stay | Switch |
|----------------|------------|------------:|:----:|:------:|
| A | B | 1/6 | ✅ | ❌ |
| A | C | 1/6 | ✅ | ❌ |
| B | C | 1/3 | ❌ | ✅ |
| C | B | 1/3 | ❌ | ✅ |

Adding the probabilities:

- **Stay wins:** 1/6 + 1/6 = **1/3 ≈ 33.3%**
- **Switch wins:** 1/3 + 1/3 = **2/3 ≈ 66.7%**

---

# Conclusion

Your initial choice has only a **1/3 probability** of being correct.

The remaining **2/3 probability** belongs to the other two doors. Once the host reveals a goat, that entire **2/3 probability** transfers to the only unopened door.

Therefore:

- **Staying wins with probability 1/3 (33.3%).**
- **Switching wins with probability 2/3 (66.7%).**

The simulation on the next page demonstrates this result experimentally. As the number of simulations increases, the win rates converge to approximately **33.3%** for staying and **66.7%** for switching.
""")
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
    
