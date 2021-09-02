from classes.Calendar import Calendar


class Calendars:
    def __init__(self, calendars: list):
        self.calendars = calendars

    def get_calendars(self):
        calendars_list = []
        for cal in self.calendars:
            calendar = Calendar(cal['name'], cal['meetings'])
            calendars_list.append(calendar)
        return calendars_list

    def get_all_meetings(self):
        cals = self.get_calendars()
        all_meet = []
        for i in range(len(cals)):
            all_meet = all_meet + cals[i].get_meetings()
        return all_meet

    @classmethod
    def all_meeting_timestamps_list(cls, all_meetings_list):
        all_meetings_timestamps = [(x.start_time, x.end_time) for x in all_meetings_list]
        return all_meetings_timestamps

    @classmethod
    def merge_ranges(cls, meetings):
        if len(meetings) == 0:
            return meetings
        meetings.sort(key=lambda x: x[0])
        merged_list = [(meetings[0])]
        for current_start_time, current_end_time in meetings[1:]:
            # check if the current start time is less than the end time of the latest end time in the merged list
            last_merged_start, last_merged_end = merged_list[-1]
            if current_start_time <= last_merged_end:
                merged_list[-1] = (last_merged_start, max(current_end_time, last_merged_end))
            else:
                merged_list.append((current_start_time, current_end_time))
        return merged_list