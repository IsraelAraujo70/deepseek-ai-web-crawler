import asyncio
import json

from crawl4ai import AsyncWebCrawler
from dotenv import load_dotenv

from config import BASE_URL, CSS_SELECTOR, REQUIRED_KEYS
from utils.data_utils import (
    save_venues_to_csv,
)
from utils.scraper_utils import (
    fetch_and_process_page,
    get_browser_config,
    get_llm_strategy,
)

load_dotenv()


async def crawl_petshops():
    """
    Função principal para coletar dados de pet shops do site.
    """
    # Inicializa configurações
    browser_config = get_browser_config()
    llm_strategy = get_llm_strategy()

    # Inicia o crawler
    async with AsyncWebCrawler(config=browser_config) as crawler:
        # Executa o crawler
        result = await crawler.arun(
            url=BASE_URL,
            config=llm_strategy
        )

        if result.success and result.extracted_content:
            # Converte o conteúdo extraído de string JSON para lista de dicionários
            try:
                pet_shops = json.loads(result.extracted_content)
                # Processa e salva os resultados
                save_venues_to_csv(pet_shops, "pet_shops.csv")
                print(f"Salvos {len(pet_shops)} pet shops em 'pet_shops.csv'.")
            except json.JSONDecodeError as e:
                print(f"Erro ao decodificar JSON: {e}")
                print("Conteúdo extraído:", result.extracted_content)
        else:
            print("Nenhum pet shop foi encontrado durante a busca.")
            if result.error_message:
                print(f"Erro: {result.error_message}")


async def main():
    """
    Ponto de entrada do script.
    """
    await crawl_petshops()


if __name__ == "__main__":
    asyncio.run(main())
