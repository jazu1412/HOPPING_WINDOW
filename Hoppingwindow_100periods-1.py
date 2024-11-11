# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 10:21:43 2024

@author: chvuppal
"""

import pandas as pd
import numpy as np

# Create a sample time series dataframe
data = {
    'timestamp': pd.date_range(start='2024-01-01', periods=100, freq='h'),
    'value': np.random.randint(1, 10, 100)
}
df = pd.DataFrame(data)

# Set the timestamp as the index
df.set_index('timestamp', inplace=True)

# Define hopping window parameters
window_size = '3h'  # Window duration
hop_size = '1h'     # Hop interval

# Create hopping windows
df['hopping_mean'] = df['value'].rolling(window=window_size, min_periods=1).mean().shift(-1)

print(df)

df = df.reset_index()
import matplotlib.pyplot as plt

# Create the plot with improved styling
plt.figure(figsize=(12, 6))
plt.plot(df['timestamp'], df['value'], label='Original Data', linewidth=1)
plt.plot(df['timestamp'], df['hopping_mean'], label='Hopping Mean', linewidth=1.5)
plt.legend()
plt.title('Temperature Readings: Original vs Hopping Window Mean')
plt.xlabel('Timestamp')
plt.ylabel('Temperature Value')
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
plt.savefig('hopping_window_visualization.png', dpi=300, bbox_inches='tight')
plt.show()
