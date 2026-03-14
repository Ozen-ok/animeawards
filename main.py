import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Anime Awards 🏆", page_icon="🎬", layout="centered")

# Banco de dados na memória do servidor
@st.cache_resource
def pegar_banco_de_votos():
    return []

votos_db = pegar_banco_de_votos()

st.title("🏆 Anime Awards - Aberturas e Encerramentos")
st.write("Escolha seu nome, assista ao vídeo e dê sua nota!")

# 1. Seletor de Votantes
votantes = ["Chrystian", "Mateus", "Lucas", "Giovana", "Gustavo"]
votante_atual = st.selectbox("👤 Quem está votando agora?", votantes)

st.divider()

# 2. Lendo os vídeos locais da pasta 'videos'
pasta_videos = "videos"

# Verifica se a pasta existe. Se não, cria na hora pra não dar erro.
if not os.path.exists(pasta_videos):
    os.makedirs(pasta_videos)
    
# Pega todos os arquivos .mp4 da pasta
arquivos_mp4 = [f for f in os.listdir(pasta_videos) if f.endswith(".mp4")]

if not arquivos_mp4:
    st.warning(f"⚠️ Nenhum vídeo encontrado. Coloque seus arquivos .mp4 dentro da pasta '{pasta_videos}'.")
else:
    # Tira o ".mp4" do nome pra ficar mais bonito no menu (ex: "Jujutsu Kaisen.mp4" vira "Jujutsu Kaisen")
    nomes_animes = [arquivo.replace(".mp4", "") for arquivo in arquivos_mp4]
    
    anime_selecionado_bonito = st.selectbox("🎵 Escolha a Abertura/Encerramento:", nomes_animes)
    
    # Reconstrói o caminho exato do arquivo pra dar o play
    arquivo_selecionado = f"{anime_selecionado_bonito}.mp4"
    caminho_video = os.path.join(pasta_videos, arquivo_selecionado)

    # 3. Player de Vídeo Local e Nota
    st.video(caminho_video)
    nota = st.slider("⭐ Que nota essa abertura/ending merece?", min_value=0.0, max_value=10.0, value=5.0, step=0.5)

    # 4. Salvar o Voto
    if st.button("Salvar Voto 💾"):
        voto_existente = next((v for v in votos_db if v["Votante"] == votante_atual and v["Anime"] == anime_selecionado_bonito), None)
        
        if voto_existente:
            st.warning(f"Ei! {votante_atual} já votou em {anime_selecionado_bonito}. Deixa o resto da galera votar!")
        else:
            votos_db.append({
                "Votante": votante_atual,
                "Anime": anime_selecionado_bonito,
                "Nota": nota
            })
            st.success(f"Voto de {votante_atual} registrado com sucesso!")

st.divider()

# 5. Tabela de Resultados Ao Vivo
st.subheader("📊 Resultados em Tempo Real")

if votos_db:
    df = pd.DataFrame(votos_db)
    
    with st.expander("Ver todos os votos detalhados"):
        st.dataframe(df, use_container_width=True)
    
    st.write("**🏆 Ranking Atual (Média das Notas):**")
    ranking = df.groupby("Anime")["Nota"].mean().reset_index()
    ranking = ranking.sort_values(by="Nota", ascending=False).reset_index(drop=True)
    
    st.dataframe(ranking, use_container_width=True)
else:
    st.info("Nenhum voto registrado ainda. Comecem os trabalhos!")