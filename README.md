# Monkey
A python cli wrapper for Monkeyrunner.

## Usage
```
$ pip install --editable .
$ cd YOUR_DIRECTORY
$ monkey script.txt
```

## Sample Script
```   
com.domain.app
com.domain.app.activity.SplashActivity
    
# Action 1
swipe 100,100 50,100 3
touch 800,1000
sleep 3

# Action 2 
touch 500,600
swipe 100,200 50,200
swipe 50,200 100,200
touch 100,100

# Action 3 
touch 500,500
swipe 100,100 50,100

# Action 4
touch 800,1000
touch 100,100

# Action 5 
swipe 100,100 50,100
```  

## Todo
Finish monkey command basic functionality.
