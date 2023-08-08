import matplotlib.pyplot as plt

throughput1 = [4.30, 7.60, 13.93, 19.35] # duration 1, num_clients 1
throughput2 = [8.56, 15.03, 27.35, 38.32]
throughput3 = [12.75, 22.33, 40.98, 57.11]
throughput4 = [16.91, 29.29, 53.84, 74.48]
throughput5 = [21.08, 36.35, 66.54, 92.26]

latency1 = [0.313634, 0.615134, 1.550, 3.066]
latency2 = [0.309409 , 0.612486, 1.503, 3.054]
latency3 = [0.308986, 0.617714, 1.532, 3.060]
latency4 = [0.309417, 0.621002, 1.542, 3.072]
latency5 = [0.311192, 0.614211, 1.541, 3.019]

# Plotting
plt.figure(figsize=(8, 6))

plt.plot( throughput1, latency1, label='num_clients: 1')
plt.plot( throughput2, latency2, label='num_clients: 2')
plt.plot( throughput3, latency3, label='num_clients: 3')
plt.plot( throughput4, latency4, label='num_clients: 4')
plt.plot( throughput5, latency5, label='num_clients: 5')

plt.xlabel('Latency (second)')
plt.ylabel('Throughput (query/second)')
plt.title('Throughput vs Latency (Duration 1 s)')
plt.legend()

plt.grid(True)
plt.show()
