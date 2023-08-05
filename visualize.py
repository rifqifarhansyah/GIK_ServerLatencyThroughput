import matplotlib.pyplot as plt

throughput1 = [1159.18, 2271.90, 4047.66, 6174.90, 6940.88, 7826.95, 7818.17]
throughput2 = [644.12, 1284.61, 2299.97, 3508.72, 3796.36, 4331.43, 4339.36]
throughput3 = [443.75, 890.41, 1593.60, 2419.49, 2605.01, 2971.51, 2992.54]
throughput4 = [339.56, 679.87, 1206.15, 1835.33, 1970.26, 2255.27, 2271.45]
throughput5 = [270.99, 551.43, 979.34, 1471.66, 1609.28, 1820.67, 1835.63]
throughput6 = [136.21, 277.28, 496.84, 744.75, 830.58, 912.84, 919.87]

latency1 = [840.32, 857.06, 964.84, 1271.53, 2280.28, 4059.18, 8130.94]

latency2 = [1528.75, 1532.31, 1714.01, 2254.40, 4186.96, 7351.82, 14675.12]

latency3 = [2228.47, 2220.18, 2483.86, 3279.49, 6112.66, 10732.33, 21301.78]

latency4 = [2918.74, 2914.59, 3288.65, 4330.10, 8089.65, 14147.92, 28080.66]

latency5 = [3662.78, 3598.54, 4055.53, 5405.76, 9909.30, 17528.79, 34786.10]

latency6 = [7308.47, 7178.53, 8015.20, 10704.29, 19220.29, 34995.37, 69382.51]

# Plotting
plt.figure(figsize=(8, 6))

plt.plot( throughput1, latency1, label='L = 10')
plt.plot( throughput2, latency2, label='L = 20')
plt.plot( throughput3, latency3, label='L = 30')
plt.plot( throughput4, latency4, label='L = 40')
plt.plot( throughput5, latency5, label='L = 50')
plt.plot( throughput6, latency6, label='L = 100')

plt.xlabel('Latency')
plt.ylabel('Throughput')
plt.title('Throughput vs Latency')
plt.legend()

plt.grid(True)
plt.show()
