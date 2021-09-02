from classes.meeting import Meeting
from calculations.timestamps_calculations import convert_str_to_timestamp


class Calendar:
    def __init__(self, name: str, meetings_list: list):
        self.name = name
        self.meetings_list = meetings_list

    def get_meetings(self):
        meetings_object_list = []
        for meeting_id, meet in enumerate(self.meetings_list):
            meeting_start_time = convert_str_to_timestamp(meet['startTime'])
            meeting_end_time = convert_str_to_timestamp(meet['endTime'])
            calendar = Meeting(meeting_start_time, meeting_end_time, meet['subject'], meeting_id)
            meetings_object_list.append(calendar)
        return meetings_object_list

    @classmethod
    def sort_meetings_by_start_time(cls, meetings_object_list):
        sorted_meetings_list = meetings_object_list.sort(key=lambda x: x.start_time)
        return sorted_meetings_list