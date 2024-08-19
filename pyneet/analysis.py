import matplotlib.pylab as plt
import seaborn as sns
import pandas as pd
import streamlit as st



file_path = 'jupyertFile/data/diabetes.csv'

def dataFrame(file_path=file_path):
    return pd.read_csv(file_path)

def sampleData():
    df = dataFrame()
    df['Outcome'] = df['Outcome'].apply(lambda x: "Positive Case" if x==1 else "Negative Case")
    st.dataframe(df.sample(5), hide_index=True)
    

def heatMap():
    df = dataFrame()
    fig, ax = plt.subplots()
    sns.heatmap(df.corr(), annot=True, ax=ax)
    ax.set_title("Heat Map")
    st.pyplot(fig=fig)

def boxPlot():
    df = dataFrame().iloc[:,:4]
    fig, ax = plt.subplots()
    sns.boxplot(df, ax=ax)
    ax.set_title("Box Plot")
    st.pyplot(fig=fig)

    df = dataFrame().iloc[:,4:]
    fig, ax = plt.subplots()
    sns.boxplot(df, ax=ax)
    ax.set_title("Box Plot")
    st.pyplot(fig=fig)

def num_dist_plot():
    df = dataFrame()
    fig, ax = plt.subplots()
    sns.histplot(x=df['Age'], kde=True, hue=df['Outcome'])
    ax.set_title("Hist plot")
    st.pyplot(fig=fig)

    df = dataFrame()
    fig, ax = plt.subplots()
    sns.kdeplot(x=df['Age'], hue=df['Outcome'])
    ax.set_title("kde plot")
    st.pyplot(fig=fig)



