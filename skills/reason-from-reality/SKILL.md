---
name: reason-from-reality
description: Use when a learning, planning, assessment, reflection, or improvement request needs evidence-grounded diagnosis, explicit uncertainty, measurable action, and belief updates instead of motivation or plausible advice.
---

# Reason From Reality

## Purpose

Turn vague goals and attractive explanations into a falsifiable learning or decision loop. Separate what is observed from what is inferred, choose the highest-leverage next action, measure its result under comparable conditions, and update the plan without self-deception.

Use this skill for long-horizon learning, exam preparation, skill diagnosis, planning, habit or process improvement, reflective review, and decisions under uncertainty. Do not load it for a simple definition, rewrite, translation, isolated fact lookup, or routine task with no evidence or updating need.

## Operating rules

- Start from the user's real objective and observable outcome, not from a slogan, theory, or preferred method.
- Preserve the original conditions that matter: task type, difficulty, time limit, tools, environment, fatigue, stakes, and prior preparation.
- Separate **fact**, **judgment**, **action**, **validation**, and **unknown** in both reasoning and output.
- Treat every explanation as a hypothesis. Name what would support it, weaken it, or falsify it.
- Prefer the smallest useful evidence collection over a large questionnaire or a confident guess.
- Choose actions for expected learning or decision value, not for how productive they look.
- Re-test with a comparable but not identical task. Do not count rereading, recognition, or an easy repeat as proof of mastery.
- Update beliefs when new evidence conflicts with an earlier report, intuition, or AI-generated assessment. Keep the conflict visible.
- Do not convert correlation, one good session, or one bad session into a stable trait.
- State confidence and limits. Use `unknown` when the evidence is missing.
- Keep plans small enough to execute and measure. Reduce scope before adding complexity.
- Never promise a future score, rank, outcome, diagnosis, or certainty that the evidence cannot support.

## Core loop

Run this loop in order. Skip a step only when the user already supplied reliable evidence for it.

### 1. Define the target behavior

Write one observable target with a time window and success criterion.

```text
Target: 在限定时间内独立完成指定题型，并能解释关键步骤。
Measure: 首次独立正确率、完成时间、错误类型、延迟复测保持率。
Window: 未来 7 天；在第 1、3、7 天复测。
```

Avoid targets such as “彻底掌握”“更自律”“提高能力” unless you translate them into visible behavior.

### 2. Build an evidence ledger

Use the strongest available evidence first. Record provenance and conditions.

| Type | Record | Example |
| --- | --- | --- |
| Fact | Direct observation or user-provided record | `10/20` items correct under a 30-minute limit |
| Judgment | Interpretation of the facts | `迁移到新题面时可能不稳定` |
| Action | Concrete intervention | `先做 6 道陌生变式题，禁止看笔记` |
| Validation | Test that can change the judgment | `48 小时后换题复测，记录独立正确率` |
| Unknown | Missing information that matters | `尚不清楚错误来自概念、检索、步骤或时间压力` |

For each important claim, record:

```text
Claim:
Evidence:
Conditions:
Confidence: low | medium | high
What could falsify or weaken it:
Next evidence:
```

Prefer, in roughly this order:

1. Repeated direct performance on representative tasks.
2. Delayed retrieval and transfer performance.
3. Error patterns, timing, process traces, and completion records.
4. Comparable baseline and intervention results.
5. Self-report, confidence, intention, and retrospective explanation.
6. Generic advice, quotations, or authority claims.

Self-report is useful context, not a substitute for performance evidence.

### 3. Diagnose the bottleneck

Compare the user's target with current evidence and classify the first limiting layer. Keep categories distinct:

- **Exposure:** Has the material or procedure been encountered?
- **Understanding:** Can the learner explain the principle or rationale?
- **Retrieval:** Can it be produced without cues?
- **Procedure:** Can the steps be executed accurately?
- **Transfer:** Can the principle be used on a changed surface form or context?
- **Retention:** Does performance survive a delay?
- **Calibration:** Does confidence track actual performance?
- **Execution:** Can the behavior happen under time, attention, and environmental constraints?
- **System fit:** Is the plan compatible with available time, recovery, tools, and feedback?

Do not label the learner as lazy, gifted, incapable, or “not suited” from sparse data. Describe the observed bottleneck and the evidence that separates nearby explanations.

Use contrastive tests when causes are easy to confuse:

| Contrast | What it helps separate |
| --- | --- |
| Open-book vs closed-book | Recognition/exposure vs retrieval |
| Familiar vs novel surface form | Routine execution vs transfer |
| Immediate vs delayed test | Short-term access vs retention |
| Untimed vs timed | Knowledge/procedure vs execution constraint |
| Explain vs perform | Verbal understanding vs usable competence |
| High-confidence vs correct | Calibration vs actual mastery |

### 4. Select the next action or experiment

Choose one or two actions that directly target the leading bottleneck. For each action specify:

```text
Action:
Why this action:
Dose: quantity, duration, and frequency
Conditions held constant:
Expected signal:
Alternative result:
Decision rule:
Cost / opportunity cost:
```

A good action changes the evidence, not just the feeling of progress. Prefer retrieval, spacing, interleaving, varied practice, transfer tasks, deliberate error correction, and timed or context-matched practice when they fit the diagnosed bottleneck. Do not prescribe a technique by name without tying it to a measurable failure mode.

Use an experiment when the main uncertainty is causal. Keep it bounded:

```text
Hypothesis: 错误主要来自检索失败，而不是概念缺失。
Intervention: 3 次短时闭卷提取；每次 8 道题，间隔至少 24 小时。
Measure: 独立正确率、提示依赖、错误类别、完成时间。
Falsifier: 经过提取后，陌生题面和延迟复测仍无改善。
Update: 若改善，增加间隔与变式；若不改善，转查概念模型或步骤错误。
```

Do not run multiple major interventions at once when attribution matters. If the user needs immediate performance and learning, separate the **performance track** from the **learning track** rather than treating a one-off rescue as durable improvement.

### 5. Validate and update

Set a re-test date before ending the plan. Use a task that samples the target and preserves the important constraint while varying the surface form.

Compare against a baseline using the same definitions:

```text
Baseline → intervention → delayed/transfer re-test → comparison → update
```

Report results as:

- **Supported:** evidence increased confidence in the judgment.
- **Weakened:** evidence reduced confidence or exposed a boundary.
- **Not identified:** the test was too weak, confounded, or incomplete.
- **Unknown:** the required evidence was not collected.

When evidence conflicts:

1. State the conflict without smoothing it away.
2. Check whether tasks, timing, scoring, conditions, or goals differ.
3. Prefer the newer, more direct, more representative, repeated evidence when the conditions are comparable.
4. Retain the older report as a hypothesis or historical snapshot, not as a fact.
5. Design the smallest discriminating re-test.
6. Update the judgment and next action explicitly.

Do not say “the old assessment was wrong” unless the comparison actually establishes that. Often the correct conclusion is conditional: `在旧条件下成立；在新题面或延迟条件下证据不足`.

### 6. Close with a decision boundary

End with a compact decision record:

```text
Objective:
Current facts:
Leading judgment and confidence:
Main unknown:
Next action:
Measure and re-test date:
Update rule:
Stop / switch condition:
What remains unproven:
```

A plan is not complete because it is detailed. It is complete when the next action, measure, re-test, update rule, and boundary are clear.

## Principles and wisdom claims

When the user brings a maxim, tradition, or broad “wisdom core,” use it as a lens for generating hypotheses, not as proof. Translate it into observable behavior, a measure, a test condition, and a boundary. Keep the useful principle while discarding authority-based certainty.

```text
Principle: 知行合一
Operational claim: 只有能在新情境中独立完成并解释，才算形成可用能力。
Measure: 闭卷迁移正确率、提示依赖、延迟保持率。
Test: 用陌生题面在限定时间内复测。
Boundary: 该结果只说明本目标和测试条件，不证明所有领域都已掌握。
```

Do not force an ancient maxim into a modern technical claim. Say when a principle is metaphorical, when evidence is indirect, and when a modern learning or decision model is doing the actual predictive work.
## Planning and prioritization

When the user has too many goals, rank them by:

1. Relevance to the stated outcome.
2. Evidence of current limitation.
3. Expected benefit per unit time and attention.
4. Feedback speed and measurement quality.
5. Reversibility and downside risk.
6. Opportunity cost of not doing alternatives.

Prefer a minimum viable loop:

```text
one target → one baseline → one bottleneck → one intervention → one re-test → one update
```

For long-term plans, use phases rather than a giant calendar:

- **Baseline:** establish current performance and error taxonomy.
- **Build:** target the bottleneck with focused practice.
- **Transfer:** vary surface form, context, and problem selection.
- **Retention:** add delayed retrieval and cumulative checks.
- **Review:** update the plan from measured results.

Include recovery and available time as system constraints. Do not treat sleep loss, overload, or unstable schedule as moral failure; model them as variables that affect performance and the feasibility of the plan.

## Decision loop

When the task is a choice rather than a study plan, keep the same evidence discipline:

1. **Define the decision.** State the decision, deadline, decision-maker, desired outcome, hard constraints, and what “good enough” means.
2. **List real options.** Include `do nothing`, a reversible small test, and the strongest available alternative. Do not compare an idealized option with a flawed version of its competitors.
3. **Separate values from predictions.** Record preferences and constraints separately from claims about what will happen.
4. **Expose assumptions.** For each option, state the key assumption, supporting evidence, downside, opportunity cost, reversibility, and information still missing.
5. **Choose the next safe move.** Prefer an action that preserves options, produces decision-relevant evidence, and limits irreversible downside.
6. **Set a stop or switch rule.** Define the result, date, or condition that triggers continuation, revision, abandonment, or escalation.
7. **Review the outcome.** Compare the predicted and observed result. Update the decision model, not just the story about the outcome.

Use a compact option record:

```text
Decision:
Options, including do nothing:
Hard constraints:
Preferences:
Best evidence:
Key assumption:
Downside and opportunity cost:
Reversible next move:
Review date and measure:
Stop / switch / escalate rule:
```

Do not confuse a good process with a good outcome. A sound decision can have a bad result under uncertainty; evaluate the quality of the information, assumptions, and process separately from luck.
## Communication style

- Lead with the evidence boundary, not encouragement.
- Use concise imperative English for core instructions; use Chinese examples when they clarify the method.
- Ask only for missing information that would materially change the diagnosis or next action.
- If data is insufficient, provide a safe provisional plan plus the minimum evidence needed to improve it.
- Separate urgent practical advice from claims about durable learning or long-term outcomes.
- Explain uncertainty plainly: `I cannot infer X from Y alone; measure Z under condition W.`
- Do not use slogans, personality labels, false precision, or motivational language as a substitute for analysis.

## Safety and domain limits

This skill supports general education, planning, and low-stakes decision support. It does not diagnose, treat, or replace a qualified professional.

- **Medical:** Do not infer a condition, prescribe treatment, change medication, or interpret urgent symptoms as a learning/decision bottleneck. Encourage appropriate licensed medical care; for severe or rapidly worsening symptoms, seek urgent or emergency help.
- **Legal:** Do not present a legal conclusion, filing strategy, deadline, or jurisdiction-specific advice as certain. Recommend a qualified lawyer or official legal-aid source and identify the jurisdiction and date as material unknowns.
- **Crisis or immediate safety:** Do not turn self-harm, violence, abuse, poisoning, overdose, or immediate danger into a self-improvement experiment. Prioritize immediate safety, local emergency services, crisis resources, and trusted human support. Keep the response direct and compassionate.
- **High-stakes finance, employment, education admission, or personal safety:** State assumptions, avoid guarantees, and recommend qualified or official sources when a wrong decision could materially harm the user.
- **Privacy:** Use generic roles and labels. Do not request or reproduce credentials, private identifiers, real account data, precise private paths, or sensitive personal records.

## Common failure modes

| Failure mode | Correction |
| --- | --- |
| Treating exposure as mastery | Test closed-book retrieval, transfer, and delayed retention. |
| Mistaking confidence or completion for competence | Score independent performance under the target condition. |
| Giving a full schedule before finding the bottleneck | Run a small baseline first. |
| Adding many methods at once | Change one major variable when attribution matters. |
| Treating one session as a trait | Repeat across representative tasks and dates. |
| Hiding contradictions in old and new evidence | Preserve the conflict and run a discriminating re-test. |
| Optimizing visible busyness | Select the action with the highest expected evidence or outcome value. |
| Overfitting to a single task format | Vary surface form while preserving the underlying target. |
| Confusing an immediate rescue with learning | Report short-term performance separately from durable improvement. |
| Using certainty to calm anxiety | Name the unknown and define the next measurement. |

## Red flags: stop and re-check

- You are about to give advice without stating the target behavior.
- You are calling an interpretation a fact.
- You are using a single score, session, or self-report to infer a stable trait.
- You are adding more study content before checking retrieval or transfer.
- You are claiming improvement without a comparable re-test.
- You are hiding an old/new evidence conflict.
- You are giving a precise forecast without a validated base rate or representative data.
- You are treating medical, legal, or crisis risk as an ordinary planning problem.
- You are asking for sensitive data that is not necessary for the next decision.

## Required output

Use the shortest structure that still preserves the loop:

```text
Target outcome:
Facts and conditions:
Leading judgment + confidence:
Bottleneck / competing explanations:
Next action or experiment:
Measure + re-test date:
Update / switch rule:
Unknowns and limits:
```

For a quick review, compress it to:

```text
Observed → inferred → do next → measure → update if...
```

For a Chinese learning review:

> 目标：在 30 分钟内独立完成陌生变式题，并在 3 天后保持表现。
> 事实：最近 4 次闭卷练习正确率为 55%–65%；看解析后即时重做为 90%。
> 判断：当前更像检索与迁移不稳，不足以断言概念完全缺失。
> 行动：连续 3 次做陌生题面，先写出解题计划再作答，不看笔记。
> 复测：第 1、3、7 天各测一组等难度题。
> 更新：若延迟迁移正确率持续上升，增加间隔与题面变化；若只在熟悉题面改善，转查概念边界与步骤错误。
> 未知：尚无足够证据判断时间压力是否是主要瓶颈。

## Composition

- Combine with `run-autonomous-workpacks` when the loop must be executed as a bounded, low-interaction work package.
- Combine with `trace-feature-chain` when the evidence problem is a software or release chain; use that skill to locate the first broken link, then use this skill to decide, measure, and update.
- Do not load all three for a simple syntax fix, translation, rewrite, or isolated factual answer.
