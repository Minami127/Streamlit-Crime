import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

def main() :
    st.title('경찰청 인천광역시경찰청_관서별 5대범죄 112신고건수 현황')

    if st.checkbox('보기'):
        df=pd.read_csv('./data/crime.csv', encoding='euc-kr')
        st.dataframe(df)

    st.subheader('통계데이터 확인하기')

    if st.checkbox('더보기') :
        st.dataframe(df.describe())

if __name__ == '__main__' :
    main()