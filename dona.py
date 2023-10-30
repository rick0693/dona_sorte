import requests
import pytz
from datetime import datetime
import time
import json
import sqlite3
import streamlit as st
import pygame   
from collections import Counter
import os

st.set_page_config(
    page_title="Dona sorte",
    page_icon=":robot_face:",
    layout="wide",
    initial_sidebar_state="expanded"
)
valor_tentativa = 0

saldo_inicial = 1000



config_carregadas = False  # Inicialmente, as configurações não estão carregadas


# Carregar o JSON com as configurações a partir do upload de arquivo
#uploaded_file = st.file_uploader("Carregar arquivo de configurações JSON", type="json")

#if uploaded_file is not None and not config_carregadas:
#    config_data = json.load(uploaded_file)
#    config_carregadas = False 
config_file_path = "configuracoes.json"  # Nome do arquivo de configurações

# Carregar configurações do arquivo, se existir
if os.path.exists(config_file_path):
    with open(config_file_path, "r") as json_file:
        config_data = json.load(json_file)
        config_carregadas = True
        st.toast('Configurações carregadas!', icon='🚀')
else:
    st.warning("Arquivo de configurações não encontrado. Certifique-se de que o arquivo 'configuracoes.json' está na mesma pasta.")
    st.stop()

# Usar os valores do JSON para preencher as configurações
with st.expander("Configurações de Login"):
    email = st.text_input("Digite o seu email:", value=config_data.get("email", ""))
    senha = st.text_input("Digite a sua senha:", type="password", value=config_data.get("senha", ""))

with st.expander("Configurações Gerais"):
    valor_inicial = st.number_input("Digite o valor inicial de aposta:", value=config_data.get("valor_inicial", 0.10))
    valor_meta = st.number_input("Determine o valor da sua meta:", value=config_data.get("valor_meta", 0.10))
    numero_vitorias_desejado = st.number_input("Digite o número de vitórias desejado para desligar:", min_value=0, step=1, value=config_data.get("numero_vitorias_desejado", 0))
    numero_alerta_derrotas = st.number_input("Número de derrotas consecutivas para ativar o alerta sonoro:", min_value=0, step=1, value=config_data.get("numero_alerta_derrotas", 0))            
    opcoes_alerta = ["Apenas Alertar", "Alertar e Desligar"]

    # Carregar os índices das opções de alerta do JSON
    opcao_alerta_derrota_index = config_data.get("opcao_alerta_derrota_index", 1)
    opcao_alerta_vitoria_index = config_data.get("opcao_alerta_vitoria_index", 1)

    # Usar os índices para selecionar as opções de alerta
    opcao_alerta_derrota = st.selectbox("Escolha a opção de alerta para derrotas:", opcoes_alerta, index=opcao_alerta_derrota_index)
    opcao_alerta_vitoria = st.selectbox("Escolha a opção de alerta para vitórias:", opcoes_alerta, index=opcao_alerta_vitoria_index)

desligar = False

import requests
import time
import streamlit as st
import requests
import time




def verificar_condicao(api_url):
    cor1, cor2, cor3, cor4 = None, None, None, None
    
    while True:
        # Fazer uma requisição GET para a API
        response = requests.get(api_url)

        # Verificar se a requisição foi bem-sucedida (código de status 200)
        if response.status_code == 200:
            # Analisar os dados JSON da resposta
            dados_api = response.json()

            # Pegar os últimos 4 valores da coluna "color"
            cores = [item["color"] for item in dados_api[:4]]

            # Atribuir os valores a variáveis separadas
            cor1, cor2, cor3, cor4 = cores

            print(f"Últimos valores da coluna 'color': {cores}")

            # Verificar a condição
            if cor1 == 1 and cor2 == 1 and cor3 == 1 and cor4 == 1:
                return True  # Condição atendida
            elif cor1 == 2 and cor2 == 2 and cor3 == 2 and cor4 == 2:
                return True  # Condição atendida       

            else:
                print("Aguardando condição. Verifique se a condição foi atendida.")

        else:
            # Imprimir uma mensagem de erro se a requisição não foi bem-sucedida
            print("Error:", response.status_code)

        # Aguardar 30 segundos antes da próxima requisição
        time.sleep(30)


# URL da API para obter os dados do jogo mais recente
api_url = "https://blaze-4.com/api/roulette_games/recent/"

# Chamar a função e imprimir o resultado
condicao_atendida = verificar_condicao(api_url)


while not desligar:
    if condicao_atendida:
    
        st.write("Condição atendida. Iniciando o código...")

        col1, col2, col3, col4 = st.columns(4)
        dica1 = col1.empty() # Indicação
        contagem_derrotas = col2.empty() # Derrotas
        contagem_vitorias = col3.empty() # Vitórias
        contagem_rodadas = col4.empty() # Resultado da aposta anterior

        # Restante do seu código aqui



        col5, col6, col7,col8= st.columns(4)
        Resultado = col5.empty() # Banca atual
        valor_ganho = col6.empty()  # Ganho real
        entrada = col7.empty()     # Entrada
        Valor_perdido = col8.empty()   # Valor_perdido


        col9, col10, col11, col12 = st.columns(4)
        dado9 = col9.empty()# Tabela de dados
        dado10 = col10.empty() # Tabela de dados
        dado11 = col11.empty() # Tabela de dados
        dado12 = col12.empty() # Tabela de dados




        url = 'https://blaze-4.com/api/roulette_bets'

        headers = {
            'authority': 'blaze-4.com',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
            'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjQ3NDg3OCwiYmxvY2tzIjpbXSwiaWF0IjoxNjk3OTIzNzc1LCJleHAiOjE3MDMxMDc3NzV9.cssBE0e2UccZvo9dD6wSIvvJeY3ER6v5h6QLwBXdteo',
            'content-type': 'application/json;charset=UTF-8',
            'cookie': '_ga=GA1.2.290723358.1697917314; _gid=GA1.2.1102140021.1697917314; nvg89115=13831afe7cec8caa608201771610|0_295; __zlcmid=1IRmDHJUXFggeTJ; _gat=1; _did=web_1759238278A1D0D; mp_u=1362603591.4034950832.1697917315.1697917315.1697917315.1697925265.1; AMP_c9c53a1635=JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjJjOTQ1YjA1ZS05YmY4LTRiZGMtOTI5Ni1jZDEwMzRkM2Y3ZmElMjIlMkMlMjJ1c2VySWQlMjIlM0EyNDc0ODc4JTJDJTIyc2Vzc2lvbklkJTIyJTNBMTY5NzkyMzA0MDA1MiUyQyUyMm9wdE91dCUyMiUzQWZhbHNlJTJDJTIybGFzdEV2ZW50VGltZSUyMiUzQTE2OTc5MjUyNzYyNjklMkMlMjJsYXN0RXZlbnRJZCUyMiUzQTI3JTdE',
            'device_id': 'c945b05e-9bf8-4bdc-9296-cd1034d3f7fa',
            'origin': 'https://blaze-4.com',
            'referer': 'https://blaze-4.com/pt/games/double',
            'sec-ch-ua': '"Chromium";v="118", "Brave";v="118", "Not=A?Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'sec-gpc': '1',
            'session_id': '1697923040052',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
            'x-client-language': 'pt',
            'x-client-version': 'v2.1235.0',
        }

        # Função para converter horário para o fuso horário de Brasília
        def converter_para_horario_brasilia(created_at):
            fuso_horario_utc = pytz.timezone('UTC')
            fuso_horario_brasilia = pytz.timezone('America/Sao_Paulo')
            horario_utc = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%S.%fZ")
            horario_utc = horario_utc.replace(tzinfo=fuso_horario_utc)
            horario_brasilia = horario_utc.astimezone(fuso_horario_brasilia)
            return horario_brasilia.strftime("%Y-%m-%d %H:%M:%S")



        # Inicializar contadores
        def calcular_dica_versao_1(color0, color1, color2, color3):

            #D(P)VVVP
            if color0 == 1 and color1 == 1 and color2 == 1 and color3 == 2:
                return 2
            #D(V)PPPV
            elif color0 == 2 and color1 == 2 and color2 == 2 and color3 == 1:
                return 1

            
            #D(P)BPPP
            elif color0 == 0 and color1 == 2 and color2 == 2 and color3 == 2:
                return 2
            #D(V)BVVV
            elif color0 == 0 and color1 == 1 and color2 == 1 and color3 == 1:
                return 1
            #D(P)BPBP
            elif color0 == 0 and color1 == 2 and color2 == 0 and color3 == 2:
                return 2
            #D(V)BVPV   
            elif color0 == 0 and color1 == 1 and color2 == 2 and color3 == 1:
                return 1
            #D(V)BVBV 
            elif color0 == 0 and color1 == 1 and color2 == 0 and color3 == 1:
                return 1
            #D(V)BVPB     
            elif color0 == 0 and color1 == 1 and color2 == 2 and color3 == 0:
                return 1

            else:
                
                #D(V)VVV     
                if color0 == 1 and color1 == 1 and color2 == 1:
                    return 1
                #D(P)PPP             
                elif color0 == 2 and color1 == 2 and color2 == 2:
                    return 2
                
                #D(P)VVP                     
                elif color0 == 1 and color1 == 1 and color2 == 2:
                    return 2
                #D(V)PPV                             
                elif color0 == 2 and color1 == 2 and color2 == 1:
                    return 1
                            
                #D(V)VPP                                     
                elif color0 == 1 and color1 == 2 and color2 == 2:
                    return 1
                #D(P)PVV                                           
                elif color0 == 2 and color1 == 1 and color2 == 1:
                    return 2
                
                
                #D(P)VPV                                               
                elif color0 == 1 and color1 == 2 and color2 == 1:
                    return 2
                #D(V)PVP                                                             
                elif color0 == 2 and color1 == 1 and color2 == 2:
                    return 1
        
        
                elif color0 ==0:
                    return 1
                elif color1 ==0:
                    return 2    
                elif color2 ==0:
                    return 1 
                else:
                    return None


        def obter_ultimos_resultados(api_url, quantidade=20):
            # Fazer uma requisição GET para a API
            response = requests.get(api_url)

            # Verificar se a requisição foi bem-sucedida (código de status 200)
            if response.status_code == 200:
                # Analisar os dados JSON da resposta
                dados_api = json.loads(response.text)

                # Pegar as últimas 'quantidade' cores
                ultimos_resultados = [item["color"] for item in dados_api[:quantidade]]

                # Imprimir os resultados
                print(f"Últimos {quantidade} resultados da coluna 'color': {ultimos_resultados}")

                # Contar as ocorrências de cada valor na lista
                contagem_ocorrencias = Counter(ultimos_resultados)

                # Armazenar o número de ocorrências em variáveis diferentes
                numero0_ocorrencias = contagem_ocorrencias[0]
                numero1_ocorrencias = contagem_ocorrencias[1]
                numero2_ocorrencias = contagem_ocorrencias[2]

                # Imprimir as contagens
                print(f'Número0 = {numero0_ocorrencias}')
                print(f'Número1 = {numero1_ocorrencias}')
                print(f'Número2 = {numero2_ocorrencias}')

                return ultimos_resultados, numero0_ocorrencias, numero1_ocorrencias, numero2_ocorrencias
            else:
                # Imprimir uma mensagem de erro se a requisição não foi bem-sucedida
                print("Error:", response.status_code)
                return None




        # URL da API para obter os dados do jogo mais recente
        api_url = "https://blaze-4.com/api/roulette_games/recent/"

        # Lista para armazenar sementes de servidor únicas
        server_seeds = []

        # Lista para armazenar as duas últimas dicas
        ultimas_dicas = []

        # Contador para o número de requisições
        contador = 0


        # Número de perdas consecutivas
        perdeu_consecutivas_global = 0

        # Contadores de vitórias e derrotas consecutivas
        ganhou_consecutivas = 0
        perdeu_consecutivas_local = 0  # Renomeada para evitar conflitos



        # Máximas vitórias e derrotas consecutivas
        max_ganhou_consecutivas = 0
        max_perdeu_consecutivas = 0

        # Conectar ao banco de dados SQLite (será criado se não existir)
        conn = sqlite3.connect('blaze_data.db')
        cursor = conn.cursor()

        # Criar a tabela se não existir
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS apostas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                color INTEGER,
                server_seed TEXT,
                horario TEXT,
                numero INTEGER,
                tip INTEGER,
                resultado TEXT,
                valor_aposta REAL,
                coluna1 INTEGER,
                coluna2 TEXT,
                coluna3 REAL,
                coluna4 TEXT
            )
        ''')
        conn.commit()


        result_df_placeholder = st.empty()  # Este é o espaço reservado para o DataFrame

        query_ultima_entrada = "SELECT * FROM apostas WHERE resultado = 'Estamos a um passo de começar.' ORDER BY id DESC LIMIT 1"

        while not desligar:
            # Fazer uma requisição GET para a API
            response = requests.get(api_url)

            # Verificar se a requisição foi bem-sucedida (código de status 200)
            if response.status_code == 200:
                # Analisar os dados JSON da resposta
                dados_api = json.loads(response.text)
                
                server_seed = dados_api[0]["server_seed"]
                if "valor_inicial" in config_data:
                    valor_inicial = config_data["valor_inicial"]            
                    
                contador += 1
                print(f"Requisição número: {contador}")
                
                if len(server_seeds) == 0:
                    server_seeds.append(server_seed)
                    print(f"Primeiro dado obtido: {server_seed}")
                    st.toast('Primeiro dado obtido', icon='🚀')

                elif len(server_seeds) == 1:
                    if server_seed != server_seeds[0]:
                        server_seeds.append(server_seed)
                        print(f"Segundo dado obtido: {server_seed}")
                        st.toast('Segundo dado obtido', icon='🚀')

                        time.sleep(28)
                    else:
                        time.sleep(1)
                else:
                    if server_seed not in server_seeds:
                        server_seeds.pop(0)
                        server_seeds.append(server_seed)

                        # Extrair outras informações
                        color0 = dados_api[0]["color"]
                        color1 = dados_api[1]["color"]
                        color2 = dados_api[2]["color"]
                        color3 = dados_api[3]["color"]
                        
                        horario = converter_para_horario_brasilia(dados_api[0]["created_at"])
                        horario1 = converter_para_horario_brasilia(dados_api[1]["created_at"])
                        
                        numero = dados_api[0]["roll"]
                        numero1 = dados_api[1]["roll"]

                        tip = calcular_dica_versao_1(color0, color1, color2, color3)
                        # Armazenar as duas últimas dicas
                        ultimas_dicas.append(tip)
                        if len(ultimas_dicas) > 2:
                            ultimas_dicas.pop(0)

                        # Imprimir as informações extraídas e a dica
                        print("Color:", color0)
                        print("Server Seed:", server_seed)
                        print("Horario:", horario)
                        print("Numero:", numero)
                        print("Dica:", tip)

                        # Verificar se a segunda dica-to-última coincide com color0
                        if len(ultimas_dicas) == 2:
                            penultimo_dica = ultimas_dicas[-2] if len(ultimas_dicas) >= 2 else None
                            ultimo_color1 = color0

                            if penultimo_dica == ultimo_color1:
                                resultado = "Ganhou"
                                st.toast('Ganhamos', icon='🚀')

                                perdeu_consecutivas_local = 0  # Reiniciar contagem de derrotas consecutivas
                                ganhou_consecutivas += 1  
                                # Incrementar sequência de vitórias consecutivas
                                if ganhou_consecutivas > max_ganhou_consecutivas:
                                    max_ganhou_consecutivas = ganhou_consecutivas
                            elif penultimo_dica is None:
                                resultado = None  # Resultado indefinido na primeira vez
                                perdeu_consecutivas_local = 0 
                                ganhou_consecutivas = 0
                            else:
                                resultado = "Perdeu"
                                perdeu_consecutivas_local += 1
                                ganhou_consecutivas = 0
                                if perdeu_consecutivas_local > max_perdeu_consecutivas:
                                    max_perdeu_consecutivas = perdeu_consecutivas_local

                        else:
                            resultado = "Iniciando"
                            perdeu_consecutivas_local = 0 
                            ganhou_consecutivas = 0



                        # Calcular o valor da aposta
                        valor_aposta = valor_meta if resultado == "Ganhou" else valor_inicial * (2 ** perdeu_consecutivas_local)

                        print(f"Resultado: {resultado}")
                        print(f"Valor da aposta: {valor_aposta}")
                        print(f"perdeu_consecutivas_global: {perdeu_consecutivas_local}")

                        valor_entrada = config_data.get("valor_inicial")

                        # Preparar os dados para a aposta
                        json_data = {
                            'amount': valor_entrada,
                            'currency_type': 'BRL',
                            'color': tip,
                            'free_bet': False,
                            'wallet_id': 6261990,
                        }

                        # Tentar fazer a aposta, e se ocorrer o erro, tentar novamente
                        while True:
                            response = requests.post(url, headers=headers, json=json_data)
                            response_data = response.json()
                            if "error" in response_data and response_data["error"]["code"] == 1040:
                                print("Erro: This round has already started. Tentando novamente...")
                                time.sleep(1)
                            else:
                                break

                        print(response.text)

                    # Armazenar os dados no banco de dados
                        cursor.execute('''
                            INSERT INTO apostas (color, server_seed, horario, numero, tip, resultado, valor_aposta, coluna1, coluna2, coluna3, coluna4)
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                        ''', (color0, server_seed, horario, numero, tip, resultado, valor_aposta, None, None, None, None))

                        conn.commit()


                        # Consulta SQL para contar as ocorrências de "Ganhou"
                        query_ganhou = "SELECT COUNT(*) FROM apostas WHERE resultado = 'Ganhou'"

                        # Consulta SQL para contar as ocorrências de "Perdeu"
                        query_perdeu = "SELECT COUNT(*) FROM apostas WHERE resultado = 'Perdeu'"

                        # Consulta SQL para contar as ocorrências de "Perdeu"
                        query_iniciando = "SELECT COUNT(*) FROM apostas WHERE resultado = 'Iniciando'"


                        # Executar as consultas
                        cursor.execute(query_ganhou)
                        ganhou_count = cursor.fetchone()[0]

                        cursor.execute(query_perdeu)
                        perdeu_count = cursor.fetchone()[0]

                        total_rodadas = ganhou_count + perdeu_count

                        # Imprimir os resultados
                        print(f"Total de 'Ganhou': {ganhou_count}")
                        print(f"Total de 'Perdeu': {perdeu_count}")
                        print(f"Total de rodadas: {total_rodadas}")

                        ultimos_resultados = obter_ultimos_resultados(api_url, quantidade=20)


                        def contar_apos_iniciando(resultado):
                            # Consulta SQL para contar as ocorrências de "Ganhou" ou "Perdeu" após "Iniciando"
                            query_apos_iniciando = f"""
                                SELECT COUNT(*) 
                                FROM apostas 
                                WHERE resultado = '{resultado}' 
                                AND id > (SELECT MAX(id) FROM apostas WHERE resultado = 'Iniciando')
                            """

                            # Executar a consulta
                            cursor.execute(query_apos_iniciando)
                            count_apos_iniciando = cursor.fetchone()[0]

                            # Imprimir o resultado
                            print(f"Total de '{resultado}' após 'Iniciando': {count_apos_iniciando}")

                            return count_apos_iniciando

                        # Exemplo de uso para "Ganhou"
                        ganhou_apos_iniciando_count = contar_apos_iniciando('Ganhou')

                        # Exemplo de uso para "Perdeu"
                        perdeu_apos_iniciando_count = contar_apos_iniciando('Perdeu')

                        ganho_total= ganhou_count*valor_inicial
                        saldo_atual = ganho_total+saldo_inicial

                        tempo_real = saldo_atual- valor_aposta
                        
                        #valor_json = valor_aposta + valor_inicial if valor_aposta > 0.11 else valor_inicial

                        #colunas col1, col2, col3, col4 = st.columns(4)
                        dica1.metric("Dica", tip)
                        contagem_derrotas.metric("Derrotas", perdeu_count )
                        contagem_vitorias.metric("Vitorias",ganhou_count )
                        contagem_rodadas.metric(f"Rodadas",total_rodadas )
                        Resultado.metric(f"Ultimo resultado ",resultado )
                        entrada.metric("Entrada", valor_aposta)
                        valor_ganho.metric("Ganhou após Iniciando", ganhou_apos_iniciando_count)    
                        Valor_perdido.metric("Perdeu após Iniciando", perdeu_apos_iniciando_count)
                        dado9.metric("Saldo atual", saldo_atual)
                        dado10.metric("Lucro", ganho_total)
                        dado11.metric("Saldo em tempo real", tempo_real)
                        dado12.metric("Perdeu após Iniciando", perdeu_apos_iniciando_count)

                        # Aumentar o valor_tentativa apenas quando desligar e valor_aposta > valor_meta
                        if perdeu_consecutivas_local >= numero_alerta_derrotas:
                            valor_tentativa += 1

                        recuperacao= valor_tentativa *valor_inicial
                        
                        configuracoes_json = {
                            "email": "rick0693@gmail.com",
                            "senha": 'Ric@rdo06@Sara',
                            "valor_inicial": valor_aposta+recuperacao,
                            "valor meta": valor_meta,
                            "escolha_estrategia": 1,  # Atualisze com o valor desejado
                            "numero_vitorias_desejado": numero_vitorias_desejado,  # Substitua com o valor desejado
                            "Numero de tentativa": valor_tentativa,  # 
                            "numero_alerta_derrotas": numero_alerta_derrotas,
                            "opcao_alerta_derrota_index": 1,  # Atualize com o valor desejado
                            "opcao_alerta_vitoria_index": 1  # Atualize com o valor desejado

                        }

                        # Salvar o JSON em um arquivo
                        with open("configuracoes.json", "w") as json_file:
                            json.dump(configuracoes_json, json_file)


                        # Adicione a chamada à função em seu código onde você deseja obter os últimos resultados

                        if ganhou_apos_iniciando_count >= numero_vitorias_desejado:
                            if opcao_alerta_vitoria == "Alertar e Desligar":
                                st.toast('Ganhamos', icon='🚀')
                                st.warning(f"Alerta sonoro ativado! Número desejado de vitórias alcançado. Desligando o código.", icon='🚀')
                                pygame.mixer.init()
                                pygame.mixer.music.load("fim.mp3")  # Substitua pelo caminho do seu arquivo de som
                                pygame.mixer.music.play()
                                desligar = True
                                st.rerun()

                        if perdeu_consecutivas_local >= numero_alerta_derrotas:
                            pygame.mixer.init()
                            pygame.mixer.music.load("alerta.mp3")  # Substitua pelo caminho do seu arquivo de som
                            pygame.mixer.music.play()
                            st.rerun()
                            if opcao_alerta_derrota == "Alertar e Desligar":
                                st.warning(f"Alerta sonoro ativado! Número desejado de derrotas consecutivas alcançado. Desligando o código.")
                                desligar = True

                        time.sleep(28)

                        # Resetar o contador de requisições
                        contador = 0
                    else:
                        time.sleep(1)
            else:
                # Imprimir uma mensagem de erro se a requisição não foi bem-sucedida
                print("Error:", response.status_code)
