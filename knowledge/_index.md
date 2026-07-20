# 📊 学习仪表盘 — 基于 verl 的企业级大模型 RL 后训练

> 单一真相来源见 [[curriculum]]。本页是快速导航与状态快照。

## 🎯 当前状态
- **当前 Phase**：🎉 全部 7 个 Phase 已完成（42 课），进入复习与期末项目阶段
- **教学模式**：🧠 苏格拉底（理论） + 🛠️ 示范驱动（工程）
- **主线算法**：GRPO（对比 PPO / DAPO）
- **实验模型**：Qwen3-1.7B/4B（小资源） · Qwen3-8B（集群）

## 🗺️ 学习路线图
可视化见 `learning-roadmap.canvas`（用 Obsidian 打开本库）。

```mermaid
mindmap
  root((verl RL 后训练))
    P1 地基
      全景/环境
      参数量计算
      量化
      显存精算
    P2 数学
      策略梯度
      PPO clip
      KL 正则
      优势估计
      GRPO 推导
    P3 架构数据流
      DataProto
      parquet 格式
      batch 体系
      3D-HybridEngine
    P4 首个 GRPO
      GSM8K 实战
      双档脚本
      参数精讲
      OOM 排查
    P5 分布式
      DP/TP/PP/SP
      FSDP/Megatron
      显存重分配
    P6 Reward 与评测
      reward 设计
      reward hacking
      评测集构建
      评估体系
    P7 生产化
      性能调优
      调参手册
      异常诊断
      上线 checklist
```

## 📚 Phase 导航
- [[01-foundations/]] — Phase 1 地基
- [[02-math/]] — Phase 2 数学原理
- [[03-architecture/]] — Phase 3 架构与数据流
- [[04-first-grpo/]] — Phase 4 首个 GRPO
- [[05-distributed/]] — Phase 5 分布式训练
- [[06-reward-eval/]] — Phase 6 Reward 与评测
- [[07-production/]] — Phase 7 生产化

## 📈 总进度
Phase 1：██████████ 100% · Phase 2：██████████ 100% · Phase 3：██████████ 100%
Phase 4：██████████ 100% · Phase 5：██████████ 100% · Phase 6：██████████ 100% · Phase 7：██████████ 100%

**总课时**：42/42 🎉

## 🕘 最近更新
- 2026-07-20：知识库初始化，课程骨架就绪。
- 2026-07-20：✅ 全部 7 个 Phase、42 篇详细笔记 + 4 个可运行实验脚本完成。
