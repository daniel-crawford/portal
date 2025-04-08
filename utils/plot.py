import numpy as np
import pandas as pd
import plotly.express as px
from PIL import Image

COLOR_SCHEMES = {
    "Gas": "#FFA07A",       # Light Salmon
    "Electric": "#FFD700",  # Gold
    "Water": "#87CEFA"       # Light Sky Blue
}

def generate_dummy_data():
    dates = pd.date_range(end=pd.Timestamp.today(), periods=30)
    usage = np.random.uniform(50, 150, size=30)
    cost = usage * np.random.uniform(0.1, 0.3)
    df = pd.DataFrame({"Date": dates, "Usage": usage, "Cost": cost})
    return df

def plot_usage(df, utility):
    fig = px.line(df, x="Date", y="Usage", title=f"{utility} Usage Over Time",
                  markers=True, color_discrete_sequence=[COLOR_SCHEMES[utility]])
    return fig

def plot_cost(df, utility):
    fig = px.bar(df, x="Date", y="Cost", title=f"{utility} Cost Over Time",
                 color_discrete_sequence=[COLOR_SCHEMES[utility]])
    return fig