# 🌍 Climate Change Monitoring Dashboard  

> **Full-stack data analysis project** | **PostgreSQL + Tableau + Python**  
> Tracking climate trends, analyzing risks, and enabling informed decision-making with automated reporting & interactive dashboards.  

---

## 🚀 Project Overview  
Climate change is one of the most pressing global challenges, yet organizations struggle to:  
- Collect and clean diverse climate datasets  
- Generate **timely, accurate reports**  
- Assess **economic & population risks** tied to extreme weather events  

This project solves that challenge with a **comprehensive data pipeline and BI solution**:  
- **SQL-powered ETL**: Robust data cleaning & integration across 7 countries  
- **Automated Reporting**: Weekly PDF/Excel delivery  
- **Interactive Tableau Dashboard**: Real-time exploration of KPIs & climate risk  

🔗 **[Explore the Live Dashboard on Tableau Public](#)**  
🔗 **[LinkedIn Case Study](#)**  

---

## 🛠️ Tech Stack  
- **Database**: PostgreSQL (schemas, table design, data cleaning, unions, constraints)  
- **Data Wrangling**: SQL (window functions, CTEs, joins, data validation)  
- **Visualization**: Tableau Public (interactive filters, KPI bands, custom color formatting)  
- **Automation**: Python scripts for report generation (CSV/Excel, PDF, backups)  
- **Version Control**: GitHub + GitHub Actions (SQL lint, automated checks)  

---

## 📊 Key Insights from Analysis  
Some highlights discovered in the dataset:  
- 🌡️ **Temperature Trends**: January consistently recorded the highest average temperatures, while March was the lowest.  
- ⚡ **Extreme Weather Events**: August & March showed spikes, with **South Africa & Brazil most affected**.  
- 📉 **Air Quality Index**: Deteriorated by **12% YoY** in industrial zones.  
- 💰 **Economic Impact vs Infrastructure**: Weak infrastructure cities showed **3x higher losses** per event.  

---

## 🔑 Business Value  
This solution enables:  
- **Policy makers** → Identify climate hotspots for proactive planning  
- **NGOs** → Quantify population exposure and target aid  
- **Businesses** → Assess climate risks to supply chains & operations  
- **Data teams** → Automate reporting workflows and reduce manual effort  

---

## 📂 Repository Structure  
```
climate-change-monitoring-dashboard/
│── sql/                # Schemas, cleaning, analysis queries
│── data/sample/        # Sample CSV datasets (India, Germany demo)
│── automation/         # Python scripts for reports & backup
│── tableau/            # Dashboard notes, calculated fields
│── assets/             # Dashboard screenshots
│── .github/workflows/  # CI for SQL linting
│── README.md           # Documentation (this file)
```

---

## ⚙️ Setup & Usage  
1. **Load Data into PostgreSQL**  
   ```sql
   CREATE DATABASE climate_monitoring;
   \c climate_monitoring;
   \i sql/create_schemas.sql
   \i sql/import_clean_data.sql
   ```  
2. **Run Analysis Queries**  
   ```sql
   \i sql/analysis_trends.sql
   ```  
3. **Open Tableau Dashboard**  
   - Connect to PostgreSQL or use the sample `.twbx` file  
   - Explore KPIs, trends, and filters  

4. **Generate Reports**  
   ```bash
   python automation/export_reports.py
   ```

---

## 📈 Dashboard Preview  
![Dashboard](./assets/dashboard.png)  

---

## 🧠 Lessons Learned  
- The importance of **data type discipline** (text vs numeric vs date) for smooth imports  
- How to structure **multi-country datasets** with schema separation + `UNION ALL`  
- Designing Tableau KPIs with **calculated fields & conditional formatting**  
- Automating end-to-end reporting for non-technical stakeholders  

---

## 📌 Next Steps  
- Add **real-world APIs** (NASA, NOAA, Copernicus) for live climate data  
- Implement **predictive analytics (time series, regression)**  
- Deploy as a **self-service BI portal** with row-level security  

---

## 📬 Connect  
👨‍💻 **Author**: [Tushar Kshirsagar](#)  
---

✨ *This isn’t just a project—it’s a demonstration of end-to-end problem solving: from business understanding to BI delivery.*  
