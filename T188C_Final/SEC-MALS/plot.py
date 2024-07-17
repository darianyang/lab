import pandas as pd
import matplotlib.pyplot as plt

#plt.style.use("~/github/wedap/wedap/styles/default.mplstyle")

# Read the CSV file
file_path = 'CA-CTD-MALS.csv'
file_path = 'CA-CTD-MALS-filtered.csv'
df = pd.read_csv(file_path)

# Extract columns for plotting
# The assumption is that the columns are in a repeating pattern of 4: volume (mL), UV, volume (mL), molar mass
num_columns = df.shape[1]
num_sets = num_columns // 4

# Create a figure and axis
fig, ax1 = plt.subplots()
# secondary y-axis
ax2 = ax1.twinx()

labels = ["WT CA-CTD 200 $\mu$M", "WT CA-CTD 10 $\mu$M", "T188C 200 $\mu$M", "T188C 10 $\mu$M" ]
colors = ['blue', 'cornflowerblue', 'red', 'lightsalmon']
idx = 0

# Plot UV data and molar mass data
for i in range(num_sets):
    vol_uv_col = df.columns[i * 4]
    uv_col = df.columns[i * 4 + 1]
    vol_mm_col = df.columns[i * 4 + 2]
    mm_col = df.columns[i * 4 + 3]
    
    # Plot UV data
    #ax1.plot(df[vol_uv_col], df[uv_col], label=uv_col.split('[')[0], color=colors[color_idx])
    ax1.plot(df[vol_uv_col], df[uv_col], label=labels[idx], color=colors[idx])
    
    # Plot molar mass data on secondary y-axis as scatter plot with log scale
    ax2.scatter(df[vol_mm_col], df[mm_col], color=colors[idx], s=5)
    ax2.set_yscale('log')
    
    idx = (idx + 1) % len(colors)

ax1.set_xlabel('Volume (mL)')
ax1.set_xlim(12.5,22.5)
ax1.set_ylabel('UV (Normalized Abs)')
#ax1.tick_params(axis='y', labelcolor='tab:blue')

ax2.set_ylabel('Molar Mass (Daltons)')
ax2.set_ylim(1000,100000)
# 9.95 kDa
ax2.axhline(9946, color="gray", linestyle="--")
ax2.text(13, 10500, "Theoretical Monomer")
# 19.9 kDa
ax2.axhline(9946*2, color="gray", linestyle="--")
ax2.text(13, 21000, "Theoretical Dimer")
#ax2.tick_params(axis='y', labelcolor='tab:red')

# Add a legend
fig.legend(loc='upper right', bbox_to_anchor=(1,1), bbox_transform=ax1.transAxes, frameon=False)

# Show the plot
#plt.title('CA-CTD SEC-MALS')
plt.tight_layout()
plt.savefig("SEC-MALS.pdf")
plt.show()
