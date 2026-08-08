import urllib.parse
import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="BeatFinder | DJ Tool", page_icon="🎛️", layout="centered"
)

# Estilos CSS personalizados para lograr el diseño de tarjetas oscuras
st.markdown(
    """
    <style>
    .stApp { background-color: #0e1117; color: #ffffff; }
    .stTextInput input { 
        background-color: #161b22; 
        color: white; 
        border-radius: 10px; 
        border: 1px solid #30363d; 
        padding: 10px;
    }
    .card {
        background-color: #161b22;
        border-radius: 12px;
        padding: 16px;
        margin-bottom: 12px;
        border: 1px solid #30363d;
    }
    .metric-title { 
        font-size: 11px; 
        color: #8b949e; 
        text-transform: uppercase; 
        letter-spacing: 1.2px; 
        font-weight: 600;
    }
    .metric-value { 
        font-size: 22px; 
        font-weight: bold; 
        margin-top: 4px;
    }
    .store-btn {
        background-color: #161b22;
        padding: 14px 18px;
        border-radius: 10px;
        border: 1px solid #30363d;
        display: flex;
        justify-content: space-between;
        align-items: center;
        color: white;
        text-decoration: none;
        margin-bottom: 8px;
        transition: border-color 0.2s;
    }
    .store-btn:hover {
        border-color: #58a6ff;
    }
    .badge {
        background: #21262d; 
        padding: 5px 12px; 
        border-radius: 6px; 
        font-size: 12px; 
        border: 1px solid #30363d;
        color: #c9d1d9;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Cabecera de la App
st.markdown(
    "<h1 style='margin-bottom: 0px;'>BeatFinder 🎛️</h1>", unsafe_allow_html=True
)
st.markdown(
    "<p style='color: #8b949e; font-size: 14px;'>Buscador técnico de música y tiendas oficiales para DJs — por @djgabocl</p>",
    unsafe_allow_html=True,
)
st.markdown("<br>", unsafe_allow_html=True)

# Barra de búsqueda principal
query_input = st.text_input(
    "Ingresa el nombre del track y artista:",
    placeholder="Ej: Fisher - Losing It",
)

if query_input:
    encoded_query = urllib.parse.quote_plus(query_input)

    st.markdown("---")
    st.markdown(f"### 🎧 Resultados para: *{query_input}*")

    # Tarjetas de Métricas (BPM y Key simulados / orientativos)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            """
            <div class='card'>
                <div class='metric-title'>BPM Estimado</div>
                <div class='metric-value' style='color: #3fb950;'>124 - 128</div>
            </div>
        """,
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            """
            <div class='card'>
                <div class='metric-title'>Tonalidad Sugerida</div>
                <div class='metric-value' style='color: #58a6ff;'>Compatible / Key</div>
            </div>
        """,
            unsafe_allow_html=True,
        )

    # Tarjeta de formatos
    st.markdown(
        """
        <div class='card'>
            <div class='metric-title'>Formato de audio recomendado</div>
            <div style='margin-top: 6px; font-size: 14px;'>🟢 <b>Lossless (WAV/AIFF)</b> &nbsp;|&nbsp; 🔵 <b>320kbps MP3</b></div>
        </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 🛒 Tiendas Oficiales")

    # Enlaces directos a tiendas con diseño de botones pro
    beatport_url = f"https://www.beatport.com/search?q={encoded_query}"
    traxsource_url = f"https://www.traxsource.com/search?term={encoded_query}"
    apple_url = f"https://music.apple.com/us/search?term={encoded_query}"
    youtube_url = (
        f"https://www.youtube.com/results?search_query={encoded_query}+audio"
    )

    st.markdown(
        f"""
        <a href="{beatport_url}" target="_blank" class="store-btn">
            <span>🟢 <b>Beatport</b></span>
            <span class="badge">View Track ↗</span>
        </a>
        <a href="{traxsource_url}" target="_blank" class="store-btn">
            <span>🟠 <b>Traxsource</b></span>
            <span class="badge">View Track ↗</span>
        </a>
        <a href="{apple_url}" target="_blank" class="store-btn">
            <span>⚪ <b>Apple Music</b></span>
            <span class="badge">View Track ↗</span>
        </a>
        <a href="{youtube_url}" target="_blank" class="store-btn">
            <span>🔴 <b>YouTube Audio</b></span>
            <span class="badge">View Track ↗</span>
        </a>
    """,
        unsafe_allow_html=True,
    )
    
