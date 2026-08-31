# Compatibility Guide

## Supported usage paths

| Platform / Tool | Recommended method | Notes |
|---|---|---|
| Claude | Install/upload the Skill containing `SKILL.md` | `SKILL.md` is the canonical instruction set. |
| ChatGPT | Use `chatgpt/CHATGPT-MASTER-PROMPT.txt` or install the Skill when Skills are available to the account/workspace | Native Skills availability depends on the ChatGPT surface and workspace settings. |
| Codex | Load the Skill as a supported Skill/instruction resource | Keep `SKILL.md` at the Skill root. |
| Other AI tools | System instructions, knowledge file, uploaded Skill, or equivalent | Exact behavior depends on the tool's instruction/file support. |

## Canonical source

`SKILL.md` is the source of truth for the Skill itself.

The ChatGPT edition is a product-specific adaptation of the same methodology, not a replacement for the canonical Skill.

## Important compatibility rule

Do not assume that every AI product supports the same Skill installation mechanism. When native Skills are unavailable, use the provided prompt/documentation path for that product.

## Version

Current release line: **v3.2.x**

Repository: https://github.com/kiarash65/sunjob-math-major-skill
