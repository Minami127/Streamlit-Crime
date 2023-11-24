import streamlit as st
from app_eda import run_eda_app
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

def main() :
    st.title('경찰청 인천광역시경찰청_관서별 5대범죄 112신고건수 현황')

    menu=['Home','EDA','ML']

    choice = st.sidebar.selectbox('메뉴선택', menu)

   
    st.subheader('통계데이터 확인하기')

    if choice == menu[0] :
        pass
    elif choice == menu[1] :
       run_eda_app()
    elif choice == menu[2] :
        pass

   

if __name__ == '__main__' :
    main()