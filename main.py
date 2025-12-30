from crewai.flow.flow import Flow, listen, start
from crews.meeting_crew import MeetingAssistantCrew
from crews.schemas.types import MeetingTask
from typing import List
from pydantic import BaseModel


class MeetingState(BaseModel):
    id: str = "meeting-flow-1"
    transcript: str = "Meeting transcript goes here"
    tasks: List[MeetingTask] = []


class MeetingFlow(Flow[MeetingState]):
    initial_state = MeetingState
    
    @start()
    def load_meeting_notes(self, path: str = 'data/meeting_transcript.txt'):
        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as file:
                self.state.transcript = file.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"Arquivo não encontrado: {path}")
        
    @listen(load_meeting_notes)
    def generate_tasks_meeting_transcript(self):
        output = (
            MeetingAssistantCrew()
            .crew()
            .kickoff(
                inputs={'transcript': self.state.transcript}
            )
        )
        
        tasks = output["tasks"]
        print('--- RESULTADO ---')
        print('  ')
        print(tasks)
        self.state.tasks = tasks
        
    
def kickoff():
    """
    Run the flow
    """
    meeting_flow = MeetingFlow()
    meeting_flow.kickoff()
    
def plot():
    """
    Plot the flow
    """
    meeting_flow = MeetingFlow()
    meeting_flow.plot()
    

if __name__ == '__main__':
    kickoff()