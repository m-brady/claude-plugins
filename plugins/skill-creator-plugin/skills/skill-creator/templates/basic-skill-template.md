---
name: skill-name
description: Use when [specific trigger]. [What it does]. [When to use specifics]. Mentions of [keywords], [error messages], or [tools] trigger this.
---

# Skill Name

Brief statement of purpose - what problem does this solve?

## Instructions

Write instructions that address the specific failures you observed in baseline testing:

1. **First critical step** - Counter the first observed failure
2. **Second critical step** - Address the rationalization you saw
3. **Third critical step** - Handle the edge case that was missed
4. **Final step** - Ensure clear, actionable output

Be specific. Reference actual behaviors you want to change.

## Example

**One excellent example beats three mediocre ones.**

```bash
# Show a realistic, concrete example
command --with-real-options actual-file.txt

# Show what happens
```

Expected output:
```
Show the exact result with explanation of what makes this correct
```

## Anti-Patterns

**Red Flags** (rationalizations to reject):
- "This is simple, so I'll skip..." ← Why this fails
- "The user didn't explicitly ask for..." ← Why this fails
- "I can optimize by skipping..." ← Why this fails

**Why these fail**: Explain the consequences of taking shortcuts

## Requirements

If external dependencies are needed:
- Required packages: `pip install package1 package2`
- Version constraints (if critical): `package1>=2.0.0`
- System requirements: OS, tools, configurations
