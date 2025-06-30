import streamlit as st
import openai

# Streamlit 앱 설정
st.set_page_config(page_title="GPT 맞춤법 & 높임말 교정기", layout="centered")
st.title("🤖 GPT 기반 맞춤법 & 높임말 교정 챗봇")

# OpenAI API 키 설정 (직접 넣기보다는 secrets.toml 사용 추천)
openai.api_key = st.secrets["OPENAI_API_KEY"]  # secrets.toml에 저장했다고 가정

# 사용자 입력
user_input = st.text_area("✍️ 문장을 입력하세요:", height=250)

def correct_text_gpt(text):
    prompt = (
        "다음 문장의 맞춤법, 띄어쓰기, 높임말을 자연스럽고 올바르게 고쳐주세요. "
        "문장 뜻은 바꾸지 말고, 어른에게 하는 말투로 높임말을 사용하세요.\n\n"
        f"문장: {text}\n\n"
        "수정된 문장:"
    )
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=300,
        )
        corrected = response.choices[0].message.content.strip()
        return corrected
    except Exception as e:
        return f"오류가 발생했습니다: {e}"

# 버튼 클릭 시 교정 실행
if st.button("✨ 교정하기"):
    if user_input.strip() == "":
        st.warning("먼저 문장을 입력해주세요!")
    else:
        with st.spinner("교정 중입니다..."):
            corrected_text = correct_text_gpt(user_input)
            st.subheader("✅ 교정된 문장")
            st.success(corrected_text)

st.markdown("---")
st.markdown("💡 예시: 안녕 나는 유나라고해. 내가 책을 만들었어. 한번 읽어볼래??")
