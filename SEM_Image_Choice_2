import streamlit as st

st.title("Image Matching Game")

# Main image (URL instead of file)
main_image_url = "https://upload.wikimedia.org/wikipedia/commons/3/36/Hopetoun_falls.jpg"
st.subheader("Match this image:")
st.image(main_image_url, use_container_width=True)

# Four option images (URLs)
options = [
    "https://upload.wikimedia.org/wikipedia/commons/5/50/VdNH_Cathedral_SaoPaulo.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/f/f6/Eiffel_Tower_at_dawn_from_the_Trocad%C3%A9ro_-_June_2006_edit.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/a/a8/Taj-Mahal.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/6/6e/Golde33443.jpg"
]

# Correct answer index
correct_index = 2  # Taj Mahal in this example

st.subheader("Choose the correct match:")

# Two rows of two columns each
for row in range(2):
    cols = st.columns(2)
    for col, i in zip(cols, range(row*2, (row+1)*2)):
        with col:
            st.image(options[i], use_container_width=True)
            if st.button(f"Option {i+1}"):
                st.session_state.choice = i

# Feedback
if "choice" in st.session_state:
    if st.session_state.choice == correct_index:
        st.success("✅ Correct!")
    else:
        st.error("❌ Try again.")
