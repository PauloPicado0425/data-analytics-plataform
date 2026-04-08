# Data Analytics Plataform 

A fullstack data analysis platform where users can upload CSV files and automatically generate insights, visualizations, and downloadable reports.

---

## Features 
- Upload CSV datasets
- Automatic data analysis with statistics
- Dynamic chart generation 
- Data preview table
- Export PDF reports
- Fast API backend with real-time processing

---

## Tech Stack

#Backend
- Python
- FastAPI
- Pandas
- Matplotlib
- ReportLab

#Frontend
- React
- TailwindCSS

---

## Instalation 

1- Clone the repository
In git bash:
git clone https://github.com/PauloPicado0425/data-analytics-platform.git
cd data-analytics-platform

2- Backend Setup
cd backend
python -m vemv venv
source  venv/Scripts/activate   # Windows (Git Bash)

pip install -r requirements.txt

Run backend
python - uvicorn app:main:app --reload 

3- Frontend Setup
cd FrontEnd/client
npm install
npm start

---

## Usage
1- Open: http://localhost:3000
2- Upload a CSV file
3- Click Analyze
4- View charts and data
5- Download PDF report

Example CSV:
empleado,edad,salario,ventas,horas_trabajadas
Carlos,25,600,20,40
Maria,32,1200,50,45
Luis,29,900,35,42
Ana,27,850,30,38
Pedro,45,1600,70,50
Sofia,31,1100,55,44

Author
Paulo André Picado Jiménez 

Project Status
In development 
