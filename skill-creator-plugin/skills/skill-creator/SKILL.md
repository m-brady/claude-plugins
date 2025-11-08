---
name: skill-creator
description: Create well-structured Claude Code skills with proper YAML frontmatter, validation, and best practices. Use when the user wants to create a new skill, generate SKILL.md files, or needs help structuring a skill.
---

# Skill Creator

This skill helps you create well-structured Claude Code skills with proper formatting, validation, and adherence to best practices.

## Instructions

When a user wants to create a new skill, follow these steps:

### 1. Gather Requirements

Ask the user about:
- **Skill name**: What should the skill be called?
  - Must use lowercase letters, numbers, and hyphens only
  - Maximum 64 characters
  - Example: `pdf-processor`, `commit-helper`, `code-reviewer`

- **Description**: What does this skill do and when should it be used?
  - Maximum 1024 characters
  - Should include both WHAT it does and WHEN to use it
  - Should mention key terms that trigger the skill
  - Example: "Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction."

- **Location**: Where should the skill be created?
  - Personal skill: `~/.claude/skills/skill-name/`
  - Project skill: `.claude/skills/skill-name/`
  - Plugin skill: `plugin-name/skills/skill-name/`

- **Tool restrictions** (optional): Should this skill be restricted to specific tools?
  - Use `allowed-tools` to limit which tools Claude can use
  - Example: Read-only skills might use: `allowed-tools: Read, Grep, Glob`
  - Security-sensitive workflows benefit from tool restrictions

### 2. Validate Inputs

Before creating the skill, validate:
- Name uses only lowercase letters, numbers, and hyphens
- Name is under 64 characters
- Description is under 1024 characters
- Description includes both what the skill does AND when to use it
- Location path is valid and accessible

### 3. Create Directory Structure

```bash
# For personal skills
mkdir -p ~/.claude/skills/skill-name

# For project skills
mkdir -p .claude/skills/skill-name

# For plugin skills
mkdir -p plugin-name/skills/skill-name
```

### 4. Generate SKILL.md

Create a SKILL.md file with this structure:

```yaml
---
name: skill-name
description: Brief description of what this skill does and when to use it
# Optional: restrict tool access
# allowed-tools: Read, Grep, Glob, Bash
---

# Skill Name

Brief overview of what this skill does.

## Instructions

1. Step-by-step instructions for Claude
2. Be specific and actionable
3. Include error handling guidance
4. Reference supporting files when needed

## Examples

Show concrete examples of using this skill:

\`\`\`python
# Example code
import example
example.do_something()
\`\`\`

## Best Practices

- List important considerations
- Common pitfalls to avoid
- Performance tips
- Security considerations

## Requirements

If the skill needs external dependencies:
- List required packages
- Note that they must be installed in the environment
- Example: "Requires pypdf and pdfplumber packages"
```

### 5. Create Supporting Files (Optional)

Ask if the user needs:
- **Reference documentation**: `reference.md` for detailed API docs
- **Additional examples**: `examples.md` for more use cases
- **Helper scripts**: `scripts/helper.py` for utility functions
- **Templates**: `templates/template.txt` for file templates

Organize like this:
```
skill-name/
├── SKILL.md (required)
├── reference.md (optional)
├── examples.md (optional)
├── scripts/
│   └── helper.py (optional)
└── templates/
    └── template.txt (optional)
```

### 6. Best Practices Checklist

Ensure the skill follows these best practices:
- **Focused scope**: One skill addresses one capability
- **Clear description**: Includes what it does and when to use it
- **Specific triggers**: Uses key terms users would mention
- **Progressive disclosure**: Links to supporting files for details
- **Concrete examples**: Shows real-world usage
- **Error handling**: Guides how to handle common issues
- **Tool restrictions**: Uses `allowed-tools` when appropriate for safety

### 7. Testing Guidance

After creating the skill, provide testing instructions:
1. Restart Claude Code to load the new skill
2. Test with questions that match the description
3. Verify the skill activates automatically (model-invoked)
4. Check that supporting files load when referenced
5. Validate tool restrictions work as expected

## Examples

### Example 1: Simple Read-Only Skill

```yaml
---
name: log-analyzer
description: Analyze application logs for errors, warnings, and patterns. Use when debugging, investigating issues, or analyzing log files.
allowed-tools: Read, Grep, Glob
---

# Log Analyzer

Analyze application logs to identify errors, warnings, and patterns.

## Instructions

1. Use Read to view log files
2. Use Grep to search for error patterns
3. Use Glob to find log files by pattern
4. Summarize findings with timestamps and severity
5. Suggest potential root causes

## Common Patterns

- Error patterns: `ERROR|FATAL|Exception`
- Warning patterns: `WARN|WARNING`
- Performance issues: `timeout|slow|latency`

## Best Practices

- Always include context lines around errors
- Look for patterns over time
- Correlate errors across multiple log files
```

### Example 2: Skill with Scripts

```yaml
---
name: database-migration
description: Create and manage database migrations with proper versioning and rollback support. Use when creating database migrations, schema changes, or data migrations.
---

# Database Migration Helper

Create safe, reversible database migrations.

## Instructions

1. Analyze the schema change needed
2. Generate migration file with timestamp
3. Include both up and down migrations
4. Add validation checks
5. Test rollback scenario

See [migration-template.md](migration-template.md) for the standard format.

## Script Usage

Generate a new migration:
\`\`\`bash
python scripts/generate_migration.py "add_users_table"
\`\`\`

## Best Practices

- Always include rollback logic
- Test migrations on a copy of production data
- Use transactions when possible
- Document breaking changes
```

### Example 3: Multi-File Skill

```yaml
---
name: api-client-generator
description: Generate type-safe API clients from OpenAPI specs. Use when working with REST APIs, OpenAPI/Swagger specs, or generating API clients.
---

# API Client Generator

Generate type-safe API clients from OpenAPI specifications.

## Quick Start

\`\`\`bash
python scripts/generate_client.py openapi.yaml --output ./client
\`\`\`

For detailed options, see [REFERENCE.md](REFERENCE.md).
For examples, see [EXAMPLES.md](EXAMPLES.md).

## Instructions

1. Validate OpenAPI spec
2. Generate client code with types
3. Add authentication handling
4. Generate tests
5. Create documentation

## Requirements

Requires packages: openapi-generator-cli, pyyaml
```

## Validation Rules

When creating skills, enforce these rules:

### Name Validation
- Lowercase letters, numbers, hyphens only
- No spaces, underscores, or special characters
- Maximum 64 characters
- Must be unique in the target location

### Description Validation
- Maximum 1024 characters
- Must include WHAT the skill does
- Must include WHEN to use it
- Should include key terms for discovery

### YAML Frontmatter
- Must start with `---` on line 1
- Must end with `---` before content
- Required fields: `name`, `description`
- Optional fields: `allowed-tools`
- No tabs in YAML (use spaces)
- Proper YAML syntax

### File Structure
- SKILL.md is required
- All other files are optional
- Use forward slashes in paths
- Reference files with relative paths
- Keep supporting files in subdirectories

## Common Mistakes to Avoid

1. **Vague descriptions**: Always be specific about when to use the skill
   - Bad: "Helps with data"
   - Good: "Analyze CSV files, detect outliers, generate statistics. Use when working with CSV data or spreadsheets."

2. **Invalid names**: Follow naming rules strictly
   - Bad: `My_Skill`, `skill name`, `Skill-123`
   - Good: `my-skill`, `skill-name`, `skill123`

3. **Missing triggers**: Include key terms in description
   - Bad: "Processes files"
   - Good: "Process PDF files, extract text, fill forms. Use when working with PDFs."

4. **Too broad**: Keep skills focused
   - Bad: "All document processing"
   - Good: Separate skills for PDFs, Word docs, spreadsheets

5. **Forgetting tool restrictions**: Use `allowed-tools` for safety
   - Read-only skills should restrict to: Read, Grep, Glob
   - Analysis skills might add: Bash (for analysis commands)

## Troubleshooting New Skills

If a newly created skill doesn't work:

1. **Restart Claude Code**: Skills load at startup
2. **Check YAML syntax**: Validate frontmatter format
3. **Verify file path**: Ensure SKILL.md is in correct location
4. **Test description**: Make sure it includes trigger terms
5. **Run with --debug**: See skill loading errors

## Supporting Files Reference

Link to supporting files in SKILL.md:
- `[reference.md](reference.md)` - Detailed documentation
- `[examples.md](examples.md)` - Additional examples
- `scripts/helper.py` - Helper scripts
- `templates/template.txt` - File templates

Claude loads these files only when needed (progressive disclosure).
