def validar_qualidade_dados(df):
    """Aplica regras de qualidade nos dados de forma compatível com a nuvem."""
    import great_expectations as ge
    
    # Formato universal e seguro para ler o DataFrame na nuvem
    context = ge.get_context()
    datasource = context.sources.add_pandas(name="my_pandas_datasource")
    data_asset = datasource.add_dataframe_asset(name="my_df_asset")
    batch_request = data_asset.build_batch_request(dataframe=df)
    validator = context.get_validator(batch_request=batch_request)
    
    # Aplica as expectativas usando o validador moderno
    validacao_id = validator.expect_column_values_to_not_be_null("id_transacao")
    validacao_valores = validator.expect_column_values_to_not_be_null("valor_venda")
    
    return {
        "id_valido": validacao_id["success"],
        "valores_validos": validacao_valores["success"],
        "erros_valores_contagem": validacao_valores["result"].get("unexpected_count", 0)
    }

