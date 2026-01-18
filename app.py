import streamlit as st

st.set_page_config(
    page_title="AI Video Character Prompt Tool (VI-EN)",
    layout="wide"
)

st.title("🎬 AI Video Character Prompt Generator (VI – EN)")
st.caption("Tạo prompt nhân vật video nhất quán | Xuất Tiếng Việt & English")

# =========================
# CHARACTER INFO
# =========================
st.header("1️⃣ Thông tin nhân vật")

col1, col2 = st.columns(2)

with col1:
    topic_vi = st.text_input("Chủ đề chính (VI)", "Giáo dục tài chính cá nhân")
    topic_en = st.text_input("Main topic (EN)", "Personal finance education")

    gender = st.selectbox("Giới tính", ["Nam", "Nữ", "Phi giới tính"])
    age = st.text_input("Độ tuổi", "28–32")

    appearance_vi = st.text_area(
        "Ngoại hình (VI)",
        "Gương mặt thân thiện, phong thái chuyên nghiệp, ăn mặc hiện đại"
    )

    appearance_en = st.text_area(
        "Appearance (EN)",
        "Friendly face, professional demeanor, modern outfit"
    )

with col2:
    personality_vi = st.text_area(
        "Tính cách & khí chất (VI)",
        "Tự tin, truyền cảm hứng, dễ hiểu"
    )

    personality_en = st.text_area(
        "Personality & vibe (EN)",
        "Confident, inspiring, easy to understand"
    )

    voice_vi = st.text_area(
        "Giọng nói (VI)",
        "Giọng ấm, rõ ràng, tốc độ vừa phải"
    )

    voice_en = st.text_area(
        "Voice style (EN)",
        "Warm, clear voice, moderate speed"
    )

    visual_style = st.text_area(
        "Phong cách hình ảnh",
        "Realistic, cinematic lighting, 4K, sharp focus"
    )

st.divider()

# =========================
# VIDEO STYLE
# =========================
st.header("2️⃣ Phong cách & bối cảnh video")

video_style = st.text_area(
    "Phong cách video",
    "Talking head, eye-level camera, stable shot"
)

scene = st.text_area(
    "Bối cảnh",
    "Modern studio, minimal background, soft light"
)

st.divider()

# =========================
# EPISODE CONTENT
# =========================
st.header("3️⃣ Nội dung tập video")

episode_vi = st.text_input(
    "Chủ đề tập (VI)",
    "Cách quản lý chi tiêu hiệu quả"
)

episode_en = st.text_input(
    "Episode topic (EN)",
    "How to manage personal expenses effectively"
)

duration = st.selectbox(
    "Thời lượng",
    ["30s", "45s", "60s", "90s"]
)

cta_vi = st.text_input(
    "CTA (VI)",
    "Theo dõi để xem thêm video hữu ích"
)

cta_en = st.text_input(
    "CTA (EN)",
    "Follow for more useful videos"
)

# =========================
# GENERATE
# =========================
if st.button("🚀 Tạo Prompt Song Ngữ"):
    # ---------- MASTER PROMPT ----------
    st.subheader("🎯 MASTER CHARACTER PROMPT (EN)")

    master_prompt_en = f"""
You are creating a consistent AI video character.

Character profile:
- Gender: {gender}
- Age range: {age}
- Appearance: {appearance_en}
- Personality: {personality_en}
- Voice style: {voice_en}

Visual style:
- {visual_style}

This character must remain consistent across all videos in the series.
"""

    st.code(master_prompt_en.strip(), language="text")

    # ---------- VIDEO PROMPT ----------
    st.subheader("🎬 VIDEO PROMPT (EN)")

    video_prompt_en = f"""
Create a {duration} AI video.

Main topic:
{topic_en}

Episode content:
{episode_en}

Character:
Use the exact same character defined in the MASTER CHARACTER PROMPT.

Video style:
- {video_style}
- Scene: {scene}

Tone:
Professional, friendly, clear, engaging.

Ending CTA:
"{cta_en}"

High quality, cinematic look, stable camera, natural movement.
"""

    st.code(video_prompt_en.strip(), language="text")

    # ---------- VIETNAMESE VERSION ----------
    st.subheader("🇻🇳 BẢN DIỄN GIẢI TIẾNG VIỆT (ĐỂ REVIEW)")

    explain_vi = f"""
NHÂN VẬT:
- Giới tính: {gender}
- Độ tuổi: {age}
- Ngoại hình: {appearance_vi}
- Tính cách: {personality_vi}
- Giọng nói: {voice_vi}

CHỦ ĐỀ:
- Chủ đề chính: {topic_vi}
- Tập này nói về: {episode_vi}

PHONG CÁCH VIDEO:
- {video_style}
- Bối cảnh: {scene}

CTA:
- {cta_vi}
"""

    st.text(explain_vi.strip())

    st.success("✅ Đã tạo prompt song ngữ – dùng trực tiếp cho AI Video")
