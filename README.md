# 🚀 CloudMetrics: Plataforma de Migração, FinOps & IA Generativa

![Python](https://shields.io)
![Streamlit](https://shields.io)
![AWS](https://shields.io)
![Great Expectations](https://shields.io)
![LangChain](https://shields.io)

Este projeto simula uma plataforma executiva de controle para a empresa fictícia *CloudMetrics Analytics, demonstrando a modernização e migração de um ambiente de Data Warehouse legado local para uma arquitetura moderna e serverless na nuvem da **AWS*. 

A aplicação foi desenvolvida seguindo rigorosamente as práticas de *Código Limpo (Clean Code)* e *Arquitetura Modular*, separando a camada visual (Front-end no Streamlit) das regras de negócio e motores analíticos (Back-end em módulos isolados).

---

## 📈 Impacto Financeiro e Métricas de Negócio (FinOps & ROI)

A implementação desta arquitetura e o monitoramento contínuo geram retornos diretos na eficiência da infraestrutura e na governança corporativa:

### 💰 1. Otimização de Custos em Nuvem (FinOps)
* *Redução de 60% no Custo Mensal de Infraestrutura:* A migração do ambiente analítico local tradicional para soluções sob demanda da AWS (como AWS S3, Athena e Glue) reduziu o custo operacional de *R\$ 15.000* para *R\$ 6.000* por mês.
* *Economia Anual de R\$ 108.000:* Através de recomendações automatizadas de FinOps — como o particionamento inteligente de dados e o desligamento programado de ambientes de homologação (Staging) nos fins de semana — garante-se o controle total sobre o orçamento de nuvem.

### 🛡️ 2. Data Governance & Observabilidade de Dados
* *Garantia de Qualidade de Dados (Data Quality):* Utilização do framework *Great Expectations* integrado ao pipeline de ingestão de dados. O sistema monitora anomalias em tempo real e barra registros nulos ou inválidos na origem, disparando alertas automatizados diretamente para o canal de comunicação do time de engenharia (Slack/Teams).

### 🧪 3. Validação Científica de Negócio (Teste A/B)
* *Tomada de Decisão Orientada a Dados:* Módulo estatístico integrado que realiza o cálculo automático do *Teste t de Student (P-Valor)* para validar experimentos de negócios (Teste A/B de novos layouts do sistema), garantindo com 95% de confiança matemática se uma alteração trouxe aumento real de receita ou se foi fruto do acaso.

---

## 🏗️ Arquitetura de Software & Metodologia Ágil

Para garantir a manutenibilidade do ecossistema, o projeto adota os seguintes frameworks:
* *Gestão Ágil:* Organização de entregas através de frameworks equivalentes ao *Scrum/Kanban*, mapeando dependências, impedimentos e o andamento do Sprint Backlog diretamente na interface administrativa.
* *Práticas de CI/CD:* Automação de pipelines simulada com validações de qualidade e deploy de microserviços em nuvem via AWS CodePipeline / GitHub Actions.
* *IA Generativa & RAG (Retrieval-Augmented Generation):* Mecanismo de assistente inteligente desenvolvido com *LangChain* para engenharia de prompt. O modelo simula a busca semântica em logs de FinOps e responde perguntas complexas de gestores de forma instantânea.

---

## 📂 Estrutura do Projeto (Clean Code)

text
├── .streamlit/
│   └── config.toml      # Configurações de identidade visual e cores corporativas
├── data/
│   └── logo.svg         # Logotipo institucional da CloudMetrics
├── modules/             # Camada de Inteligência e Regras de Negócio (Back-end)
│   ├── __init__.py      # Inicializador do pacote de módulos
│   ├── ai_engine.py     # Lógica e simulação de IA Generativa / RAG
│   ├── finops.py        # Métricas de custos AWS e logs de CI/CD
│   ├── quality.py       # Validações automatizadas com Great Expectations
│   └── statistics.py    # Cálculos matemáticos do Teste A/B estatístico
├── app_hub.py           # Interface Web e renderização do painel (Front-end)
└── requirements.txt     # Dependências de software do projeto


---

## 🚀 Como Executar a Aplicação Localmente

### 1. Clonar o Repositório
bash
git clone https://github.com
cd seu-repositorio


### 2. Configurar o Ambiente e Instalar as Dependências
bash
python -m venv venv
# No Windows:
.\venv\Scripts\activate
# No Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt


### 3. Iniciar a Plataforma Web Interativa
bash
python -m streamlit run app_hub.py

A aplicação abrirá automaticamente no seu navegador padrão de internet de forma instantânea e totalmente otimizada.

---

## 🛠️ Tecnologias e Frameworks Dominados
* *Linguagem:* Python 3.10+
* *Framework Web:* Streamlit (UI/UX Customizada)
* *Engenharia de Dados:* Pandas, Numpy e Grandes Volumes de Ingestão
* *Qualidade e Validação:* Great Expectations & Engenharia de Observabilidade
* *Estatística Avançada:* Scipy Stats (Inferência Estatística / Teste A/B)
* *Inteligência Artificial:* LangChain (Prompt Engineering / RAG)