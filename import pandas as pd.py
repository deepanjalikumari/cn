import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("connections.txt", delim_whitespace=True, header=None, 
                 names=["time", "src_ip", "dst_ip", "src_port", "dst_port"])

# Convert time to float
df["time"] = df["time"].astype(float)

# Sort by start time
df = df.sort_values("time")

# Assign default duration for unclosed connections
df["duration"] = 100

# Plot
plt.figure(figsize=(10, 5))
plt.scatter(df["time"], df["duration"], label="TCP Connections")
plt.axvline(x=df["time"].min() + 20, color="r", linestyle="--", label="Attack Start")
plt.axvline(x=df["time"].min() + 120, color="g", linestyle="--", label="Attack End")
plt.xlabel("Connection Start Time (seconds)")
plt.ylabel("Connection Duration (seconds)")
plt.legend()
plt.title("Connection Duration vs. Start Time")
plt.show()
