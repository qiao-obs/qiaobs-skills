# `reason-from-reality`: Let Evidence Revise the Plan

> 10-second definition: Turn long-term learning, planning, diagnosis, or uncertain decisions into a loop of observable targets, evidence, action, measurement, re-testing, and updates.

- [简体中文说明](reason-from-reality.zh-CN.md)
- [Execution entrypoint](../../skills/reason-from-reality/SKILL.md)

## The expensive failure mode it addresses

A plan can sound complete while leaving the decisive questions unanswered: What behavior is the target? What does current performance show? Which bottleneck is first? What action will test the explanation? When will the result change the plan?

Learning adds a common trap: exposure is treated as mastery, immediate rework as durable learning, and one good session as a stable capability. Decision-making adds another: a polished explanation is protected from evidence that contradicts it.

This Skill also makes “civilization-level wisdom core” operational rather than mystical. Cross-tradition principles must become observable behaviors, measures, experiments, and boundaries. Reality, logic, practice, outcomes, and re-tests outrank slogans, authority, old reports, and the agent’s own confidence.

## Use it / do not use it

Use it for long-term study, exam preparation, capability diagnosis, plan review, habit or process improvement, reflection, and decisions under uncertainty.

Do not load it for a one-off fact, translation, rewrite, title suggestion, isolated syntax fix, or routine task with no meaningful measurement or update.

Medical, legal, crisis, major financial, employment, admission, and personal-safety questions are not ordinary optimization problems. Follow the [safety and domain boundaries](../../skills/reason-from-reality/references/safety-and-domain-boundaries.md) and use an appropriate professional or official source.

## What the civilization-level core means

“Civilization-level” means extracting reusable patterns across traditions and historical settings. It does not mean omniscience, moral superiority, a sacred canon, or allegiance to any era, country, school, thinker, or author.

“Wisdom core” means translating a principle into:

```text
principle → observable behavior → measure → small experiment → boundary → update rule
```

Prior AI output is an auditable judgment, not a source of new facts. Missing evidence stays `UNKNOWN`. AI can explain, generate practice, give feedback, and schedule tests, but it should not replace the learner’s own retrieval, derivation, writing, problem solving, or programming when those capabilities are the target.

## Core loop

```text
Goal → reality → gap → main bottleneck → action
→ measure → transfer/delayed re-test → update
```

### 1. Define the target behavior

Translate “mastery,” “discipline,” or “improvement” into a task, conditions, time window, and success criterion:

```text
Target: complete unfamiliar variants independently in 30 minutes and explain the key steps
Measures: first-pass accuracy, time, error type, delayed retention
Window: seven days; re-test on days 1, 3, and 7
```

### 2. Build an evidence ledger

Separate every important statement into:

- **FACT:** direct observation and conditions;
- **JUDGMENT:** interpretation and confidence;
- **ACTION:** a concrete intervention;
- **VALIDATION:** a test that can change the judgment;
- **UNKNOWN:** missing information that matters.

Confidence, intention, and self-report are context, not substitutes for representative performance.

### 3. Diagnose the first bottleneck

Keep exposure, understanding, retrieval, procedure, transfer, retention, environment, and energy/motivation distinct. Do not infer a stable trait from one score or session, and do not generate a complete schedule before checking the bottleneck.

### 4. Choose a small action or experiment

Select one main variable when attribution matters. Define the behavior, condition, duration, data record, and stop/switch rule. Choose the action for expected evidence or target-value, not for visible busyness.

### 5. Measure immediate, transfer, and delayed performance

These layers are not interchangeable:

```text
exposure → explanation → cue-free retrieval → procedure
→ transfer to a changed surface → delayed retention
```

Immediate rework after seeing a solution is partial evidence. Re-test on a comparable but not identical task at a meaningful delay.

### 6. Update, switch, or stop

- If the target improves on immediate and delayed/transfer tests, keep the method and vary the surface gradually.
- If only immediate performance improves, reduce recognition cues and add cue-free, varied retrieval.
- If the measure does not move after a bounded trial, revisit the bottleneck or change one main variable.
- If risk or uncertainty exceeds the evidence, stop ordinary optimization and escalate to the appropriate source.

## Inputs and outputs

Inputs:

- target outcome and target behavior;
- practice or work records with conditions and timing;
- current performance, error patterns, process traces, and self-report;
- available time, resources, and risk boundaries;
- a re-test date and decision rules.

Output:

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

## Complete anonymized case

A learner reported, “I follow the explanation but cannot solve an unfamiliar version.” Four recent closed-book attempts were 55–65% correct, while immediate rework after viewing the solution reached 90%.

An ordinary response might add more explanations, increase volume, or use encouragement to cover uncertainty. This Skill separates understanding from independent performance, treats retrieval/transfer instability as a leading but medium-confidence judgment, and proposes a small experiment: unfamiliar variants without notes, a written solution plan, error-type logging, and day-1, day-3, and day-7 re-tests on changed surfaces.

If delayed transfer improves, vary the surface gradually. If only familiar forms improve, investigate concept boundaries and procedural errors. These numbers are an anonymized example, not universal thresholds or an outcome promise.

## Ordinary handling versus this Skill

| Ordinary handling | With `reason-from-reality` |
| --- | --- |
| Treat “I understand” as mastery | Separate confidence, immediate performance, transfer, and delay |
| Generate a complete schedule first | Run a small baseline and find the first bottleneck |
| Change many methods at once | Change one major variable when attribution matters |
| Treat an old AI report as fact | Preserve the conflict and audit it against current evidence |
| Use reassurance to remove uncertainty | Mark `UNKNOWN` and choose the next discriminating measure |

## Three copyable prompts

1. “Use my closed-book practice records to distinguish exposure, understanding, retrieval, procedure, transfer, and delayed retention. Separate fact, judgment, action, validation, and unknown; design a small test before a full schedule.”
2. “An old AI assessment says the bottleneck is missing concepts, but recent independent performance disagrees. Preserve the conflict, list competing explanations, and design the smallest re-test that separates them.”
3. “Translate ‘learn by doing’ into observable behavior, measures, an experiment, boundaries, a re-test date, and update rules. Do not use quotations as evidence.”

## Typical output fragment

```text
Target outcome: complete unfamiliar variants independently in 30 minutes and retain the skill on day 3
Facts: four closed-book attempts at 55–65%; immediate assisted rework at 90%
Judgment + confidence: retrieval/transfer instability is more likely; medium confidence
Next experiment: unfamiliar surfaces without notes; record time and error type
Re-tests: days 1, 3, and 7
Update: if delayed transfer stays flat, inspect concept boundaries and procedure
Unknown: whether time pressure is the dominant bottleneck
```

## Boundaries, anti-patterns, and failure conditions

- Do not present history or philosophy as unquestionable authority.
- Do not invent quotations, research outcomes, or precise universal thresholds.
- Do not turn one session, confidence, or self-report into a stable trait.
- Do not let AI replace the capability the user is trying to form.
- Do not request unnecessary private records.
- Do not continue ordinary optimization inside medical, legal, crisis, or other high-stakes boundaries.
- Do not fill `unknown` with a comforting guess.

## How to combine it

- Pair with `run-autonomous-workpacks`: this Skill defines the judgment, measures, experiments, and update rules; workpacks execute them within authorization.
- Pair with `trace-feature-chain`: trace the first software/release mismatch first, then use this Skill to choose and update the intervention.
- Do not load all three for a simple fact, translation, rewrite, or syntax fix.

## FAQ

**Why not give a full study plan immediately?** Without a target behavior, baseline, conditions, and bottleneck, a plan can be elaborate but untestable.

**Is “civilization-level” an exaggeration?** It is if treated as a universal knowledge base. Here it means cross-tradition principles are operationalized, measured, and rejected when reality does not support them.

**Can AI learn for me?** AI can explain, generate practice, check work, and schedule tests. The learner still needs to perform the target retrieval, derivation, writing, problem solving, or programming.

**When should ordinary optimization stop?** When the question enters a medical, legal, crisis, major financial, employment, admission, or personal-safety boundary, or when evidence cannot support the next action.
