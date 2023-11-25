import matplotlib.pyplot as plt
import numpy as np


# Define the plot_results function
def plot_results(data):
    if data:
        # Initialize empty lists to store extracted values
        labels = []
        word_counts = []
        accuracies = []
        times = []
        phrases = []
        time_str = []

        # Iterate through the data and extract values
        for item in data:
            for key, value in item.items():
                # Extract values and convert to appropriate types
                label = f"{value[0]} ({key})"
                phrase = value[0]
                word_count = int(value[1].strip())
                accuracy = float(value[2])
                time = float(value[3])
                minute = int(time / 60)
                remaining_seconds = int(time % 60)
                # Append extracted values to the respective lists
                phrases.append(phrase)
                labels.append(label)
                word_counts.append(word_count)
                accuracies.append(accuracy)
                times.append(time)
                time_str.append(f"{minute:02d}:{remaining_seconds:02d}")

        # Create a 2x2 subplot structure
        fig, axs = plt.subplots(2, 2, figsize=(14, 10))

        # Create the bar chart in the first subplot
        x = np.arange(len(labels))
        width = 0.35
        axs[0, 0].bar(x, accuracies, width, label="Accuracy")
        axs[0, 0].set_xlabel("Result")
        axs[0, 0].set_ylabel("Accuracy (%)")
        axs[0, 0].set_title("Accuracy by Result")
        axs[0, 0].set_xticks(x)
        axs[0, 0].set_xticklabels(labels, rotation=45, ha="right")
        axs[0, 0].legend()

        # Add average accuracy annotation above the bars
        for i, bar in enumerate(axs[0, 0].containers[0]):
            height = bar.get_height()
            axs[0, 0].annotate(
                f"{height:.2f}%",
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha="center",
                va="bottom",
            )

        # Populate the second subplot with a table, replacing the old ax_table
        cell_text = []
        for i in range(len(labels)):
            time_per_word = (word_counts[i] * 60) / times[i]
            cell_text.append(
                [
                    f"{phrases[i]}",
                    f"{word_counts[i]}",
                    time_str[i],
                    f"{time_per_word:.2f} word/m",
                ]
            )

        table = axs[1, 0].table(
            cellText=cell_text,
            colLabels=["Phrase", "Word Count", "Time (s)", "Time/Word"],
            cellLoc="center",
            loc="center",
        )
        table.auto_set_font_size(False)
        table.set_fontsize(12)
        table.scale(1, 1.5)
        axs[1, 0].axis("off")  # Turn off the axis

        # Adjust the remaining subplots as placeholders or for future use
        axs[0, 1].axis("off")  # Placeholder for future plot
        axs[1, 1].axis("off")  # Placeholder for future plot

        # Adjust layout
        plt.tight_layout()
        plt.show()

    else:
        print("\nNo result to plot!\n")


# Example usage
"""data = [
    {"1": ["work hard", "50", "80", "3"]},
    {"2": ["work smart", "100", "100", "5"]},
    {"3": ["work smart", "300", "70", "70"]},
]

plot_results(data)"""
