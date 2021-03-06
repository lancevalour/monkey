# import monkeyrunner only when using cli, for testing MonkeyParser class,
# remove the import.
import random
import sys
from os.path import dirname
sys.path.append(dirname(__file__))


class MonkeyParser:
    ACTION_DICT = {
        'touch': 'touch',
        'swipe': 'swipe',
        'press': 'press',
        'sleep': 'sleep'}

    def __init__(self):
        self.__device_width = 600
        self.__device_height = 800

    def set_device_width(self, device_width):
        self.__device_width = device_width

    def set_device_height(self, device_height):
        self.__device_height = device_height

    def get_device_width(self):
        return self.__device_width

    def get_device_height(self):
        return self.__device_height

    def get_lines(self, script_file):
        lines = []
        f = open(script_file)
        for line in iter(f):
            line = line.strip().rstrip()
            if line and (line[0] != "#"):
                lines.append(line)

        f.close()
        return lines

    def parse_line(self, line):
        commands = str(line).split(" ")

        action = str(commands[0])

        commands = commands[1:len(commands)]

        if action == self.ACTION_DICT['touch']:
            print("action: " + action)
            return [action, self.parse_touch(commands)]
        elif action == self.ACTION_DICT['swipe']:
            print("action: " + action)
            return [action, self.parse_swipe(commands)]
        elif action == self.ACTION_DICT['sleep']:
            print("action: " + action)
            return [action, self.parse_sleep(commands)]
        elif action == self.ACTION_DICT['press']:
            print("action: " + action)
            return [action, self.parse_press(commands)]
        else:
            print("Command " + action + " not available")

        return []

    # sleep
    # sleep 3
    def parse_sleep(self, commands):
        if len(commands) == 0:
            print("Sleep 1 sec")
            return 1
        elif len(commands) == 1:
            if not str(commands[0]).isdigit():
                return "Invalid sleep time"
            else:
                print("sleep " + str(commands[0]) + " secs")
                return str(commands[0])

        return "Invalid sleep option"

    # touch 3
    # touch 100,100
    # touch 100,100 200,200 300,300
    # touch 100,100 3
    # touch 100,100 200,200 300,300 3
    def parse_touch(self, commands):
        position_list = []
        # print(commands)

        if len(commands) == 0:
            position_list.append([str(random.randint(1, self.__device_width)),
                                  str(random.randint(1, self.__device_height))])
            return position_list

        last_command = commands[len(commands) - 1]
        # mid_commands = commands[1 : len(commands) - 1]

        if str(last_command).isdigit():
            mid_commands = commands[0: len(commands) - 1]

            if len(mid_commands) == 0:
                for i in range(0, int(last_command)):
                    position_list.append([str(random.randint(1, self.__device_width)),
                                          str(random.randint(1, self.__device_height))])
            else:
                for i in range(0, int(last_command)):
                    for j in range(0, len(mid_commands)):
                        position = str(mid_commands[j]).split(",")
                        if len(position) == 2 and str(position[0]).isdigit() and str(position[1]).isdigit():
                            position_list.append(str(mid_commands[j]).split(","))
                        else:
                            return "Invalid touch position"
        else:
            mid_commands = commands[0: len(commands)]

            for i in range(0, len(mid_commands)):
                position = str(mid_commands[i]).split(",")
                if len(position) == 2 and str(position[0]).isdigit() and str(position[1]).isdigit():
                    position_list.append(str(mid_commands[i]).split(","))
                else:
                    return "Invalid touch position"

        return position_list

    # swipe
    # swipe 3
    # swipe 100,100 200,200
    # swipe 100,100 200,200 3
    # swipe 100,100 200,200 200,200 300,300
    # swipe 100,100 200,200 200,200 300,300 6
    def parse_swipe(self, commands):
        position_list = []

        if len(commands) == 0:
            position_list.append(
                [[str(random.randint(1, self.__device_width)), str(random.randint(1, self.__device_height))],
                 [str(random.randint(1, self.__device_width)), str(random.randint(1, self.__device_height))]])
            return position_list

        last_command = commands[len(commands) - 1]

        if str(last_command).isdigit():
            mid_commands = commands[0: len(commands) - 1]

            if len(mid_commands) == 0:
                for i in range(0, int(last_command)):
                    position_list.append(
                        [[str(random.randint(1, self.__device_width)), str(random.randint(1, self.__device_height))],
                         [str(random.randint(1, self.__device_width)), str(random.randint(1, self.__device_height))]])
            elif len(mid_commands) % 2 == 0:
                for i in range(0, int(last_command)):
                    for j in range(0, len(mid_commands), 2):
                        start = str(mid_commands[j]).split(",")
                        stop = str(mid_commands[j + 1]).split(",")
                        if len(start) == 2 and str(start[0]).isdigit() and str(start[1]).isdigit()\
                                and len(stop) == 2 and str(stop[0]).isdigit() and str(stop[1]).isdigit():
                            position_list.append([start, stop])
                        else:
                            return "Invalid swipe position"
            else:
                return "Invalid swipe position pair"
        else:
            mid_commands = commands[0: len(commands)]
            if len(mid_commands) % 2 == 0:
                for i in range(0, len(mid_commands), 2):
                    start = str(mid_commands[i]).split(",")
                    stop = str(mid_commands[i + 1]).split(",")
                    if len(start) == 2 and str(start[0]).isdigit() and str(start[1]).isdigit() \
                            and len(stop) == 2 and str(stop[0]).isdigit() and str(stop[1]).isdigit():
                        position_list.append([start, stop])
                    else:
                        return "Invalid swipe position"

            else:
                return "Invalid swipe position pair"

        return position_list

    # press
    # press 3
    # press 3 3
    # press 100,100 3 3
    # press 100,100
    def parse_press(self, commands):
        print("Action = " + "press")



# print("### parse_sleep test ###")
# print(parser.parse_sleep([]))
# print(parser.parse_sleep(["1"]))
# print(parser.parse_sleep(["3", "3"]))
# print(parser.parse_sleep(["d"]))
# print("### parse_sleep test ###\n")
#
# print("### parse_touch test ###")
# print(parser.parse_touch([]))
# print(parser.parse_touch(["3"]))
# print(parser.parse_touch(["100,100"]))
# print(parser.parse_touch(["100,100", "200,200"]))
# print(parser.parse_touch(["100,100", "200,200", "300,300"]))
# print(parser.parse_touch(["100,100", "3"]))
# print(parser.parse_touch(["100,100", "3", "3"]))
# print(parser.parse_touch(["100,100", "3", "100,100", "3"]))
# print(parser.parse_touch(["100,100", "200,200", "300,300", "3"]))
# print("### parse_touch test ###\n")

#
# print("### parse_swipe test ###")
# print(parser.parse_swipe([]))
# print(parser.parse_swipe(["3"]))
# print(parser.parse_swipe(["100,100"]))
# print(parser.parse_swipe(["100,100", "200,200"]))
# print(parser.parse_swipe(["100,100", "200,200", "3"]))
# print(parser.parse_swipe(["100,100", "200,200", "300,300"]))
# print(parser.parse_swipe(["100,100", "200,200", "300,300", "400,400"]))
# print(parser.parse_swipe(["100,100", "200,200", "300,300", "400,400", "3"]))
# print(parser.parse_swipe(["100,100", "3"]))
# print(parser.parse_swipe(["100,100", "3", "3"]))
# print(parser.parse_swipe(["100,100", "3", "100,100", "3", "3"]))
# print(parser.parse_swipe(["100,100", "200,200", "3", "3"]))
# print("### parse_swipe test ###\n")

# f = open(os.path.join(os.path.abspath(os.sep), monkey.temp_file_dir))
# paths = []
# for _line in iter(f):
#     _line = _line.strip().rstrip()
#     paths.append(_line)
# f.close()
#
# os.remove(os.path.join(os.path.abspath(os.sep), monkey.temp_file_dir))
#
# parser = MonkeyParser(paths[0], paths[1])
# parser.parse_line(parser.get_lines()[3])
#
#
