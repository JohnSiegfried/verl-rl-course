"""GSM8K -> verl parquet 预处理脚本（对应笔记 4.1）"""
import re, os, argparse
import datasets


def extract_solution(solution_str):
    """抽取 '#### ' 之后的最终数值答案"""
    solution = re.search("#### (\\-?[0-9\\.\\,]+)", solution_str)
    assert solution is not None
    final = solution.group(0).split('#### ')[1].replace(',', '')
    return final


INSTRUCTION = 'Let\'s think step by step and output the final answer after "####".'
DATA_SOURCE = 'openai/gsm8k'


def make_map_fn(split):
    def process_fn(example, idx):
        question = example.pop('question') + ' ' + INSTRUCTION
        answer = example.pop('answer')
        solution = extract_solution(answer)
        return {
            "data_source": DATA_SOURCE,
            "prompt": [{"role": "user", "content": question}],
            "ability": "math",
            "reward_model": {"style": "rule", "ground_truth": solution},
            "extra_info": {"split": split, "index": idx},
        }
    return process_fn


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--local_dir', default='./data/gsm8k')
    args = ap.parse_args()

    ds = datasets.load_dataset(DATA_SOURCE, 'main')
    train = ds['train'].map(make_map_fn('train'), with_indices=True)
    test = ds['test'].map(make_map_fn('test'), with_indices=True)

    os.makedirs(args.local_dir, exist_ok=True)
    train.to_parquet(os.path.join(args.local_dir, 'train.parquet'))
    test.to_parquet(os.path.join(args.local_dir, 'test.parquet'))
    print(f"train={len(train)}  test={len(test)}  -> {args.local_dir}")
