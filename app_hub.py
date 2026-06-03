import streamlit as st

# 🚀 COMANDO MÁGICO: DEIXA O SITE LARGO DE PONTA A PONTA
st.set_page_config(layout="wide")

import pandas as pd
import numpy as np

# IMPORTANDO NOSSOS MÓDULOS LIMPOS (Back-end)
import modules.finops as finops_mod
import modules.quality as quality_mod
import modules.statistics as stats_mod

# ==========================================
# 🔍 AJUSTE DE ACESSIBILIDADE: FONTES MAIORES
# ==========================================
st.markdown("""
<style>
    /* Aumenta o tamanho de todos os textos comuns da página */
    html, body, [data-testid="stMarkdownContainer"], p, li {
        font-size: 20px !important;
        line-height: 1.6 !important;
    }
    /* Aumenta o tamanho dos títulos das abas */
    button[data-baseweb="tab"] p {
        font-size: 18px !important;
        font-weight: 600 !important;
    }
    /* Aumenta as letras das caixas de digitação */
    input {
        font-size: 20px !important;
    }
    /* Aumenta o tamanho dos subtítulos (h2 e h3) */
    h2 {
        font-size: 32px !important;
    }
    h3 {
        font-size: 26px !important;
    }
</style>
""", unsafe_allow_html=True)

# Configuração Visual do Site
# ==========================================
# 🎨 TOPO CORPORATIVO COM LOGO BLINDADO
# ==========================================
# Cria o desenho do logotipo usando HTML direto no navegador
logo_svg_code = """
<div style="display: flex; align-items: center; gap: 20px; margin-bottom: 20px;">
    <svg xmlns="http://w3.org" viewBox="0 0 500 120" width="280px">
      <g transform="translate(10, 10)">
        <path d="M40,75 C25,75 15,65 15,50 C15,36 26,26 40,25 C45,12 58,5 72,5 C88,5 101,16 104,30 C115,30 125,40 125,52 C125,65 115,75 100,75 Z" fill="#2563EB" opacity="0.85"/>
        <path d="M55,75 C43,75 35,67 35,55 C35,44 44,36 55,35 C59,25 70,19 81,19 C94,19 105,28 107,40 C116,40 124,48 124,58 C124,69 116,75 105,75 Z" fill="#10B981" opacity="0.75"/>
        <rect x="55" y="45" width="6" height="20" rx="2" fill="#FFFFFF"/>
        <rect x="67" y="35" width="6" height="30" rx="2" fill="#FFFFFF"/>
        <rect x="79" y="40" width="6" height="25" rx="2" fill="#FFFFFF"/>
      </g>
      <text x="150" y="60" font-family="Segoe UI, Arial, sans-serif" font-size="42" font-weight="800" fill="#1E293B">Cloud<tspan fill="#2563EB">Metrics</tspan></text>
      <text x="152" y="88" font-family="Segoe UI, Arial, sans-serif" font-size="16" font-weight="600" fill="#64748B" letter-spacing="4">ANALYTICS HUB</text>
    </svg>
    <div style="border-left: 2px solid #E2E8F0; padding-left: 20px;">
        <h2 style="margin: 0; color: #1E293B; font-family: Segoe UI, sans-serif; font-size: 24px;">Plataforma de Migração, FinOps & IA Generativa</h2>
        <span style="color: #64748B; font-family: Segoe UI, sans-serif; font-size: 14px;">⚙️ Ambiente Analítico AWS • DataOps & Compliance</span>
    </div>
</div>
"""
# Mostra o cabeçalho completo e estilizado na tela do site
st.markdown(logo_svg_code, unsafe_allow_html=True)
st.markdown("---")


# ==========================================
# 📊 GERENCIAMENTO DOS DADOS (Simulação)
# ==========================================
if 'df_vendas' not in st.session_state:
    np.random.seed(42)
    dados = {
        "id_transacao": [f"TRX_{i:04d}" for i in range(1, 101)],
        "valor_venda": np.random.normal(loc=150, scale=30, size=100).round(2).tolist(),
        "categoria": np.random.choice(["Eletrônicos", "Moda", "Home"], size=100).tolist(),
        "versao_layout": np.random.choice(["A", "B"], size=100).tolist()
    }
    dados["valor_venda"][15] = None # Introduz anomalia para teste de qualidade
    st.session_state['df_vendas'] = pd.DataFrame(dados)

df = st.session_state['df_vendas']



# ==========================================
# 🗂️ CRIAÇÃO DAS ABAS VISUAIS (Front-end)
# ==========================================
aba1, aba2, aba3, aba4, aba5 = st.tabs([
    "🏃 Agilidade & CI/CD", 
    "💰 AWS Migração & FinOps", 
    "🛡️ Data Quality & Observabilidade", 
    "🧪 Teste A/B Estatístico", 
    "🤖 Assistente IA Generativa (RAG)"
])

# ABA 1: METODOLOGIA ÁGIL
with aba1:
    st.header("📋 Gestão Ágil & Pipelines de Microserviços")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🗓️ Sprint Backlog (Scrum/Kanban)")
        st.info("🟢 *Concluído:* Migração do DW Legado para AWS S3/Athena.")
        st.info("🟢 *Concluído:* Implementação de Microserviços de ingestão via AWS Lambda.")
        st.warning("🟡 *Em Execução:* Validação automatizada de Data Quality no Pipeline.")
    with col2:
        st.subheader("🔄 Pipeline de CI/CD (GitHub Actions / AWS CodePipeline)")
        st.code(finops_mod.obter_pipeline_cicd_log(), language="groovy")

# ABA 2: FINOPS AWS
with aba2:
    st.header("☁️ Otimização de Custos em Nuvem (FinOps)")
    dados_financeiros = finops_mod.obter_dados_finops()
    
    c1, c2, c3 = st.columns(3)
    c1.metric("Custo Mensal Antigo", f"R$ {dados_financeiros['custo_antigo']:,}")
    c2.metric("Custo Mensal Atual", f"R$ {dados_financeiros['custo_atual']:,}", delta="-60% Redução")
    c3.metric("Economia Anual", f"R$ {dados_financeiros['economia_anual']:,}")
    
    st.subheader("💡 Recomendações de Otimização Automatizadas")
    for rec in dados_financeiros["recomendacoes"]:
        st.markdown(rec)

# ABA 3: DATA QUALITY
with aba3:
    st.header("🛡️ Governança de Dados com Great Expectations")
    res_validacao = quality_mod.validar_qualidade_dados(df)
    
    col_q1, col_q2 = st.columns(2)
    with col_q1:
        st.subheader("✅ Regra 1: IDs de Transação Nulos")
        if res_validacao["id_valido"]:
            st.success("PASSOU: Todos os IDs estão preenchidos.")
        else:
            st.error("FALHOU!")
            
    with col_q2:
        st.subheader("🚨 Regra 2: Valores de Venda Nulos (Observabilidade)")
        if not res_validacao["valores_validos"]:
            st.error(f"FALHOU: Encontrada {res_validacao['erros_valores_contagem']} anomalia. Alerta enviado ao Slack!")
        else:
            st.success("PASSOU!")
            
    st.dataframe(df.head(8))

# ABA 4: TESTE A/B
with aba4:
    st.header("🧪 Validação de Negócio via Teste A/B")
    media_a, media_b, p_valor = stats_mod.calcular_teste_ab(df)
    
    col_t1, col_t2 = st.columns(2)
    col_t1.metric("Média - Layout A (Antigo)", f"R$ {media_a:.2f}")
    col_t2.metric("Média - Layout B (Novo)", f"R$ {media_b:.2f}")
    
    st.subheader("📊 Resultado do Teste de Hipótese (P-Valor)")
    st.write(f"O P-Valor calculado foi de: *{p_valor:.4f}*")
    st.success("✨ *Resultado Significativo!") if p_valor < 0.05 else st.warning("😴 **Sem Diferença Estatística.*")

# ABA 5: IA GENERATIVA
with aba5:
    st.header("🤖 Inteligência Artificial Generativa & Engenharia de Prompt")
    pergunta = st.text_input("Faça uma pergunta sobre a nuvem:", "Quanto economizamos por ano com o projeto?")
    
    if st.button("Enviar Pergunta para a IA"):
        pergunta_lower = pergunta.lower()
        
        # Resposta direta e instantânea na memória
        if "economiz" in pergunta_lower or "ano" in pergunta_lower:
            resposta = [
                "O custo atual da AWS é de R$ 6.000 por mês.",
                "Economizamos R$ 108.000 por ano após a migração do Data Warehouse antigo.",
                "O bloqueio de segurança impede que o público acesse dados sem passar pelo pipeline de Data Quality."
            ]
        elif "custo" in pergunta_lower or "mensal" in pergunta_lower or "aws" in pergunta_lower:
            resposta = ["O custo atual da AWS é de R$ 6.000 por mês."]
        elif "segurança" in pergunta_lower or "quality" in pergunta_lower:
            resposta = ["O bloqueio de segurança impede que o público acesse dados sem passar pelo pipeline de Data Quality."]
        else:
            resposta = ["Desculpe, não encontrei essa informação específica nos logs de nuvem do FinOps."]
            
        # Limpa os colchetes e mostra cada resposta bonita em uma linha
        with st.chat_message("assistant"):
            st.write("*Resposta da IA (Logs do FinOps):*")
            for item in resposta:
                st.markdown(f"- {item}")

            

            

