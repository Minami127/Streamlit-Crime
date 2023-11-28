import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt


def run_eda_app () :
     
     st.subheader('통계데이터 확인하기')
    
     df=pd.read_csv('./data/crime.csv', encoding='euc-kr')
     
     df=df.drop(columns=df.columns[0],axis=1)
     new_first_column_name='범죄 분류'
     df.rename(columns={df.columns[0]: new_first_column_name}, inplace=True)
     st.dataframe(df)




     st.text('범죄대분류 보기')
     df1=pd.read_csv('./data/crime.csv', encoding='euc-kr')


     

     new_checkbox =st.checkbox('보기')
     
     if new_checkbox :
          radiohead1=['범죄대분류','범죄소분류']
          radio1 = st.radio(' ',radiohead1)

          if radio1 == radiohead1[0]:
               unique_values_col1 = df1.iloc[:, 0].unique()
               st.write(' ', unique_values_col1)


          elif radio1 == radiohead1[1]:
               grouped_data = {}
               for value in df1.iloc[:, 0].unique():
                    grouped_data[value] = df1[df1.iloc[:, 0] == value].iloc[:, 1].tolist()

               st.write('')
               for key, values in grouped_data.items():
                    st.write(f"{key}: {values}")

     

     st.subheader('지역별 범죄 건수')
     
     region=st.text_input('검색해서 찾기')

     fixed_column = df.columns[0]
     matching_columns = [col for col in df.columns[1:] if region.lower() in col.lower()]

     if matching_columns:
          fixed_column_df = df[[fixed_column]]
    
          selected_columns_df = df[matching_columns]

          result_df = pd.concat([fixed_column_df, selected_columns_df], axis=1)
          result_df.set_index(fixed_column, inplace=True)

          st.dataframe(result_df)
     else:
          st.text('데이터가 없습니다.')


     radiohead=['지역별 범죄건수', '지역별 상위 5개 범죄','지역별 하위 5개 범죄']
     
     fixed_column = '범죄 분류'

     st.info('분류별로 보기')

     radio = st.radio('',radiohead)
     column_list=df.columns[1 : ]
     
     pd.set_option('display.max_colwidth', None)

     if radio == radiohead[0] :
          selected_region = st.selectbox('',df.columns[1:])
          selected_data = df[[fixed_column,selected_region]]
          selected_data = df[[fixed_column, selected_region]].transpose()
          st.dataframe(selected_data)
     elif radio == radiohead[1] :
          selected_column=st.selectbox('', column_list)
          top5_selected_column_df = df.nlargest(5, selected_column)[[fixed_column, selected_column]]
          st.dataframe(top5_selected_column_df)
          fig1 = px.bar(top5_selected_column_df, y=selected_column, x=fixed_column, title=f'{selected_column}의 상위 5개 범죄건수 ')
          st.plotly_chart(fig1)
     elif radio == radiohead[2] :
          selected_column=st.selectbox('', column_list)
          bottom5_selected_column_df = df.nsmallest(5, selected_column)[[fixed_column, selected_column]]
          st.dataframe(bottom5_selected_column_df)
          fig2 = px.bar(bottom5_selected_column_df, y=selected_column, x=fixed_column, title=f'{selected_column}의 하위 5개 범죄건수')
          st.plotly_chart(fig2)
     
    

     st.subheader('지역별 범죄 건수 비교')
     
     df2=pd.read_csv('./data/crime.csv', encoding='euc-kr')
     if st.checkbox('데이터 보기') :
          st.dataframe(df)
     else :
          st.text('')

     print(df2.columns[1:])

     column_menu = df2.columns[1:]

     choice_list=st.multiselect('지역을 선택하세요',column_menu)

     print(choice_list)

     if len(choice_list) != 0:

          df2_selected = df2[choice_list]


          df2_selected.index = df2.iloc[:, 0].tolist()


          st.line_chart(data=df2_selected)
          st.area_chart(data=df2_selected)
     
    



          


if __name__ == '__main__' :
     main()