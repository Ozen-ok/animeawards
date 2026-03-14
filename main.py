import streamlit as st
import pandas as pd

st.set_page_config(page_title="CINEMINHAINHA ANIME AWARDS 🏆", page_icon="🎬", layout="centered")

# Banco de dados na memória do servidor
@st.cache_resource
def pegar_banco_de_votos():
    return []

votos_db = pegar_banco_de_votos()

st.title("🏆 CINEMINHAINHA ANIME AWARDS - Aberturas e Encerramentos")
st.write("Escolha seu nome, assista ao vídeo e dê sua nota!")

# 1. Seletor de Votantes (Os 5 jurados)
votantes = ["Chrystian", "Mateus", "Lucas", "Giovana", "Gustavo"]
votante_atual = st.selectbox("👤 Quem está votando agora?", votantes)

st.divider()

# 2. Lista dos animes (Ajuste os nomes e links reais aqui)
animes = [
    {"nome": "Solo Leveling Season 2: Arise from the Shadow", "link": "https://www.youtube.com/watch?v=sgnYEfM7U2U"},
    {"nome": "The Summer Hikaru Died", "link": "https://www.youtube.com/watch?v=UP7la6a1H1g"},
    {"nome": "'Kakumei Douchuu (革命道中)' by AiNA THE END (アイナ・ジ・エンド)", "link": "https://www.youtube.com/watch?v=DCCRNzKvWRg"}
]

# Descobre em quais animes o votante atual JÁ votou
votos_do_usuario = [v["Anime"] for v in votos_db if v["Votante"] == votante_atual]

# Filtra a lista para mostrar apenas os que ele AINDA NÃO votou
animes_pendentes = [a for a in animes if a["nome"] not in votos_do_usuario]

# 3. Lógica da Fila Automática
if len(animes_pendentes) > 0:
    # Pega sempre o próximo anime da fila
    anime_atual = animes_pendentes[0]
    nome_anime = anime_atual["nome"]
    link_atual = anime_atual["link"]
    
    st.subheader(f"🎵 Avaliando agora: {nome_anime}")
    st.write(f"**🎬 Link do Vídeo:** [Assista aqui]({link_atual})")
    
    # Player do YouTube
    st.video(link_atual)
    
    # IMPORTANTE: A key única no slider impede que a nota do anime anterior "vaze" pro próximo
    nota = st.slider("⭐ Que nota essa abertura/ending merece?", min_value=0.0, max_value=10.0, value=5.0, step=0.5, key=f"nota_{nome_anime}")

    # 4. Salvar o Voto
    if st.button("Salvar Voto e Ir para o Próximo ⏭️"):
        votos_db.append({
            "Votante": votante_atual,
            "Anime": nome_anime,
            "Nota": nota
        })
        # Recarrega a página instantaneamente para puxar o próximo da fila
        st.rerun()
        
else:
    # Quando zerar a fila de animes pendentes pra essa pessoa
    st.success(f"🎉 Aêê! {votante_atual} já avaliou todas as aberturas e encerramentos!")

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
    
    st.dataframe(ranking, use_container_width=True, hide_index=True)
else:
    st.info("Nenhum voto registrado ainda. Comecem os trabalhos!")