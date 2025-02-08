from extraction.api_client import APIClient
import json


def extrair_emails():
    """Extrai todos os emails da API com paginação até o último registro."""
    api_client = APIClient()
    endpoint = "emails"  # Endpoint correto da API

    # Definindo a lógica de paginação
    page_size = 50  # Define 50 registros por página
    page = 1
    todos_os_emails = []

    while True:
        # Configura os parâmetros da requisição para paginação
        params = {
            'page_size': page_size,
            'page': page
        }

        # Faz a requisição à API
        response = api_client.get(endpoint, params=params)

        if response:  # Verifica se há resposta
            if 'items' in response:
                emails = response['items']
                if emails:
                    todos_os_emails.extend(emails)  # Adiciona os emails à lista
                    page += 1  # Avança para a próxima página
                else:
                    break  # Se não houver mais emails, interrompe o loop
            else:
                print("⚠ Resposta não contém 'items', verificando erro.")
                break  # Se não houver 'items', interrompe
        else:
            print("❌ Falha ao obter emails da API.")
            break  # Se houver falha na requisição, interrompe

    if todos_os_emails:
        print(f"✅ {len(todos_os_emails)} emails extraídos com sucesso!")
    else:
        print("⚠ Nenhum email encontrado.")

    return todos_os_emails


# Teste rápido:
if __name__ == "__main__":
    emails_extraidos = extrair_emails()
    print(json.dumps(emails_extraidos, indent=4))  # Exibe os emails no formato JSON
