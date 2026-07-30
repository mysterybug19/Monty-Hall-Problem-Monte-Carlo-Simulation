# Simulare Monty Hall

### Link

monty-hall-problem-monte-carlo-simulation.streamlit.app/

## Descriere

Acest proiect reprezintă o aplicație interactivă realizată în **Python** folosind biblioteca **Streamlit**, având scopul de a ilustra celebra problemă de probabilitate **Monty Hall**. Aplicația permite utilizatorului să înțeleagă conceptul atât prin intermediul unui joc interactiv, cât și printr-o demonstrație teoretică și simulări statistice.

Problema lui Monty Hall constă în alegerea uneia dintre trei uși, în spatele uneia aflându-se o mașină, iar în spatele celorlalte două câte o capră. După alegerea inițială, prezentatorul deschide întotdeauna o ușă care ascunde o capră, iar jucătorul poate decide dacă păstrează alegerea inițială sau o schimbă. În mod contraintuitiv, schimbarea ușii dublează probabilitatea de câștig.

---

## Funcționalități

Aplicația este împărțită în trei componente principale:

### Joc interactiv

Utilizatorul poate simula problema Monty Hall prin alegerea unei uși și poate decide ulterior dacă își păstrează alegerea sau o schimbă. La final este afișat rezultatul jocului.

### Explicație teoretică

Aplicația oferă o prezentare detaliată a problemei, incluzând:

* descrierea regulilor jocului;
* demonstrația probabilistică;
* analiza tuturor cazurilor posibile;
* justificarea matematică a strategiei optime.

### Simulare statistică

Utilizatorul poate alege un număr de simulări cuprins între **1** și **10.000.000**.

Pentru fiecare simulare sunt calculate rezultatele strategiilor:

* păstrarea alegerii inițiale;
* schimbarea ușii.

Rezultatele sunt afișate sub forma:

* procentelor finale de câștig;
* unui grafic al convergenței probabilităților către valorile teoretice.

---

## Tehnologii utilizate

* Python 3
* Streamlit
* NumPy
* Pandas
* Plotly

---

## Instalare

1. Clonați repository-ul:

```bash
git clone <repository_url>
cd <repository>
```

2. Instalați dependențele:

```bash
pip install -r requirements.txt
```

3. Rulați aplicația:

```bash
streamlit run app.py
```

---

## Structura aplicației

Aplicația este organizată în următoarele secțiuni:

* Pagina principală;
* Jocul Monty Hall;
* Explicația teoretică;
* Simularea statistică.

Navigarea între secțiuni este realizată prin intermediul obiectului `st.session_state`.

---

## Rezultate așteptate

Pe măsură ce numărul de simulări crește, probabilitățile observate converg către valorile teoretice:

| Strategie         | Probabilitate |
| ----------------- | ------------: |
| Păstrezi alegerea |       ≈ 33,3% |
| Schimbi alegerea  |       ≈ 66,7% |

Acest comportament confirmă rezultatele teoretice ale problemei și ilustrează legea numerelor mari.

---

## Scopul proiectului

Obiectivele principale ale aplicației sunt:

* prezentarea intuitivă a problemei Monty Hall;
* explicarea rezultatului probabilistic asociat;
* demonstrarea experimentală a avantajului schimbării ușii;
* utilizarea simulărilor Monte Carlo pentru validarea rezultatelor teoretice.

---
