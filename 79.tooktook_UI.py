import streamlit as st


USER_DATA = {
    "admin": "1234",
    "user1": "pass1",
    "user2": "pass2",
    "guest": "guest123"
}

#로그인 세션관리
if "logged_in" not in st.session_state: #로그인 세션
    st.session_state['logged_in'] = False 
    
if "username" not in st.session_state: #누가 로그인했는지 관리세션
    st.session_state["username"] = ""
    

#제목 
st.title('TookTook 상담 관리페이지')

#로그인 전 세션
if not st.session_state["logged_in"]:
        
    with st.container():
        st.subheader("🔒 로그인")
        username = st.text_input("아이디")
        password = st.text_input("비밀번호", type="password")
        login_btn = st.button("로그인")

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
else:
    st.success(f"✅ {st.session_state['username']}님 로그인 중")
    if st.button("로그아웃"):
        st.session_state["logged_in"] = False
        st.session_state["username"] = ""