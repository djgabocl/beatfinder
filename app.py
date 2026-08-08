import streamlit as st
import urllib.parse

# Configuración de la página (Estilo Oscuro DJ)
st.set_page_config(page_title="BeatFinder 🎛️", page_icon="🎧", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0e0e12; color: #ffffff; }
    .stButton>button { background-color: #ffe600; color: #000000; font-weight: bold; width: 100%; border-radius: 8px; }
    </style>
""", unsafe_allow_html=True)

st.title("BeatFinder 🎛️")
st.caption("Buscador de tiendas oficiales y plataformas para DJs — por @djgabocl")

# Campo de búsqueda
track_input = st.text_input("Ingresa el nombre del track y artista:", placeholder="Ej: Fisher - Losing It")

if track_input:
    # Codificar el texto para que sea una URL válida
    query = urllib.parse.quote_plus(track_input)
    
    st.subheader("🛒 Tiendas y Plataformas Oficiales")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.link_button("🟢 Beatport", f"https://www.beatport.com/search?q={query}")
        st.link_button("⛺ Bandcamp", f"https://bandcamp.com/search?q={query}")
        st.link_button("🟠 Traxsource", f"https://www.traxsource.com/search?term={query}")
        
    with col2:
        st.link_button("🎧 Spotify", f"https://open.spotify.com/search/{query}")
        st.link_button("▶️ YouTube Music", f"https://music.youtube.com/search?q={query}")
        st.link_button("🍎 Apple Music", f"https://music.apple.com/us/search?term={query}")

    st.success("Haz clic en cualquiera de las tiendas para ir directo al resultado de búsqueda exacto.")
  
