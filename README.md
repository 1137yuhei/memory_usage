# memory_usage
メモリ使用率をトピックから出力するROS2のパッケージです。

[![test](https://github.com/1137yuhei/Memory_Usage/actions/workflows/test.yml/badge.svg)](https://github.com/1137yuhei/Memory_Usage/actions/workflows/test.yml)

##  ノード概要

###  MemoryUsagePiblisherノード

- ```MemoryUsagePiblisher```ノードはシステムのメモリの使用率を1秒ごとに計測し、トピックにパブリッシュします。

###  listenerノード

- テスト用
- メッセージをサブスクライブして受け取ります。

##  トピック

###  memory_usageトピック

  このトピックはFloat64型のメッセージを受け取ることができます。

## テスト環境

- ubuntu 22.04 LTS
- ROS2 Humble

## 使用方法

### パッケージのセットアップ

  psutilをインストールします。（インストールされていない方のみ）
```
sudo apt install python3-pip
pip install psutil
```

###  ノードの実行

  以下のコマンドをターミナルで実行します。（何も表示されません。）

```
ros2 run memory_usage memory_usage_publisher
```

###  listenerを使用したテスト結果
　以下のコマンドを別の端末のターミナルで実行してテストをしました。
```
ros2 run memory_usage listener
```
```
[INFO] [1736054915.031510683] [memory_listener]: Memory_listener: 8.9%
[INFO] [1736054916.032067852] [memory_listener]: Memory_listener: 8.9%
[INFO] [1736054917.031301668] [memory_listener]: Memory_listener: 8.9%
[INFO] [1736054918.031673777] [memory_listener]: Memory_listener: 8.9%
[INFO] [1736054919.031690321] [memory_listener]: Memory_listener: 8.9%
[INFO] [1736054920.031189195] [memory_listener]: Memory_listener: 8.9%
[INFO] [1736054921.031777313] [memory_listener]: Memory_listener: 8.9%
[INFO] [1736054922.031720671] [memory_listener]: Memory_listener: 8.9%
...
```
## テストに使用したコンテナ  
上田教授の[コンテナ](https://hub.docker.com/repository/docker/ryuichiueda/ubuntu22.04-ros2)を使用させていただきました。
## ライセンス
- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます.
- このパッケージのコードの一部は，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
    - [ryuichiueda/slides_marp/robosys2024](https://github.com/ryuichiueda/slides_marp/tree/master/robosys2024)
- ©2024 Mitsuno Yuhei
