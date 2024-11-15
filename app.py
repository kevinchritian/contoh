import streamlit as st
import requests
import streamlit as st
from PIL import Image
import base64
import io


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout='wide')


hide_streamlit_style = """
<style>
    #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 0rem; padding-left:0rem; padding-right:0rem; padding-bottom:0rem;}
</style>
"""

# Memasukkan CSS custom ke dalam aplikasi
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


# Fungsi untuk mengonversi gambar ke format Base64
def convert_image_to_base64(image):
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode()



# Fungsi untuk mengonversi gambar menjadi base64
def convert_image_to_base64(image):
    # Membuka gambar dan mengubahnya ke dalam base64
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return img_str




# Memuat gambar dengan PIL

images_banner = Image.open('images/sampah.jpg')
image_base65 = convert_image_to_base64(images_banner)



# Menyisipkan link Bootstrap 5 ke dalam aplikasi Streamlit
st.markdown("""
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
""", unsafe_allow_html=True)

# Membaca file CSS dari file terpisah
with open("style/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


# Banner

# Membaca gambar dan mengonversinya ke Base64
with open("images/logo.png", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode()




# Menyisipkan gambar Base64 ke dalam tag <img>
st.markdown(f"""
<style>
    .try {{
        background-image: linear-gradient(to left, rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.8)), url('data:image/jpg;base64,{image_base65}');
        background-reapat: no-reapet;
        background-size: cover;
        background-position:center;
    }}
</style>
<div class="container-fluid banner try">
    <div class="container banner-content">
            <div>
                <div class="gambar mt-3 d-none d-md-block text-center">
                </div>
                <div>
                    <h1 class="text-center text-light tulisan-banner">
                        Pemilahan Sampah Pintar <br> 
                        <span class="txt-bld">Bersama NatureAIClassify</span>
                    </h1>
                </div>
            </div>
    </div>
</div>
""", unsafe_allow_html=True)