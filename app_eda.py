import streamlit as st
import pandas as pd
import plotly.express as px

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
     
     radiohead=['지역별 신고건수', '가장 많이 들어오는 신고건수','가장 적게 들어오는 신고건수']
     
     fixed_column = '범죄 분류'

     

     st.info('분류별로 보기')

     radio = st.radio('',radiohead)
     pd.set_option('display.max_colwidth', None)

     if radio == radiohead[0] :
          selected_region = st.selectbox('',df.columns[1:])
          selected_data = df[[fixed_column,selected_region]]
          selected_data = df[[fixed_column, selected_region]].transpose()
          st.dataframe(selected_data)
     elif radio == radiohead[1] :
          column_list=df.columns[1 : ]
          selected_column=st.selectbox('', column_list)
          top5_selected_column_df = df.nlargest(5, selected_column)[[fixed_column, selected_column]]
          st.dataframe(top5_selected_column_df)
          fig1 = px.pie(top5_selected_column_df, values=selected_column, names=fixed_column, title=f'{selected_column}의 상위 5개 신고건수 ')
          st.plotly_chart(fig1)
     elif radio == radiohead[2] :
          column_list=df.columns[1 : ]
          selected_column=st.selectbox('', column_list)
          bottom5_selected_column_df = df.nsmallest(5, selected_column)[[fixed_column, selected_column]]
          st.dataframe(bottom5_selected_column_df)
          fig2 = px.pie(bottom5_selected_column_df, values=selected_column, names=fixed_column, title=f'{selected_column}의 하위 5개 신고건수')
          st.plotly_chart(fig2)
          


     st.header('지역별 신고건수 비교하기')


if __name__ == '__main__' :
     main()