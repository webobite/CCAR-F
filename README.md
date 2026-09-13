# CCAR-F

This repo is used to practise for my certification.

## Folders

| Folder | Description |
| --- | --- |
| [D_1-Agentic_Foundations-Agents-vs-Workflows](D_1-Agentic_Foundations-Agents-vs-Workflows) | Jupyter notebooks exploring agentic foundations (agents vs. workflows) using the Anthropic and OpenAI SDKs |
| [test-folder](test-folder) | Scratch space for testing OpenAI/Claude API calls via a Python script |

## Notebooks

| Notebook | Description |
| --- | --- |
| [Making-request-with-claude-api.ipynb](D_1-Agentic_Foundations-Agents-vs-Workflows/Making-request-with-claude-api.ipynb) | Basic single- and multi-turn requests to Claude via the Anthropic SDK and via the OpenAI SDK pointed at an AICredits gateway |
| [Simple-chat-bot.ipynb](D_1-Agentic_Foundations-Agents-vs-Workflows/Simple-chat-bot.ipynb) | A simple interactive chat loop that maintains conversation history across turns |
| [system_prompt.ipynb](D_1-Agentic_Foundations-Agents-vs-Workflows/system_prompt.ipynb) | Examples of using system prompts to steer model behavior (e.g. a step-by-step math tutor persona) |

## Setup

Install dependencies from [requirment.txt](requirment.txt):

```bash
pip install -r requirment.txt
```

Create a `.env` file with the required API keys (e.g. `ANTHROPIC_API_KEY`, `AICREDITS_API_KEY`) — see `load_dotenv()` usage in the notebooks.
