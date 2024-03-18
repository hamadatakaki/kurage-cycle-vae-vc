import argparse
import itertools
import os
from pathlib import Path
import random


def random_choice(dataset: list, size: int) -> tuple[list, list]:
    if len(dataset) < size:
        raise ValueError("size is too big")

    shuffled = random.sample(dataset, len(dataset))

    return shuffled[:size], shuffled[size:]


def create_dataset(
    source: str, target: str, corpus_path: Path, exp_path: Path, test_size: int
):
    assert corpus_path.exists()

    source_gen = (corpus_path / source / "parallel100" / "wav24kHz16bit").glob("*.wav")
    target_gen = (corpus_path / target / "parallel100" / "wav24kHz16bit").glob("*.wav")
    source_dic = {str(path)[-7:]: path for path in source_gen}
    target_dic = {str(path)[-7:]: path for path in target_gen}

    keys = list(set(source_dic.keys()) & set(target_dic.keys()))

    all_dataset = []
    for key in keys:
        src, tar = source_dic[key], target_dic[key]
        if src is None or tar is None:
            raise ValueError(f"key: '{key}' is undefined")

        all_dataset.append(f"{src} {tar}")

    test, train = random_choice(all_dataset, test_size)

    os.makedirs(exp_path, exist_ok=True)

    with open(exp_path / "test_dataset.scp", "w") as file:
        file.write("\n".join(test))

    with open(exp_path / "train_dataset.scp", "w") as file:
        file.write("\n".join(train))


if __name__ == "__main__":
    parser = argparse.ArgumentParser("create train/test dataset of cycle-vae-vc")

    parser.add_argument("source", type=str, help="source speaker id")
    parser.add_argument("target", type=str, help="target speaker id")
    parser.add_argument("corpus_path", type=Path, help="corpus path")
    parser.add_argument("exp_path", type=Path, help="experiment path")
    parser.add_argument("--test_size", type=int, default=10, help="test dataset size")

    args = parser.parse_args()

    create_dataset(
        args.source, args.target, args.corpus_path, args.exp_path, args.test_size
    )
