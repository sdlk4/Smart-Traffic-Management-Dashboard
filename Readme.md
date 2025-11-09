Smart Traffic Management Dashboard



A complete end-to-end traffic analytics and forecasting system designed to help city planners, transportation analysts, and machine learning practitioners monitor traffic volume, analyze congestion patterns, and predict future traffic conditions. This solution transforms raw sensor data into actionable insights using Python, MySQL, and Power BI. The system includes automated data ingestion, feature engineering, a forecasting model, and a fully interactive Power BI dashboard.



Business Problem



Urban mobility systems face several challenges including peak hour congestion, unpredictable traffic surges, and weather-based fluctuations. Manual data inspection makes it difficult to understand behavioral patterns or anticipate congestion in advance. Transportation decision-makers require:



Accurate traffic volume analysis across different times of day



Identification of congestion hotspots



Understanding of weather impact on traffic flow



Daily, weekly, and monthly patterns in traffic behavior



Reliable forecasting to support planning and policy decisions



This project provides automated data processing, analytical insights, and machine learning-driven forecasting to support data-driven transportation management.



Project Structure



Below is the structure adapted to your actual project layout:



smart\_traffic/

├── data/

│   └── raw/                              # Original traffic dataset

├── src/

│   ├── config.py                         # MySQL connection configuration

│   ├── ingest.py                         # Loads CSV into MySQL

│   ├── features.py                       # Feature engineering and creation of derived metrics

│   └── forecast.py                       # Machine learning forecasting model

├── smart\_traffic\_dashboard.pbix          # Power BI dashboard

├── .env                                  # Environment variables for DB connection

└── requirements.txt                      # Python dependencies



Success Metrics and Dashboard Features



The dashboard delivers insights across the following analytical dimensions:



Traffic Performance



Total traffic volume



Average hourly traffic



Peak versus non-peak traffic comparison



Daily and hourly traffic trends



Monthly traffic patterns



Congestion Analysis



Congestion classification (low, moderate, high)



Hour by day-of-week congestion matrix



High congestion percentage



Congestion-level distribution comparison



Weather Impact



Traffic volume during rainy conditions



Traffic volume during snowy conditions



Comparison across different weather categories



Weather-based reduction or increase in average volume



Temporal Behavior



Hourly cycle patterns



Weekly cycle patterns



Seasonal trends



Holiday traffic deviations



Forecasting



Prediction of next-hour traffic volume using machine learning



Evaluation metrics including RMSE and R² score



Visual comparison of actual versus predicted traffic



Getting Started

Prerequisites



Python 3.9 or higher



Power BI Desktop



MySQL Server 8.0 or higher



MySQL ODBC or .NET connector installed for Power BI



Kaggle Metro Interstate Traffic Volume dataset



Installation



Clone the repository:



git clone https://github.com/YOUR\_USERNAME/smart-traffic-management.git

cd smart-traffic-management





Install dependencies:



pip install -r requirements.txt





Configure environment variables:



Copy .env.example to .env and provide your MySQL configuration:



MYSQL\_HOST=localhost

MYSQL\_USER=root

MYSQL\_PASSWORD=yourpassword

MYSQL\_DB=smart\_traffic





Place the raw Kaggle dataset into:



data/raw/Metro\_Interstate\_Traffic\_Volume.csv





Load the dataset into MySQL:



python src/ingest.py





Generate engineered features:



python src/features.py





Run forecasting model:



python src/forecast.py





Open the Power BI dashboard:



Open smart\_traffic\_dashboard.pbix in Power BI Desktop and refresh the data source if needed.



How It Works

Data Ingestion (src/ingest.py)



Loads raw CSV



Handles null or invalid timestamps



Creates MySQL table



Inserts data in optimized batches



Feature Engineering (src/features.py)



Extracts hour, month, and day-of-week



Creates peak hour indicator



Classifies congestion level using predefined volume thresholds



Inserts enhanced dataset into MySQL for analytics and visualization



Forecasting Model (src/forecast.py)



Loads engineered data



Creates lag-based historical features (1, 2, 3, 24, 168 hours)



Trains XGBoost regression model



Evaluates using RMSE and R²



Generates prediction output for analysis



Dashboard (smart\_traffic\_dashboard.pbix)



Includes:



KPI cards



Time-series analysis



Congestion-level metrics



Weather impact views



Heatmap matrix



Forecast vs actual comparison (if prediction table loaded)



Key Features



End-to-end data pipeline



Real-time aggregation using MySQL



Feature-rich analytics dashboard



Automated congestion classification



Weather correlation analysis



Machine learning forecasting model



Fully documented workflow



Sample Insights



Traffic peaks consistently between 6–9 AM and 4–7 PM



Rain and snow cause significant reductions in peak volume



Weekends exhibit lower congestion compared to weekdays



Cloud coverage has moderate impact on traffic



Holiday traffic patterns differ from normal weekdays, showing afternoon spikes



Technical Requirements

Python Dependencies



Listed in requirements.txt below.



Power BI Requirements



Power BI Desktop



Stable MySQL ODBC or .NET connector



Active MySQL service



Performance Considerations



Dataset size: ~48,204 rows



Power BI refresh time: under 10 seconds



Feature engineering time: under 5 seconds



Machine learning model training: under 10 seconds



Memory requirement: 4GB minimum recommended



Contributing



Fork the repository



Create a feature branch:



git checkout -b feature/new\_metric





Commit changes



Push branch



Submit pull request with explanation



Support and Troubleshooting



Common issues include:



MySQL authentication errors (use mysql\_native\_password)



Power BI not connecting (install correct 64-bit ODBC driver)



Dataset path errors (verify raw CSV location)



Forecasting script errors (ensure no missing lag rows)



Getting Help



Review project issues on GitHub



Create a new issue describing the error in detail



Check troubleshooting steps above

