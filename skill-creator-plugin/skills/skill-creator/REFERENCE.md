# Skill Creator Reference

Comprehensive reference for creating Claude Code skills.

## Table of Contents

- [Validation Rules](#validation-rules)
- [YAML Frontmatter Specification](#yaml-frontmatter-specification)
- [Description Best Practices](#description-best-practices)
- [File Organization](#file-organization)
- [Tool Restrictions](#tool-restrictions)
- [Testing Skills](#testing-skills)

## Validation Rules

### Name Requirements

**Format**: `^[a-z0-9-]+$`

- Only lowercase letters (a-z)
- Numbers (0-9)
- Hyphens (-)
- No spaces, underscores, or special characters
- Maximum length: 64 characters

**Valid examples**:
- `pdf-processor`
- `commit-helper`
- `log-analyzer-2`
- `api-client-gen`

**Invalid examples**:
- `PDF_Processor` (uppercase and underscore)
- `commit helper` (space)
- `log.analyzer` (period)
- `api-client!` (special character)

### Description Requirements

**Length**: Maximum 1024 characters

**Must include**:
1. What the skill does (capabilities)
2. When to use it (triggers)
3. Key terms for discovery

**Structure**:
```
[What it does]. [When to use it]. [Optional: Requirements].
```

**Good example**:
```
Extract text and tables from PDF files, fill forms, merge documents.
Use when working with PDF files, forms, or document extraction.
Requires pypdf and pdfplumber packages.
```

**Poor example**:
```
Helps with documents.
```

### YAML Frontmatter Rules

**Structure**:
```yaml
---
name: skill-name
description: Skill description
allowed-tools: Tool1, Tool2, Tool3  # Optional
---
```

**Rules**:
- Must start with `---` on line 1
- Must end with `---` before content starts
- Use spaces, not tabs
- Required fields: `name`, `description`
- Optional fields: `allowed-tools`
- Follow YAML syntax strictly

**Common errors**:
```yaml
# Error: Missing opening ---
name: skill-name
---

# Error: Tab character instead of spaces
---
name:	skill-name  # <- Tab here
---

# Error: Unquoted string with special chars
---
description: It's a skill  # <- Apostrophe breaks YAML
---

# Fix: Quote strings with special chars
---
description: "It's a skill"
---
```

## YAML Frontmatter Specification

### Required Fields

#### name
- Type: String
- Format: `^[a-z0-9-]+$`
- Max length: 64 characters
- Must be unique within the skill directory

#### description
- Type: String
- Max length: 1024 characters
- Should be descriptive and include triggers

### Optional Fields

#### allowed-tools
- Type: String (comma-separated) or Array
- Valid tools: Read, Write, Edit, Glob, Grep, Bash, etc.
- Restricts which tools Claude can use with this skill

**String format**:
```yaml
allowed-tools: Read, Grep, Glob
```

**Array format**:
```yaml
allowed-tools:
  - Read
  - Grep
  - Glob
```

## Description Best Practices

### Include What and When

**Structure**: `[Capabilities]. [When to use]. [Requirements].`

### Use Specific Triggers

Include terms users would actually say:

**Good**:
- "working with Excel files"
- "analyzing log files"
- "creating API clients"
- "when the user mentions PDFs"

**Poor**:
- "for data"
- "helps with files"
- "general purpose"

### Examples by Domain

#### File Processing
```
Process and analyze [file type] files, [specific operations].
Use when working with [file extensions], [user terms], or [tasks].
```

#### Development Tools
```
[Action] for [technology/framework], [specific features].
Use when [development task], [user scenario], or [technical context].
```

#### Analysis Skills
```
Analyze [data type] for [patterns/metrics], [output format].
Use when [analysis task], [debugging scenario], or [investigation type].
```

## File Organization

### Basic Structure

```
skill-name/
└── SKILL.md (required)
```

### With Supporting Files

```
skill-name/
├── SKILL.md (required)
├── REFERENCE.md (optional - detailed docs)
├── EXAMPLES.md (optional - more examples)
├── scripts/
│   ├── helper.py
│   └── validator.js
└── templates/
    ├── template1.txt
    └── template2.md
```

### File Naming Conventions

- Use lowercase
- Use hyphens for spaces
- Use descriptive names
- Group by type in subdirectories

**Good**:
- `scripts/validate-input.py`
- `templates/api-client-template.ts`
- `docs/advanced-usage.md`

**Poor**:
- `Scripts/ValidateInput.py`
- `template.txt`
- `file1.md`

### Referencing Files

Use relative paths from SKILL.md:

```markdown
See [detailed documentation](REFERENCE.md).
For examples, check [EXAMPLES.md](EXAMPLES.md).

Run the helper:
```bash
python scripts/helper.py
```
```

## Tool Restrictions

Use `allowed-tools` to limit tool access for safety and focus.

### Common Patterns

#### Read-Only Skills
```yaml
allowed-tools: Read, Grep, Glob
```

Use for:
- Analysis tasks
- Log investigation
- Code review
- Documentation reading

#### Analysis with Execution
```yaml
allowed-tools: Read, Grep, Glob, Bash
```

Use for:
- Data analysis that needs computation
- Test execution
- Build analysis

#### Limited Write Access
```yaml
allowed-tools: Read, Write, Grep, Glob
```

Use for:
- Report generation
- Template expansion
- Safe file creation

### Available Tools

Common tools you can restrict to:
- **Read**: Read file contents
- **Write**: Create new files
- **Edit**: Modify existing files
- **Glob**: Find files by pattern
- **Grep**: Search file contents
- **Bash**: Execute shell commands
- **WebFetch**: Fetch web content
- **WebSearch**: Search the web

### When to Use Tool Restrictions

**Use restrictions when**:
- Skill should be read-only
- Skill has limited scope
- Security is important
- You want to prevent accidental modifications

**Don't restrict when**:
- Skill needs full flexibility
- Multiple operations required
- User might need varied access

## Testing Skills

### Pre-Testing Checklist

Before testing a new skill:

1. **Validate YAML**:
   ```bash
   head -n 20 SKILL.md
   # Check frontmatter format
   ```

2. **Check file location**:
   ```bash
   # Personal
   ls ~/.claude/skills/skill-name/SKILL.md

   # Project
   ls .claude/skills/skill-name/SKILL.md

   # Plugin
   ls plugin-name/skills/skill-name/SKILL.md
   ```

3. **Verify name format**:
   - Lowercase, numbers, hyphens only
   - No spaces or special characters

4. **Check description**:
   - Includes what and when
   - Contains trigger terms
   - Under 1024 characters

### Testing Process

1. **Restart Claude Code**:
   ```bash
   # Skills load at startup
   claude
   ```

2. **Test with trigger phrases**:
   - Use terms from your description
   - Ask questions that match "when to use"
   - Vary phrasing to test discovery

3. **Verify activation**:
   - Skill should activate automatically
   - Claude should follow instructions
   - Supporting files should load when referenced

4. **Test edge cases**:
   - Invalid inputs
   - Missing dependencies
   - Error conditions

### Debug Mode

Run with debug flag to see skill loading:

```bash
claude --debug
```

Look for:
- Skill discovery messages
- Loading errors
- YAML parse errors
- File not found errors

### Common Test Scenarios

#### Scenario 1: Does it activate?
```
User: [Use trigger phrase from description]
Expected: Skill activates and provides help
```

#### Scenario 2: Are restrictions working?
```
User: [Request that needs restricted tool]
Expected: Permission denied or alternative approach
```

#### Scenario 3: Do supporting files load?
```
User: [Ask question requiring reference docs]
Expected: Claude references the supporting file
```

## Troubleshooting

### Skill Doesn't Activate

**Check**: Description specificity
- Add more trigger terms
- Be more explicit about when to use
- Include user vocabulary

**Check**: YAML validity
```bash
# View frontmatter
cat SKILL.md | head -n 10
```

**Check**: File location
```bash
# Verify SKILL.md exists in correct location
ls [path]/SKILL.md
```

### YAML Parse Errors

**Common causes**:
- Tabs instead of spaces
- Missing quotes around special characters
- Invalid structure
- Missing opening/closing `---`

**Fix**:
```yaml
# Before (broken)
---
description: It's broken
---

# After (fixed)
---
description: "It's fixed"
---
```

### Tool Restrictions Not Working

**Verify syntax**:
```yaml
# Correct
allowed-tools: Read, Grep, Glob

# Also correct
allowed-tools:
  - Read
  - Grep
  - Glob
```

**Check tool names**:
- Use exact tool names (case-sensitive)
- Common names: Read, Write, Edit, Bash, Grep, Glob
- Separate with commas in string format

### Supporting Files Not Loading

**Check paths**:
- Use relative paths from SKILL.md
- Use forward slashes (/)
- Don't use absolute paths

**Check file exists**:
```bash
cd skill-directory
ls -la
# Verify all referenced files exist
```

## Best Practices Summary

### DO

- Keep skills focused on one capability
- Write specific, detailed descriptions
- Include trigger terms users would say
- Use tool restrictions for safety
- Provide concrete examples
- Test thoroughly before sharing
- Document requirements clearly
- Use progressive disclosure (supporting files)

### DON'T

- Create vague, generic descriptions
- Use invalid characters in names
- Make skills too broad
- Forget to include "when to use"
- Skip validation before testing
- Use absolute paths for supporting files
- Mix tabs and spaces in YAML
- Omit error handling guidance

## Version History

When documenting skill changes, use semantic versioning:

```markdown
## Version History
- v2.0.0 (2025-11-07): Breaking changes to API
- v1.1.0 (2025-10-15): Added new features
- v1.0.0 (2025-10-01): Initial release
```

This helps team members understand what changed between versions.
