import streamlit as st

# 頁面標題與簡介
st.title("🎵 專屬音樂風格診斷室")
st.write("回答以下簡單的問題，測出最適合你的音樂風格與推薦歌單！")

st.divider() # 畫一條分隔線

# 題目一：單選題
q1 = st.radio(
"1. 當你心情沉重、想放空時，你通常會選擇？",
["獨自戴上耳機聽輕柔配樂", "播放輕快的流行歌轉移注意力", "聽重金屬/搖滾樂宣洩情緒"]
)

# 題目二：滑桿選擇
energy = st.slider("2. 你現在希望音樂帶給你的能量感（1最低 ～ 10最高）：", 1, 10, 5)

# 測驗按鈕與結果判斷
if st.button("✨ 產生我的音樂風格診斷"):
    st.balloons() # 跑出氣球特效！
    st.subheader("📊 診斷結果如下：")

if energy <= 4:
    st.success("🍵 **你的靈魂類型：深夜獨立/Lofi 療癒系**")
    st.write("你需要安靜且富有情感的旋律來平復心情，適合在讀書或睡前聆聽。")
    st.caption("💡 推薦歌單：Lofi Girl Chill Beats / 獨立民謠系列")
elif energy <= 7:
    st.success("🎧 **你的靈魂類型：都會流行/節奏藍調 Pop & R&B**")
    st.write("你喜歡有節奏感但又不至於太吵雜的音樂，能幫你保持好心情！")
    st.caption("💡 推薦歌單：Chill Pop / R&B Grooves")
else:
    st.success("🔥 **你的靈魂類型：高能搖滾/電子派對 Rock & EDM**")
    st.write("你現在充滿能量！需要節奏強烈、重低音滿滿的音樂來炸翻全場！")
    st.caption("💡 推薦歌單：Workout EDM / Hard Rock Essentials")

import streamlit as st

st.subheader("🎵 你的專屬音樂風格：Pop 流行樂")

# 使用網路圖片 URL (例如 Spotify 的專輯封面連結)
album_cover_url = "https://i.scdn.co/image/ab67616d0000b273e8b03176723040d7607a270a"

st.image(album_cover_url, caption="推薦專輯：1989 (Taylor Version)", width=300)





