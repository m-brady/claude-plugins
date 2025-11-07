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
/plugin install sqlc-go@claude-plugins

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
/plugin enable sqlc-go@claude-plugins
/plugin disable sqlc-go@claude-plugins

# Uninstall a plugin
/plugin uninstall sqlc-go@claude-plugins

# Update marketplace plugin list
/plugin marketplace update claude-plugins

# Remove marketplace and all its plugins
/plugin marketplace remove claude-plugins
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
      "marketplace": "claude-plugins"
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
/plugin install sqlc-go@claude-plugins
```

**Usage:**
After installation, Claude automatically uses this skill when you ask about sqlc-related tasks:
- "Help me configure sqlc for my project"
- "Write a sqlc query to get users by email"
- "How do I map a JSONB column to a Go struct?"
- "Create a migration to add an index"

### example-plugin

An example plugin demonstrating the structure and components of a Claude Code plugin.

**Features:**
- Custom slash commands
- Example agents
- Plugin structure demonstration

**Installation:**
```shell
/plugin install example-plugin@claude-plugins
```

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

### Adding a New Plugin

1. Create a new directory under `plugins/`:
   ```bash
   mkdir -p plugins/your-plugin/.claude-plugin
   ```

2. Create the plugin manifest:
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

3. Add your components (commands, agents, etc.)

4. Update the marketplace manifest (`.claude-plugin/marketplace.json`) to include your plugin:
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

5. Test locally:
   ```shell
   /plugin marketplace add ./path/to/claude-plugins
   /plugin install your-plugin@claude-plugins
   ```

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