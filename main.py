import json
from link_collector import process_and_save_source

with open('parser_config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)


process_and_save_source(config["sources"][1], "product_links.json", max_pages=10000, max_depth=10, num_threads=10)

