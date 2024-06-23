from icmplib import ping
import time
import matplotlib.pyplot as plt
import numpy


last = 0

interval = 0.5

graph_seconds = 10

graph_length = round(graph_seconds / interval)

plot_no = 1


while True:
    pings = []

    for i in range(graph_length):
        sleep_time = interval - (time.time() - last)

        if sleep_time > 0:
            time.sleep(sleep_time)

        last = time.time()

        pings.append(ping("1.1.1.1", count=1).avg_rtt)

    plt.plot(
        numpy.arange(
            (plot_no - 1) * graph_seconds,
            (plot_no - 1) * graph_seconds + graph_seconds,
            interval,
        ),
        pings,
    )

    plt.ylabel("Latency (ms)")
    plt.xlabel("Time (s)")

    plt.savefig(f"plot{plot_no}.png")

    plt.clf()

    plot_no += 1
