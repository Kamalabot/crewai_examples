from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task, before_kickoff, after_kickoff
from whatsapp_extractor.tools.whatsapp_selenium_tool import WhatsAppSeleniumTool

@CrewBase
class WhatsappExtractor():
    """WhatsApp Data Extraction Crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @before_kickoff
    def setup_browser(self, inputs):
        """Ensure WhatsApp Web is ready"""
        print("Please ensure WhatsApp Web is open in Chrome with remote debugging enabled")
        print("Run Chrome with: google-chrome --remote-debugging-port=9222")
        return inputs

    @after_kickoff
    def process_results(self, output):
        """Process and save the extraction results"""
        print(f"Extraction completed. Results: {output}")
        return output

    @agent
    def researcher(self) -> Agent:
        """WhatsApp Data Extraction Specialist"""
        return Agent(
            config=self.agents_config['researcher'],
            tools=[WhatsAppSeleniumTool()],
            verbose=True
        )

    @agent
    def data_processor(self) -> Agent:
        """WhatsApp Data Processing Analyst"""
        return Agent(
            config=self.agents_config['data_processor'],
            verbose=True
        )

    @task
    def extract_chats_task(self) -> Task:
        """Task to extract available chats"""
        return Task(
            config=self.tasks_config['extract_chats_task']
        )

    @task
    def extract_messages_task(self) -> Task:
        """Task to extract messages from specified chat"""
        return Task(
            config=self.tasks_config['extract_messages_task']
        )

    @task
    def process_data_task(self) -> Task:
        """Task to process extracted data"""
        return Task(
            config=self.tasks_config['process_data_task']
        )

    @crew
    def crew(self) -> Crew:
        """Creates the WhatsApp Extraction crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            verbose=2,
            process=Process.sequential
        )
