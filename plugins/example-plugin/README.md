# Example Plugin

An example plugin demonstrating the structure and components of a Claude Code plugin.

## Features

- **Commands**: Custom slash commands (see `commands/example.md`)
- **Agents**: Custom agents (see `agents/example-agent.md`)
- **Hooks**: Event handlers (see `hooks/hooks.json`)
- **Skills**: Agent Skills (add to `skills/` directory)

## Installation

```shell
/plugin marketplace add your-org/claude-plugins
/plugin install example-plugin@claude-plugins
```

## Usage

After installation, try the example command:

```shell
/example
```

## Development

To modify this plugin:

1. Edit the relevant files in this directory
2. Uninstall the plugin: `/plugin uninstall example-plugin@claude-plugins`
3. Reinstall the plugin: `/plugin install example-plugin@claude-plugins`
4. Test your changes

## Structure

```
example-plugin/
├── .claude-plugin/
│   └── plugin.json          # Plugin metadata
├── commands/                 # Custom slash commands
│   └── example.md
├── agents/                   # Custom agents
│   └── example-agent.md
├── skills/                   # Agent Skills
│   └── (add SKILL.md files here)
├── hooks/                    # Event handlers
│   └── hooks.json
└── README.md                # This file
```
