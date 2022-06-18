def three_line_keyboard_generation(keyboard_of_unit_time, unit_of_time):
    count_of_unit_time = 0
    three_unit_time_for_line = []
    for unit in unit_of_time:
        if count_of_unit_time == 3:
            keyboard_of_unit_time.keyboard.append(three_unit_time_for_line)
            three_unit_time_for_line = []
            count_of_unit_time = 0
        three_unit_time_for_line.append(unit)
        count_of_unit_time += 1
    if len(three_unit_time_for_line) != 0:
        keyboard_of_unit_time.keyboard.append(three_unit_time_for_line)

