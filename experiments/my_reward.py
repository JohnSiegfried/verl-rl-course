"""自定义数学 reward：带格式分 + 部分分 + dict 返回（对应笔记 6.2）
用法：
  reward_model.custom_reward_function.path=experiments/my_reward.py
  reward_model.custom_reward_function.name=compute_score
"""
import re


def _extract_after_marker(solution_str, marker="####"):
    m = re.search(marker + r"\s*(\-?[0-9\.\,]+)", solution_str)
    if m is None:
        return None
    return m.group(1).replace(",", "").strip()


def compute_score(data_source, solution_str, ground_truth, extra_info=None):
    """GSM8K 风格：对=1.0，格式对但错=0.1，格式错=0.0。返回 dict 便于观测子指标。"""
    pred = _extract_after_marker(solution_str)
    format_ok = pred is not None
    if not format_ok:
        return {"score": 0.0, "acc": 0, "format_ok": 0}

    gt = str(ground_truth).replace(",", "").strip()
    try:
        correct = abs(float(pred) - float(gt)) < 1e-6
    except (ValueError, TypeError):
        correct = (pred == gt)

    score = 1.0 if correct else 0.1
    return {"score": score, "acc": int(correct), "format_ok": 1}


def compute_score_with_length_penalty(data_source, solution_str, ground_truth,
                                       extra_info=None, max_len=1024):
    """在正确性基础上加长度惩罚（对应笔记 6.4 reward hacking 缓解）。"""
    base = compute_score(data_source, solution_str, ground_truth, extra_info)
    score = base["score"]
    # 超长软惩罚：超过 max_len 线性扣分，最低扣到 0
    over = max(0, len(solution_str) - max_len)
    score = max(0.0, score - over / max_len * 0.5)
    base["score"] = score
    base["len_penalty"] = over
    return base
