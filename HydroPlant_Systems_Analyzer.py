
import pandas as pd
import matplotlib.pyplot as plt

# Simulated plant data with capped max power output of 31.4 MW
data = {
    'Time (s)': [0, 10, 20, 30, 40, 50, 60],
    'Turbine Speed (RPM)': [260, 263, 265, 268, 270, 273, 272],
    'Guide Vane Opening (%)': [40, 50, 60, 70, 80, 90, 85],
    # Assuming power is roughly proportional to guide vane opening
    'Power Output (MW)': [12.6, 15.7, 18.8, 22.0, 25.1, 28.3, 26.7],
    'PLC Status': ['OK', 'OK', 'OK', 'OK', 'OK', 'ALERT', 'OK']
}

# Load into DataFrame
df = pd.DataFrame(data)

# Plotting the system behavior
plt.figure(figsize=(12, 6))
plt.plot(df['Time (s)'], df['Turbine Speed (RPM)'], marker='o', label='Turbine Speed (RPM)')
plt.plot(df['Time (s)'], df['Guide Vane Opening (%)'], marker='s', label='Guide Vane Opening (%)')
plt.plot(df['Time (s)'], df['Power Output (MW)'], marker='^', label='Power Output (MW)')
plt.title('HydroPlant Systems Analyzer – Turbine Performance Overview')
plt.xlabel('Time (s)')
plt.ylabel('System Metrics')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Anomaly detection logic
for i, row in df.iterrows():
    if row['Turbine Speed (RPM)'] > 273:
        print(f"⚠️ Overspeed Alert at {row['Time (s)']}s: {row['Turbine Speed (RPM)']} RPM")
    if row['Power Output (MW)'] > 31.4:
        print(f"⚠️ Power Output Limit Exceeded at {row['Time (s)']}s: {row['Power Output (MW)']} MW")
    if row['PLC Status'] == 'ALERT':
        print(f"🔴 PLC Alert at {row['Time (s)']}s – check governor or servomotor behavior")
