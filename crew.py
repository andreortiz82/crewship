from crewai import Agent, Crew, Process, Task
from openai import OpenAI
from crewai.project import CrewBase, agent, crew, task
from custom_tool import GenerateCover, GenerateWhisper
from datetime import datetime

client = OpenAI()
cover_tool = GenerateCover()
whisper_tool = GenerateWhisper()
datetime_tag = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

@CrewBase
class CrewshipCrew():
	"""Crewship crew"""
	agents_config = 'agents.yaml'
	tasks_config = 'tasks.yaml'

	@agent
	def storyteller(self) -> Agent:
		return Agent(
			config=self.agents_config['storyteller'],
			verbose=True,
			memory=False,
			allow_delegation=True,
		)
	
	@agent
	def cover_designer(self) -> Agent:
		return Agent(
			config=self.agents_config['cover_designer'],
			verbose=True,
			tools=[cover_tool],
			allow_delegation=False,
		)

	@agent
	def markdown_developer(self) -> Agent:
		return Agent(
			config=self.agents_config['markdown_developer'],
			verbose=True,
			allow_delegation=False,
		)
	
	@task
	def storyteller_task(self) -> Task:
		return Task(
			config=self.tasks_config['storyteller_task'],
			agent=self.storyteller(),
			tools=[whisper_tool]
		)
	
	@task
	def cover_designer_task(self) -> Task:
		return Task(
			config=self.tasks_config['cover_designer_task'],
			agent=self.cover_designer(),
			requires_input=True
		)
	
	@task
	def markdown_developer_task(self) -> Task:
		return Task(
			config=self.tasks_config['markdown_developer_task'],
			agent=self.markdown_developer(),
			requires_input=True,
			output_file=f"content-{datetime_tag}.md",
		)
	
	@crew
	def crew(self) -> Crew:
		"""Creates the Crewship crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)