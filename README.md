# RedisTimeSeries Basic Demos

A set of basic demoes showcasing the integration of RedisTimeSeries with Prometheus and Grafana.

## Setup
```
$ docker-compose up --force-recreate --build
```

## Demos
Open a second terminal for running the demoes:
```
$ pip install -r requirements.txt
```

Open your browser to grafana
[http://localhost:3000](http://localhost:3000)

Default username and passwords are:
 - username: `admin`
 - password: `admin`

### Demo 1: weather station under `/weather_station`
```
$ python3 weather_station/sensors.py
```
This script will add random measurements for temperature and humidity for a number of sensors.
![Weather Station](/img/sensors.png)

### Demo 2: Page view visitors counting under `/counters`
```
$ python3 counters/viewer.py
```
This script will randomly increment the number of page views on certain endpoints and regions.
![Page Views](/img/views.png)
Open up a third terminal and inspect the keys
```
127.0.0.1:6379> keys *
 1) "view:/post/3:China"
 2) "view:/post/2:US"
 3) "view:/post/1:MiddleEast"
 4) "view:/post/1:China"
 5) "view:/home:China"
 6) "view:/post/1:US"
 7) "view:/home:MiddleEast"
 8) "view:/post/3:US"
 9) "view:/post/1:EU"
10) "view:/post/3:EU"
11) "view:/post/2:EU"
12) "view:/post/2:China"
13) "view:/home:EU"
14) "view:/post/2:MiddleEast"
15) "view:/post/3:MiddleEast"
16) "view:/home:US"
127.0.0.1:6379> ts.get view:/post/3:China
1) (integer) 1559899314
2) "43352"
```
