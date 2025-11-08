# Claude Plugins Marketplace

A marketplace for Claude Code plugins, containing custom commands, agents, hooks, Skills, and MCP servers.

## What's Inside

This marketplace provides plugins that extend Claude Code's functionality:

- **Commands**: Custom slash commands for common workflows
- **Agents**: Specialized agents for specific tasks
- **Skills**: Model-invoked capabilities that Claude uses autonomously
- **Hooks**: Event handlers for automation
- **MCP Servers**: Integrations with external tools

## Quick Start

### Adding This Marketplace

Add this marketplace to Claude Code using one of these methods:

```shell
# From GitHub (recommended)
/plugin marketplace add m-brady/claude-plugins

# From local path
/plugin marketplace add /Users/michael/git/claude-plugins

# From any Git URL
/plugin marketplace add https://github.com/m-brady/claude-plugins.git
```

Verify the marketplace was added:
```shell
/plugin marketplace list
```

### Installing Plugins

Once the marketplace is added, install plugins:

```shell
# Browse available plugins interactively (recommended)
/plugin

# Install a specific plugin directly
/plugin install sqlc-go@m-brady/claude-plugins

# Check installed plugins
/plugin list
```

### Using Installed Plugins

**Skills** (like sqlc-go):
- Skills are automatically invoked by Claude when relevant to your request
- No manual activation needed - Claude decides when to use them
- Example: After installing sqlc-go, just ask "Help me write a sqlc query for users"

**Commands**:
- Use with `/command-name` syntax
- View all commands with `/help`

**Hooks**:
- Automatically trigger on configured events
- No manual invocation required

### Managing Plugins

```shell
# Enable/disable plugins
/plugin enable sqlc-go@m-brady/claude-plugins
/plugin disable sqlc-go@m-brady/claude-plugins

# Uninstall a plugin
/plugin uninstall sqlc-go@m-brady/claude-plugins

# Update marketplace plugin list
/plugin marketplace update m-brady/claude-plugins

# Remove marketplace and all its plugins
/plugin marketplace remove m-brady/claude-plugins
```

### For Team Use

To automatically install this marketplace for your team, add to your project's `.claude/settings.json`:

```json
{
  "extraKnownMarketplaces": [
    {
      "source": "m-brady/claude-plugins"
    }
  ],
  "enabledPlugins": [
    {
      "name": "sqlc-go",
      "marketplace": "m-brady/claude-plugins"
    }
  ]
}
```

When team members trust the repository, Claude Code will:
1. Automatically install the marketplace
2. Install and enable specified plugins
3. Make all commands and skills available immediately

## Available Plugins

### sqlc-go

Expert guidance for using sqlc with Go and PostgreSQL, including query writing, type mappings, and migration management.

**What it provides:**
- sqlc v2 configuration and setup patterns
- PostgreSQL query writing (JSONB, arrays, CTEs, window functions)
- Type override patterns for custom Go struct mappings
- golang-migrate integration and workflow guidance
- Transaction patterns and best practices
- Troubleshooting common sqlc issues

**Type:** Skill (model-invoked)

**Installation:**
```shell
/plugin install sqlc-go@m-brady/claude-plugins
```

**Usage:**
After installation, Claude automatically uses this skill when you ask about sqlc-related tasks:
- "Help me configure sqlc for my project"
- "Write a sqlc query to get users by email"
- "How do I map a JSONB column to a Go struct?"
- "Create a migration to add an index"

### cloudflare-workers

Skill for developing and deploying Cloudflare Workers with TypeScript, supporting Workers KV, Durable Objects, D1, R2, and more.

**Type:** Skill (model-invoked)

**Installation:**
```shell
/plugin install cloudflare-workers@m-brady/claude-plugins
```

**Usage:**
Claude automatically uses this when working with Cloudflare Workers, edge computing, or serverless functions.

### skill-creator

Create and edit Claude Code skills using Test-Driven Development principles. Enforces the RED-GREEN-REFACTOR cycle for skill development.

**What it provides:**
- Test-Driven Development approach for skills
- "The Iron Law": No skill without baseline tests first
- Support for both creating new skills and editing existing ones
- Anti-Patterns sections to prevent rationalizations
- Templates with validation and best practices
- "One excellent example > three mediocre ones" philosophy

**Type:** Skill (model-invoked)

**Installation:**
```shell
/plugin install skill-creator@m-brady/claude-plugins
```

**Usage:**
After installation, Claude uses this skill when you ask about creating or editing skills:
- "Create a skill for analyzing log files"
- "Help me improve the database-migration skill"
- "Let's work on the commit-helper skill"

## Creating Your Own Plugins

### Plugin Structure

Each plugin follows this structure:

```
your-plugin/
├── .claude-plugin/
│   └── plugin.json          # Plugin metadata (required)
├── commands/                 # Custom slash commands (optional)
│   └── command.md
├── agents/                   # Custom agents (optional)
│   └── agent.md
├── skills/                   # Agent Skills (optional)
│   └── skill-name/
│       └── SKILL.md
├── hooks/                    # Event handlers (optional)
│   └── hooks.json
└── README.md                # Documentation (recommended)
```

### Adding a New Plugin to This Marketplace

Follow these steps to add a new plugin to this marketplace:

#### 1. Create Plugin Structure

Create a new directory under `plugins/`:
```bash
mkdir -p plugins/your-plugin/.claude-plugin
```

#### 2. Create Plugin Manifest

Create `plugins/your-plugin/.claude-plugin/plugin.json`:
```json
{
  "name": "your-plugin",
  "description": "What your plugin does",
  "version": "1.0.0",
  "author": {
    "name": "Your Name"
  }
}
```

#### 3. Add Plugin Components

Add your components (commands, agents, skills, hooks, etc.) following the structure below.

#### 4. Register in Marketplace Manifest

**IMPORTANT:** Update `.claude-plugin/marketplace.json` to register your plugin:

```json
{
  "plugins": [
    {
      "name": "your-plugin",
      "source": "./plugins/your-plugin",
      "description": "Your plugin description"
    }
  ]
}
```

Add your plugin entry to the `plugins` array alongside existing plugins like `sqlc-go`, `cloudflare-workers`, and `skill-creator`.

#### 5. Update README

Add your plugin to the "Available Plugins" section in this README with:
- Description
- What it provides
- Type (Skill, Command, etc.)
- Installation instructions
- Usage examples

#### 6. Test Locally

Test your plugin before committing:
```shell
# Add marketplace from local path
/plugin marketplace add /Users/michael/git/claude-plugins

# Install your plugin
/plugin install your-plugin@m-brady/claude-plugins

# Test functionality
```

#### 7. Commit and Push

```bash
git add plugins/your-plugin/ .claude-plugin/marketplace.json README.md
git commit -m "Add your-plugin to marketplace"
git push
```

**Remember:** Every plugin MUST be registered in `.claude-plugin/marketplace.json` to be discoverable in the marketplace!

## Marketplace Structure

```
claude-plugins/
├── .claude-plugin/
│   └── marketplace.json     # Marketplace manifest
├── plugins/                  # Plugin directories
│   ├── example-plugin/
│   └── your-plugin/
└── README.md                # This file
```

## Resources

- [Claude Code Plugins Documentation](https://code.claude.com/docs/en/plugins.md)
- [Plugin Reference](https://code.claude.com/docs/en/plugins-reference.md)
- [Plugin Marketplaces Guide](https://code.claude.com/docs/en/plugin-marketplaces.md)
- [Skills Guide](https://code.claude.com/docs/en/skills.md)

## License

[Add your license here]