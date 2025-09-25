import streamlit as st

st.title("Image Matching Game")

# Main image (URL)
main_image_url = "https://i0.wp.com/www.beanthinking.org/wp-content/uploads/2016/11/Zeiss_Flickr_CoffeeGrounds750x.jpg?ssl=1"
st.subheader("Match this image:")
st.image(main_image_url, use_container_width=True)

# Four option images (URLs) with labels
options = [
    {
        "url": "https://www.peachtreepestcontrol.com/wp-content/uploads/2023/07/Wasps-in-Comb-on-rustic-wooden-board.jpg",
        "label": "Wasp Nest"
    },
    {
        "url": "https://www.cooperscoffeeco.com/wp-content/uploads/2023/04/coffee-beans-and-ground-coffee-on-a-wooden-table-l-2022-11-15-14-35-11-utc.jpg",
        "label": "Ground Coffee"
    },
    {
        "url": "https://www.filter-elements.org/img/aluminum-foam.jpg",
        "label": "Aluminum Foam"
    },
    {
        "url": "https://www.widgetco.com/cdn/shop/collections/1-1-wine-corks_be4d5471-97c5-4818-8566-d6a336b15bc0.jpg?v=1612468346&width=500",
        "label": "Cork"
    }
]

# Correct answer index (0-based)
correct_index = 1  # Ground Coffee

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
            st.caption(options[i]['label'])

# ✅ Updated API
choice = st.query_params.get("choice")
if choice:
    choice = int(choice[0])
    st.session_state.choice = choice

# Feedback
if "choice" in st.session_state:
    if st.session_state.choice == correct_index:
        st.success("✅ Correct!")
    else:
        st.error("❌ Try again.")
