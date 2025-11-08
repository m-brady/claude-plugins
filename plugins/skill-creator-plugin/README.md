# Skill Creator Plugin

A Claude Code plugin that helps you create and edit skills using Test-Driven Development principles.

## What is this?

This plugin provides a skill that guides you through creating new skills or editing existing ones using a TDD approach. It teaches you to run baseline tests first, identify failures, then write minimal skills that address those specific failures. This ensures your skills teach the right thing based on observed behavior, not assumptions.

## Installation

### For Development

1. Clone this repository
2. Copy the plugin to your Claude Code plugins directory:
   ```bash
   cp -r skill-creator-plugin ~/.claude/plugins/skill-creator
   ```
3. Restart Claude Code

### From Marketplace (when published)

```bash
claude plugin install skill-creator
```

## What's Included

### Skills

- **skill-creator**: Guides you through creating or editing skills using Test-Driven Development
  - RED: Run baseline tests to identify failures
  - GREEN: Write minimal skill addressing those failures
  - REFACTOR: Test and close loopholes through iteration

### Templates

- `basic-skill-template.md`: Template for standard skills with Anti-Patterns section
- `readonly-skill-template.md`: Template for read-only analysis skills with tool restrictions

### Scripts

- `validate-skill.py`: Python script to validate SKILL.md files (YAML, naming, structure)

### Documentation

- `REFERENCE.md`: Comprehensive reference for validation rules, file organization, and troubleshooting

## Usage

Once installed, Claude will automatically use the skill-creator skill when you ask to create or edit skills:

**Creating new skills:**
```
I want to create a skill for analyzing log files
```

**Editing existing skills:**
```
Help me improve the database-migration skill to enforce testing rollbacks
```

**General skill work:**
```
Let's work on the commit-helper skill
```

Claude will guide you through the TDD process:

**RED Phase:**
1. Identify test scenarios
2. Run baseline tests without the skill (or with old version)
3. Document specific failures and rationalizations

**GREEN Phase:**
1. Gather requirements (name, location, description)
2. Write skill content that directly addresses observed failures
3. Add Anti-Patterns section for discipline skills
4. Create minimal supporting files (only if 100+ lines)

**REFACTOR Phase:**
1. Test with the skill active
2. Identify new loopholes or rationalizations
3. Update skill to close loopholes
4. Iterate until skill reliably prevents failures

## Validating Skills

You can also manually validate a SKILL.md file using the included script:

```bash
python ~/.claude/skills/skill-creator/scripts/validate-skill.py path/to/SKILL.md
```

This will check:
- YAML frontmatter format
- Name validation (lowercase, hyphens, length)
- Description completeness and length
- File structure and references
- Best practices compliance

## Examples

### Creating a Simple Skill

```
User: Create a skill for generating commit messages

Claude: I'll help you create a commit message skill. Let me gather some information...

[Claude guides through the process]

Claude: I've created the skill at ~/.claude/skills/commit-helper/SKILL.md
Restart Claude Code to use it!
```

### Creating a Read-Only Analysis Skill

```
User: Make a skill that analyzes test coverage but can't modify files

Claude: I'll create a read-only skill for test coverage analysis...

[Claude creates skill with allowed-tools: Read, Grep, Glob]
```

## Features

- **Test-Driven Approach**: Enforces RED-GREEN-REFACTOR cycle for skill development
- **The Iron Law**: No skill deploys without failing baseline tests first
- **Guided Creation & Editing**: Step-by-step for both new and existing skills
- **Validation**: Built-in validation for names, descriptions, YAML structure
- **Templates**: Updated templates with Anti-Patterns sections
- **Best Practices**: Ensures skills address actual failures, not assumptions
- **Tool Restrictions**: Configures appropriate tool access for safety
- **Minimal Files**: Encourages self-contained skills with progressive disclosure

## What Gets Validated

When creating skills, the plugin validates:

### Name
- Lowercase letters, numbers, hyphens only
- Maximum 64 characters
- No spaces, underscores, or special characters

### Description
- Maximum 1024 characters
- Includes "what" the skill does
- Includes "when" to use it
- Contains trigger terms

### YAML Frontmatter
- Proper opening and closing `---`
- Required fields present
- Valid YAML syntax
- No tabs, only spaces

### File Structure
- SKILL.md exists
- Referenced files exist
- Proper directory organization

## Tips for Creating Great Skills

### The TDD Mindset

1. **Always Run Baseline Tests First**
   - Don't skip the RED phase - it's not optional
   - Test WITHOUT the skill to see actual failures
   - Document rationalizations you observe

2. **Write Descriptions for Discovery**
   - Start with "Use when..."
   - Include error messages, tool names, symptoms
   - Optimize for how Claude would search, not how you'd explain it
   - Good: "Use when debugging errors, analyzing logs, or investigating failures. Mentions of stack traces, error messages, or log files trigger this."
   - Poor: "Helps with debugging"

3. **One Excellent Example > Three Mediocre Ones**
   - Show realistic, concrete usage
   - Demonstrate what "correct" looks like
   - Don't pad with multiple trivial examples

4. **Add Anti-Patterns for Discipline Skills**
   - List the rationalizations you observed in testing
   - Explain why each rationalization fails
   - Make it explicit so Claude can't find loopholes

5. **Keep Content Self-Contained**
   - Only create supporting files for 100+ lines of reference
   - Most skills should be entirely in SKILL.md
   - Progressive disclosure is good, but don't overuse it

6. **Use Tool Restrictions Appropriately**
   - Read-only analysis: `allowed-tools: Read, Grep, Glob`
   - Analysis with computation: Add `Bash`
   - Limited write access: Add `Write` carefully

## Contributing

To contribute improvements to this plugin:

1. Fork the repository
2. Make your changes
3. Test thoroughly
4. Submit a pull request

## License

MIT License - See LICENSE file for details

## Support

For issues or questions:
- GitHub Issues: [your-repo]/issues
- Documentation: See REFERENCE.md in the skill directory
- Claude Code Docs: https://docs.claude.com/en/docs/claude-code

## Version History

- v2.0.0 (2025-11-07): TDD-focused rewrite
  - Added Test-Driven Development approach (RED-GREEN-REFACTOR)
  - The Iron Law: No skill without baseline tests
  - Support for editing existing skills
  - Updated templates with Anti-Patterns sections
  - Emphasis on self-contained skills
  - Improved description optimization for discovery

- v1.0.0 (2025-11-07): Initial release
  - skill-creator skill
  - Validation script
  - Templates and reference documentation
