# Cloudflare Workers Plugin

Official Cloudflare Workers skill for Claude Code that helps you build production-ready serverless applications on the Cloudflare Workers platform.

## Features

This plugin provides a specialized skill for developing Cloudflare Workers applications with:

- **TypeScript-first** code generation with proper types
- **Complete solutions** including worker code and wrangler.jsonc configuration
- **Best practices** for security, performance, and error handling
- **All Cloudflare services** including Workers KV, Durable Objects, D1, R2, Hyperdrive, Queues, Vectorize, Workers AI, and more
- **Modern patterns** including WebSocket Hibernation API and AI Agents
- **Production-ready** code with proper error handling and logging

## Installation

```shell
# Add the marketplace (if not already added)
/plugin marketplace add your-username/claude-plugins

# Install the plugin
/plugin install cloudflare-workers@claude-plugins
```

## Usage

The skill activates automatically when you mention Cloudflare Workers-related terms like:
- "Cloudflare Workers"
- "Workers KV"
- "Durable Objects"
- "Workers AI"
- "Edge functions"
- "Serverless"

### Example Prompts

```
Create a Cloudflare Worker that handles authentication with KV storage

Build a WebSocket chat room using Durable Objects

Create an API that uses Workers AI for text generation

Set up a queue consumer that processes background jobs
```

## What You Get

When using this skill, Claude Code will provide:

1. **Complete Worker Code** - Fully functional TypeScript code
2. **Configuration** - Ready-to-use wrangler.jsonc with all bindings
3. **Type Definitions** - Proper TypeScript interfaces and types
4. **Testing Examples** - curl commands and sample requests
5. **Best Practices** - Security, performance, and error handling built-in

## Supported Services

- **Workers KV** - Key-value storage
- **Durable Objects** - Strongly consistent state
- **D1** - Relational database
- **R2** - Object storage
- **Hyperdrive** - PostgreSQL connections
- **Queues** - Asynchronous processing
- **Vectorize** - Vector search
- **Workers Analytics Engine** - Event tracking
- **Workers AI** - AI inference
- **Browser Rendering** - Remote browser capabilities
- **Workers Static Assets** - Frontend hosting
- **Workflows** - Multi-step operations
- **Agents** - AI agent state management

## Code Standards

All generated code follows Cloudflare's best practices:

- TypeScript by default with ES modules format
- Compatibility date: 2025-03-07
- Node.js compatibility enabled
- Full observability support
- Proper error handling and logging
- Security headers and input validation
- No hardcoded secrets

## Examples

### Basic API Worker

Ask: "Create a simple REST API worker"

You'll get a complete TypeScript worker with proper error handling, routing, and configuration.

### Durable Object with WebSockets

Ask: "Build a real-time chat using Durable Objects"

You'll get a WebSocket implementation using the modern Hibernation API with proper handlers.

### AI-Powered Worker

Ask: "Create a worker that uses Workers AI for sentiment analysis"

You'll get a complete AI integration with proper streaming and error handling.

## Learn More

- [Cloudflare Workers Docs](https://developers.cloudflare.com/workers/)
- [Wrangler CLI](https://developers.cloudflare.com/workers/wrangler/)
- [Workers Examples](https://developers.cloudflare.com/workers/examples/)

## Credits

Based on the official Cloudflare Workers prompt from https://developers.cloudflare.com/workers/prompt.txt
