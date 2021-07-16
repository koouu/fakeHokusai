# フェイク北斎

初めてのハッカソン ～オンライン開発合宿vol.3～

* python 3.7.10
* pytorch 1.8.0
* torchaudio 0.8.0
* torchvision 0.9.0
* cuda 10.2

使い方

以下のURLから変換モデルをダウンロードしてください

cpu用
https://drive.google.com/file/d/1UJyj5q1o-A-AnHabFfA08ivw6F6I0xSR/view?usp=sharing

gpu用
https://drive.google.com/file/d/1CKZD36aol6KZsfWibiY3aI9-1MWJCU24/view?usp=sharing


model.ptをmodelフォルダの中に入れてください。

```
python main.py
```

立ち上がったローカルサーバーにアクセス  

http://127.0.0.1:5000/upload

画像をアップロードし変換


変換だけしたい場合

dataset/picture2art/testAの中にある画像をすべて変換します

```
python test.py  
```









