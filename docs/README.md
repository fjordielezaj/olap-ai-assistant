# 📊 OLAP AI Assistant - Retail Analytics

This project is an intelligent Business Intelligence (BI) application built for **Tier 2: Builder**. The application leverages Artificial Intelligence (Google Gemini) to transform natural language queries into OLAP operations and graphical visualizations.

## 🚀 Features
- **LLM Integration**: Uses Gemini 1.5 Flash for generating Pandas and Plotly code.
- **OLAP Operations**: Supports Slice, Dice, Drill-down, Roll-up, and Compare.
- **Interactive Visualizations**: Dynamic charts powered by Plotly Express.
- **Data Handling**: Processes a retail dataset containing over 10,000 transactions.

## 🛠️ Technologies Used
- **Python** (Core Language)
- **Streamlit** (Web Interface)
- **Pandas** (Data Analysis)
- **Plotly** (Charting/Visuals)
- **Google Generative AI** (AI Logic Engine)

## 📦 Installation and Usage

Follow these steps to get the application running:

### 1. Install Dependencies
Ensure you have Python installed, then run:
```bash
pip install -r requirements.txt
2. Configure API Key
Create a new file named .env in the root directory of the project and add your key:
GOOGLE_API_KEY=AIzaSy...your_key_here

3. Generate Data
To create the dataset with 10,000 transactions (CSV file), execute:

Bash
python generate_data.py
4. Launch the Application
To open the graphical interface in your browser, use the command:

Bash
streamlit run app.py
📂 Project Structure
app.py: The main Streamlit application and chat interface.

prompts.py: Prompt Engineering strategy and instructions for the AI.

data_utils.py: Functions for data loading and cleaning.

generate_data.py: Script for creating the synthetic retail dataset.

docs/prompt_design.md: Technical documentation regarding the prompt design.