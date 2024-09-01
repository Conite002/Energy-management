# Transformer Power and Efficiency Calculator

## Description

This application allows users to calculate the power and efficiency of a transformer. It features an interactive interface for inputting data, performing calculations, and displaying results. Users can also view a history of previous calculations, modify or delete entries, and visualize efficiency trends using a graph.

## Features

- **Calculate Transformer Power and Efficiency**: Input voltage and current values to compute power and efficiency.
- **History Sidebar**: View a history of previous calculations in a sidebar. Each entry can be expanded to view detailed information.
- **Modify and Delete Calculations**: Update or remove previous calculations from the history.
- **Graphical Representation**: Visualize efficiency trends over time with a line graph.
- **Data Persistence**: Save and load calculations from a JSON file.

## Requirements

- Python 3.7 or higher
- Streamlit
- Matplotlib
- JSON

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/transformer-calculator.git
    cd transformer-calculator
    ```

2. Install the required packages:

    ```bash
    pip install streamlit matplotlib
    ```

## Usage

1. Run the Streamlit application:

    ```bash
    streamlit run main.py
    ```

2. Open the application in your browser at `http://localhost:8501`.

## Functionality

### User Interface

- **Main Screen**:
  - **Input Fields**: Enter the primary and secondary voltages and currents.
  - **Calculate Button**: Compute the power and efficiency based on the input values.
  - **Results Display**: Shows the calculated power and efficiency with color-coded values.
  - **History Sidebar**: Lists previous calculations. Each item can be expanded to view details.

### History Management

- **View History**: Click on the items in the sidebar to expand and view details of previous calculations.
- **Delete History**: Remove a calculation by clicking the "Delete" button associated with each entry. The page will refresh to reflect changes.

### Graphical Representation

- **Efficiency Graph**: Displays a line graph showing the trend of efficiency over time.

## File Structure

- `main.py`: The main Streamlit application script.
- `calculations.json`: JSON file used to store calculation history.

## Example JSON Format

```json
[
    {
        "id": 1,
        "input_voltage": 230,
        "output_voltage": 110,
        "input_current": 5,
        "output_current": 10,
        "power_in": 1150,
        "power_out": 1100,
        "efficiency": 95.65
    },
    {
        "id": 2,
        "input_voltage": 240,
        "output_voltage": 120,
        "input_current": 4.5,
        "output_current": 9,
        "power_in": 1080,
        "power_out": 1080,
        "efficiency": 100.00
    }
]
