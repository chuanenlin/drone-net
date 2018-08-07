# DroneNet

DroneNet is [Joseph Redmon's YOLO real-time object detection system](https://github.com/pjreddie/darknet/) retrained on 2664 images of DJI drones, labeled.</br>
The original and labeled images used for retraining can be found under the **image** and **label** folders respectively.

---

## Setting up

1. Install the [Ubuntu](https://www.ubuntu.com/) Linux distribution.

2. Install [Python 2.7](https://www.python.org/downloads/release/python-2714/)

3. Open terminal and enter the following lines to build [Darknet](https://pjreddie.com/darknet/):
```
git clone https://github.com/pjreddie/darknet.git
cd darknet
make
```

4. Move **yolo-drone.data** under the **cfg** folder.

5. Move **yolo-drone.cfg** under the **cfg** folder.

6. Create a **weights** directory and move **yolo-drone.weights** into the folder.

6. Put **drone.jpg** under the **data** folder.

---

## Running

Open terminal in the root directory of the **darknet** executable and enter:
```
./darknet detector test cfg/yolo-drone.data cfg/yolo-drone.cfg weights/yolo-drone.weights data/drone.jpg
```

---

## Updates
