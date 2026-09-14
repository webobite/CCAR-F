# CCAR-F

This repo is used to practise for my certification.

## Folders

| Folder | Description |
| --- | --- |
| [Building_with_Claude_API_Courses](Building_with_Claude_API_Courses) | Jupyter notebooks from "Building with the Claude API" course covering agentic foundations, streaming, output control, and prompt evaluation using the Anthropic and OpenAI SDKs |
| [test-folder](test-folder) | Scratch space for testing OpenAI/Claude API calls via a Python script |

## Notebooks

Notebooks in [Building_with_Claude_API_Courses](Building_with_Claude_API_Courses) follow the [Building with the Claude API](https://anthropic-partners.skilljar.com/claude-with-the-anthropic-api) course.

| Notebook | Description |
| --- | --- |
| [Making-request-with-claude-api.ipynb](Building_with_Claude_API_Courses/Making-request-with-claude-api.ipynb) | Basic single- and multi-turn requests to Claude via the Anthropic SDK and via the OpenAI SDK pointed at an AICredits gateway |
| [Simple-chat-bot.ipynb](Building_with_Claude_API_Courses/Simple-chat-bot.ipynb) | A simple interactive chat loop that maintains conversation history across turns |
| [system_prompt.ipynb](Building_with_Claude_API_Courses/system_prompt.ipynb) | Examples of using system prompts to steer model behavior (e.g. a step-by-step math tutor persona) |
| [temperature_demo.ipynb](Building_with_Claude_API_Courses/temperature_demo.ipynb) | Demonstrates the effect of the `temperature` parameter on response creativity/determinism using both the OpenAI and Anthropic SDKs |
| [streaming.ipynb](Building_with_Claude_API_Courses/streaming.ipynb) | Demonstrates streaming responses chunk-by-chunk using the OpenAI and Anthropic SDKs |
| [controlling_output.ipynb](Building_with_Claude_API_Courses/controlling_output.ipynb) | Demonstrates constraining model output (e.g. prefilling a response and using stop sequences to produce parseable JSON/CLI output) with the OpenAI and Anthropic SDKs |
| [prompt_evaluation.ipynb](Building_with_Claude_API_Courses/prompt_evaluation.ipynb) | Builds a prompt evaluation pipeline: generates a test dataset, runs prompts against it, and grades outputs using code-based, model-based, and syntax validation graders |
| [prompt_engineering_techiniques.ipynb](Building_with_Claude_API_Courses/prompt_engineering_techiniques.ipynb) | Implements a reusable `PromptEvaluator` framework (test case generation, concurrent grading, HTML report output) to evaluate prompt engineering techniques such as being specific, clear and direct, and providing examples, steps, and guidelines |

## Notes

Reference images used alongside the notebooks, in [Building_with_Claude_API_Courses/notes](Building_with_Claude_API_Courses/notes):

| Note | Description |
| --- | --- |
| [temperature-ranges.png](Building_with_Claude_API_Courses/notes/temperature-ranges.png) | Visual reference for how `temperature` values map to more deterministic vs. more creative model outputs |
| [streaming-response-understanding.png](Building_with_Claude_API_Courses/notes/streaming-response-understanding.png) | Visual reference explaining how streaming responses work |
| [grader-types.png](Building_with_Claude_API_Courses/notes/grader-types.png) | Visual reference comparing code, model, and human graders for evaluating prompt outputs |
| [prompt_engineering_technique_be_specific.png](Building_with_Claude_API_Courses/notes/prompt_engineering_technique_be_specific.png) | Visual reference for the "be specific" prompt engineering technique |
| [prompt_engineering_technique_clear_direct.png](Building_with_Claude_API_Courses/notes/prompt_engineering_technique_clear_direct.png) | Visual reference for the "clear and direct" prompt engineering technique |
| [prompt_engineering_technique_provide_examples.png](Building_with_Claude_API_Courses/notes/prompt_engineering_technique_provide_examples.png) | Visual reference for the "provide examples" prompt engineering technique |
| [prompt_engineering_technique_provide_steps.png](Building_with_Claude_API_Courses/notes/prompt_engineering_technique_provide_steps.png) | Visual reference for the "provide steps" prompt engineering technique |
| [prompt_engineering_technique_guidelines.png](Building_with_Claude_API_Courses/notes/prompt_engineering_technique_guidelines.png) | Visual reference for the "provide guidelines" prompt engineering technique |

## Setup

Install dependencies from [requirment.txt](requirment.txt):

```bash
pip install -r requirment.txt
```

Create a `.env` file with the required API keys (e.g. `ANTHROPIC_API_KEY`, `AICREDITS_API_KEY`) — see `load_dotenv()` usage in the notebooks.
