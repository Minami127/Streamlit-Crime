import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

def main() :
    st.header('경찰청 인천광역시경찰청_관서별 5대범죄 112신고건수 현황')
    df=pd.read_csv('C:\Users\40005\Documents\GitHub\Streamlit-Crime\data\crime.csv')
    st.dataframe(df)

if __name__ == '__main__' :
    main()