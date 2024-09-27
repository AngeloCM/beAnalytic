import pandas as pd
import numpy as np

def gerar_dados() -> pd.DataFrame:
    np.random.seed(1)

    embalagens_data = pd.DataFrame({
        'ID do Produto': range(1, 101),
        'Altura(cm)': np.random.uniform(5, 50, 100),
        'Largura(cm)': np.random.uniform(5, 50, 100),
        'Profundidade(cm)': np.random.uniform(5, 50, 100),
        'Peso do Produto(kg)': np.random.uniform(0.5, 25, 100),
        'Material de Embalagem': np.random.choice(['Papelão', 'Plástico', 'Isopor'], 100),
        'Custo por Unidade de Material': np.random.uniform(0.1, 1.0, 100),
        'Volume de Vendas': np.random.randint(100, 1000, 100)
    })

    return embalagens_data

def calcular_volume_com_protecao(df, margin: float) -> pd.DataFrame:
    df['Volume_Produto_Ideal(cm3)'] = df['Altura(cm)'] * df['Largura(cm)'] * df['Profundidade(cm)'] * (1 + margin)

    return df

def calcular_peso_total(df, margin: float) -> pd.DataFrame:
    df['Peso_Total'] = df['Peso do Produto(kg)'] * (1 + margin)

    return df