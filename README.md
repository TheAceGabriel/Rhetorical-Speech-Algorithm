## Why?
Because I got the idea that some speeches work like software for programming humans, and there's a pattern.

## The Algorithm

The speech generation process can be represented mathematically using the following formula:

### Variables

- L = Leader
- T = Topic
- A = Audience
- G = Goal
- V = Values
- P = Positive Vision
- F = Future Goal
- Adv = Adversary
- Emo = Emotion
- Act = Actions

### Functions

- R(p, n) = Repeat phrase p n times.
- Q(q) = Rhetorical question q.
- L_C(V) = List of values or actions V.

### Final Formula

\[
S = I(A) + R(P_1(Adv, G), 3) + Q(P_2) + L_C(V) + L_C(Act) + Emo(Emo) + V(F, G, P) + C(T, P)
\]

Where:

- **Introduction**:
\[
  I(A) = "My fellow " + A + ", today we stand at a crossroads."
\]
  
- **Repetition (emphasis on adversary and goal)**:
\[
  P_1(Adv, G) = "How long can we allow " + Adv + " to hinder our " + G + "?"
\]

- **Rhetorical Question**:
\[
  P_2 = "Are we ready to rise to the occasion?"
\]

- **List of Values**:
\[
  L_C(V) = "We believe in the core values of " + \{ V_1, V_2, ..., V_n \}
\]

- **List of Actions**:
\[
  L_C(Act) = "It is these values that will guide us as we " + \{ Act_1, Act_2, ..., Act_n \}
\]

- **Emotional Appeal**:
\[
  Emo(Emo) = "I feel the " + Emo + " in every corner of this nation!"
\]

- **Vision for the Future**:
\[
  V(F, G, P) = "Let us strive for " + P + ". Together, we will " + G + ", and through unity, achieve " + F
\]

- **Closing**:
\[
  C(T, P) = "Together, we will " + P + ". Together, we will succeed! Thank you, and may " + T + " reign forever."
\]

### Explanation of the Formula

- **Introduction**: I(A) introduces the speech to the audience.
- **Repetition**: R(P_1, 3) emphasizes the struggle with the adversary using repetition.
- **Rhetorical Question**: Q(P_2) poses a challenge to the audience.
- **Core Values and Actions**: L_C(V) and L_C(Act) present values and actions as lists.
- **Emotion**: Emo(Emo) makes an emotional appeal to the audience.
- **Vision**: V(F, G, P) paints a positive vision for the future.
- **Closing**: C(T, P) provides a unifying and hopeful conclusion.

# Code (generate_speech.py)

This is a Python script that generates a political speech using rhetorical devices like repetition and rhetorical questions. The variables for the speech, such as leader name, values, and goals, are defined in thr `config.json` file.

## Features

- Customizable speech variables
- Automatically generates common rhetorical devices
- Flexible and adaptable to any spoken language

## To Do
- Test across various languages
- Move more of the speech compone ts into JSON

## Requirements

- Python 3.x

## Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/speech-generator.git
   cd speech-generator
