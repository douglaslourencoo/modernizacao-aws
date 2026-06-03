def obter_dados_finops():
    """Retorna os indicadores financeiros e custos da migração AWS."""
    return {
        "custo_antigo": 15000,
        "custo_atual": 6000,
        "economia_anual": 108000,
        "recomendacoes": [
            "✔️ AWS Athena/Glue: Particionamento de dados ativo. Redução de 40% no volume de dados escaneados por query.",
            "💡 Dica FinOps: Identificamos 3 ambientes de testes (Staging) ligados nos finais de semana. Desligar pode economizar mais US$ 400/mês."
        ]
    }

def obter_pipeline_cicd_log():
    """Retorna a string de configuração do pipeline de CI/CD."""
    return """
stage('Testes Automatizados') {
    steps {
        sh 'pytest tests/'
        sh 'great_expectations checkpoint run'
    }
}
stage('Deploy Microserviços AWS') {
    steps {
        sh 'sam deploy --template-file template.yaml'
    }
}
    """.strip()
