# SpeedPage: Analisador de Desempenho de Páginas Web
O SpeedPage é uma ferramenta simples para analisar o desempenho de páginas da web. Ele fornece várias métricas importantes, como velocidade de carregamento, tempo até o primeiro byte (TTFB), número de solicitações HTTP, tamanho total da página e otimização de imagens.

Funcionalidades
O SpeedPage atualmente oferece as seguintes funcionalidades:

Calcular Velocidade de Carregamento: Mede a velocidade de carregamento de uma página da web em termos de KB/s.

Calcular TTFB e Avaliar: Calcula o tempo até o primeiro byte (TTFB) de uma página da web e avalia se é bom ou ruim.

Calcular Page Load Time e Avaliar: Calcula o tempo total de carregamento de uma página da web e avalia se é bom ou ruim.

Calcular Número de Solicitações HTTP: Conta o número de solicitações HTTP necessárias para carregar uma página da web.

Calcular Tamanho Total da Página: Calcula o tamanho total da página da web em bytes, KB ou MB.

Verificar Otimização de Imagens: Verifica se as imagens em uma página da web estão otimizadas em termos de tamanho de arquivo.

Como Usar
Instalação das Dependências: Antes de usar o SpeedPage, certifique-se de instalar todas as dependências listadas no arquivo requirements.txt. Você pode fazer isso executando o comando pip install -r requirements.txt.

Execução do Aplicativo: Para executar o aplicativo, você pode chamar os métodos fornecidos no script index.py com os parâmetros apropriados ou integrar esses métodos em seu próprio script.

Integração com o Streamlit: Se você deseja integrar o SpeedPage em um aplicativo Streamlit, você pode importar os métodos relevantes do script index.py e usá-los conforme necessário.

Nota sobre o Streamlit Share
Por favor, note que o SpeedPage depende do Selenium para algumas funcionalidades, como a medição do tempo de carregamento da página e a verificação da otimização de imagens. O Streamlit Share atualmente não suporta a execução de aplicativos que dependem do Selenium, pois não inclui um navegador para executar tarefas de automação. Portanto, se você pretende hospedar o SpeedPage no Streamlit Share, pode ser necessário adaptar o código para remover a dependência do Selenium ou considerar outras opções de hospedagem.
