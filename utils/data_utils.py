import csv
from typing import Dict, List, Set

from models.venue import Venue


def is_duplicate_venue(venue_name: str, seen_names: set) -> bool:
    return venue_name in seen_names


def is_complete_venue(venue: dict, required_keys: list) -> bool:
    return all(key in venue for key in required_keys)


def is_complete_petshop(petshop: Dict, required_keys: List[str]) -> bool:
    """
    Verifica se um pet shop tem todos os campos obrigatórios.

    Args:
        petshop (Dict): Dicionário com os dados do pet shop
        required_keys (List[str]): Lista de chaves obrigatórias

    Returns:
        bool: True se todos os campos obrigatórios estão presentes e não vazios
    """
    return all(
        petshop.get(key) and isinstance(petshop[key], str) and petshop[key].strip()
        for key in required_keys
    )


def is_duplicate_petshop(name: str, seen_names: Set[str]) -> bool:
    """
    Verifica se um pet shop já foi processado.

    Args:
        name (str): Nome do pet shop
        seen_names (Set[str]): Conjunto de nomes já vistos

    Returns:
        bool: True se o pet shop já foi processado
    """
    return name in seen_names


def save_venues_to_csv(venues: list, filename: str):
    if not venues:
        print("No venues to save.")
        return

    # Use field names from the Venue model
    fieldnames = Venue.model_fields.keys()

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(venues)
    print(f"Saved {len(venues)} venues to '{filename}'.")


def save_venues_to_csv(petshops: List[Dict], filename: str) -> None:
    """
    Salva a lista de pet shops em um arquivo CSV.

    Args:
        petshops (List[Dict]): Lista de dicionários com dados dos pet shops
        filename (str): Nome do arquivo CSV
    """
    if not petshops:
        print("Nenhum pet shop para salvar.")
        return

    # Obtém as chaves do primeiro pet shop como cabeçalho
    fieldnames = petshops[0].keys()

    # Salva os dados no arquivo CSV
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(petshops)

    print(f"Dados salvos com sucesso em '{filename}'!")
