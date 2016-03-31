from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import os
import random


class MonkeyParser:
    ACTION_DICT = {
        'touch': 'touch',
        'swipe': 'swipe',
        'press': 'press',
        'sleep': 'sleep'}

    def __init__(self, file_name):
        self.file_name = file_name
        self.file = None
        self.lines = None
        self.package = None
        self.start_activity = None
        self.device = None
        self.device_width = 800
        self.device_height = 1000

    def set_file(self, file_name):
        self.file_name = file_name

    def get_lines(self):
        lines = []
        f = open(self.file_name)
        for line in iter(f):
            line = line.strip().rstrip()
            if line and (line[0] != "#"):
                lines.append(line)

        f.close()

        return lines

    def run(self):
        self.lines = self.get_lines()

        if len(self.lines) < 2:
            return "Invalid script file."

        self.device = MonkeyRunner.waitForConnection()

        package_name = self.lines[0]
        apk_path = self.device.shell('pm path ' + package_name)
        if apk_path.startswith('package:'):
            self.device.removePackage(package_name)

        self.device.installPackage(package_name)

        self.device_width = int(self.device.getProperty('display.width'))
        self.device_height = int(self.device.getProperty('display.height'))

        print(self.device_width + "   " + self.device_height)

        for i in range(2, len(self.lines)):
            print("haha")
            # parse_line(self.lines[i])

    def parse_line(self, line):
        commands = str(line).split(" ")
        print(commands)

        action = str(commands[0])
        print(action)

        commands = commands[1:len(commands)]

        if action == self.ACTION_DICT['touch']:
            self.parse_touch(commands)
        elif action == self.ACTION_DICT['swipe']:
            self.parse_swipe(commands)
        elif action == self.ACTION_DICT['sleep']:
            self.parse_sleep(commands)
        elif action == self.ACTION_DICT['press']:
            self.parse_press(commands)
        else:
            print("Command " + action + " not available")

    # touch
    # touch 3
    # touch 100,100
    # touch 100,100 200,200 300,300
    # touch 100,100 3
    # touch 100,100 200,200 300,300 3
    def parse_touch(self, commands):
        position_list = []
        # print(commands)

        if len(commands) == 0:
            position_list.append([str(random.randint(1, self.device_width)), str(random.randint(1, self.device_height))])
            return position_list

        last_command = commands[len(commands) - 1]
        # mid_commands = commands[1 : len(commands) - 1]

        if str(last_command).isdigit():
            mid_commands = commands[0: len(commands) - 1]

            if len(mid_commands) == 0:
                for i in range(0, int(last_command)):
                    position_list.append([str(random.randint(1, self.device_width)), str(random.randint(1, self.device_height))])
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


    # positions = []
    #
    # if len(commands) < 2:
    #     positions[0] = [random.randint(1, self.device_width), random.randint(1, self.device_height)]
    #
    # if len(commands) == 2:
    #     if str(commands[1]).isdigit():
    #         for i in range(0, commands[1]):
    #             positions[i] = [random.randint(1, self.device_width), random.randint(1, self.device_height)]
    #     else:
    #         coordinates = str(commands[1]).split(";")
    #         for i in range(0, len(coordinates)):
    #             positions[i] = str(coordinates[i]).split(",")
    # else:
    #     last_command = commands[len(commands) - 1]
    #     mid_commands = commands[1:len(commands) - 1]
    #
    #     if str(last_command).isdigit():
    #         for i in range(0, last_command):
    #             if str(mid_commands[0]).find(self.COMMA) != -1:
    #
    #             for j in range(1, len(mid_commands)):
    #                 if ',' in mid_commands[j]:
    #
    #             positions[i] = [random.randint(1, self.device_width), random.randint(1, self.device_height)]
    #
    #

    # sleep
    # sleep 3
    def parse_sleep(self, commands):
        if len(commands) == 0:
            print("Sleep 1 sec")
        elif len(commands) == 1:
            if not str(commands[0]).isdigit():
                return "Invalid sleep time"
            else:
                print("sleep " + str(commands[0]) + " secs")
        else:
            return "Invalid sleep option"

        return "Sleep command good"

    # swipe
    # swipe 3
    # swipe 100,100 200,200
    # swipe 100,100 200,200 3
    # swipe 100,100 200,200 200,200 300,300
    # swipe 100,100 200,200 200,200 300,300 6
    def parse_swipe(self, commands):
        print("Action = " + "swipe")


    # press
    # press 3
    # press 3 3
    # press 100,100 3 3
    # press 100,100
    def parse_press(self, commands):
        print("Action = " + "press")


cur_dir = os.getcwd()
parser = MonkeyParser("C:/Users/ZhangY/Desktop/demo/sample.txt")
print("### parse_sleep test ###")
print(parser.parse_sleep([]))
print(parser.parse_sleep(["1"]))
print(parser.parse_sleep(["3", "3"]))
print(parser.parse_sleep(["d"]))
print("### parse_sleep test ###\n")

print("### parse_touch test ###")
print(parser.parse_touch([]))
print(parser.parse_touch(["3"]))
print(parser.parse_touch(["100,100"]))
print(parser.parse_touch(["100,100", "200,200"]))
print(parser.parse_touch(["100,100", "200,200", "300,300"]))
print(parser.parse_touch(["100,100", "3"]))
print(parser.parse_touch(["100,100", "3", "3"]))
print(parser.parse_touch(["100,100", "3", "100,100", "3"]))
print(parser.parse_touch(["100,100", "200,200", "300,300", "3"]))
print("### parse_touch test ###")


