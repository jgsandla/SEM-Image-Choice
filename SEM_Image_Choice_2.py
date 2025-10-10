import streamlit as st

st.title("Microscope Image of the Day")

# --- Track which image set we're on (0 or 1) ---
if "image_index" not in st.session_state:
    st.session_state.image_index = 0

# --- Define TWO image sets, each with its own correct answer ---
image_sets = [
    {
        "main_image": "https://i0.wp.com/www.beanthinking.org/wp-content/uploads/2016/11/Zeiss_Flickr_CoffeeGrounds750x.jpg?ssl=1",
        "options": [
            {"url": "https://www.peachtreepestcontrol.com/wp-content/uploads/2023/07/Wasps-in-Comb-on-rustic-wooden-board.jpg", "label": "Wasp Nest"},
            {"url": "https://www.cooperscoffeeco.com/wp-content/uploads/2023/04/coffee-beans-and-ground-coffee-on-a-wooden-table-l-2022-11-15-14-35-11-utc.jpg", "label": "Ground Coffee"},
            {"url": "https://www.filter-elements.org/img/aluminum-foam.jpg", "label": "Aluminum Foam"},
            {"url": "https://stonesdirect.com/cdn/shop/articles/Polished-mixed-gravel.jpg?v=1723461817&width=957", "label": "Pebbles"}
        ],
        "correct_index": 1  # Ground Coffee
    },
    {
        "main_image": "https://askabiologist.asu.edu/sites/default/files/resources/articles/buildingblocks/Hooke_Micrographia_cork_260.jpg",
        "options": [
            {"url": "https://upload.wikimedia.org/wikipedia/commons/0/02/Bumblebee%27s_wing.jpg", "label": "Insect Wing"},
            {"url": "https://upload.wikimedia.org/wikipedia/commons/c/c7/Lisc_lipy.jpg", "label": "Leaf"},
            {"url": "https://cdn11.bigcommerce.com/s-z9t2ne/images/stencil/600w/products/43534/409981/vision-cl-stone-upholstery-heavy-curtain-fabric__36877.1652014387.jpg?c=2", "label": "Fabric"},
            {"url": "https://www.widgetco.com/cdn/shop/collections/1-1-wine-corks_be4d5471-97c5-4818-8566-d6a336b15bc0.jpg?v=1612468346&width=500", "label": "Cork"}
        ],
        "correct_index": 2  # Sand
    }
]

# --- Select current set ---
current = image_sets[st.session_state.image_index]
main_image_url = current["main_image"]
options = current["options"]
correct_index = current["correct_index"]

# --- Main image ---
st.subheader("What is today's mystery image?")
st.image(main_image_url, use_container_width=True)

# --- Choices ---
st.subheader("Choose the correct match:")

for row in range(2):
    cols = st.columns(2)
    for col, i in zip(cols, range(row * 2, (row + 1) * 2)):
        with col:
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

# --- Read selection from query params (newer Streamlit returns a string) ---
qp_choice = st.query_params.get("choice")
if qp_choice is not None:
    try:
        st.session_state.choice = int(qp_choice)
    except ValueError:
        pass
    # Clear so the selection doesn't persist across reruns or image sets
    st.query_params.clear()

# --- Feedback (for the current image set only) ---
if "choice" in st.session_state:
    if st.session_state.choice == correct_index:
        st.success("✅ Correct! This is a scanning electron microscope image of roasted, ground coffee beans.")
    else:
        st.error("❌ Try again.")

# --- Next image button: only shown on the first image set ---
if st.session_state.image_index == 0:
    if st.button("Next image ▶️"):
        st.session_state.image_index = 1
        st.session_state.pop("choice", None)  # reset any previous selection
        st.rerun()
