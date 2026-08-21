<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/hero-dark.png">
  <source media="(prefers-color-scheme: light)" srcset="assets/hero-light.png">
  <img src="assets/hero-light.png" alt="qiaobs-skills：TRACE、EXECUTE、UPDATE 三个证据优先的 Agent Skill 能力模块">
</picture>

# qiaobs-skills

**从真实项目中长出来的三套 Agent Skills：找到第一处偏差，连续完成已授权工作，让现实修正判断。**

[English](README.en.md) · [快速安装](#快速安装) · [选择 Skill](#我该选哪个-skill) · [真实案例](#一个匿名真实案例)

[![Validate skills](https://github.com/qiao-obs/qiaobs-skills/actions/workflows/validate.yml/badge.svg)](https://github.com/qiao-obs/qiaobs-skills/actions/workflows/validate.yml)
[![MIT License](https://img.shields.io/badge/license-MIT-0B1220.svg)](LICENSE)
[![Agent Skills standard](https://img.shields.io/badge/standard-Agent%20Skills-2563EB.svg)](https://agentskills.io/)

## 30 秒理解

很多 Agent 任务不是“不会写代码”，而是**没有沿着现实发生的路径把问题看完**：

- 功能只在某个角色、真机、入口或非空数据下失败，错误文案却把人引向了错误的层；
- 工作已经明确授权，却每完成一个相邻步骤就停下来重新询问，导致检查、实现、测试和收尾彼此脱节；
- 计划听起来合理、学习记录看起来努力，却没有用独立表现、迁移和延迟复测去修正判断。

这三个 Skill 分别回答三个不同问题：

```text
TRACE    现实从哪一环开始偏离？
EXECUTE  如何在授权边界内少打断地把工作做完？
UPDATE   如何让事实、实践和复测修正判断与计划？
```

它们是**独立能力，可以按需组合**，不是每次都要一起加载。

## 我该选哪个 Skill？

| 你现在遇到的情况 | 应使用 | 它交付什么 |
| --- | --- | --- |
| 功能只在特定角色、设备、入口、数据状态或发布版本下失败 | [`trace-feature-chain`](skills/trace-feature-chain/SKILL.md) | 第一处偏差、最小修复、分层验证和真实发布边界 |
| 任务已授权，包含检查、修改、测试、文档和收尾，希望少交接地完成 | [`run-autonomous-workpacks`](skills/run-autonomous-workpacks/SKILL.md) | 有依赖和检查点的工作包、失败重试、真实最终状态 |
| 长期学习、能力诊断、计划或决策需要证据和更新 | [`reason-from-reality`](skills/reason-from-reality/SKILL.md) | 事实/判断/行动/验证/未知、测量指标、复测和切换规则 |

### 1. TRACE · 首个偏差链路追踪

**一句话价值：** 从真实角色和入口开始，沿着页面、权限、API、数据、共享契约、运行时、构建和发布一路取证，找到第一处不匹配，而不是追着最后一条报错跑。

**它防止什么高代价错误：** 把真机运行时问题误判成服务器问题；用账号 ID 特判掩盖共享契约缺陷；把“源代码改了”误报成“用户已经拿到修复”。

**何时用 / 何时不要用：**

- 用于跨层功能故障、角色或数据条件差异、模拟器与真机差异、构建/预览/上传版本不一致。
- 不用于普通 UI 美化、独立语法错误、翻译或没有失败链需要定位的泛化部署。

**核心工作方式：**

```text
真实场景 → 身份/权限 → 命令/API → 数据/契约
→ 运行时 → 构建物 → 预览/发布 → 原场景复测
```

1. 冻结角色、设备、真实入口、数据条件、唯一失败和预期结果；
2. 为每一环记录 `expected / observed / evidence / status`；
3. 停在第一处有证据的不匹配；
4. 只修根因层，按层验证，不把测试、构建、预览、上传和验收混成一个结论。

**会得到什么输出：** 场景谓词、证据矩阵、第一处偏差、最小安全修复、未证明的发布层和剩余风险。

**一个真实提示词：**

> 平台运营角色在模拟器能编辑公开资料，但真实手机只在存在头像 URL 时失败。请沿完整链路找第一处不匹配，只修真正根因，并明确测试、构建、预览和上传分别证明了什么。

**一个简短输出示例：**

> API 返回形状正常；带媒体地址时共享契约调用目标真机不保证存在的浏览器 API。第一处偏差在共享契约/运行时边界。修共享层并补原始数据条件回归；后端不动。源测试通过不等于手机预览或上传版本已验证。

深入阅读：[用户说明页](docs/skills/trace-feature-chain.zh-CN.md) · [执行入口](skills/trace-feature-chain/SKILL.md) · [证据矩阵](skills/trace-feature-chain/references/evidence-matrix.md)

### 2. EXECUTE · 有界自主工作包

**一句话价值：** 当任务已经授权且包含多个相邻阶段时，把它组织成有边界、可验证的工作包，减少人工交接，并持续推进到完成、部分完成或真实阻塞。

**何时用 / 何时不要用：**

- 用于已明确授权的多阶段检查、实现、测试、文档、构建和收尾。
- 不用于把“只分析、不修改”变成实施许可，也不用于缺少关键事实、需要 MFA/人工审批、付费、破坏性或未授权生产动作。

**核心工作方式：**

```text
任务契约 → 工作包卡片 → 依赖顺序
→ 安全执行 → 失败诊断/有限重试
→ 分层验证 → COMPLETE/PARTIAL/BLOCKED
```

**工作包应记录：** 目标、完成条件、输入、依赖、准确写入范围、明确不触碰的范围、风险、检查、恢复路径和证据。源代码、测试、构建、预览、上传、合并、Release 和用户验收分别证明不同层次，不能互相替代。

**它不改变什么：** 该 Skill 只规定工作组织、执行边界和验证方法，不改变 Codex 原生的对话、进度展示或子代理体验。

| 用户不必做 | Skill 负责做 |
| --- | --- |
| 替 Agent 拆分已授权的相邻步骤 | 创建有依赖和完成条件的工作包 |
| 反复复制文件清单和检查结果 | 在工作包记录中保留输入、输出和证据 |
| 把本地测试结果推导成发布结果 | 区分已验证、未知、跳过和阻塞层 |
| 为普通实现细节重新作决定 | 在已有授权与安全边界内连续推进 |

**一个真实提示词：**

> 请在当前授权范围内连续完成审计、实现、回归测试、文档和 Git 收尾；保留已有修改，不使用破坏性命令。只在登录/MFA、权限拒绝、未授权高影响动作或关键事实缺失时停下，并把每一层证据分开记录。

**一个简短收口记录：**

> `PARTIAL`：基线审计、实现和目标测试已验证；远程合并因权限拒绝而跳过。变更文件和未触碰范围已记录，未把本地通过写成发布完成。

深入阅读：[用户说明页](docs/skills/run-autonomous-workpacks.zh-CN.md) · [执行入口](skills/run-autonomous-workpacks/SKILL.md) · [工作包生命周期](skills/run-autonomous-workpacks/references/workpack-lifecycle.md)

### 3. UPDATE · 文明级智慧内核的现实闭环

**一句话价值：** 把跨传统可复用的实践原则、科学方法、学习科学和反馈控制压缩成可测量的行动闭环，让结果而不是漂亮解释决定下一步。

**它防止什么高代价错误：** 用鼓励、名言或 AI 口吻替代诊断；把“看懂”当成“会做”；用一次好表现预测长期能力；在医疗、法律或危机边界内继续做普通优化。

**“文明级智慧内核”是什么意思：** 它不是思想家合集、神秘权威或事实数据库，而是跨传统提炼出的**可操作、可检验原则集合**。任何传统、研究、旧报告和 AI 自身都不能免于现实、逻辑、实践、结果和复测的检验；证据不足就标记 `UNKNOWN`。

**核心循环：**

```text
目标 → 现实 → 差距 → 主要矛盾 → 行动
→ 测量 → 迁移/延迟复测 → 更新
```

**何时用 / 何时不要用：**

- 用于长期备考、能力诊断、计划评估、复盘、习惯/流程改进和不确定性决策。
- 不用于一次性事实问答、翻译、改写、简单语法修复或没有测量与更新需求的普通任务。

**会得到什么输出：** 目标行为、事实账本、竞争解释、下一项行动/实验、即时与延迟/迁移测量、继续/调整/停止规则和未知项。

**一个真实提示词：**

> 请根据我最近的闭卷练习记录诊断为什么“看懂但不能迁移”。区分事实、判断、行动、验证和未知，设计一个小实验和第 1、3、7 天复测；不要用鼓励或名言替代证据。

**一个简短输出示例：**

> 事实：闭卷正确率 55%–65%，看解析后即时重做 90%。判断：更像检索/迁移不稳，而不是概念缺失（中等置信度）。行动：做陌生变式题并禁止看笔记。若延迟迁移仍不上升，切换到概念边界诊断。

深入阅读：[用户说明页](docs/skills/reason-from-reality.zh-CN.md) · [执行入口](skills/reason-from-reality/SKILL.md) · [证据循环](skills/reason-from-reality/references/evidence-and-decision-loop.md)

## 三者如何组合

不要为了“完整”而每次加载三个：

| 场景 | 主 Skill | 可组合 Skill |
| --- | --- | --- |
| 跨前后端、真机和发布的复杂 Bug | `trace-feature-chain` | `run-autonomous-workpacks` 负责低交互推进 |
| 根因已明确的大型实现任务 | `run-autonomous-workpacks` | 通常不需要另外两个 |
| 长期备考、能力诊断和行动复盘 | `reason-from-reality` | `run-autonomous-workpacks` 负责实施工作包 |
| 简单语法修复、翻译、改写、一次性事实问答 | 不必加载三者 | 保持简单 |

## 快速安装

列出可用 Skill：

```bash
npx skills add qiao-obs/qiaobs-skills --list
```

为 Codex 安装某个 Skill：

```bash
npx skills add qiao-obs/qiaobs-skills --skill trace-feature-chain -a codex
npx skills add qiao-obs/qiaobs-skills --skill run-autonomous-workpacks -a codex
npx skills add qiao-obs/qiaobs-skills --skill reason-from-reality -a codex
```

支持整仓安装的客户端也可以：

```bash
npx skills add qiao-obs/qiaobs-skills -a codex
```

备用方式：复制需要的 `skills/<name>/` 目录，并保持 `SKILL.md`、`references/`、`agents/openai.yaml` 和 `assets/` 一起存在。不要把仓库级 README、CHANGELOG 或安装文档复制进 Skill 目录。

## 一个匿名真实案例

某匿名校园信息小程序里，一个有权限的运营角色在模拟器可以编辑公开资料；真实手机只在账号已有头像或背景图时失败。后端返回正常，第一处可操作偏差位于共享图片契约对真机不保证存在的浏览器 API 的依赖。

这个案例的可复用方法是：

1. 不把“平台运营账号”当成前端特判理由，先确认权限和数据事实；
2. 用非空媒体 URL 保留原始失败条件；
3. 把共享层修复和回归测试放在根因位置；
4. 分开记录代码、测试、构建、手机预览、上传和用户验收。

该案例曾记录 1 个共享源文件、1 个回归测试文件、31 项定向检查通过，并避免无关后端重新部署。这些数字只描述一个匿名案例，不是本仓库的性能基准，也不是所有环境的承诺。

## 信任与验证

- **静态验证：** frontmatter、目录、引用、隐私、占位符、异常转义、图片和元数据一致性；
- **触发边界：** 每个 Skill 使用中英文正例和近邻负例，覆盖显式点名、隐式触发、短请求与长上下文；
- **情境评测：** 记录真实的 forward-test 结果；没有模型路由或 baseline 证据时明确写 `NOT RUN`；
- **安全边界：** 不扩大授权，不覆盖用户修改，不公开私密项目数据，不把测试/构建/预览/上传/验收混为一谈。

详见：[来源与方法](docs/origins-and-method.md) · [Skill 工程说明](docs/skill-engineering-notes.md) · [评测记录](evals/verification-record.md) · [场景量表](evals/scenario-rubrics.md)

## 兼容性

Codex 是主要目标。其他遵循开放 Agent Skills 约定的客户端为尽力兼容；本仓库不声称未经验证平台“完全兼容”。

## 贡献、许可证与安全

请先阅读 [`CONTRIBUTING.md`](CONTRIBUTING.md)、[`SECURITY.md`](SECURITY.md) 和 [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md)。本仓库采用 MIT License，致谢与非背书说明见 [`ACKNOWLEDGEMENTS.md`](ACKNOWLEDGEMENTS.md)。

## 深入文档

- [`trace-feature-chain` 用户说明](docs/skills/trace-feature-chain.zh-CN.md) · [English](docs/skills/trace-feature-chain.md)
- [`run-autonomous-workpacks` 用户说明](docs/skills/run-autonomous-workpacks.zh-CN.md) · [English](docs/skills/run-autonomous-workpacks.md)
- [`reason-from-reality` 用户说明](docs/skills/reason-from-reality.zh-CN.md) · [English](docs/skills/reason-from-reality.md)
- [工程设计与评测](docs/skill-engineering-notes.md)

## 版本

当前稳定版本为 [`v0.2.0`](https://github.com/qiao-obs/qiaobs-skills/releases/tag/v0.2.0)。
