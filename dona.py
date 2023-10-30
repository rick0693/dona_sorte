import streamlit as st
import requests

def obter_dados_da_api():
    # URL da API
    url_api = "https://blaze-4.com/api/roulette_games/recent/"
    
    # Fazendo uma requisição GET para a API
    response = requests.get(url_api)
    
    # Verificando se a requisição foi bem-sucedida (código 200)
    if response.status_code == 200:
        # Convertendo a resposta para formato JSON
        dados = response.json()
        return dados
    else:
        # Exibindo mensagem de erro se a requisição falhar
        st.error(f"Falha ao obter dados da API. Código de status: {response.status_code}")
        return None

# Criando o aplicativo Streamlit
def main():
    # Título do aplicativo
    st.title("Exemplo de Consumo de API com Streamlit")
    
    # Obtendo dados da API
    dados_api = obter_dados_da_api()
    
    # Se os dados foram obtidos com sucesso
    if dados_api:
        # Exibindo os dados em uma tabela
        st.write("Dados da API:")
        st.json(dados_api)

# Executando o aplicativo
if __name__ == "__main__":
    main()
