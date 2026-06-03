def calcular_teste_ab(df):
    """Separa os grupos do layout A e B e realiza o teste t de Student."""
    import scipy.stats as stats # O import pesado fica escondido aqui dentro!
    df_limpo = df.dropna()
    grupo_a = df_limpo[df_limpo['versao_layout'] == 'A']['valor_venda']
    grupo_b = df_limpo[df_limpo['versao_layout'] == 'B']['valor_venda']
    
    media_a = grupo_a.mean()
    media_b = grupo_b.mean()
    
    _, p_valor = stats.ttest_ind(grupo_a, grupo_b)
    return media_a, media_b, p_valor

