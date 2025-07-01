# 📊 YouTube Data Analytics Project

This project explores personal YouTube data to uncover viewing patterns, behaviour, and engagement trends using data exported via Google Takeout. The goal is to demonstrate skills in data cleaning, database design, analytics, and visualisation using real-world, messy data.

---

## 🚀 Project Workflow

| Phase | Task                 | Tools                      | Goal                                      
|-------|----------------------|----------------------------|---------------------------------------------------
| 1     | Extract Data         | Google Takeout             | Get raw YouTube .json history                     |
| 2     | Explore & Clean      | Python (json, pandas)      | Flatten and prep nested, inconsistent data        |
| 3     | Design Schema        | Notion / Sketch / Paper    | Create schema: watch_history, videos, channels    |
| 4     | Build Database       | SQLite or PostgreSQL       | Load structured, cleaned data                     |
| 5     | Analyse              | SQL                        | Ask & answer core behavioural questions           |
| 6     | Visualise            | Power BI                   | Build dashboards and tell a data-driven story     |
| 7     | Showcase             | GitHub + LinkedIn          | Present final insights and personal reflections   |

---

## 🧰 Tech Stack

- **Language**: Python 3.11  
- **Libraries**: `json`, `csv`, `pandas`  
- **Tools**: VS Code, Git, GitHub, PowerShell  
- **Database**: SQLite (option to migrate to PostgreSQL)  
- **Visualisation**: Power BI  

## 🗂️ Project Structure

YouTube-Data-Analytics-Project/
│
├── Data/                   # Raw and cleaned datasets
│   ├── Raw/
│   └── Cleaned/
│
├── Scripts/                # Python scripts for parsing and cleaning
├── SQL/                    # Database schema and analysis queries
├── Notebooks/              # Jupyter notebooks for data exploration
├── Dashboards/             # Power BI screenshots or exports
│
├── venv/                   # Virtual environment (ignored in Git)
├── README.md               # Project overview and documentation
├── .gitignore              # Ignore sensitive or unnecessary files
└── requirements.txt        # Python dependencies (optional)

## 🔐 Privacy Statement

All data used in this project is anonymised and stripped of personal identifiers. The `.json` files are **not** included. Visuals and findings are generalised and for educational use only.
