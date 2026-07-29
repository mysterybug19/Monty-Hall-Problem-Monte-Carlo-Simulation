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
# Problema lui Monty Hall

Problema lui Monty Hall este una dintre cele mai cunoscute probleme de probabilitate. Există **trei uși închise**:

- 🚗 În spatele unei uși se află o **mașină**.
- 🐐 În spatele celorlalte două uși se află **două capre**.

Jocul se desfășoară astfel:

1. Alegi una dintre cele trei uși.
2. Prezentatorul, care **știe unde se află mașina**, deschide una dintre celelalte două uși, dezvăluind întotdeauna o capră.
3. Ai apoi două opțiuni:
   - **Păstrezi** ușa aleasă inițial.
   - **Schimbi** alegerea cu cealaltă ușă rămasă închisă.

La prima vedere pare că, după deschiderea unei uși, fiecare dintre cele două uși rămase are o probabilitate de **50%** de a ascunde mașina. Totuși, această intuiție este greșită deoarece prezentatorul **nu deschide niciodată ușa cu mașina**.

---

# De ce este mai bine să schimbi?

Fără a pierde din generalitate (**WLOG**), presupunem că **mașina se află în spatele Ușii A**.

Inițial, fiecare ușă are aceeași probabilitate de a fi aleasă.

| Alegerea inițială | Probabilitate |
|-------------------|--------------:|
| Ușa A (mașina) | 1/3 |
| Ușa B (capră) | 1/3 |
| Ușa C (capră) | 1/3 |

Analizăm fiecare caz posibil.

### Cazul 1: Alegi Ușa A (probabilitate = 1/3)

Prezentatorul poate deschide fie Ușa B, fie Ușa C.

- **Păstrezi** → Câștigi
- **Schimbi** → Pierzi

Cum cele două variante sunt echiprobabile:

| Prezentatorul deschide | Probabilitate |
|-------------------------|--------------:|
| Ușa B | 1/6 |
| Ușa C | 1/6 |

---

### Cazul 2: Alegi Ușa B (probabilitate = 1/3)

Prezentatorul este obligat să deschidă Ușa C.

- **Păstrezi** → Pierzi
- **Schimbi** → Câștigi

---

### Cazul 3: Alegi Ușa C (probabilitate = 1/3)

Prezentatorul este obligat să deschidă Ușa B.

- **Păstrezi** → Pierzi
- **Schimbi** → Câștigi

---

# Combinarea probabilităților

| Alegerea inițială | Prezentatorul deschide | Probabilitate | Păstrezi | Schimbi |
|-------------------|------------------------|--------------:|:--------:|:--------:|
| A | B | 1/6 | ✅ | ❌ |
| A | C | 1/6 | ✅ | ❌ |
| B | C | 1/3 | ❌ | ✅ |
| C | B | 1/3 | ❌ | ✅ |

Adunând probabilitățile obținem:

- **Câștig dacă păstrezi:** 1/6 + 1/6 = **1/3 ≈ 33,3%**
- **Câștig dacă schimbi:** 1/3 + 1/3 = **2/3 ≈ 66,7%**

---

# Concluzie

Alegerea inițială are doar o **probabilitate de 1/3** de a fi corectă.

Celelalte două uși au împreună o probabilitate de **2/3** de a ascunde mașina. După ce prezentatorul elimină una dintre ele, dezvăluind o capră, întreaga probabilitate de **2/3** se transferă către singura ușă rămasă închisă.

Prin urmare:

- **Dacă păstrezi alegerea inițială, vei câștiga în aproximativ 33,3% din cazuri.**
- **Dacă schimbi ușa, vei câștiga în aproximativ 66,7% din cazuri.**

Simularea din această aplicație confirmă acest rezultat. Pe măsură ce numărul de simulări crește, probabilitățile observate se apropie de **1/3** pentru strategia de păstrare și de **2/3** pentru strategia de schimbare.
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
    
