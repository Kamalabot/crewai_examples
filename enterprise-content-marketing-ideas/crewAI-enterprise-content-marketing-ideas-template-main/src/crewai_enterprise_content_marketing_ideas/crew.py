from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Uncomment the following line to use an example of a custom tool
# from crewai_enterprise_content_marketing_ideas.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
from crewai_tools import SerperDevTool


@CrewBase
class CrewaiEnterpriseContentMarketingCrew:
    """CrewaiEnterpriseContentMarketing crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["researcher"],
            tools=[SerperDevTool()],
            verbose=True,
        )

    @agent
    def content_generator(self) -> Agent:
        return Agent(config=self.agents_config["content_generator"], verbose=True)

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config["research_task"],
        )

    @task
    def content_generation_task(self) -> Task:
        return Task(
            config=self.tasks_config["content_generation_task"], output_file="report.md"
        )

    @crew
    def crew(self) -> Crew:
        """Creates the CrewaiEnterpriseContentMarketing crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
