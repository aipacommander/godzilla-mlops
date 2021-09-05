# godzilla-mlops

## labelimg

```
docker run -it \
--user $(id -u) \
-e DISPLAY=unix$DISPLAY \
--workdir=$(pwd) \
--volume="/Users/$USER:/Users/$USER" \
--volume="/etc/group:/etc/group:ro" \
--volume="/etc/passwd:/etc/passwd:ro" \
--volume="/etc/shadow:/etc/shadow:ro" \
--volume="/etc/sudoers.d:/etc/sudoers.d:ro" \
-v /tmp/.X11-unix:/tmp/.X11-unix \
tzutalin/py2qt4
```

↑できんかった（多分macじゃ動かない？？？）


```
$ brew install qt
$ brew install libxml2
$ cd labelImg
$ make qt5py3  # 失敗
$ pip3 install pyqt5 lxml
$ make qt5py3  # 成功
$ python3 labelImg.py  # 起動した!
```