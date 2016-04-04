# import monkeyrunner only when using cli, for testing MonkeyParser class,
# remove the import.
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import os
import sys
from os.path import dirname
sys.path.append(dirname(__file__))
from monkey_parser import MonkeyParser
import monkey


class MonkeyRun:

    def __init__(self):
        self.__work_dir = None
        self.__apk_file = None
        self.__script_file = None
        self.__device = None

    def __read_temp_file(self):
        f = open(os.path.join(os.path.abspath(os.sep), monkey.temp_file_dir))

        paths = []
        for _line in iter(f):
            _line = _line.strip().rstrip()
            paths.append(_line)
        f.close()

        os.remove(os.path.join(os.path.abspath(os.sep), monkey.temp_file_dir))

        return paths

    def run(self):
        paths = self.__read_temp_file()
        self.__work_dir = paths[0]
        self.__apk_file = paths[1]
        self.__script_file = paths[2]

        parser = MonkeyParser()

        lines = parser.get_lines(self.__script_file)

        if len(lines) < 2:
            return "Invalid script file."

        self.__device = MonkeyRunner.waitForConnection()

        package_name = lines[0]
        starting_activity = lines[1]

        apk_path = self.__device.shell('pm path ' + package_name)
        if apk_path.startswith('package:'):
            self.__device.removePackage(package_name)

        self.__device.installPackage(self.__apk_file)

        device_width = int(self.__device.getProperty('display.width'))
        device_height = int(self.__device.getProperty('display.height'))

        print(str(device_width) + "   " + str(device_height))

        parser.set_device_height(device_height)
        parser.set_device_width(device_width)

        # Start MonkeyRunner procedure
        self.__device.startActivity(component=package_name + '/' + starting_activity)
        self.capture_screen(-1)

        for i in range(2, len(lines)):
            command = parser.parse_line(lines[i])

            action = command[0]
            value = command[1]
            print(value)
            if action == "touch":
                for j in range(0, len(value)):
                    self.capture_screen(str(i) + "_" + str(j))
                    self.__device.touch(int(value[j][0]), int(value[j][1]), MonkeyDevice.DOWN_AND_UP)
            elif action == "swipe":
                for j in range(0, len(value)):
                    self.capture_screen(str(i) + "_" + str(j))
                    self.__device.drag((int(value[j][0][0]), int(value[j][0][1])),
                                       (int(value[j][1][0]), int(value[j][1][1])), 0.2)

            elif action == "sleep":
                MonkeyRunner.sleep(int(value))

    def capture_screen(self, index):
        MonkeyRunner.sleep(1)
        screenshot = self.__device.takeSnapshot()
        screenshot.writeToFile(self.__work_dir +
                               self.__device.getProperty('am.current.comp.class').split('.')[-1] +
                               str(index) + '.png', 'png')

monkey_run = MonkeyRun()
monkey_run.run()


