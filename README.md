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


## label studio

こっち採用したい

### 起動
```
$ docker run -it -p 8081:8080 -v `pwd`/mydata:/label-studio/data heartexlabs/label-studio:latest
```


### annotationの更新

patchじゃないんか。。。（部分更新できると思ってたが違うっぽい？

```
$ curl localhost:8081/api/annotations/14 -H 'Content-type: application/json' -H 'Authorization: Token ${token}' -XPATCH \
    -d '{
        "result": [{
            "value": {
                "x": 31.733333333333333,
                "y": 2.664298401420959,
                "width": 54.66666666666667,
                "height": 93.42806394316163,
                "rotation": 0,
                "rectanglelabels": [
                    "godzilla"
                ]
            },
            "id": "_bKlx5nTr_",
            "from_name": "label",
            "to_name": "image",
            "type": "rectanglelabels"
        }]
    }' | jq .
```

### pre annotationのやり方

1. label studioへ画像をアップロード
2. api経由でそれぞれ取得 → vision apiでアノテーション
3. label studioへpost