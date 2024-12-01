from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import ScrapeWebsiteTool, SerperDevTool


@CrewBase
class SalesOfferCrew:
    """SalesOffer crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def customer_needs_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["customer_needs_analyst"],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            allow_delegation=False,
            verbose=True,
        )

    @agent
    def product_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config["product_specialist"],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            allow_delegation=False,
            verbose=True,
        )

    @agent
    def pricing_strategist(self) -> Agent:
        return Agent(
            config=self.agents_config["pricing_strategist"],
            tools=[],
            allow_delegation=False,
            verbose=True,
        )

    @agent
    def offer_composer(self) -> Agent:
        return Agent(
            config=self.agents_config["offer_composer"],
            tools=[],
            allow_delegation=False,
            verbose=True,
        )

    @task
    def analyze_customer_needs_task(self) -> Task:
        return Task(
            config=self.tasks_config["analyze_customer_needs_task"],
            agent=self.customer_needs_analyst(),
        )

    @task
    def select_products_services_task(self) -> Task:
        return Task(
            config=self.tasks_config["select_products_services_task"],
            agent=self.product_specialist(),
        )

    @task
    def determine_pricing_task(self) -> Task:
        return Task(
            config=self.tasks_config["determine_pricing_task"],
            agent=self.pricing_strategist(),
        )

    @task
    def compose_offer_task(self) -> Task:
        return Task(
            config=self.tasks_config["compose_offer_task"],
            agent=self.offer_composer(),
            output_file="offer_content.md",
        )

    @crew
    def crew(self) -> Crew:
        """Creates the SalesOffer crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
