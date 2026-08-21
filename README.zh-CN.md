# qiaobs-skills（桥 obs 的 Agent Skills）

三个从真实问题中提炼、可组合、可验证的 Agent Skill：根因链路追踪、低交互自主工作包、证据约束的学习与决策。

[English README](README.md)

[![Validate skills](https://github.com/qiao-obs/qiaobs-skills/actions/workflows/validate.yml/badge.svg)](https://github.com/qiao-obs/qiaobs-skills/actions/workflows/validate.yml)
[![MIT License](https://img.shields.io/badge/license-MIT-1f2937.svg)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/standard-Agent%20Skills-526581.svg)](https://agentskills.io/)

![qiaobs-skills banner](assets/banner.svg)

## 三个 Skill

| Skill | 解决的问题 | 何时触发 | 典型输出 |
| --- | --- | --- | --- |
| [`trace-feature-chain`](skills/trace-feature-chain/SKILL.md) | 找到功能链中第一处偏离现实的位置 | 特定角色、设备、入口、数据条件失败，或代码与发布版本不一致 | 场景谓词、证据矩阵、根因、最小修复、验证和发布边界 |
| [`run-autonomous-workpacks`](skills/run-autonomous-workpacks/SKILL.md) | 在安全边界内连续推进相邻阶段，减少交接 | 用户授权“尽量一次做完”“继续执行”或完整实施 | 用户专属阻塞、执行顺序、检查点、重试和真实最终状态 |
| [`reason-from-reality`](skills/reason-from-reality/SKILL.md) | 把原则变成可测量的学习、计划、诊断和复盘闭环 | 长期学习、备考、能力诊断、决策或持续改进 | 事实／判断／行动／验证／未知，指标、复测和更新规则 |

## 为什么是这三个

- `trace-feature-chain` 回答：**现实从哪一环开始偏离？**
- `run-autonomous-workpacks` 回答：**如何在授权范围内少交接地完成？**
- `reason-from-reality` 回答：**如何依据证据行动并更新，而不是自我欺骗？**

它们可以组合，但不互相扩大权限。例如，低交互修复跨层 Bug 时，用 `run-autonomous-workpacks` 组织执行，用 `trace-feature-chain` 定位根因；长期备考系统中，用 `reason-from-reality` 处理诊断内核，再用 `run-autonomous-workpacks` 推进实施。

## 安装

列出 Skills：

```bash
npx skills add qiao-obs/qiaobs-skills --list
```

为 Codex 安装三个 Skill：

```bash
npx skills add qiao-obs/qiaobs-skills --skill trace-feature-chain -a codex
npx skills add qiao-obs/qiaobs-skills --skill run-autonomous-workpacks -a codex
npx skills add qiao-obs/qiaobs-skills --skill reason-from-reality -a codex
```

支持时也可以安装整个仓库：

```bash
npx skills add qiao-obs/qiaobs-skills -a codex
```

备用方式：只复制需要的 `skills/<name>/` 目录到你的 Agent 客户端所记录的 Skill 目录，并保持 `SKILL.md` 与其引用文件一起存在。

## 使用示例

**跨层 Bug：**

> 平台运营账号在模拟器可以编辑公开主页，但真实手机只在存在头像 URL 时失败。请沿完整逻辑链找第一处不匹配，做最小安全修复，并明确还缺哪些构建、预览或发布证据。

**长期备考：**

> 我准备一个长期考试目标。请先区分事实、判断、行动、验证和未知，不要用鼓励替代诊断；根据真实练习记录设计主动提取、间隔复习、迁移练习和复测规则。

## 兼容性

Codex 是主要目标。其他遵循开放 Agent Skills 约定的客户端为尽力兼容；本仓库不声称未经验证平台“完全兼容”。

## 安全边界

Skill 不会扩大授权。必须保留用户修改，避免破坏性历史重写，拒绝泄露凭据和私人数据，并区分诊断与实施。公开发布、生产变更、外部消息、付费动作、数据删除和账号认证仍需明确边界。测试、构建、预览、上传、部署或用户验收只能证明各自层级。

## 来源与方法

方法来自一个匿名校园信息平台小程序的长期开发、真实故障、迭代和复盘。公开版本只保留可复用方法，不包含私人日志、标识符、凭据、基础设施细节或真实用户数据。详见 [`docs/origins-and-method.md`](docs/origins-and-method.md)。

## 评测与质量

仓库包含确定性结构验证、含近邻负例的触发数据、情境评分量表和组合测试。CI 只运行静态验证；模型触发与前向测试采用版本化、可复现的真实记录，不伪造分数。详见 [`docs/skill-engineering-notes.md`](docs/skill-engineering-notes.md) 与 [`evals/scenario-rubrics.md`](evals/scenario-rubrics.md)。

## 贡献与许可证

请先阅读 [`CONTRIBUTING.md`](CONTRIBUTING.md)。许可证为 MIT，致谢与非背书说明见 [`ACKNOWLEDGEMENTS.md`](ACKNOWLEDGEMENTS.md)。
