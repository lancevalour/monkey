# Imports the monkeyrunner modules used by this program
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import os

print(__name__)


class Demo:
    def __init__(self):
        pass

    def run(self):

        WORK_DIRECTORY = 'C:/Users/ZhangY/Desktop/demo/'
        PACKAGE = 'com.faro.android.tracker'
        STARTING_ACTIVITY = PACKAGE + '.activity.SplashActivity'
        NUM_TOURGUIDE_PAGES = 3
        NUM_MAIN_TABS = 3

        file_list=os.listdir(WORK_DIRECTORY)
        for _file in file_list:
            if _file.endswith('.png'):
                os.remove(WORK_DIRECTORY + _file)


        # Connects to the current device, returning a MonkeyDevice object
        device = MonkeyRunner.waitForConnection()

        apk_path = device.shell('pm path ' + PACKAGE)
        if apk_path.startswith('package:'):
            device.removePackage(PACKAGE)

        device.installPackage(WORK_DIRECTORY + 'app-debug.apk')

        DEVICE_WIDTH = int(device.getProperty('display.width'))
        DEVICE_HEIGHT = int(device.getProperty('display.height'))

        print(DEVICE_WIDTH, DEVICE_HEIGHT)

        # Start StartingActivity
        device.startActivity(component=PACKAGE + '/' + STARTING_ACTIVITY)
        MonkeyRunner.sleep(1)

        # StartingActivity capture
        result = device.takeSnapshot()
        result.writeToFile(WORK_DIRECTORY +
                           device.getProperty('am.current.comp.class').split('.')[-1]
                           +'.png','png')

        MonkeyRunner.sleep(3)

        # TourGuideActivity capture

        for i in range(0, NUM_TOURGUIDE_PAGES):
            MonkeyRunner.sleep(1)
            result = device.takeSnapshot()
            result.writeToFile(WORK_DIRECTORY +
                               device.getProperty('am.current.comp.class').split('.')[-1]
                               + str(i)
                               + '.png','png')

            drag_length = DEVICE_WIDTH / 2
            device.drag((DEVICE_WIDTH - 10, DEVICE_HEIGHT / 2),
                        (DEVICE_WIDTH - 10 - drag_length, DEVICE_HEIGHT / 2), 0.2)
            MonkeyRunner.sleep(2)

        # Click Tour Guide finish button
        device.touch(DEVICE_WIDTH - 100, DEVICE_HEIGHT -100, MonkeyDevice.DOWN_AND_UP)

        MonkeyRunner.sleep(1)

        # LoginActivity capture

        result = device.takeSnapshot()
        result.writeToFile(WORK_DIRECTORY +
                           device.getProperty('am.current.comp.class').split('.')[-1]
                           + '_login' +'.png','png')
        MonkeyRunner.sleep(1)

        # Click Find Trackers Button
        device.touch(DEVICE_WIDTH / 2, DEVICE_HEIGHT - 600, MonkeyDevice.DOWN_AND_UP)

        MonkeyRunner.sleep(1)

        # FindDevicesActivity capture

        result = device.takeSnapshot()
        result.writeToFile(WORK_DIRECTORY +
                           device.getProperty('am.current.comp.class').split('.')[-1]
                           + '_finddevices' + '.png','png')
        MonkeyRunner.sleep(1)


        # Click FindTrackerActivity back button
        device.touch(100, 100, MonkeyDevice.DOWN_AND_UP)

        MonkeyRunner.sleep(1)

        # Click Login Button
        device.touch(DEVICE_WIDTH / 2, DEVICE_HEIGHT - 700, MonkeyDevice.DOWN_AND_UP)

        MonkeyRunner.sleep(3)

        # MainActivity capture

        for i in range(0, NUM_MAIN_TABS):
            if i is 1:
                # Click Setting Button
                device.touch(DEVICE_WIDTH - 200, 200, MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(2)

                # SettingActivity capture
                result = device.takeSnapshot()
                result.writeToFile(WORK_DIRECTORY +
                                   device.getProperty('am.current.comp.class').split('.')[-1]
                                   +'.png','png')
                MonkeyRunner.sleep(1)

                device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(1)

                
                
            MonkeyRunner.sleep(1)
            result = device.takeSnapshot()
            result.writeToFile(WORK_DIRECTORY +
                               device.getProperty('am.current.comp.class').split('.')[-1]
                               + '_tab' + str(i)
                               + '.png','png')
            MonkeyRunner.sleep(1)

            drag_length = DEVICE_WIDTH / 2
            device.drag((DEVICE_WIDTH - 10, DEVICE_HEIGHT / 2),
                        (DEVICE_WIDTH - 10 - drag_length, DEVICE_HEIGHT / 2), 0.2)
            MonkeyRunner.sleep(2)


        # Click Setting Button
        device.touch(DEVICE_WIDTH - 100, 100, MonkeyDevice.DOWN_AND_UP)

        MonkeyRunner.sleep(2)

        # SettingActivity capture
        result = device.takeSnapshot()
        result.writeToFile(WORK_DIRECTORY +
                           device.getProperty('am.current.comp.class').split('.')[-1]
                           +'.png','png')
        MonkeyRunner.sleep(1)

        # Click SettingActivity back button
        device.touch(100, 100, MonkeyDevice.DOWN_AND_UP)

        MonkeyRunner.sleep(1)


        # Click MainActivity back button
        device.touch(100, 100, MonkeyDevice.DOWN_AND_UP)

        MonkeyRunner.sleep(1)

        # Click Back button
        device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)

        MonkeyRunner.sleep(1)


demo = Demo()
demo.run()


