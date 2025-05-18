import streamlit as st
from datetime import datetime

# 🎈 Page Config
st.set_page_config(
    page_title="Happy Birthday Sankar!",
    page_icon="🎂",
    layout="centered"
)

# 🌟 Title Banner
st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>🎉 Happy Birthday 🎉</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>🎉 Sankar Hariharan! 🎉</h1>", unsafe_allow_html=True)

st.markdown("---")

# 💌 Personal Heartfelt Message
st.subheader("💖 A Note from Me to You")
st.markdown("""Dear Hari(JK) Sankar,

I honestly don’t know where to begin — because words will always fall short when it comes to describing what you mean to me.

You’ve been more than a friend. You’ve been my anchor in chaos, my cheerleader in success, and my strength in moments I thought I couldn’t make it through. Through every high and low, every laugh and tear, you've stood by me without question, without hesitation — just pure, unconditional presence.

When things felt heavy, you never let me carry it alone. When I doubted myself, you believed in me more than I believed in myself. And when life gave us moments to celebrate, you made them unforgettable.

I can say this with my whole heart: you are everything to me. Not just because you were there, but because you chose to stay — and that means the world.

Thank you for being my constant, my safe space, my home in human form.

I’m grateful for every memory we’ve made and every one yet to come. Here's to you, and to a lifetime of being by each other’s side — through every up, down, twist, and turn.

With all my love and gratitude,
""")

# 📸 Photo Gallery
st.markdown("### 📸 Some Memories Together")

photos = [f"images/{i}.jpg" for i in range(1, 18)]

# Initialize session state
if "photo_index" not in st.session_state:
    st.session_state.photo_index = 0

# Display current photo
st.image(
    photos[st.session_state.photo_index],
    caption=f"Memory {st.session_state.photo_index + 1}",
    use_container_width=True
)

# Navigation buttons
col1, col2, col3 = st.columns([2, 5, 2])
with col1:
    if st.button("⬅️ Previous") and st.session_state.photo_index > 0:
        st.session_state.photo_index -= 1
with col3:
    if st.button("Next ➡️") and st.session_state.photo_index < len(photos) - 1:
        st.session_state.photo_index += 1

# 🕰️ Memory Lane
# 🕰️ Memory Lane (Styled Cards)
st.markdown("### 🕰️ Memory Lane")

memory_list = [
    {"year": "2021", "event": "We first met, and life hasn’t been the same since."},
    {"year": "2022", "event": "Late-night talks, spontaneous hangouts, and bonding over shared dreams."},
    {"year": "2023", "event": "Your birthday bash was unforgettable. You deserve the world."},
    {"year": "2024", "event": "We stood by each other through thick and thin. Forever grateful."},
]

for memory in memory_list:
    st.markdown(f"""
    <div style="border-left: 4px solid #FF4B4B; padding-left: 15px; margin: 20px 0;">
        <h4 style="color:#FF4B4B;">{memory['year']}</h4>
        <p style="margin-top: -10px;">{memory['event']}</p>
    </div>
    """, unsafe_allow_html=True)
# 🎵 Optional Music/Video
st.markdown("### 🎶 A Song for You")
st.video("https://www.youtube.com/watch?v=HT1afWWYeyY")  # Replace with his favorite song!

# ⏳ Countdown (Optional - if before 24 May)
today = datetime.today()
bday = datetime(today.year, 5, 24)
if today < bday:
    countdown = (bday - today).days
    st.info(f"⏳ Only **{countdown} days** left until the big day!")

# 🧁 Final Wish
st.markdown("---")
st.markdown("<h2 style='text-align: center;'>Have an amazing year ahead, Sankar! 🥳</h2>", unsafe_allow_html=True)

import time
from datetime import datetime, timedelta


st.markdown("### 💌 A Letter to Sankar")
st.markdown("""
<div style="padding: 20px; border: 2px dashed #ff4b4b; border-radius: 10px; background-color: #fff0f5;">
    <p style="font-size: 18px; line-height: 1.7;">
    Dear Sankar,

    Some bonds defy explanation — and ours is one of them. Through smiles and storms, you’ve been a constant.  
    You’ve shown me what true friendship feels like, what presence means, and how rare people like you are.  

    On your special day, I just want to say: thank you for being my anchor, my chaos, my joy, and my strength.  
    May this year bring you more growth, love, laughter, and dreams come true.

    Yours always,
    Karthik.K
    
</div>
""", unsafe_allow_html=True)

st.markdown("""
<style>
@keyframes fireworks {
  0% { transform: scale(0); opacity: 1; }
  100% { transform: scale(1); opacity: 0; }
}
.firework {
  position: fixed;
  width: 10px;
  height: 10px;
  background: #FF4B4B;
  border-radius: 50%;
  animation: fireworks 1s ease-out infinite;
  z-index: 999;
}
</style>
<div class="firework" style="top:100px; left:200px;"></div>
<div class="firework" style="top:150px; left:300px;"></div>
<div class="firework" style="top:200px; left:400px;"></div>
""", unsafe_allow_html=True)

import streamlit as st
from docx import Document
from io import BytesIO

# Create the letter content
letter = """
To Sankar — My Person

It’s been nearly four years since we met, and I still remember that very first day — you with your blue mask, and me awkwardly calling you “anna.” Feels like yesterday. Who would’ve thought that all those silly, cringey moments we’ve shared since then would grow into something so deep and real?

I know the early days of our friendship weren’t the smoothest. We clashed, misunderstood each other, and struggled to connect. But somewhere along the way, we began to adjust, to understand — and slowly, we built something beautiful.

I’m not someone people usually stick around with. I know that. But you — you were different. You chose to stay, to grow with me, and even to change in certain ways just to make things work. That means everything.

From IVs to projects, from late-night rants to all the times I just needed someone to listen — you’ve been there. Patient. Supportive. Constant. You deserve a hat’s off for that, bro.

My life has had its fair share of ups and downs, and in every single one of them, you’ve been by my side. From celebrating victories to fighting over the dumbest things, from watching movies together to our endless arguments — it’s all been part of this crazy, meaningful bond we’ve built.

Whether it was hackathon stress, project chaos, or random wins — you’ve always been the first person I’ve wanted to call. You’re the one I want to share all my happiest, proudest moments with. And honestly… I love you for that, bro.

I just hope we never lose this bond — the same silly fights, the same deep talks, the same random “let’s go out” energy. Life’s got surprises waiting for both of us, and I hope yours are beautiful and well-deserved.

Just be the same old you — but don’t be afraid to change when it matters. That’s part of being a good human. And hey, don’t wait for me to speak up — wake me up like you always do, annoy me, share the stuff you love, talk to me without hesitation. I want to know more and more about you.and not to have feeling of losing you bro…..

And if this message feels like it’s going a little deep… well, that’s just how much you mean to me.

Take care of yourself — and keep taking care of me too, bro.

Forever grateful, always your person.
"""

# Generate Word file in memory
doc = Document()
doc.add_paragraph(letter)

buffer = BytesIO()
doc.save(buffer)
buffer.seek(0)

# Show button to download
st.markdown("## 🎁 Click to Get Your Surprise")
st.download_button(
    label="Click to download your special letter 💌",
    data=buffer,
    file_name="Dear_Sankar_Letter.docx",
    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
)

# 🎂 Birthday Countdown Timer
st.markdown("## ⏳ Countdown to Sankar's Birthday")

# Target birthday (May 24, current year)
birthday = datetime(datetime.now().year, 5, 24, 0, 0, 0)

# If birthday has passed this year, use next year
if datetime.now() > birthday:
    birthday = birthday.replace(year=birthday.year + 1)

countdown_placeholder = st.empty()

while True:
    now = datetime.now()
    time_left = birthday - now

    if time_left.total_seconds() <= 0:
        countdown_placeholder.markdown("### 🎉 It's Sankar's Birthday Today! 🎉")
        break

    days = time_left.days
    hours, remainder = divmod(time_left.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    countdown_placeholder.markdown(
        f"""
        ### 🗓️ {days} days, {hours:02d} hours, {minutes:02d} minutes, {seconds:02d} seconds left!
        """,
        unsafe_allow_html=True
    )

    time.sleep(1)

