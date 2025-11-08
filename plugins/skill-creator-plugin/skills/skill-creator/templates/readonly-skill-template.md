---
name: skill-name
description: Use when [analyzing/investigating/reviewing] [specific thing]. Read-only analysis that finds [patterns/issues/metrics]. Mentions of [keywords], [error types], or [analysis needs] trigger this.
allowed-tools: Read, Grep, Glob
---

# Skill Name (Read-Only Analysis)

Brief statement of purpose - what does this analyze and why?

## Instructions

This is a read-only skill. Follow these steps to provide thorough analysis:

1. **Find all relevant files**: Use Glob to locate files matching the criteria
2. **Search for patterns**: Use Grep with context (-C flag) to find issues
3. **Read detailed content**: Use Read on specific files for deeper analysis
4. **Correlate findings**: Connect patterns across multiple files
5. **Summarize with evidence**: Provide findings with file paths and line numbers

## Example

```bash
# Find all relevant files
glob "**/*.log"

# Search with context
grep -C 5 "ERROR|WARN" application.log

# Read specific file for details
read config/settings.json
```

Expected analysis:
```
Found 3 ERROR entries in application.log:
- Line 42: Database connection timeout
- Line 156: Failed authentication attempt
- Line 289: Memory allocation error

Root cause: Database connection timeout at line 42 triggered cascade of errors.
Recommendation: Investigate database connection pool settings.
```

## Anti-Patterns

**Red Flags**:
- "I found some errors" ← Where? Which files? What lines?
- "The logs show issues" ← What specific issues? How do they correlate?
- "I'll just check one file" ← Did you search all relevant files?

**Why these fail**: Incomplete analysis misses context and root causes.

## Tool Restrictions

This skill is read-only by design:
- ✓ Can: Read files, search content, find patterns
- ✗ Cannot: Modify files, execute commands, write files

If modifications are needed, recommend creating a separate skill or getting user permission.
