# 🇦🇪 UAE Job Market Analysis Dashboard 2026

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red?style=flat&logo=streamlit)
![Plotly](https://img.shields.io/badge/Plotly-Charts-purple?style=flat&logo=plotly)
![HTML](https://img.shields.io/badge/HTML-Standalone-orange?style=flat&logo=html5)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)

> An interactive data analytics dashboard analyzing the UAE job market for Data Science, ML Engineering, AI Development, and Data Analysis roles in 2026.

---

## 📌 Table of Contents
- [Demo](#demo)
- [Features](#features)
- [Key Insights](#key-insights)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Setup & Installation](#setup--installation)
- [How to Run](#how-to-run)
- [Author](#author)

---

## 🎥 Demo

> Filter by category → Explore salary trends → Discover top skills

![Dashboard Demo](https://raw.githubusercontent.com/saqibkhan91/UAEJobMarket/main/assets/demo.png)

---

## ✨ Features

- 📊 **7 interactive charts** — salary, skills, companies, city distribution
- 🔍 **Live filters** by job category and city
- 💰 **Salary range analysis** per job category (AED/month)
- 🛠️ **Skills heatmap** — which skills are needed for which roles
- 🏢 **Top hiring companies** in UAE data market
- 🖥️ **Dual mode** — Streamlit app + standalone HTML version
- 📋 **Full job listings table** with salary bars

---

## 📈 Key Insights

| Insight | Finding |
|---|---|
| Most in-demand skill | **Python** (100% of all roles) |
| Highest paid category | **ML Engineering** (avg AED 26,875/month) |
| Top hiring city | **Dubai** (83% of all jobs) |
| Most open roles | **Data Science & Data Analysis** |
| Top hiring companies | Careem, BCG X, Binance, Al-Futtaim |

---

## 🛠️ Tech Stack

| Category | Tools |
|---|---|
| Language | Python 3.8+ |
| Data Analysis | Pandas, NumPy |
| Visualization | Plotly, Chart.js |
| UI (App) | Streamlit |
| UI (Standalone) | HTML, CSS, JavaScript |

---

## 📁 Project Structure

```
UAEJobMarket/
├── data/
│   └── uae_jobs.csv         # 41 UAE job listings dataset
├── collect_data.py          # Data collection script
├── app.py                   # Streamlit dashboard
├── index.html               # Standalone HTML dashboard
├── requirements.txt         # Python dependencies
└── README.md
```

---

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Git

### Step 1 — Clone the Repository
```bash
git clone https://github.com/saqibkhan91/UAEJobMarket.git
cd UAEJobMarket
```

### Step 2 — Create Virtual Environment
```bash
# Create venv
python3 -m venv venv

# Activate (Mac/Linux)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate
```

### Step 3 — Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4 — Generate Dataset
```bash
python3 collect_data.py
```
You should see:
```
✅ 41 jobs collected
✅ Data saved to data/uae_jobs.csv
```

---

## 🚀 How to Run

### Option 1 — Streamlit App
```bash
streamlit run app.py
```
Open: **http://localhost:8501**

### Option 2 — Standalone HTML (No server needed!)
```bash
open index.html        # Mac
start index.html       # Windows
xdg-open index.html    # Linux
```

---

## 👤 Author

**M Saqib Bilal** — Junior Data Scientist

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat&logo=linkedin)](https://linkedin.com/in/saqibkhan91)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=flat&logo=github)](https://github.com/saqibkhan91)
[![Email](https://img.shields.io/badge/Email-Contact-red?style=flat&logo=gmail)](mailto:itssaqibkhan91@gmail.com)

---

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).
