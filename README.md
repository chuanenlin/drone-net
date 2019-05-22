# DroneNet

DroneNet is [Joseph Redmon's YOLO real-time object detection system](https://github.com/pjreddie/darknet/) retrained on 2664 images of DJI drones, labeled.</br>
The original and labeled images used for retraining can be found under the **image** and **label** folders respectively.

---

## Setting up

1. Install the [Ubuntu](https://www.ubuntu.com/) Linux distribution.

2. Open terminal and enter the following lines to build [Darknet](https://pjreddie.com/darknet/):
```
git clone https://github.com/pjreddie/darknet.git
cd darknet
make
```

> **Note**: if you are using another variant of Darknet (e.g [AlexeyAB fork](https://github.com/AlexeyAB/darknet)), the labels are in a different format. Original Yolo uses absolute coordinates to indicate the target box in the image, whereas AlexeyAB (and others) adopts relative coordinates. Depending on your version, the appropriate labels can be found in the directory `labels` (absolute coords) or `normalized-labels` (relative). Of course, images remain the same. |

3. Move **drone.data**, **drone.names**, and **yolo-drone.cfg** under the **cfg** folder, create a **weights** directory and move **yolo-drone.weights** into the folder, move **drone.jpg** under the **data** folder, and move **test.txt** and **train.txt** in the root directory of your cloned darknet.

4. Change lines 2 and 3 to your path in **drone.data**.

---

## Running

Open terminal in the root directory of the **darknet** executable and enter:
```
./darknet detector test cfg/drone.data cfg/yolo-drone.cfg weights/yolo-drone.weights data/drone.jpg
```

---

## Updates
