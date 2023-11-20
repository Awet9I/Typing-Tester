import matplotlib.pyplot as plt

import numpy as np
from play import final_res
from collections import deque


def plot_results(data):
    """data = [
        {"1": ["work hard", "50", "80", "3 seconds"]},
        {"2": ["work smart", "100", "90", "5 seconds"]},
        {"3": ["work smart", "300", "70", "7 seconds"]},
    ]"""
    # data = final_res()
    # Initialize empty lists to store extracted values
    if data:
        word_counts = []
        accuracies = []
        times = []

        # Iterate through the data and extract values
        for item in data:
            for key, value in item.items():
                # Extract values and convert to appropriate types
                word_count = int(value[1].strip())
                accuracy = float(value[2])
                time = float(value[3])

                # Append extracted values to the respective lists
                word_counts.append(word_count)
                accuracies.append(accuracy)
                times.append(time)

                # Append extracted values to the respective lists

                word_counts.append(word_count)
                accuracies.append(accuracy)
                times.append(time)
        # Calculate average accuracy
        avg_accuracy = sum(accuracies) / len(accuracies)
        # Create a plot
        # Create a plot
        fig, ax = plt.subplots(figsize=(10, 6))

        # Scatter plot
        sc = ax.scatter(
            word_counts,
            accuracies,
            c=times,
            cmap="viridis",
            marker="o",
            label="Data Points",
        )
        cbar = plt.colorbar(sc, label="Time (s)")

        # Line plot to connect data points
        ax.plot(
            word_counts,
            accuracies,
            linestyle="-",
            marker="o",
            color="b",
            label="Connected Line",
        )

        # Add average accuracy annotation beside the colorbar
        avg_annotation = f"Average Accuracy: {avg_accuracy:.2f}%"
        ax.annotate(
            avg_annotation,
            xy=(1.2, 0.9),
            xycoords="axes fraction",
            fontsize=12,
            color="red",
            rotation=0,
            va="center",
            bbox=dict(boxstyle="round,pad=0.3", edgecolor="red", facecolor="white"),
        )

        ax.set_xlabel("Word Count")
        ax.set_ylabel("Accuracy (%)")
        ax.set_title("Accuracy vs. Word Count")
        ax.legend()
        ax.grid(True)

        # Show the plot
        plt.tight_layout()
        plt.show()


# Call the function to plot the results
# plot_results()
"""def plotter():
    games = []
    result = []
    
    final_list = final_res()
    data_points = deque(maxlen=len(final_list))

    for data in final_list:
        for key, value in data.items(): 
          games.append(key)
          for i in value:
           result.append(value[i])
    
    labels = []
    for i in range(len(games)):
       labels.append(f"game{i+1}")
    
    fig, ax = plt.subplots()
    line = ax.plot([])

    for i in range(len(final_list)):
       
       new_x = result[i]

    x = np.array[]
    y = np.array[25, 45, 65, 85]
"""
