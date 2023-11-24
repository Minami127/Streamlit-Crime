import streamlit as st

def run_eda_app () :
     df=pd.read_csv('./data/crime.csv', encoding='euc-kr')
     st.dataframe(df)

    

if __name__ == '__main__' :
    main()