import streamlit as st
from difflib import ndiff

st.set_page_config(page_title="높임말 & 맞춤법 교정기", layout="centered")
st.title("📝 높임말 & 맞춤법 교정 챗봇")

# 사용자 입력 받기
user_input = st.text_area("✍️ 아이가 쓴 글을 붙여넣으세요:", height=250)

# 띄어쓰기 자동 보정 (간단한 rule 기반 예시)
def fix_spacing(text):
    text = text.replace("내가말했어", "내가 말했어")
    text = text.replace("엄마가말씀하셨다", "엄마가 말씀하셨다")
    text = text.replace("한번", "한 번")
    text = text.replace("읽어볼래??", "읽어 볼래요?")
    return text

# 교정 함수
def correct_text(text):
    corrections = {
        "유나라고해": "유나라고 해",
        "줬다": "드렸어요",
        "했어": "했습니다",
        "봤다": "보았습니다",
        "먹었어": "드셨어요",
        "갔어": "가셨어요",
        "엄마가 말했다": "어머님께서 말씀하셨어요",
        "아빠가 줬다": "아버지께서 주셨어요"
    }
    for wrong, right in corrections.items():
        text = text.replace(wrong, right)
    return text

# 교정 비교 출력 함수
def show_diff(original, corrected):
    diff = list(ndiff(original.split(), corrected.split()))
    added = [d[2:] for d in diff if d.startswith('+ ')]
    removed = [d[2:] for d in diff if d.startswith('- ')]
    st.markdown("### 🔍 변경된 단어:")
    st.write(f"- **추가됨:** {', '.join(added) if added else '없음'}")
    st.write(f"- **제거됨:** {', '.join(removed) if removed else '없음'}")

# 버튼 클릭 시 교정 실행
if st.button("✨ 교정하기"):
    if user_input.strip() == "":
        st.warning("먼저 글을 입력해주세요!")
    else:
        with st.spinner("교정 중입니다..."):
            spaced = fix_spacing(user_input)
            corrected = correct_text(spaced)
            st.subheader("✅ 교정된 글")
            st.success(corrected)
            show_diff(user_input, corrected)

st.markdown("---")
st.markdown("💡 예시: 안녕 나는 유나라고해. 내가 책을 만들었어. 한번 읽어볼래??")
