import streamlit as st

st.title("Microscope Image of the Day")

# Main image (URL)
main_image_url = "https://askabiologist.asu.edu/sites/default/files/resources/articles/buildingblocks/Hooke_Micrographia_cork_260.jpg"
st.subheader("What is today's mystery image?")
st.image(main_image_url, use_container_width=True)

# Four option images (URLs) with labels
options = [
    {
        "url": "https://upload.wikimedia.org/wikipedia/commons/0/02/Bumblebee%27s_wing.jpg",
        "label": "Insect Wing"
    },
    {
        "url": "https://upload.wikimedia.org/wikipedia/commons/c/c7/Lisc_lipy.jpg",
        "label": "Leaf"
    },
    {
        "url": "https://cdn11.bigcommerce.com/s-z9t2ne/images/stencil/600w/products/43534/409981/vision-cl-stone-upholstery-heavy-curtain-fabric__36877.1652014387.jpg?c=2",
        "label": "Fabric"
    },
    {
        "url": "https://www.widgetco.com/cdn/shop/collections/1-1-wine-corks_be4d5471-97c5-4818-8566-d6a336b15bc0.jpg?v=1612468346&width=500",
        "label": "Cork"
    }
]

# Correct answer index (0-based)
correct_index = 3  # Cork

st.subheader("Choose the correct match:")

# Arrange in 2x2 grid
for row in range(2):
    cols = st.columns(2)
    for col, i in zip(cols, range(row*2, (row+1)*2)):
        with col:
            # Create an image-as-button using markdown
            button_html = f"""
            <style>
            .img-button {{
                border: none;
                background: none;
                padding: 0;
            }}
            .img-button img {{
                width: 100%;
                border-radius: 8px;
                cursor: pointer;
                transition: transform 0.1s;
            }}
            .img-button img:hover {{
                transform: scale(1.03);
                border: 2px solid #4CAF50;
            }}
            </style>
            <form action="" method="get">
                <button class="img-button" type="submit" name="choice" value="{i}">
                    <img src="{options[i]['url']}">
                </button>
            </form>
            """
            st.markdown(button_html, unsafe_allow_html=True)
            st.markdown(
                f"<div style='text-align:center; font-size:18px; font-weight:600; color:#222;'>"
                f"{options[i]['label']}</div>",
                unsafe_allow_html=True
            )
# ✅ Updated API
choice = st.query_params.get("choice")
if choice:
    choice = int(choice[0])
    st.session_state.choice = choice

# Feedback
if "choice" in st.session_state:
    if st.session_state.choice == correct_index:
        st.success("✅ Correct!", icon="✅")
        st.markdown(
            """
            <a href="https://www.youtube.com/watch?v=fu3qH7xpSgE" target="_blank" style="text-decoration: none; color: #1E90FF;">
                👉 Click here to learn more from MIT Learn
            </a>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.error("❌ Try again.")
