import streamlit as st

st.title("Image Matching Game")

# Main image (URL)
main_image_url = "https://i0.wp.com/www.beanthinking.org/wp-content/uploads/2016/11/Zeiss_Flickr_CoffeeGrounds750x.jpg?ssl=1"
st.subheader("Match this image:")
st.image(main_image_url, use_container_width=True)

# Four option images (URLs)
options = [
    "https://www.peachtreepestcontrol.com/wp-content/uploads/2023/07/Wasps-in-Comb-on-rustic-wooden-board.jpg",
    "https://www.cooperscoffeeco.com/wp-content/uploads/2023/04/coffee-beans-and-ground-coffee-on-a-wooden-table-l-2022-11-15-14-35-11-utc.jpg",
    "https://www.filter-elements.org/img/aluminum-foam.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/6/6e/Golde33443.jpg"
]

# Correct answer index
correct_index = 2  # Taj Mahal

st.subheader("Choose the correct match:")

# Arrange in 2x2 grid
for row in range(2):
    cols = st.columns(2)
    for col, i in zip(cols, range(row*2, (row+1)*2)):
        with col:
            # Use a form to capture clicks uniquely
            with st.form(f"form_{i}"):
                st.image(options[i], use_container_width=True)
                submitted = st.form_submit_button("")
                if submitted:
                    st.session_state.choice = i

# Feedback
if "choice" in st.session_state:
    if st.session_state.choice == correct_index:
        st.success("✅ Correct!")
    else:
        st.error("❌ Try again.")
