import streamlit as st
import pandas as pd

st.set_page_config(page_title="CINEMINHAINHA ANIME AWARDS 🏆", page_icon="🎬", layout="centered")

# Banco de dados na memória do servidor
@st.cache_resource
def pegar_banco_de_votos():
    return []

votos_db = pegar_banco_de_votos()

st.title("🏆 CINEMINHAINHA ANIME AWARDS")
st.write("Escolha seu nome, assista ao vídeo e dê sua nota!")

# Listas de Animes (Aberturas e Encerramentos)
animes_op = [
    {"anime": "Chainsaw Man O Filme - Arco da Reze", "musica": "IRIS OUT by Kenshi Yonezu", "exibicao": "Chainsaw Man: Reze Arc", "link": "https://www.youtube.com/watch?v=LmZD-TU96q4"},
    {"anime": "Clevatess", "musica": "Ruler by Mayu Maeshima", "exibicao": "Clevatess", "link": "https://www.youtube.com/watch?v=jQnIPTsWyC4"},
    {"anime": "Dandadan", "musica": "Kakumei Douchuu by AiNA THE END", "exibicao": "Dandadan", "link": "https://www.youtube.com/watch?v=DCCRNzKvWRg"},
    {"anime": "Demon Slayer: Castelo Infinito", "musica": "Taiyou ga Noboranai Sekai by Aimer", "exibicao": "Demon Slayer: Infinity Castle", "link": "https://www.youtube.com/watch?v=rspzC40lGVk"},
    {"anime": "Even Given the Worthless 'Appraiser' Class", "musica": "Crescendo by ASTERISM", "exibicao": "Strongest Appraiser", "link": "https://www.youtube.com/watch?v=aFE6AYJXEgk"},
    {"anime": "Gachiakuta", "musica": "HUGs by Paledusk", "exibicao": "Gachiakuta", "link": "https://www.youtube.com/watch?v=9f89PWhv8YE"},
    {"anime": "Isekai Quartet 3", "musica": "Isekai Concerto", "exibicao": "Isekai Quartet 3", "link": "https://www.youtube.com/watch?v=NwSaAjwNBrw"},
    {"anime": "Kowloon Generic Romance", "musica": "Summertime Ghost by Suiyoubi no Campanella", "exibicao": "Kowloon Generic Romance", "link": "https://www.youtube.com/watch?v=XBByBaC1WbM"},
    {"anime": "May I Ask for One Final Thing?", "musica": "Senjou no Hana by CHiCO with HoneyWorks", "exibicao": "One Final Thing", "link": "https://www.youtube.com/watch?v=DSYj9FLVqMY"},
    {"anime": "New Panty & Stocking with Garterbelt", "musica": "Theme of New PANTY & STOCKING by TeddyLoid", "exibicao": "Panty & Stocking", "link": "https://www.youtube.com/watch?v=4AXQpImawSQ"},
    {"anime": "New Saga", "musica": "Enja by 4s4ki", "exibicao": "New Saga", "link": "https://www.youtube.com/watch?v=_SpiB2tqgcg"},
    {"anime": "Nukitashi the Animation", "musica": "Utopia or Dystopia by Yuki Yumeno", "exibicao": "Nukitashi", "link": "https://www.youtube.com/watch?v=UKyXxUc7obg"},
    {"anime": "One-Punch Man 3° Temporada", "musica": "Get No Satisfied ! by JAM Project feat.BABYMETAL", "exibicao": "One-Punch Man S3", "link": "https://www.youtube.com/watch?v=Mo6yWVF6Md0"},
    {"anime": "Orb: On the Movements of the Earth", "musica": "Kaijuu by Sakanaction", "exibicao": "Orb", "link": "https://www.youtube.com/watch?v=eZAocot63s8"},
    {"anime": "Re:Zero 3° Temporada", "musica": "Reweave by Konomi Suzuki", "exibicao": "Re:Zero S3", "link": "https://www.youtube.com/watch?v=hCxZx7uHO1I"},
    {"anime": "Secrets of the Silent Witch", "musica": "Feel by Hitsujibungaku", "exibicao": "Silent Witch", "link": "https://www.youtube.com/watch?v=DWNiF9QdQ_E"},
    {"anime": "Solo Leveling 2° Temporada", "musica": "ReawakeR (feat. Felix of Stray Kids) by LiSA", "exibicao": "Solo Leveling S2", "link": "https://www.youtube.com/watch?v=C0zMWogztQs"},
    {"anime": "Sono Bisque Doll 2° Temporada", "musica": "Ao to Kirameki by Spira Spica", "exibicao": "Sono Bisque Doll S2", "link": "https://www.youtube.com/watch?v=ie5GcVid_8k"},
    {"anime": "Takopi's Original Sin", "musica": "Happy Lucky Chappy by ano", "exibicao": "Takopi's Original Sin", "link": "https://www.youtube.com/watch?v=ciFvLHCThdg"},
    {"anime": "The 100 Girlfriends 2° Temporada", "musica": "Arigato, Daisuki ni Natte Kurete by Rentarou Family", "exibicao": "100 Girlfriends S2", "link": "https://www.youtube.com/watch?v=Itke9o80go0"},
    {"anime": "The Apothecary Diaries 2° Temporada", "musica": "Kusushiki by Mrs. GREEN APPLE", "exibicao": "Apothecary Diaries S2", "link": "https://www.youtube.com/watch?v=HrRxvh4bkHE"},
    {"anime": "The Banished Court Magician", "musica": "Quest by Kiiro Akiyama", "exibicao": "Banished Court Magician", "link": "https://www.youtube.com/watch?v=U5Xgk4yW7mA"},
    {"anime": "The Beginning After the End", "musica": "KINGSBLOOD by KALA", "exibicao": "Beginning After the End", "link": "https://www.youtube.com/watch?v=FkgC37ERJCY"},
    {"anime": "The Fragrant Flower Blooms with Dignity", "musica": "Manazashi wa Hikari by Tatsuya Kitani", "exibicao": "Fragrant Flower", "link": "https://www.youtube.com/watch?v=8WLNNu78mUk"},
    {"anime": "The Shiunji Family Children", "musica": "Honey Lemon by NACHERRY", "exibicao": "Shiunji Family", "link": "https://www.youtube.com/watch?v=MqKDozk20eA"},
    {"anime": "The Summer Hikaru Died", "musica": "Saikai by Vaundy", "exibicao": "The Summer Hikaru Died", "link": "https://www.youtube.com/watch?v=UP7la6a1H1g"},
    {"anime": "To Be Hero X", "musica": "INERTIA by SawanoHiroyuki[nZk]:Rei", "exibicao": "To Be Hero X", "link": "https://www.youtube.com/watch?v=j0KhH04xMlE"}
]

animes_ed = [
    {"anime": "Chainsaw Man O Filme - Arco da Reze", "musica": "JANE DOE by Kenshi Yonezu", "exibicao": "Chainsaw Man: Reze Arc", "link": "https://www.youtube.com/watch?v=qYcU41ew_BM"},
    {"anime": "Clevatess", "musica": "Destiny by Ellie Goulding", "exibicao": "Clevatess", "link": "https://www.youtube.com/watch?v=d4rp4rBPQks"},
    {"anime": "Dandadan", "musica": "Doukashiteru by WurtS", "exibicao": "Dandadan", "link": "https://www.youtube.com/watch?v=AhNYcpN1pEU"},
    {"anime": "Demon Slayer: Castelo Infinito", "musica": "Zankoku na Yoru ni Kagayake by LiSA", "exibicao": "Demon Slayer: Infinity Castle", "link": "https://www.youtube.com/watch?v=ysdtX8kRTuQ"},
    {"anime": "Even Given the Worthless 'Appraiser' Class", "musica": "Rock wa Shinanai by 22/7", "exibicao": "Strongest Appraiser", "link": "https://www.youtube.com/watch?v=FH8docU39PM"},
    {"anime": "Gachiakuta", "musica": "Tomoshibi by DUSTCELL", "exibicao": "Gachiakuta", "link": "https://www.youtube.com/watch?v=EXneg1C9iLg"},
    {"anime": "Isekai Quartet 3", "musica": "Kimi-iro, Boku-iro by Konomi Suzuki", "exibicao": "Isekai Quartet 3", "link": "https://www.youtube.com/watch?v=NvPMPb42epQ"},
    {"anime": "Kowloon Generic Romance", "musica": "Koi no Retronym by mekakushe", "exibicao": "Kowloon Generic Romance", "link": "https://www.youtube.com/watch?v=PqaxAGC7gZE"},
    {"anime": "May I Ask for One Final Thing?", "musica": "Inferior by Shiyui", "exibicao": "One Final Thing", "link": "https://www.youtube.com/watch?v=OIZd_vynwmU"},
    {"anime": "New Panty & Stocking with Garterbelt", "musica": "Reckless by m-flo", "exibicao": "Panty & Stocking", "link": "https://www.youtube.com/watch?v=v1daqPsmVFs"},
    {"anime": "New Saga", "musica": "her by Mahiru Coda", "exibicao": "New Saga", "link": "https://www.youtube.com/watch?v=465x4w84mUc"},
    {"anime": "Nukitashi the Animation", "musica": "Saikai-kei Joshi wa Dou Surya Ii desu ka? by Rie Ayase", "exibicao": "Nukitashi", "link": "https://www.youtube.com/watch?v=FWH4VQKzcmo"},
    {"anime": "One-Punch Man 3° Temporada", "musica": "Soko ni Aru Akari by Makoto Furukawa", "exibicao": "One-Punch Man S3", "link": "https://www.youtube.com/watch?v=DsWsyXCv8bQ"},
    {"anime": "Orb: On the Movements of the Earth", "musica": "Hebi by Yorushika", "exibicao": "Orb", "link": "https://www.youtube.com/watch?v=aJel-zCuABs"},
    {"anime": "Re:Zero 3° Temporada", "musica": "NOX LUX by MYTH & ROID", "exibicao": "Re:Zero S3", "link": "https://www.youtube.com/watch?v=aPzI7S3MVI4"},
    {"anime": "Secrets of the Silent Witch", "musica": "mild days by Hitsujibungaku", "exibicao": "Silent Witch", "link": "https://www.youtube.com/watch?v=qKpNiW8T6ro"},
    {"anime": "Solo Leveling 2° Temporada", "musica": "UN-APEX by TK from Ling tosite sigure", "exibicao": "Solo Leveling S2", "link": "https://www.youtube.com/watch?v=KxeHOxO3A3I"},
    {"anime": "Sono Bisque Doll 2° Temporada", "musica": "Kawaii Kaiwai by PiKi", "exibicao": "Sono Bisque Doll S2", "link": "https://www.youtube.com/watch?v=bLA3pkr6KN4"},
    {"anime": "Takopi's Original Sin", "musica": "Glass no Sen by Tele", "exibicao": "Takopi's Original Sin", "link": "https://www.youtube.com/watch?v=uA50rpzCKqY"},
    {"anime": "The 100 Girlfriends 2° Temporada", "musica": "Unmei?", "exibicao": "100 Girlfriends S2", "link": "https://www.youtube.com/watch?v=szBT0QhzQkU"},
    {"anime": "The Apothecary Diaries 2° Temporada", "musica": "Hitorigoto by Omoinotake", "exibicao": "Apothecary Diaries S2", "link": "https://www.youtube.com/watch?v=2ujbjT7k6ak"},
    {"anime": "The Banished Court Magician", "musica": "Kakera by aruma", "exibicao": "Banished Court Magician", "link": "https://www.youtube.com/watch?v=lfeCAXn4lbM"},
    {"anime": "The Beginning After the End", "musica": "Mahiru no Tsuki by seiza", "exibicao": "Beginning After the End", "link": "https://www.youtube.com/watch?v=PBuEya9wY2w"},
    {"anime": "The Fragrant Flower Blooms with Dignity", "musica": "Hare no Hi ni by Reira Ushio", "exibicao": "Fragrant Flower", "link": "https://www.youtube.com/watch?v=W4fND8qaTtE"},
    {"anime": "The Shiunji Family Children", "musica": "Honey Lemon by NACHERRY", "exibicao": "Shiunji Family", "link": "https://www.youtube.com/watch?v=6Kb695VS4B4"},
    {"anime": "The Summer Hikaru Died", "musica": "Anata wa Kaibutsu by TOOBOE", "exibicao": "The Summer Hikaru Died", "link": "https://www.youtube.com/watch?v=_dq21OHPJTk"},
    {"anime": "To Be Hero X", "musica": "KONTINUUM by SennaRin", "exibicao": "To Be Hero X", "link": "https://www.youtube.com/watch?v=gQ940ZInrTY"}
]

# 1. Divisão por Categorias usando Tabs
tab_op, tab_ed = st.tabs(["🎵 Aberturas (Openings)", "🎞️ Encerramentos (Endings)"])

# Configuração comum
votantes = ["Chrystian", "Mateus", "Lucas", "Giovana", "Gustavo"]
votante_atual = st.sidebar.selectbox("👤 Quem está votando?", votantes)

def sistema_votacao(lista_animes, categoria):
    # Filtra votos do usuário NESTA categoria
    votos_usuario_cat = [v["Anime"] for v in votos_db if v["Votante"] == votante_atual and v["Categoria"] == categoria]
    animes_pendentes = [a for a in lista_animes if a["exibicao"] not in votos_usuario_cat]

    if animes_pendentes:
        anime_atual = animes_pendentes[0]
        st.subheader(f"{anime_atual['musica']} ({anime_atual['exibicao']})")
        st.video(anime_atual["link"], autoplay=True)
        
        nota = st.slider(f"Nota para {anime_atual['exibicao']}", 0.0, 10.0, 5.0, 0.5, key=f"n_{categoria}_{anime_atual['exibicao']}")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button(f"Salvar Voto ⏭️", key=f"btn_{categoria}_{anime_atual['exibicao']}"):
                votos_db.append({"Votante": votante_atual, "Anime": anime_atual['exibicao'], "Nota": nota, "Categoria": categoria})
                st.rerun()
    else:
        st.success(f"✅ {votante_atual} concluiu esta categoria!")

    # Lógica de "Voltar Voto"
    if votos_usuario_cat:
        st.divider()
        ultimo_anime = votos_usuario_cat[-1]
        if st.button(f"⏪ Mudar voto de: {ultimo_anime}", key=f"back_{categoria}"):
            for i, v in enumerate(votos_db):
                if v["Votante"] == votante_atual and v["Anime"] == ultimo_anime and v["Categoria"] == categoria:
                    votos_db.pop(i)
                    st.rerun()

# Renderiza os sistemas nas abas
with tab_op:
    sistema_votacao(animes_op, "Opening")

with tab_ed:
    sistema_votacao(animes_ed, "Ending")

# 5. Resultados Consolidados
st.divider()
st.subheader("📊 Resultados Gerais")

if votos_db:
    df = pd.DataFrame(votos_db)
    
    with st.expander("Votos Detalhados"):
        st.dataframe(df, use_container_width=True, hide_index=True)
    
    # Ranking por Categoria
    cat_selecionada = st.selectbox("Ver ranking de:", ["Opening", "Ending"])
    df_cat = df[df["Categoria"] == cat_selecionada]
    
    if not df_cat.empty:
        ranking = df_cat.groupby("Anime")["Nota"].mean().reset_index()
        ranking = ranking.sort_values(by="Nota", ascending=False).reset_index(drop=True)
        ranking.index = ranking.index + 1
        st.dataframe(ranking.style.format(precision=2), use_container_width=True)
    else:
        st.info("Ainda não há votos nesta categoria.")