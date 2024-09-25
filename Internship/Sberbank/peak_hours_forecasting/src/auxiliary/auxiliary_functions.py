import numpy as np
import pandas as pd
import seaborn as sns
import plotly.graph_objs as go
import matplotlib.pyplot as plt
from plotly.offline import iplot

from scipy.signal import periodogram
from sklearn.metrics import median_absolute_error, mean_squared_log_error, r2_score
from sklearn.metrics import mean_squared_error, mean_absolute_error, mean_absolute_percentage_error


def get_average_months_length(df: pd.DataFrame, first_year: int = 2011, last_year: int = 2024) -> int:
    """"""

    return df[f"{first_year}": f"{last_year}"].shape[0] // ((last_year - first_year) * 12)


def check_metrics(y_train: pd.Series, y_test: pd.Series) -> None:
    """"""

    print("R^2 error is:", r2_score(y_train, y_test))
    print("MS error is:", mean_squared_error(y_train, y_test))
    print("MA error is:", mean_absolute_error(y_train, y_test))
    print("MedA error is:", median_absolute_error(y_train, y_test))
    print("MSL error is:", mean_squared_log_error(y_train, y_test))
    print("MAP error is:", mean_absolute_percentage_error(y_train, y_test))


def eval_metric(y_train: pd.Series, y_test: pd.Series) -> float:
    """"""

    return sum([1 for day in range(len(y_train)) if round(y_train[day]) == round(y_test[day])]) / len(y_test)


def seasonal_plot(X, y, period, freq, ax=None):
    if ax is None:
        _, ax = plt.subplots()

    palette = sns.color_palette("husl", n_colors=X[period].nunique(), )
    ax = sns.lineplot(x=freq, y=y, hue=period, data=X, ci=False, ax=ax, palette=palette, legend=False)
    ax.set_title(f"Seasonal Plot ({period}/{freq})")

    for line, name in zip(ax.lines, X[period].unique()):
        y_ = line.get_ydata()[-1]

        ax.annotate(name, xy=(1, y_), xytext=(6, 0), color=line.get_color(), xycoords=ax.get_yaxis_transform(),
                    textcoords="offset points", size=14,
                    va="center")

    return ax


def plot_periodogram(ts, detrend='linear', ax=None):
    """"""

    fs = pd.Timedelta("245D") / pd.Timedelta("1D")

    freqencies, spectrum = periodogram(ts, fs=fs, detrend=detrend, window="boxcar", scaling='spectrum')

    if ax is None:
        _, ax = plt.subplots()

    ax.step(freqencies, spectrum, color="purple")
    ax.set_xscale("log")
    ax.set_xticks([1, 2, 3, 5])
    ax.set_xticklabels(
        ["(1)", "(2)", "(3)", "(5)"], rotation=90)

    ax.ticklabel_format(axis="y", style="sci", scilimits=(0, 0))
    ax.set_ylabel("Variance")
    ax.set_title("Periodogram")

    return ax


# def create_fourier_features(indexes, freq, order):
#     time = np.arange(len(indexes), dtype=np.float32)
#
#     k = 2 * np.pi / freq * time
#
#     year_sin = pd.Series(np.sin(2 * np.pi * days / year_length))
#     year_cos = pd.Series(np.cos(2 * np.pi * days / year_length))
#
#     return pd.concat({"year_cos": year_cos, "year_sin": year_sin}, axis=1)


def scatters_plot(graph_data: pd.DataFrame, graph_x_feature_name: str, graph_y_feature_name: str,
                  hue_feature_name: str, graph_title: str, graph_x_label: str, graph_y_label: str):
    """"""

    graphs_data = []

    for graph_data_hue in graph_data[hue_feature_name].unique():
        curr_graph_data = graph_data[(graph_data[hue_feature_name] == graph_data_hue)]
        graphs_data.append(go.Scatter(x=curr_graph_data[graph_x_feature_name], y=curr_graph_data[graph_y_feature_name],
                                      name=f"Entity {graph_data_hue}"))

    layout = go.Layout(title=graph_title, xaxis=dict(title=graph_x_label), yaxis=dict(title=graph_y_label))
    figure = go.Figure(data=graphs_data, layout=layout)
    iplot(figure)
