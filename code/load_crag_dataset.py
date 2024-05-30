import argparse
import json


def load_crag_dataset(file_path):
    """Load CRAG dataset from file

    Args:
        file_path (str)

    Returns:
        list[dict]: Datas in crag dataset.
            Each data is a dict with keys: "query", "answer", "alternative_answers", "search_results".
    """
    data: list[dict] = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            data.append(json.loads(line))
    return data


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file_path', type=str, default="data/CRAG_cleaned/crag_data_2735/crag_data_2735.jsonl", help='path to the crag dataset file')
    args = parser.parse_args()

    data: list[dict] = load_crag_dataset(args.file_path)
    print(data[0])