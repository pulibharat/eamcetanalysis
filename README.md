# 🎓 Andhra EAMCET College Analysis

This project analyzes **Andhra Pradesh EAMCET First counseling data(2025)**.  
It combines datasets, performs analysis, and provides both Jupyter Notebook insights and a **Streamlit app** for interactive visualization.  

---

## 📂 Project Structure

### 1. [`eamcet.csv`](./eamcet.csv)
- Contains the **raw dataset** with college, branch, category, location, and rank details.
- You can click the file above to explore the dataset directly in GitHub.

### 2. [`combining eamcet datasets.ipynb`](./combining%20eamcet%20datasets.ipynb)
- Jupyter Notebook used to **clean and merge multiple EAMCET datasets** into a single structured file.
- Outputs the combined dataset that is used for further analysis.

### 3. [`eamcet_analysis.ipynb`](./eamcet_analysis.ipynb)
- Main **analysis notebook**.  
- Includes:
  - Rank distribution across colleges
  - Branch-wise and category-wise seat analysis
  - Visualizations of top colleges
- Uses **Plotly** for visualization.

### 4. [`graph.py`](./graph.py)
- **Streamlit app** for interactive exploration of EAMCET data.
- Run  with:
  ```bash
  https://eamcetanalysis.streamlit.app/
