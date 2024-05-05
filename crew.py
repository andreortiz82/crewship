from crewai import Agent, Crew, Process, Task
from openai import OpenAI
from crewai.project import CrewBase, agent, crew, task
from custom_tool import GenerateCover, GenerateWhisper

client = OpenAI()
cover_tool = GenerateCover()
whisper_tool = GenerateWhisper()

@CrewBase
class CrewshipCrew():
	"""Crewship crew"""
	agents_config = 'agents.yaml'
	tasks_config = 'tasks.yaml'

	@agent
	def creative_mind(self) -> Agent:
		return Agent(
			config=self.agents_config['creative_mind'],
			verbose=True,
			memory=False,
			allow_delegation=True,
		)
	
	@agent
	def scribe(self) -> Agent:
		return Agent(
			config=self.agents_config['scribe'],
			verbose=True,
			allow_delegation=False,
		)
	
	@agent
	def cover_designer(self) -> Agent:
		return Agent(
			config=self.agents_config['cover_designer'],
			verbose=True,
			tools=[cover_tool],
			allow_delegation=False,
		)

	@task
	def creative_mind_task(self) -> Task:
		return Task(
			config=self.tasks_config['creative_mind_task'],
			agent=self.creative_mind(),
			tools=[whisper_tool]
		)
	
	@task
	def scribe_task(self) -> Task:
		return Task(
			config=self.tasks_config['scribe_task'],
			agent=self.scribe(),
			requires_input=True,
			output_file="index.mdx",
		)
	
	@task
	def cover_designer_task(self) -> Task:
		return Task(
			config=self.tasks_config['cover_designer_task'],
			agent=self.cover_designer(),
			requires_input=True
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