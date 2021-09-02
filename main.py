from classes.Calendars import Calendars
from example.example_input import example_input, expected_result
from calculations.timestamps_calculations import day_start_and_end_time, multi_range_diff, convert_result_to_dict


def main():
    cals = Calendars(example_input)
    calendars = cals.get_calendars()
    meetings = calendars[0].get_meetings()
    all_meetings = cals.get_all_meetings()
    all_meetings_timestamps = cals.all_meeting_timestamps_list(all_meetings)
    day = day_start_and_end_time(meetings[0].start_time)
    closed = cals.merge_ranges(all_meetings_timestamps)
    diff_range = multi_range_diff([day], closed)
    result = convert_result_to_dict(diff_range)
    print(result)
    print('Example input equals gives example output: ', result == expected_result)


if __name__ == '__main__':
    main()
