

import streamlit as st
import json
import os
import matplotlib.pyplot as plt
import random

# Charger les données depuis un fichier JSON
def load_data(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    return []

# Sauvegarder les données dans un fichier JSON
def save_data(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Calculer la puissance et le rendement
def calculate_power_and_efficiency(input_voltage, output_voltage, input_current, output_current):
    power_in = input_voltage * input_current
    power_out = output_voltage * output_current
    efficiency = (power_out / power_in) * 100 if power_in != 0 else 0
    return power_in, power_out, efficiency

# Fonction pour formater les valeurs avec des couleurs
def format_value(label, value, unit, color):
    return f'<span style="color:{color};">{label}: {value} {unit}</span>'

# Interface utilisateur
def main():
    st.title("Calculateur de Puissance et de Rendement d'un Transformateur")

    # Charger les calculs précédents
    file_path = 'calculations.json'
    data = load_data(file_path)

    # Affichage de l'historique des calculs dans la barre latérale
    st.sidebar.header("Historique des Calculs")
    for item in data:
        with st.sidebar.expander(f"Calcul {item['id']}", expanded=False):
            st.markdown(format_value("Tension d'entrée", item['input_voltage'], "V", "blue"), unsafe_allow_html=True)
            st.markdown(format_value("Tension de sortie", item['output_voltage'], "V", "green"), unsafe_allow_html=True)
            st.markdown(format_value("Courant d'entrée", item['input_current'], "A", "blue"), unsafe_allow_html=True)
            st.markdown(format_value("Courant de sortie", item['output_current'], "A", "green"), unsafe_allow_html=True)
            st.markdown(format_value("Puissance d'entrée", item['power_in'], "W", "blue"), unsafe_allow_html=True)
            st.markdown(format_value("Puissance de sortie", item['power_out'], "W", "green"), unsafe_allow_html=True)
            st.markdown(format_value("Rendement", f"{item['efficiency']:.2f}", "%", "red"), unsafe_allow_html=True)
            
            if st.button(f"Supprimer le calcul {item['id']}", key=f"delete_{item['id']}"):
                data = [i for i in data if i['id'] != item['id']]
                save_data(file_path, data)

                # Ajouter un paramètre aléatoire pour forcer le rechargement de la page
                st.experimental_set_query_params(updated=str(random.randint(0, 100000)))

    # Saisie des données pour un nouveau calcul
    st.header("Nouveau Calcul")
    input_voltage = st.number_input("Tension d'entrée (V)", min_value=0.0)
    output_voltage = st.number_input("Tension de sortie (V)", min_value=0.0)
    input_current = st.number_input("Courant d'entrée (A)", min_value=0.0)
    output_current = st.number_input("Courant de sortie (A)", min_value=0.0)

    if st.button("Calculer"):
        power_in, power_out, efficiency = calculate_power_and_efficiency(input_voltage, output_voltage, input_current, output_current)
        
        # Afficher les résultats avec des couleurs
        st.markdown(format_value("Puissance d'entrée", power_in, "W", "blue"), unsafe_allow_html=True)
        st.markdown(format_value("Puissance de sortie", power_out, "W", "green"), unsafe_allow_html=True)
        st.markdown(format_value("Rendement", f"{efficiency:.2f}", "%", "red"), unsafe_allow_html=True)

        # Enregistrer le calcul
        new_id = max([item['id'] for item in data], default=0) + 1
        data.append({
            "id": new_id,
            "input_voltage": input_voltage,
            "output_voltage": output_voltage,
            "input_current": input_current,
            "output_current": output_current,
            "power_in": power_in,
            "power_out": power_out,
            "efficiency": efficiency
        })
        save_data(file_path, data)

    # Graphe de l'efficacité
    st.header("Graphique du Rendement")
    efficiencies = [item['efficiency'] for item in data]
    if efficiencies:
        plt.figure(figsize=(8, 6))
        plt.plot(range(len(efficiencies)), efficiencies, marker='o', color='blue', linestyle='-', linewidth=2, markersize=8)
        plt.xlabel("Calcul #", fontsize=14)
        plt.ylabel("Rendement (%)", fontsize=14)
        plt.title("Évolution du Rendement des Transformateurs", fontsize=16)
        plt.grid(True)
        st.pyplot(plt)

if __name__ == "__main__":
    main()
