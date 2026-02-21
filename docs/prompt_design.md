# Prompt Engineering Design - OLAP Assistant

## Prompting Strategy
For this project, I implemented **Role-Based Prompting** and **Few-Shot Constraints** to ensure the AI generates high-quality, executable code.

### Key Highlights:
1. **Data Context**: The AI is specifically instructed on the columns within the retail dataset (revenue, profit, etc.), preventing "hallucinations" of column names.
2. **Format Enforcement**: The model returns ONLY pure Python code, eliminating verbose explanations that would otherwise break the program execution.
3. **Streamlit Integration**: Every AI output is forced to use `st.write()` or `st.plotly_chart()` commands to ensure results are correctly rendered within the UI.

## Supported OLAP Operations
- **Slice**: Filtering data based on a specific time period (e.g., Year).
- **Dice**: Filtering across multiple dimensions simultaneously (e.g., Category & Region).
- **Drill-down**: Navigating from high-level summaries to detailed data (e.g., moving from Year to Quarter).