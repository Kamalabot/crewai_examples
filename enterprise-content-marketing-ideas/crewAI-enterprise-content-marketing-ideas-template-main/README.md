# CrewaiEnterpriseContentMarketing Crew

Welcome to the CrewaiEnterpriseContentMarketing Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Goal
The goal of this crew is to generate content ideas for a given topic and company.

Our first agent is a researcher that will research the topic and company and provide a list of 10 bullet points containing the most relevant information about the topic, including emerging trends, competitor strategies, and potential KPIs for content.

Then, our second agent is a content generator that will generate content ideas for the topic and company based on the research provided by the first agent.

## Update your crew inputs
Inspect `crewai_enterprise_content_marketing_ideas/main.py` to see the inputs and how to customize the crew.


## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

1. First lock the dependencies and then install them:
```bash
uv lock
```
```bash
uv sync
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/crewai_enterprise_content_marketing_ideas/config/agents.yaml` to define your agents
- Modify `src/crewai_enterprise_content_marketing_ideas/config/tasks.yaml` to define your tasks
- Modify `src/crewai_enterprise_content_marketing_ideas/crew.py` to add your own logic, tools and specific args
- Modify `src/crewai_enterprise_content_marketing_ideas/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```
or
```bash
uv run crewai_enterprise_content_marketing_ideas
```

This command initializes the crewai-enterprise-content-marketing Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The crewai-enterprise-content-marketing Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the CrewaiEnterpriseContentMarketing Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
