# Skill engineering notes

**Research checked:** 2026-08-21 (UTC+08:00)

## Sources and adopted patterns

- [OpenAI Build Skills](https://learn.chatgpt.com/docs/build-skills): keep skills discoverable through concise metadata and package the smallest reusable instruction unit.
- [OpenAI Skill Evals](https://developers.openai.com/blog/eval-skills): evaluate triggering and behavior with realistic prompts instead of relying only on syntax checks.
- [Agent Skills specification](https://agentskills.io/specification): use a directory with `SKILL.md`, valid frontmatter, and progressive disclosure through referenced resources.
- [Agent Skills best practices](https://agentskills.io/skill-creation/best-practices): make descriptions precise, keep core instructions concise, and place specialist detail in references.
- [Anthropic Agent Skills engineering](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills): treat skills as composable instruction packages that load only when useful.
- [Vercel skills](https://github.com/vercel-labs/skills): preserve a discoverable repository layout and explicit installation examples.
- [obra/superpowers](https://github.com/obra/superpowers): use workflow stages, explicit handoffs, and verification as design patterns; do not copy its text or claim association.
- [anthropics/skills](https://github.com/anthropics/skills): use self-contained skill folders with references and practical examples; do not copy implementation text.
- [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills), [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills), [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills), [trailofbits/skills](https://github.com/trailofbits/skills): compare focused descriptions, reusable references, and validation-oriented repository structure.
- [Microsoft SkillOpt](https://www.microsoft.com/en-us/research/blog/skillopt-agent-skills-as-trainable-parameters/): preserve held-out evaluation as a useful improvement principle; this repository does not run model optimization in public CI.

## Adopted

1. Each Skill is a coherent unit with a narrow trigger boundary.
2. Metadata supports discovery; `SKILL.md` contains the always-needed workflow; references hold conditional depth.
3. Instructions are evidence-first and authorization-aware.
4. Trigger datasets use realistic near-neighbor negatives.
5. Static checks fail closed on missing, duplicate, unfinished, private, or inconsistent artifacts.
6. CI is deterministic and does not spend paid model calls.

## Deliberately not adopted

- No claims about star counts, popularity, superiority, or third-party endorsement.
- No hidden network calls, telemetry, credential access, or automatic publication.
- No large copied excerpts from third-party skills or books.
- No unverified plugin manifest fields; the first release uses the standard `skills/` layout.
- No fabricated model-trigger rates, forward-test scores, CI results, or user acceptance.

## Evaluation contract

The JSON trigger sets are routing fixtures, not model results. `evals/scenario-rubrics.md` defines the scoring contract for independent forward tests. When a harness is available, record the actual run, model/harness version, date, prompts, outcomes, and artifacts under a versioned evidence file. Never replace missing evidence with a pass label.
