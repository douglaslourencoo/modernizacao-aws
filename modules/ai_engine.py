def responder_pergunta(pergunta: str):
    """Busca a resposta conceitual de forma instantânea (Simulação RAG Otimizada)."""
    
    documentos_conhecimento = [
        "O custo atual da AWS é de R$ 6.000 por mês.",
        "Economizamos R$ 108.000 por ano após a migração do Data Warehouse antigo.",
        "O bloqueio de segurança impede que o público acesse dados sem passar pelo pipeline de Data Quality."
    ]
    
    pergunta_lower = pergunta.lower()
    if "economiz" in pergunta_lower or "ano" in pergunta_lower:
        return documentos_conhecimento
    elif "custo" in pergunta_lower or "mensal" in pergunta_lower or "aws" in pergunta_lower:
        return documentos_conhecimento
    elif "segurança" in pergunta_lower or "quality" in pergunta_lower:
        return documentos_conhecimento
        
    return "Desculpe, não encontrei essa informação específica nos logs de nuvem do FinOps."

