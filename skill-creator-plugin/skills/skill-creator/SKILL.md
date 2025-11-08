---
name: skill-creator
description: Use when creating new skills, editing existing skills, or improving skill documentation. Applies Test-Driven Development to process documentation - run baseline tests without the skill first, then write minimal skill addressing failures. Mentions of skill files, SKILL.md, skill testing, or skill improvement trigger this.
---

# Skill Creator

Writing skills IS Test-Driven Development applied to process documentation.

Skills are reusable reference guides that teach Claude how to perform specific tasks. This skill helps you create or edit skills using a test-driven approach.

## The Iron Law

**No skill deploys without a failing test first.** This applies to both new skills and edits to existing skills.

If you didn't watch an agent fail without the skill, you don't know if the skill teaches the right thing.

## Instructions

Follow the RED-GREEN-REFACTOR cycle when creating or editing skills:

### RED: Run Baseline Tests Without the Skill

Before writing or editing ANY skill:

1. **Identify test scenarios**: What specific tasks should this skill help with?
2. **Run baseline tests**: Test Claude WITHOUT the skill (or with the old version)
3. **Document failures**: Record exactly how Claude fails, what it misses, or what it does wrong
4. **Capture natural behavior**: Note rationalizations, workarounds, or shortcuts Claude attempts

Ask yourself:
- What specific errors or mistakes happen without this skill?
- What does Claude try to do instead?
- What shortcuts does Claude rationalize?
- What edge cases does Claude miss?

**This is not optional.** If you skip baseline testing, you're guessing what to teach.

### GREEN: Write Minimal Skill Addressing Failures

Now write (or edit) the skill to address the specific failures you observed:

#### 1. Gather Requirements

For NEW skills, ask about:
- **Skill name**: What should the skill be called?
  - Must use lowercase letters, numbers, and hyphens only
  - Maximum 64 characters
  - Example: `pdf-processor`, `commit-helper`, `code-reviewer`

- **Location**: Where should the skill be created?
  - Personal skill: `~/.claude/skills/skill-name/`
  - Project skill: `.claude/skills/skill-name/`
  - Plugin skill: `plugin-name/skills/skill-name/`

For EDITING existing skills:
- What specific failures did baseline testing reveal?
- What new scenarios need coverage?
- What loopholes appeared during testing?

#### 2. Write the Description

The description is critical for discovery. Write it to match how Claude would search:

**Format**: Start with "Use when..." and include specific triggers

**Optimize for search**:
- Include concrete symptoms and error messages
- Mention specific tools or commands
- Use problem-focused language, not technology names
- Include keywords users would actually say

**Good example**:
```
Use when creating skills, editing SKILL.md files, or improving skill documentation.
Applies Test-Driven Development to process documentation. Mentions of failing tests,
baseline scenarios, skill validation, or skill improvement trigger this.
```

**Poor example**:
```
Helps with skill development and documentation.
```

#### 3. Validate Inputs

Before creating the skill, validate:
- Name uses only lowercase letters, numbers, and hyphens
- Name is under 64 characters
- Description is under 1024 characters
- Description includes both what the skill does AND when to use it
- Location path is valid and accessible

#### 4. Create Directory Structure

```bash
# For personal skills
mkdir -p ~/.claude/skills/skill-name

# For project skills
mkdir -p .claude/skills/skill-name

# For plugin skills
mkdir -p plugin-name/skills/skill-name
```

#### 5. Write the SKILL.md Content

**YAML Frontmatter** (required):
```yaml
---
name: skill-name
description: Use when [trigger]. [What it does]. [When to use specifics].
# Optional: restrict tool access
# allowed-tools: Read, Grep, Glob
---
```

**Content Structure** - Address the failures you observed:

```markdown
# Skill Name

Brief statement of purpose.

## Instructions

Write instructions that directly counter the failures from your baseline tests:

1. If Claude skipped validation → Add explicit validation step
2. If Claude rationalized shortcuts → List those rationalizations as anti-patterns
3. If Claude missed edge cases → Call out those edge cases explicitly
4. If Claude used wrong approach → Show the correct approach

Be specific. Reference the actual failures you saw.

## Examples

**One excellent example beats three mediocre ones.**

Show a concrete example that demonstrates the correct behavior:
- Use realistic code/data
- Show expected output
- Highlight what makes this correct

## Anti-Patterns (for discipline skills)

If this skill enforces discipline, explicitly list rationalizations to reject:

**Red Flags**:
- "This is a simple case, so I'll skip..."
- "The user didn't explicitly ask for..."
- "I can optimize by..."

**Why these fail**: [Explain the consequences]

## Requirements

If external dependencies are needed:
- List required packages
- Note installation requirements
- Specify version constraints if critical
```

**Organization tip**: Keep content inline unless you have 100+ lines of reference material or reusable tools. Progressive disclosure via supporting files is good, but most skills should be self-contained.

#### 6. Create Supporting Files (if needed)

Only create supporting files for:
- **Heavy reference** (100+ lines): API docs, extensive tables, detailed specs
- **Reusable tools**: Scripts that multiple skills could use
- **Not needed**: Examples, brief guidance, troubleshooting

Organize like this:
```
skill-name/
├── SKILL.md (required, self-contained)
├── reference.md (only if 100+ lines)
└── scripts/
    └── helper.py (only if reusable)
```

### REFACTOR: Close Loopholes Through Testing

After writing/editing the skill, test it to find loopholes:

#### 1. Test with the Skill Active

Run the same scenarios from your baseline tests, but now WITH the skill:
- Does Claude follow the instructions?
- Does Claude still find rationalizations?
- Are there new ways to skip steps?

#### 2. Identify New Rationalizations

Watch for:
- "I can skip X because..."
- "This scenario is different because..."
- "The user probably meant..."

These are loopholes. Add them to your Anti-Patterns section.

#### 3. Test Variations

Try different phrasings, contexts, and edge cases:
- Does it work under pressure (multiple competing priorities)?
- Does it work with ambiguous requirements?
- Does it work when the easy path is tempting?

#### 4. Iterate

Update the skill to close loopholes:
- Add explicit counters to new rationalizations
- Strengthen language around discipline requirements
- Add examples showing the loophole scenarios

**Repeat RED-GREEN-REFACTOR until the skill reliably prevents failures.**

### Skill Testing Checklist

Before deploying a new or edited skill:

**RED Phase**:
- [ ] Identified 3+ realistic test scenarios
- [ ] Ran baseline tests WITHOUT the skill
- [ ] Documented specific failures and rationalizations
- [ ] Captured what Claude tried to do instead

**GREEN Phase**:
- [ ] YAML frontmatter is valid (name, description)
- [ ] Description starts with "Use when..."
- [ ] Description includes search-optimized triggers
- [ ] Instructions directly address observed failures
- [ ] Included one excellent example (not multiple mediocre ones)
- [ ] Added Anti-Patterns section (for discipline skills)
- [ ] Content is self-contained (minimal supporting files)

**REFACTOR Phase**:
- [ ] Tested WITH the skill active
- [ ] Identified new rationalizations or loopholes
- [ ] Updated skill to close loopholes
- [ ] Tested variations and edge cases
- [ ] Skill reliably prevents the original failures

## Examples

### Example 1: Discipline Skill with TDD

**RED Phase** - Baseline failures observed:
- Claude analyzed logs but missed correlating errors across files
- Claude skipped checking timestamps for patterns
- Claude gave surface-level analysis without root cause investigation

**GREEN Phase** - Skill addressing failures:

```yaml
---
name: log-analyzer
description: Use when debugging application errors, investigating log files, or analyzing system failures. Correlates errors across multiple files, identifies patterns over time, and suggests root causes. Mentions of logs, errors, stack traces, or debugging trigger this.
allowed-tools: Read, Grep, Glob
---

# Log Analyzer

Analyze application logs systematically to identify root causes, not just symptoms.

## Instructions

1. **Find all relevant logs**: Use Glob to find log files matching the timeframe
2. **Extract error context**: Use Grep with -C 5 to get surrounding context
3. **Build timeline**: Sort errors chronologically across ALL files
4. **Correlate patterns**: Look for errors that occur together
5. **Identify root cause**: Trace back to the first error in the sequence
6. **Summarize findings**: Include timestamps, affected components, and likely cause

## Example

```bash
# Find all logs from the last hour
glob "**/*.log"

# Search for errors with context
grep -C 5 "ERROR|FATAL|Exception" app.log

# Check timestamps across files
grep "2025-11-07 14:" *.log | sort
```

Expected output:
```
14:23:45 database.log: Connection timeout
14:23:47 app.log: ERROR: Failed to fetch user data
14:23:48 api.log: Exception: Database unavailable
```

Root cause: Database connection timeout cascaded to application and API errors.

## Anti-Patterns

**Red Flags**:
- "I found an error in app.log" ← Did you check other logs?
- "There are multiple ERROR entries" ← What's the root cause?
- "The logs show issues" ← What's the timeline and correlation?

**Why these fail**: Surface-level analysis misses the actual problem and wastes debugging time.
```

**REFACTOR Phase** - Loopholes closed:
- Added explicit correlation requirement
- Added timeline sorting step
- Added Anti-Patterns section to prevent shallow analysis

### Example 2: Editing an Existing Skill

**Scenario**: The `database-migration` skill exists but users reported it doesn't enforce testing rollbacks.

**RED Phase** - Test WITHOUT the rollback requirement:
- Claude created migrations with up/down scripts
- Claude skipped actually testing the rollback
- Claude rationalized: "The down migration looks correct"

**GREEN Phase** - Edit the skill to address failures:

```yaml
---
name: database-migration
description: Use when creating database migrations, schema changes, or rollback scripts. Enforces testing both up AND down migrations before deployment. Mentions of migrations, schema changes, or database updates trigger this.
---

# Database Migration Helper

Create safe, reversible database migrations with tested rollbacks.

## Instructions

1. Analyze the schema change needed
2. Generate migration file with timestamp
3. Write BOTH up and down migrations
4. **Test the up migration** on a test database
5. **Test the down migration** to verify rollback works
6. Document any data transformations or breaking changes

## Example

```sql
-- Up migration
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email VARCHAR(255) UNIQUE NOT NULL
);

-- Down migration
DROP TABLE users;
```

**Testing sequence**:
```bash
# Test up
psql test_db -f migrations/001_up.sql
# Verify schema exists

# Test down
psql test_db -f migrations/001_down.sql
# Verify schema is gone
```

## Anti-Patterns

**Red Flags**:
- "The down migration looks correct" ← Did you actually test it?
- "I'll skip testing since this is simple" ← Simple migrations can still break
- "Testing rollback isn't needed for this change" ← It's always needed

**Why these fail**: Untested rollbacks fail in production when you need them most.
```

**REFACTOR Phase**:
- Added explicit testing steps (not just writing)
- Added Anti-Patterns for the rationalization we observed
- Changed description to emphasize enforcement of testing

## Validation Quick Reference

### Name Format
- Lowercase letters, numbers, hyphens only: `^[a-z0-9-]+$`
- Maximum 64 characters
- Examples: `log-analyzer`, `pdf-processor`, `commit-helper`

### Description Format
- Start with "Use when..."
- Include specific triggers (error messages, tool names, symptoms)
- Maximum 1024 characters
- Optimize for how Claude would search

### YAML Frontmatter
```yaml
---
name: skill-name
description: Use when [trigger]. [What it does]. [Specifics].
# Optional
# allowed-tools: Read, Grep, Glob
---
```

### Common Mistakes

**Skipping baseline tests** → You're guessing what to teach
- Fix: Always run RED phase first

**Vague descriptions** → Skill won't activate when needed
- Bad: "Helps with data"
- Good: "Use when analyzing CSV files, detecting outliers, or generating statistics from spreadsheet data."

**Missing Anti-Patterns** → Claude will find rationalizations
- Fix: Add Red Flags section listing rationalizations you observed

**Too many supporting files** → Content should be self-contained
- Fix: Keep content in SKILL.md unless you have 100+ lines of reference

## Tool Restrictions

Use `allowed-tools` to limit scope and increase safety:

```yaml
# Read-only analysis
allowed-tools: Read, Grep, Glob

# Analysis with execution
allowed-tools: Read, Grep, Glob, Bash

# Minimal write access
allowed-tools: Read, Write, Glob
```

For detailed reference on validation rules, file organization, and troubleshooting, see [REFERENCE.md](REFERENCE.md).
