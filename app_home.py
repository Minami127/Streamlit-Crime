import streamlit as st

def run_home_app () :
    img_url = 'https://dimg.donga.com/wps/NEWS/IMAGE/2023/08/30/120928365.1.jpg'
    st.image(img_url,width=500)
    st.write('2015년 대한민국 주요도시 범죄 발생 지역별 통계입니다.')
if __name__ == '__main__' :
    main()