from crews.meeting_crew import MeetingAssistantCrew

def load_meeting_notes(path="data/meeting_transcript.txt"):
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo não encontrado: {path}")
    

def generate_tasks_meeting(transcript):
    output = (
        MeetingAssistantCrew()
        .crew()
        .kickoff(
            inputs={'transcript': transcript}
        )
    )
    
    tasks = output["tasks"]
    return tasks

content = load_meeting_notes()
tasks = generate_tasks_meeting(transcript=content)
print(tasks)