

import streamlit as st
import json
import os
import matplotlib.pyplot as plt

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

# Interface utilisateur
def main():
    st.title("Calculateur de Puissance et de Rendement d'un Transformateur")

    # Charger les calculs précédents
    file_path = 'calculations.json'
    data = load_data(file_path)

    # Saisie des données
    st.header("Nouveau Calcul")
    input_voltage = st.number_input("Tension d'entrée (V)", min_value=0.0)
    output_voltage = st.number_input("Tension de sortie (V)", min_value=0.0)
    input_current = st.number_input("Courant d'entrée (A)", min_value=0.0)
    output_current = st.number_input("Courant de sortie (A)", min_value=0.0)

    if st.button("Calculer"):
        power_in, power_out, efficiency = calculate_power_and_efficiency(input_voltage, output_voltage, input_current, output_current)
        st.write(f"Puissance d'entrée : {power_in} W")
        st.write(f"Puissance de sortie : {power_out} W")
        st.write(f"Rendement : {efficiency:.2f} %")

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

    # Afficher l'historique des calculs
    st.header("Historique des Calculs")
    for item in data:
        st.write(f"ID: {item['id']}")
        st.write(f"Tension d'entrée : {item['input_voltage']} V")
        st.write(f"Tension de sortie : {item['output_voltage']} V")
        st.write(f"Courant d'entrée : {item['input_current']} A")
        st.write(f"Courant de sortie : {item['output_current']} A")
        st.write(f"Puissance d'entrée : {item['power_in']} W")
        st.write(f"Puissance de sortie : {item['power_out']} W")
        st.write(f"Rendement : {item['efficiency']:.2f} %")
        
        # Options pour modifier ou supprimer un calcul
        if st.button(f"Supprimer le calcul {item['id']}"):
            data = [i for i in data if i['id'] != item['id']]
            save_data(file_path, data)
            st.experimental_rerun()

    # Graphe de l'efficacité
    st.header("Graphique du Rendement")
    efficiencies = [item['efficiency'] for item in data]
    if efficiencies:
        plt.plot(range(len(efficiencies)), efficiencies, marker='o')
        plt.xlabel("Calcul #")
        plt.ylabel("Rendement (%)")
        st.pyplot(plt)

if __name__ == "__main__":
    main()
