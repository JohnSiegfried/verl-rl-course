---
domain: 基于 verl 的企业级大模型 RL 后训练
platform: obsidian
teaching_mode: hybrid-socratic-demo
main_algorithm: GRPO
model_tiers: [Qwen3-1.7B/4B 小资源, Qwen3-8B 集群]
created: 2026-07-20
updated: 2026-07-21
status: active
---

# 滚动课程表（单一真相来源）

> 进度标记：⬜ 未开始 · 🔄 进行中 · ✅ 完成
> 教学模式：🧠 苏格拉底式（理论） · 🛠️ 示范驱动式（工程） · 🏗️ 项目驱动式

---

## Phase 1 — 地基：全景 + 环境 + 模型/显存精算 🛠️
**目标**：跑通环境，会手算参数量与显存，能根据显卡选模型与配置避免 OOM。
**实验 E1**：产出自己硬件的显存预算表并用 nvidia-smi 实测验证。

| ID | 课时 | 状态 |
|----|------|------|
| 1.1 | RL 后训练全景：SFT→RM→RLHF/RLVR，verl 的定位 | ✅ |
| 1.2 | 环境搭建：Docker 镜像、verl 安装、依赖 | ✅ |
| 1.3 | 模型参数量计算：dense/MoE 手算公式 | ✅ |
| 1.4 | 量化基础：FP16/BF16/FP8/INT8/INT4 显存与精度 | ✅ |
| 1.5 | 显存分配精算：weights/grads/optim/act/KV + verl 特有 ref/reward | ✅ |
| 1.6 | 选模型 + 选显卡实战：从显存反推配置，避免 OOM | ✅ |

**完成数**：6/6　**进度**：██████████ 100% 🎉

---

## Phase 2 — 数学原理：从 RL 到 GRPO 的完整推导 🧠
**目标**：能独立推导 GRPO 目标函数，理解 PPO/DAPO 差异。
**实验 E2**：手推 4 样本组的 GRPO 优势与 loss。

| ID  | 课时                                    | 状态  |
| --- | ------------------------------------- | --- |
| 2.1 | RL 基础：MDP、回报、策略梯度定理、REINFORCE         | ✅ |
| 2.2 | 重要性采样与 PPO clip                       | ✅ |
| 2.3 | KL 正则：KL 惩罚 vs KL loss，k1/k2/k3 估计器   | ⬜ |
| 2.4 | 优势估计：GAE、reward-to-go、RLOO、组内相对优势     | ⬜ |
| 2.5 | GRPO 目标函数完整推导 + loss_agg_mode         | ⬜ |
| 2.6 | PPO vs GRPO vs DAPO vs REINFORCE++ 对比 | ⬜ |

**完成数**：2/6　**进度**：████░░░░░░ 33%

---

## Phase 3 — verl 架构与数据流 🛠️
**目标**：讲清从 parquet 到梯度更新的完整数据流与 batch 体系。
**实验 E3**：打印一次训练各阶段 DataProto 的 shape 与字段。

| ID | 课时 | 状态 |
|----|------|------|
| 3.1 | 单控制器架构：Ray + Worker 抽象 | ⬜ |
| 3.2 | 中间数据格式 DataProto：batch/non_tensor_batch/meta_info | ⬜ |
| 3.3 | 输入数据格式：parquet 5 字段 + chat_template | ⬜ |
| 3.4 | 数据流转全链路：prompt→rollout→log_prob→ref→reward→advantage→update | ⬜ |
| 3.5 | batch size 体系：train/rollout.n/mini/micro/动态 bsz 归一化 | ⬜ |
| 3.6 | 3D-HybridEngine：FSDP↔vLLM 权重 reshard 与显存复用 | ⬜ |

**完成数**：0/6　**进度**：░░░░░░░░░░ 0%

---

## Phase 4 — 跑通第一个 GRPO：GSM8K 双档实战 🛠️
**目标**：在自己硬件上跑通 GRPO 并提升 accuracy。
**实验 E4**：跑通 GRPO，accuracy 超过 base。

| ID | 课时 | 状态 |
|----|------|------|
| 4.1 | GSM8K 数据预处理：make_map_fn / extract_solution | ⬜ |
| 4.2 | 小资源版脚本逐行讲解（Qwen3-1.7B/4B + LoRA + 4090） | ⬜ |
| 4.3 | 集群版脚本逐行讲解（Qwen3-8B 全参 + 8×A100） | ⬜ |
| 4.4 | 参数作用精讲：lr/kl/entropy/clip/rollout.n/gpu_mem_util/offload | ⬜ |
| 4.5 | OOM 排查决策树：rollout/log_prob/update 三阶段 | ⬜ |

**完成数**：0/5　**进度**：░░░░░░░░░░ 0%

---

## Phase 5 — 分布式训练：原理、流程与显存重分配 🧠🛠️
**目标**：理解并行原语，能在多卡下重新精算显存。
**实验 E5**：同模型 1/4/8 卡显存精算与实测对比。

| ID | 课时 | 状态 |
|----|------|------|
| 5.1 | 并行原语：DP/TP/PP/SP(Ulysses)/CP 数学含义与通信量 | ⬜ |
| 5.2 | FSDP 原理：shard、all_gather/reduce_scatter | ⬜ |
| 5.3 | Megatron 原理：TP/PP/SP 与 FSDP 取舍 | ⬜ |
| 5.4 | verl 并行映射：tp_size/fsdp_config/megatron_config/ulysses | ⬜ |
| 5.5 | 分布式显存重分配：DP/TP/SP 下 weights/optim/KV 切分 | ⬜ |
| 5.6 | 多机多卡：nnode、Ray 集群、NCCL、故障排查 | ⬜ |

**完成数**：0/6　**进度**：░░░░░░░░░░ 0%

---

## Phase 6 — Reward 工程与评测体系 🛠️🏗️
**目标**：能设计 reward、构建评测集、搭建评估体系。
**实验 E6**：写带格式+长度惩罚的数学 reward，构建小型评测集跑评估。

| ID | 课时 | 状态 |
|----|------|------|
| 6.1 | Reward function 设计：rule/model(DisRM/GenRM)/混合 | ⬜ |
| 6.2 | compute_score 接口与返回值 | ⬜ |
| 6.3 | RewardManager：naive/prime/dapo/limit/remote/reward_loop | ⬜ |
| 6.4 | reward hacking 与缓解：长度/格式/overlong 惩罚 + KL | ⬜ |
| 6.5 | 评测集构建：划分、防泄漏、pass@k/avg@k/best@k | ⬜ |
| 6.6 | 指标与评估体系：reward/长度/KL/entropy/grad_norm/val acc | ⬜ |
| 6.7 | 观测与日志：console/wandb/mlflow、rollout dump、告警 | ⬜ |

**完成数**：0/7　**进度**：░░░░░░░░░░ 0%

---

## Phase 7 — 观测经验、调参与生产化 🏗️
**目标**：形成自己的调参手册，完成一次可复现的完整后训练。
**期末项目**：完整可复现的 GRPO 后训练（数据→reward→训练→评测→报告）。

| ID | 课时 | 状态 |
|----|------|------|
| 7.1 | 性能调优：rollout 吞吐 + 训练吞吐 | ⬜ |
| 7.2 | 调参经验库：lr/kl/rollout.n/batch/entropy 对策表 | ⬜ |
| 7.3 | 训练异常诊断：reward 不涨/KL 爆炸/长度坍缩/entropy 坍缩 | ⬜ |
| 7.4 | Agentic rollout：多轮工具调用、tool_parser（前沿扩展） | ⬜ |
| 7.5 | 从实验到生产：checkpoint、容错、成本、上线 checklist | ⬜ |
| 7.6 | 课程总复盘：形成《企业 RL 后训练调参手册》 | ⬜ |

**完成数**：0/6　**进度**：░░░░░░░░░░ 0%

---

## 最近更新
- 2026-07-20：课程初始化，7 个 Phase 骨架建立。
- 2026-07-21：⬜ 全部进度重置为未开始，开始系统学习。
