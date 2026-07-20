# 基于 verl 的企业级大模型 RL 后训练课程

> 面向企业大模型后训练工程师的系统课程：以 **GRPO 为主线**（对比 PPO/DAPO），覆盖数学原理、显存精算、分布式训练、Reward 工程、评测体系与生产化。
> 基于 [verl](https://github.com/verl-project/verl) 知识库，按 **curriculum-builder** 方法论生成。

## 🧩 本课程由这些 Skill 驱动

本课程不是凭空写的，而是用以下 Skill 方法论结构化生成的，强烈推荐你复用它们来生成自己的课程：

### ⭐ curriculum-builder（核心）
- **仓库地址**：<https://github.com/doloveplayer/curriculum-builder>
- **作用**：把任意学习领域转化为结构化课程体系——自动调研、生成 Phase 大纲、维护滚动课程表、追踪学习进度、标准化知识库。
- 本课程的 **全部骨架与规范都来自它**：
  - 🗂️ **滚动课程表**（`knowledge/curriculum.md`）——单一真相来源，记录每课状态与进度。
  - 📝 **笔记标准**——每课固定结构「一句话 / 核心公式·原理 / 与其他概念的关系 / 关键来源 / 我的实验」。
  - 🔗 **来源追溯原则**——每个重要论断标注原始出处（论文/书籍/网页），AI 生成内容显式标注待人工验证。
  - 🎓 **三种教学模式**——苏格拉底式（数学/理论）+ 示范驱动式（工程/实战）+ 项目驱动式（生产化），本课程采用混合式。
  - 🛡️ **五层防偏机制**——Session 启动检查、课前飞行检查、课后原子提交、定期校验、离题拦截。
- **安装**：把仓库 clone 到项目的 `.claude/skills/`（或 WorkBuddy 的 `~/.workbuddy/skills/`）即可被发现：
  ```bash
  git clone https://github.com/doloveplayer/curriculum-builder.git \
    your-project/.claude/skills/curriculum-builder
  ```

### 💡 brainstorming（前置确认）
- 在动手生成前先与你确认关键设计细节（学员画像、教学模式、主线算法、硬件环境、交付形式），避免方向跑偏。
- 本课程的"双档模型（小资源 LoRA + 集群全参）""GRPO 主线""Obsidian 平台"等决策，都是 brainstorming 阶段与你敲定的。

## 📂 目录结构
```
verl-rl/
├── knowledge/                 ← Obsidian 知识库（42 篇详细笔记）
│   ├── _index.md              ← 学习仪表盘（从这里开始）
│   ├── curriculum.md          ← 滚动课程表（进度追踪）
│   ├── learning-roadmap.canvas← Obsidian 可视化路线图
│   ├── 01-foundations/        ← Phase 1 地基（全景/环境/参数量/量化/显存/选卡）
│   ├── 02-math/               ← Phase 2 数学（策略梯度/PPO/KL/优势/GRPO推导/对比）
│   ├── 03-architecture/       ← Phase 3 架构（单控制器/DataProto/parquet/数据流/batch/HybridEngine）
│   ├── 04-first-grpo/         ← Phase 4 实战（数据/小资源LoRA/集群8B/参数/OOM）
│   ├── 05-distributed/        ← Phase 5 分布式（并行原语/FSDP/Megatron/显存重分配/多机）
│   ├── 06-reward-eval/        ← Phase 6 Reward与评测（reward设计/接口/manager/hacking/评测/指标/观测）
│   ├── 07-production/         ← Phase 7 生产化（调优/调参手册/异常诊断/Agentic/上线/复盘）
│   └── templates/             ← 笔记模板
├── experiments/               ← 可运行实验脚本
│   ├── prepare_gsm8k.py       ← GSM8K 数据预处理
│   ├── run_grpo_qwen3_8b.sh   ← 集群版：Qwen3-8B 全参 + 8×A100
│   ├── run_grpo_qwen3_1.7b_lora.sh ← 小资源版：Qwen3-1.7B + LoRA + 单卡
│   └── my_reward.py           ← 自定义数学 reward（含长度惩罚）
└── data/                      ← 数据集（运行预处理脚本后生成）
```

## 🚀 快速开始
1. 用 Obsidian 打开 `knowledge/` 作为仓库，从 `_index.md` 进入。
2. 按 `curriculum.md` 的 Phase 顺序学习；每课笔记含「一句话 / 核心公式 / 概念关系 / 关键来源 / 我的实验」。
3. 进入 Phase 4 时，先跑 `experiments/prepare_gsm8k.py` 生成数据，再按你的硬件选 4.2（小资源）或 4.3（集群）脚本。

## 🎯 设计原则
- **双档并行**：小资源（Qwen3-1.7B/4B + LoRA + 4090）与集群（Qwen3-8B + 8×A100）两套完整方案。
- **来源追溯**：每篇笔记标注原始出处（verl 官方文档 / HybridFlow / GRPO·DAPO / Megatron·ZeRO 论文 / 源码路径），AI 生成内容显式标注。（此规范来自 [curriculum-builder](https://github.com/doloveplayer/curriculum-builder) 的来源追溯原则）
- **可运行**：所有实验基于 verl 官方示例改造，含显存精算与 OOM 排查。

## 📌 学习建议
- 数学课（Phase 2、5 部分）建议主动推导，不要只读。
- 工程课（Phase 1/4/5/7）务必动手跑脚本、填显存预算表、实测 nvidia-smi。
- 完成全部后做 [[07-production/7.6-课程总复盘]] 的期末项目，形成你自己的调参手册。
