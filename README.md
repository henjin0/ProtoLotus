# 先にお読みください。
このライブラリは個人的に作られたプログラムです。 当ソフトウェアによって作成された成果物と互換する製品の製造者との関係は一切ございません。また、当ソフトウェアおよび当ソフトウェアにより作成された成果物に起因するいかなる賠償要求や損失に対し、当ソフトウェアの作者はその責任を一切負わないものとします。

当ライブラリのライセンスはPyQtを使用している都合から[GPLv3ライセンス](LICENSE)に準拠します。

# ProtoLotus
穴を等間隔に開けた工作用プレートの3Dデータ(STLファイル)を自作できるソフトウェアです。
現在はネジ止め等に有効な3 mm穴とデンマークの某有名ブロックと互換する4.8 mm穴が作成できます。

# 実行方法(バイナリから)
直下にあるバイナリファイルをダブルクリックして実行してください。
```
mac: protolotus.app
（作成予定）windows: protolotus.exe
```

# 実行方法(pythonから)
```shell:version
Python 3.9.1
pip 22.1.2 
```

pullしたパッケージ中でpython -m venv \[仮想環境名\]を実行し、仮想環境を先につくってください。作成した仮想環境に入ったあとに下記コマンドでpythonパッケージをインストールしてください。
インストールできない場合にはpip3 install -U pipを実行してpipをアップデートしてください。

```shell:install
pip3 install -U pip
pip3 install -r requirements.txt
```

その後、下記コマンドでmain.pyを実行するとソフトウェアが立ち上がります。
```shell:install
python main.py
```

# バイナリのビルド方法
上記の実行方法(pythonから)を実施したあとに下記コマンドを実行してください。

```shell:build
pyinstaller main.spec  
```

# 操作方法
<img width="600" alt="ツール実行画面" src="readmeImage/tutorial.png">


# LICENSE
Please read [LICENSE](LICENSE).
