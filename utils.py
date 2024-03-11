import requests
from bs4 import BeautifulSoup
import time

def calcular_velocidade_carregamento(url):
    try:
        start_time = time.time()
        response = requests.get(url)
        end_time = time.time()

        if response.status_code == 200:
            elapsed_time = end_time - start_time
            velocidade_carregamento = len(response.content) / (1024 * elapsed_time)  # Velocidade em KB/s
            return velocidade_carregamento

    except Exception as e:
        print(f"Erro ao calcular a velocidade: {e}")

    return None

def calcular_ttfb_e_avaliar(url, limite_bom=100):
    try:
        # Faz uma solicitação GET ao url
        resposta = requests.get(url)
        
        # Calcula o tempo decorrido até a recepção do primeiro byte
        ttfb = resposta.elapsed.total_seconds() * 1000  # em milissegundos
        
        # Avalia se o TTFB é bom ou ruim
        if ttfb <= limite_bom:
            return f'O TTFB de {url} é bom ({ttfb:.2f} ms).'
        else:
            return f'O TTFB de {url} é ruim ({ttfb:.2f} ms).'
    except requests.exceptions.RequestException as e:
        return f'Erro ao acessar {url}: {str(e)}'

def calcular_numero_solicitacoes_http(url):
    try:
        # Faz uma solicitação GET ao site
        resposta = requests.get(url)
        if resposta.status_code != 200:
            return f'Erro ao acessar {url}: Código de status {resposta.status_code}'

        # Analisa o HTML da página usando BeautifulSoup
        soup = BeautifulSoup(resposta.content, 'lxml')

        # Encontra todos os elementos que fazem solicitações HTTP
        recursos = soup.find_all(['img', 'script', 'link', 'iframe', 'css', 'video', 'audio', 'source', 'embed', 'object'])

        # Calcula o número de solicitações HTTP
        numero_solicitacoes = len(recursos)

        return f'O número de solicitações HTTP para carregar {url} é {numero_solicitacoes}.'
    except Exception as e:
        return f'Erro ao acessar {url}: {str(e)}'

def calcular_tamanho_total_pagina(url):
    try:
        # Faz uma solicitação GET à página
        response = requests.get(url)
        if response.status_code != 200:
            return f'Erro ao acessar {url}: Código de status {response.status_code}'

        # Calcula o tamanho total da página em bytes
        tamanho_total_bytes = len(response.content)

        # Converte o tamanho para KB ou MB para facilitar a leitura
        if tamanho_total_bytes < 1024:
            tamanho_total = f'{tamanho_total_bytes} bytes'
        elif tamanho_total_bytes < 1024 * 1024:
            tamanho_total = f'{tamanho_total_bytes / 1024:.2f} KB'
        else:
            tamanho_total = f'{tamanho_total_bytes / (1024 * 1024):.2f} MB'

        return f'O tamanho total da página {url} é de aproximadamente {tamanho_total}.'
    except Exception as e:
        return f'Erro ao acessar {url}: {str(e)}'

def verificar_otimizacao_de_imagens(url, limite_tamanho_bytes=100000):
    try:
        # Faz uma solicitação GET à página
        response = requests.get(url)
        if response.status_code != 200:
            return f'Erro ao acessar {url}: Código de status {response.status_code}'

        # Analisa o conteúdo HTML da página usando BeautifulSoup
        soup = BeautifulSoup(response.content, 'lxml')

        # Encontra todas as tags de imagem <img>
        imagens = soup.find_all('img')

        resultados = []
        for img in imagens:
            src = img.get('src')
            if src:
                # Faz uma solicitação HEAD para obter informações sobre a imagem
                img_response = requests.head(src)
                tamanho_bytes = int(img_response.headers.get('Content-Length', 0))

                if tamanho_bytes > limite_tamanho_bytes:
                    resultados.append(f'A imagem {src} não está otimizada. Tamanho: {tamanho_bytes} bytes.')

        if resultados:
            return resultados
        else:
            return 'Todas as imagens estão otimizadas.'
    except Exception as e:
        return f'Erro ao acessar {url}: {str(e)}'
