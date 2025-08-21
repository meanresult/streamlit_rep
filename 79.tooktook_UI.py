import streamlit as st
from PIL import Image, GifImagePlugin
# CSS 정보 #########################################################
st.sidebar.markdown("""
<style>
/* 사이드바 전체 배경 톤 */
section[data-testid="stSidebar"] > div {
  background: #f3f6fa;
}

/* 메뉴 컨테이너 카드 */
.sidebar-card {
  background: #ffffff;
  border: 1px solid #e6ecf5;
  border-radius: 14px;
  padding: 80px;
  box-shadow: 0 2px 6px rgba(0,0,0,0.04);
}

/* 상단 타이틀 */
.sidebar-title {
  font-weight: 800; 
  font-size: 20px;
  margin: 4px 0 12px 2px;
}

/* 개별 메뉴 버튼 공통 */
.menu-btn {
  display: flex; align-items: center; gap: 8px;
  width: 100%; border: 1px solid transparent;
  padding: 10px 12px; border-radius: 10px; 
  background: transparent; color: #0f172a;
  cursor: pointer; text-align: left;
}

/* hover 효과 */
.menu-btn:hover { background: #eef5ff; border-color: #d6e6ff; }

/* 활성 메뉴 */
.menu-active {
  background: #e6f3ff !important;
  border-color: #c7e2ff !important;
  color: #0a4da7 !important;
  font-weight: 700;
}

/* 작은 캡션 */
.caption { color:#64748b; font-size: 12px; margin: 4px 2px 10px; }
</style>
""", unsafe_allow_html=True)

# 유저 임시 정보 ####################################################
USER_DATA = {
    "admin": "1234",
    "user1": "pass1",
    "user2": "pass2",
    "guest": "guest123"
}

USER_DATA1 = {
    "admin": "한지훈",
    "user1": "신땡콩",
    "user2": "안재이",
    "guest": "윤정환"
}

#로그인 세션관리
if "logged_in" not in st.session_state: #로그인 세션
    st.session_state['logged_in'] = False 
    
if "username" not in st.session_state: #누가 로그인했는지 관리세션
    st.session_state["username"] = ""
    

#제목 
# st.title('TookTook 상담 관리페이지')

#로그인 화면 세션########################################################
if not st.session_state["logged_in"]:
    st.title('TookTook 상담 관리페이지')
        
    with st.container():
        st.subheader("🔒 로그인")
        username = st.text_input("아이디")
        password = st.text_input("비밀번호", type="password")
        login_btn = st.button("로그인")
        st.text('ID - admin')
        st.text('PW - 1234')

        if login_btn:
            if username in USER_DATA and USER_DATA[username] == password:
                st.session_state["logged_in"] = True
                st.session_state["username"] = username
                st.success(f"{username}님 환영합니다! 🎉")
                st.rerun()
            else:
                if username not in USER_DATA:
                    st.error("아이디가 잘못되었습니다")
                else :
                    st.error("비밀번호가 잘못되었습니다")

# 로그인 후 세션 
else:
    # 페이지 기본설정
    st.set_page_config(page_title='TookTook 상담 관리페이지'
                       , layout= "wide"
                       , initial_sidebar_state= "expanded")
    
    # 전역/ 디퐅트상태
    if "menu" not in st.session_state:
        st.session_state.menu = "메인"
        
    # 사이드바 MENU 리스트
    MENU_ITEMS = [
                ("🌱", "메인"),
                ("💬", "상담창"),
                ("📃", "상담기록"),
                ("⚙", "설정"),
                ("🚪", "로그아웃"),
                    ]
    # 사이드바
    with st.sidebar:
        img = Image.open('툭툭이.png')
        st.image(img, width=400, caption=None)
        st.sidebar.header('Menu')

        for icon, label in MENU_ITEMS:
            is_active = (st.session_state.menu == label)
            if st.sidebar.button(f"{icon} {label}", key=f"btn_{label}", use_container_width=True): # 버튼 내용을 꽉 채운다 
                st.session_state.menu = label # 해당 버튼을 클릭 시 세션이 버튼기준으로 변경
            
    
                                                            
    
    # 본문 라우팅 
    if st.session_state.menu == "로그아웃":
            st.session_state["logged_in"] = False
            st.session_state["username"] = ""
    
    
    # 상단 ##########################################################
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    na1 = st.session_state['username']
    name1 = USER_DATA1[na1]
    with col6:
        st.write(f"📱상담자: {name1}")
    
    
    
    
    # 메인 #######################################################3##
    st.title('TookTook 상담 관리페이지')
    st.divider()
