# robosys_ros
robosys2016のROS課題

#動作
4個のLEDが流れるように点滅を繰り返す．

#使い方
1. $ roscore &
2. $ rosrun robosys_ros led_flusher.py &
3. $ rosrun robosys_ros led_pub.py

4. ctrl c
5. $ fg
6. ctrl c
7. $ fg
8. ctrl c
9. echo 0 2 4 6 > /dev/myled0

#動画リンク
