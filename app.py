import streamlit as st
import matplotlib.pyplot as plt
from app_home import run_home_app
from app_eda import run_eda_app

import platform
from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False
if platform.system() == 'Linux':
    rc('font', family='NanumGothic')


def main() :
    st.title('경찰청 범죄 발생 지역별 통계')

    menu=['Home','EDA','ML']

    choice = st.sidebar.selectbox('메뉴선택', menu)


    if choice == menu[0] :
        run_home_app()
    elif choice == menu[1] :
        run_eda_app()
    elif choice == menu[2] :
        pass


   

if __name__ == '__main__' :
    main()