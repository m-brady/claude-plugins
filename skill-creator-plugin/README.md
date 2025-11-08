# Skill Creator Plugin

A Claude Code plugin that helps you create well-structured skills with proper formatting, validation, and best practices.

## What is this?

This plugin provides a skill that guides you through creating new Claude Code skills. It helps ensure your skills follow best practices, have proper YAML frontmatter, and include all necessary components.

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

- **skill-creator**: Helps you create new Claude Code skills with proper structure and validation

### Templates

- `basic-skill-template.md`: Template for a standard skill
- `readonly-skill-template.md`: Template for read-only skills with tool restrictions

### Scripts

- `validate-skill.py`: Python script to validate SKILL.md files

### Documentation

- `REFERENCE.md`: Comprehensive reference for skill creation, including validation rules and best practices

## Usage

Once installed, Claude will automatically use the skill-creator skill when you ask to create a new skill:

```
I want to create a skill for analyzing log files
```

```
Help me create a read-only skill for reviewing code
```

```
Create a skill that generates API clients from OpenAPI specs
```

Claude will guide you through:
1. Choosing a name (with validation)
2. Writing a good description with triggers
3. Selecting the location (personal, project, or plugin)
4. Deciding on tool restrictions
5. Creating supporting files if needed
6. Testing your new skill

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

- **Guided Creation**: Step-by-step guidance through skill creation
- **Validation**: Built-in validation for names, descriptions, and structure
- **Templates**: Multiple templates for different skill types
- **Best Practices**: Ensures skills follow Claude Code conventions
- **Tool Restrictions**: Helps configure appropriate tool access
- **Supporting Files**: Guides creation of scripts, templates, and documentation

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

1. **Be Specific**: Include concrete trigger terms in your description
   - Good: "Use when working with PDF files, forms, or document extraction"
   - Poor: "Helps with documents"

2. **Keep Focused**: One skill = one capability
   - Don't create a "document-processing" super-skill
   - Create separate skills for PDFs, Word docs, spreadsheets

3. **Use Tool Restrictions**: Limit tools for safety
   - Read-only skills: `allowed-tools: Read, Grep, Glob`
   - Analysis skills: Add `Bash` for computation
   - Generation skills: May need `Write` or `Edit`

4. **Provide Examples**: Show concrete usage in your SKILL.md

5. **Test Thoroughly**: Use trigger phrases to verify activation

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

- v1.0.0 (2025-11-07): Initial release
  - skill-creator skill
  - Validation script
  - Templates and reference documentation
