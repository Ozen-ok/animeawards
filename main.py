import streamlit as st
import pandas as pd

st.set_page_config(page_title="Anime Awards 🏆", page_icon="🎬", layout="centered")

# Banco de dados na memória do servidor
@st.cache_resource
def pegar_banco_de_votos():
    return []

votos_db = pegar_banco_de_votos()

st.title("🏆 Anime Awards - Aberturas e Encerramentos")
st.write("Escolha seu nome, assista ao vídeo e dê sua nota!")

# 1. Seletor de Votantes (Os 5 jurados)
votantes = ["Chrystian", "Mateus", "Lucas", "Giovana", "Gustavo"]
votante_atual = st.selectbox("👤 Quem está votando agora?", votantes)

st.divider()

# 2. Lista dos animes (Ajuste os nomes e links reais aqui)
animes = [
    {"nome": "Jujutsu Kaisen (2ª Temp) - SPECIALZ", "link": "https://www.youtube.com/watch?v=5yb2N3pn2FA"},
    {"nome": "Oshi no Ko - Idol", "link": "https://www.youtube.com/watch?v=DCCRNzKvWRg"},
    {"nome": "Frieren - Yuusha", "link": "https://www.youtube.com/watch?v=lLxAbevUyIQ"}
]

nomes_animes = [a["nome"] for a in animes]
anime_selecionado = st.selectbox("🎵 Escolha a Abertura/Encerramento:", nomes_animes)

link_atual = next(a["link"] for a in animes if a["nome"] == anime_selecionado)
st.write(f"**🎬 Link do Vídeo:** [Assista aqui]({link_atual})")

# 3. Player do YouTube e Nota
st.video(link_atual)
nota = st.slider("⭐ Que nota essa abertura/ending merece?", min_value=0.0, max_value=10.0, value=5.0, step=0.5)

# 4. Salvar o Voto
if st.button("Salvar Voto 💾"):
    # Checa se o jurado já votou nessa categoria específica pra evitar clique duplo
    voto_existente = next((v for v in votos_db if v["Votante"] == votante_atual and v["Anime"] == anime_selecionado), None)
    
    if voto_existente:
        st.warning(f"Ei! {votante_atual} já votou em {anime_selecionado}. Deixa o resto da galera votar!")
    else:
        votos_db.append({
            "Votante": votante_atual,
            "Anime": anime_selecionado,
            "Nota": nota
        })
        st.success(f"Voto de {votante_atual} registrado com sucesso!")

st.divider()

# 5. Tabela de Resultados Ao Vivo
st.subheader("📊 Resultados em Tempo Real")

if votos_db:
    df = pd.DataFrame(votos_db)
    
    # Mostra os votos individuais
    with st.expander("Ver todos os votos detalhados"):
        st.dataframe(df, use_container_width=True)
    
    # Calcula o Ranking (Média de cada anime)
    st.write("**🏆 Ranking Atual (Média das Notas):**")
    ranking = df.groupby("Anime")["Nota"].mean().reset_index()
    ranking = ranking.sort_values(by="Nota", ascending=False).reset_index(drop=True)
    
    st.dataframe(ranking, use_container_width=True)
else:
    st.info("Nenhum voto registrado ainda. Comecem os trabalhos!")
