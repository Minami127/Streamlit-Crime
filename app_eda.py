import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb


def run_eda_app () :
     st.subheader('통계데이터 확인하기')
    
     df=pd.read_csv('./data/crime.csv', encoding='euc-kr')
     df=df.drop(columns=df.columns[0],axis=1)
     new_first_column_name='범죄 분류'
     df.rename(columns={df.columns[0]: new_first_column_name}, inplace=True)
     st.dataframe(df)
     
     st.subheader('기초통계데이터 확인하기')
     if st.checkbox('통계데이터보기') :
          st.dataframe(df.describe())
     else :
          st.text('')
    

     st.info('지역별 신고건수')

     fixed_column = '범죄 분류'
     selected_region = st.selectbox('지역', df.columns[1:])
     selected_data = df[[fixed_column,selected_region]]
     st.dataframe(selected_data)

     




if __name__ == '__main__' :
    main()