import streamlit as st
import pandas as pd

st.set_page_config(page_title="CINEMINHAINHA ANIME AWARDS 🏆", page_icon="🎬", layout="centered")

# Banco de dados na memória do servidor
@st.cache_resource
def pegar_banco_de_votos():
    # Agora o banco diferencia a categoria (Opening ou Ending)
    return []

votos_db = pegar_banco_de_votos()

st.title("🏆 CINEMINHAINHA ANIME AWARDS")

# 1. Divisão por Categorias usando Tabs
tab_op, tab_ed = st.tabs(["🎵 Aberturas (Openings)", "🎞️ Encerramentos (Endings)"])

# Configuração comum
votantes = ["Chrystian", "Mateus", "Lucas", "Giovana", "Gustavo"]
votante_atual = st.sidebar.selectbox("👤 Quem está votando?", votantes)

# Listas de Animes (Ajuste conforme necessário)
animes_op = [
    {"nome": "ReawakeR (feat. Felix of Stray Kids) by LiSA", "link": "https://www.youtube.com/watch?v=sgnYEfM7U2U"},
    {"nome": "Saikai (再会) by Vaundy", "link": "https://www.youtube.com/watch?v=UP7la6a1H1g"},
    {"nome": "Kakumei Douchuu (革命道中) by AiNA THE END (アイナ・ジ・エンド)", "link": "https://www.youtube.com/watch?v=DCCRNzKvWRg"},
]

animes_ed = [
    {"nome": "AiNA THE END (ED)", "link": "https://www.youtube.com/watch?v=DCCRNzKvWRg"}
]

def sistema_votacao(lista_animes, categoria):
    # Filtra votos do usuário NESTA categoria
    votos_usuario_cat = [v["Anime"] for v in votos_db if v["Votante"] == votante_atual and v["Categoria"] == categoria]
    animes_pendentes = [a for a in lista_animes if a["nome"] not in votos_usuario_cat]

    if animes_pendentes:
        anime_atual = animes_pendentes[0]
        st.subheader(f"Avaliar: {anime_atual['nome']}")
        st.video(anime_atual["link"])
        
        nota = st.slider(f"Nota para {anime_atual['nome']}", 0.0, 10.0, 5.0, 0.5, key=f"n_{categoria}_{anime_atual['nome']}")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button(f"Salvar Voto ⏭️", key=f"btn_{categoria}_{anime_atual['nome']}"):
                votos_db.append({"Votante": votante_atual, "Anime": anime_atual['nome'], "Nota": nota, "Categoria": categoria})
                st.rerun()
    else:
        st.success(f"✅ {votante_atual} concluiu esta categoria!")

    # Lógica de "Voltar Voto" (Deleta o último voto deste usuário nesta categoria)
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
        
        # Adiciona 1 ao índice para começar do 1 (1º lugar, 2º lugar...)
        ranking.index = ranking.index + 1
        
        # Exibe como dataframe (que aceita esconder o índice) em vez de table
        st.dataframe(ranking.style.format(precision=2), use_container_width=True, hide_index=True)
    else:
        st.info("Ainda não há votos nesta categoria.")