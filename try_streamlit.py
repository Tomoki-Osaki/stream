import streamlit as st
import random

# タイトルを表示
st.title('数あてゲーム')

# ランダムな正解の数を設定
if 'correct_number' not in st.session_state:
    st.session_state.correct_number = random.randint(1, 100)

# ユーザーの入力を取得
guess = st.number_input('1から100の数を入力してください:', min_value=1, max_value=100, step=1)

# ボタンが押されたかどうかを確認
if st.button('予想する'):
    if guess == st.session_state.correct_number:
        st.success('おめでとうございます！正解です！')
        st.balloons()
        st.session_state.correct_number = random.randint(1, 100)  # 新しいゲームを開始する
    elif guess < st.session_state.correct_number:
        st.warning('もっと大きな数です。')
    else:
        st.warning('もっと小さな数です。')
