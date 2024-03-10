import streamlit as st
from utils import (calcular_velocidade_carregamento, calcular_ttfb_e_avaliar,
                   calcular_page_load_time_e_avaliar, calcular_numero_solicitacoes_http,
                   calcular_tamanho_total_pagina, verificar_otimizacao_de_imagens)

# Defina a interface Streamlit
st.title('Aplicativo de Monitoramento de Desempenho')

url = st.text_input('Insira a URL da página que deseja analisar:')
if st.button('Analisar'):
    if url:
        velocidade = calcular_velocidade_carregamento(url)
        ttfb = calcular_ttfb_e_avaliar(url)
        pageload = calcular_page_load_time_e_avaliar(url)
        num_solicitacoes_http = calcular_numero_solicitacoes_http(url)
        tamanho_total = calcular_tamanho_total_pagina(url)
        otimizacao = verificar_otimizacao_de_imagens(url)
        
        st.write(f'Velocidade de carregamento: {velocidade}')
        st.write(f'Tempo até o primeiro byte: {ttfb}')
        st.write(f'Tempo de carregamento da página: {pageload}')
        st.write(f'Número de solicitações HTTP: {num_solicitacoes_http}')
        st.write(f'Tamanho total da página: {tamanho_total}')
        if isinstance(otimizacao, list):
            for item in otimizacao:
                st.error(item)
        else:
            st.success(otimizacao)

