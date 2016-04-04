# Monkey
A python cli wrapper for Monkeyrunner.

## Usage
```
$ pip install monkey
$ cd YOUR_DIRECTORY
$ monkey
$ monkey app.apk script.txt
```

## Sample Script
```   
com.domain.app
com.domain.app.activity.SplashActivity

# Action 1
swipe 1100,900 500,900 2
touch 1100,1724
sleep 3

# Action 2 
touch 600,1300
sleep 3
touch 100,100

# Action 3
touch 600,1200
sleep 8
touch 100,100

```  

## Todo
Finish monkey command basic functionality.
