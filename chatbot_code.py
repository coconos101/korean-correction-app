import streamlit as st

st.set_page_config(page_title="높임말 & 맞춤법 교정기", layout="centered")
st.title("📝 높임말 & 맞춤법 교정 챗봇")

# 사용자 입력 받기
user_input = st.text_area("✍️ 아이가 쓴 글을 붙여넣으세요:", height=250)

# 간단한 교정 예시 함수 (원하는 경우 확장 가능)
def correct_text(text):
    corrections = {
        "유나라고해": "유나라고 해",
        "한번": "한 번",
        "읽어볼래??": "읽어 볼래요?",
        "줬다": "드렸어요",
        "했어": "했습니다",
        "봤다": "보았습니다",
        "엄마가 말했다": "어머님께서 말씀하셨어요",
        "아빠가 줬다": "아버지께서 주셨어요"
    }
    for wrong, right in corrections.items():
        text = text.replace(wrong, right)
    return text

# 버튼 클릭 시 교정 실행
if st.button("✨ 교정하기"):
    if user_input.strip() == "":
        st.warning("먼저 글을 입력해주세요!")
    else:
        with st.spinner("교정 중입니다..."):
            corrected = correct_text(user_input)
            st.subheader("✅ 교정된 글")
            st.success(corrected)

st.markdown("---")
st.markdown("💡 예시: 안녕 나는 유나라고해. 내가 책을 만들었어. 한번 읽어볼래??")
