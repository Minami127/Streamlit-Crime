import streamlit as st
from app_eda import run_eda_app
from app_home import run_home_app


def main() :
    st.title('경찰청 인천광역시경찰청 관서별 5대범죄 112신고건수 현황')

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