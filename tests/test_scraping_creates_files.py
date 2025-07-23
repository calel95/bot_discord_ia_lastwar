import os
from pathlib import Path
from src.main import extract_content_full_urls

def test_scraping_creates_files():
    extract_content_full_urls()
    data_path = Path("data")
    arquivos = list(data_path.glob("*.txt"))
    assert len(arquivos) > 0, "Nenhum arquivo foi criado na pasta data"
    for arquivo in arquivos:
        assert arquivo.stat().st_size > 0, f"Arquivo {arquivo} está vazio"