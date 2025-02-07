# Web Crawler para Pet Shops

Este é um web crawler desenvolvido com Crawl4AI para coletar informações sobre pet shops em Poços de Caldas através do site Click Disk.

## Requisitos

- Python 3.8 ou superior
- Navegador Chromium (será instalado automaticamente pelo Crawl4AI)

## Instalação

1. Clone este repositório
2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Uso

Execute o script principal:
```bash
python crawler.py
```

Os dados serão salvos no arquivo `pet_shops.json` no formato:
```json
[
  {
    "name": "Nome do Pet Shop",
    "address": "Endereço completo",
    "phone": "Número de telefone"
  }
]
```

## Configuração

As configurações podem ser ajustadas no arquivo `config.py`:
- `BASE_URL`: URL base para busca
- `CSS_SELECTOR`: Seletor CSS para encontrar os elementos
- `REQUIRED_KEYS`: Campos obrigatórios para cada registro

## Recursos do Crawl4AI

Este crawler utiliza a biblioteca Crawl4AI que oferece:
- Gerenciamento automático do navegador
- Cache inteligente de requisições
- Suporte a JavaScript
- Extração de dados assíncrona
- Tratamento automático de erros 