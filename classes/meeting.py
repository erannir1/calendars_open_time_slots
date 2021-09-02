class Meeting:
    def __init__(self, start_time, end_time, subject, meeting_id: int):
        self.subject = subject
        self.start_time = start_time
        self.end_time = end_time
        self.meeting_id = meeting_id
