import streamlit as st
import streamlit.components.v1 as components

# 頁面標題與簡介
st.title("🎵 音樂風格個性診斷 Quiz")
st.write("回答以下問題，測出你今天的專屬音樂風格與推薦專輯！")

st.divider()

# --- 問題區 ---
st.subheader("1. 你今天的心情或狀態比較接近？")
  q1 = st.radio(
  "選擇一個最符合的選項：",
  ["需要來點能量，重整旗鼓 ⚡", "想要放鬆心情，順其自然 ☕"],
  index=0
)

st.subheader("2. 你現在希望音樂引起你的能量感 (1最低 ~ 10最高)：")
energy = st.slider("拉動滑塊選擇能量值：", min_value=1, max_value=10, value=5)

# --- 診斷按鈕 ---
if st.button("✨ 產生我的音樂風格診斷"):
  st.divider()
  st.header("📊 診斷結果如下：")

  # 根據 energy 數值進行條件判斷
if energy >= 7:
  style_title = "🔥 你的靈魂類型：高能搖滾 / 電子派對 Rock & EDM"
  style_desc = "你現在充滿能量！需要節奏強烈、重低音滿滿的音樂來炸翻全場！"
  album_cover = "https://picsum.photos/id/1025/300/300"
  album_caption = "推薦專輯：Linkin Park - Hybrid Theory"
  spotify_html = """
  <iframe style="border-radius:12px" src="https://open.spotify.com/embed/album/6noUdB243Bqf3uL41R9p3p?utm_source=generator" width="100%" height="152" frameborder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
  """

elif energy >= 4:
  style_title = "🎵 你的靈魂類型：Pop 流行樂 Pop Essentials"
  style_desc = "你現在適合輕快流暢的旋律，來點流行金曲讓你心情保持愉悅！"
  album_cover = "https://picsum.photos/id/1062/300/300"
  album_caption = "推薦專輯：Taylor Swift - 1989 (Taylor's Version)"
  spotify_html = """
  <iframe style="border-radius:12px" src="https://open.spotify.com/embed/album/64LU4c133RrmTYL9C1283f?utm_source=generator" width="100%" height="152" frameborder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
  """

else:
  style_title = "☕ 你的靈魂類型：深夜獨立 / Lofi 療癒系"
  style_desc = "你現在需要平靜與放鬆，輕柔的背景音樂能陪你享受專屬的舒服時光。"
  album_cover = "https://picsum.photos/id/1069/300/300"
  album_caption = "推薦專輯：Lofi Chill Beats"
  spotify_html = """
  <iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1DXdLENR312111?utm_source=generator" width="100%" height="152" frameborder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
  """

# 顯示結果內容
st.success(style_title)
st.write(style_desc)

# 顯示動態圖片
st.image(album_cover, caption=album_caption, width=300)

# 顯示 Spotify 音樂播放器
st.subheader("🎧 立即試聽：")
components.html(spotify_html, height=160)

