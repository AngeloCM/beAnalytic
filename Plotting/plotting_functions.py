import seaborn as sns
import matplotlib.pyplot as plt

def add_percentage_to_plot(ax: plt.Axes):
    """
    Adds percentage labels to each bar in a bar plot.

    Parameters:
        ax (matplotlib.axes.Axes): The Axes object containing the bar plot.

    Returns:
        None
    """
    total_height = sum(bar.get_height() for bar in ax.patches if bar.get_height() > 0)

    for bar in ax.patches:
        height = bar.get_height()
        if height > 0:
            percentage = height / total_height
            if percentage > 0:
                ax.text(
                    bar.get_x() + bar.get_width() / 2,
                    height + 0.5,
                    f"{percentage:.1%}",
                    ha="center",
                    va="bottom",
                )