def validar_qualidade_dados(df):
    """Aplica regras do Great Expectations no DataFrame de forma isolada."""
    import great_expectations as ge # O import pesado fica escondido aqui dentro!
    ge_df = ge.from_pandas(df)
    
    validacao_id = ge_df.expect_column_values_to_not_be_null("id_transacao")
    validacao_valores = ge_df.expect_column_values_to_not_be_null("valor_venda")
    
    return {
        "id_valido": validacao_id["success"],
        "valores_validos": validacao_valores["success"],
        "erros_valores_contagem": validacao_valores["result"].get("unexpected_count", 0)
    }

