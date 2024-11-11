from jinja2 import Environment, FileSystemLoader
from pathlib import Path
import json
import random
import sys
from typing import Any

name_samples = [
    "pouet",
    "lol",
    "Casablanca",
    "bouteille",
    "saucisse",
    "reblochon",
    "savoie",
    "Suisse",
    "Restaurant",
    "monsieur",
    "madame",
    "canard",
    "autruche",
    "Jamon",
    "jambon",
    "matcha",
    "cafe",
    "liste",
    "dico",
    "ensemble",
]

leaf_sample = [
    "c'est en cornichant que l'on devient cornichon",
    "les cerises sont perches sur le tabouret de mon grand pere",
    "j'ai 10 ans, je sais que ce n'est pas vrai mais j'ai 10 ans",
    "une poule sur un mur qui picore du pain dur",
    "il etait une fois l'Amerique",
    "je n'ai plus d'idee",
]


def generate_dict_recu(depth: int, current: dict[str, Any] | list[Any]) -> None:
    if isinstance(current, dict):
        key = random.choice(name_samples)
        if depth == 0:
            current[key] = random.choice(leaf_sample)
        else:
            name_samples_copy = name_samples.copy()
            for i in range(random.randrange(2, 5)):
                if random.randint(0, 4) == 0:
                    child = list()
                else:
                    child = dict()
                current[key] = child
                name_samples_copy.remove(key)
                key = random.choice(name_samples_copy)
                generate_dict_recu(depth - 1, child)
    else:
        if depth == 0:
            for i in range(random.randrange(2, 5)):
                current.append(random.choice(leaf_sample))
        else:
            for i in range(random.randrange(2, 5)):
                if random.randint(0, 4) == 0:
                    child = list()
                else:
                    child = dict()
                current.append(child)
                generate_dict_recu(depth - 1, child)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        depth = int(sys.argv[1])
    else:
        depth = 5

    sample = dict()
    generate_dict_recu(depth, sample)

    path = Path(__file__).parent

    json_encoder = json.JSONEncoder(indent=2)

    env = Environment(
        loader=FileSystemLoader(path / "templates")
    )
    template = env.get_template("template1.rst")

    rendered = template.render(sample=sample)

    json_content = json_encoder.encode(sample)

    with open(path.joinpath("json_format.json"), "w") as io:
        io.write(json_content)

    with open(path.joinpath("source/sphinx_sample.rst"), "w") as io:
        io.write(rendered)
