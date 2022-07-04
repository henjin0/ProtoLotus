# 先にお読みください。
このソフトウェアは個人的に作られたプログラムです。 当ソフトウェアによって作成された成果物と互換する製品の製造者との関係は一切ございません。また、当ソフトウェアおよび当ソフトウェアにより作成された成果物に起因するいかなる賠償要求や損失に対し、当ソフトウェアの作者はその責任を一切負わないものとします。

当ソフトウェアのライセンスはPyQtを使用している都合から[GPLv3ライセンス](LICENSE)に準拠します。

# ProtoLotus
穴を等間隔に開けた工作用プレートの3Dデータ(STLファイル)を自作できるソフトウェアです。
現在はネジ止め等に有効な3 mm穴とデンマークの某有名ブロックと互換する4.8 mm穴が作成できます。

# 実行方法(バイナリから)
現状だとmacOSとwindowsに対応しています。

### 動作確認OS

```
macOS: macOS Monterey version 12.4
windows: windows10 home x64
```

下記リンクからprotolotus_mac.zip/protolotus_windows.zipをDL&解凍してからご使用ください。

- macOS: https://drive.google.com/file/d/1yv45yj994fWbZyLL3cdTaLUU6_mYVVMA/view?usp=sharing

- windows: https://drive.google.com/file/d/1V7xl3M2dNVlaRSv-9Kjr9bmF9mCM0qSJ/view?usp=sharing

### macOS版の注意

アプリの取得元不明で実行できないため、先に**システム環境設定>セキュリティとプライバシー**から設定を許可してください。

<img width="600" alt="ツール実行画面" src="readmeImage/allowsetting.png">

### windows版の注意

「危害を及ぼす可能性～」という警告が出てきますが、無視して継続してDLしてください。

<img width="600" alt="ツール実行画面" src="readmeImage/windows_caution.png">

### バイナリファイル名
```
mac: protolotus.app
windows: protolotus.exe
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
事前に上記の実行方法(pythonから)を実施してください。

本プログラムでは.uiファイルは直接使っておらず、.pyファイルへ変換する必要があります。
画面を作成した場合は下記コマンドを参考に.uiファイルを.pyファイルを変換してください。
（venv環境を適用していればコマンドが使用できる。）

```shell:make_ui
pyuic6 ui_files/MainWindow.ui -o MainWindow.py
```

最後に下記コマンドを実行することでdistフォルダにバイナリファイル(main.app or main.exe)を作成することができます。

```shell:build
pyinstaller main.spec  
```

# 操作方法
<img width="600" alt="ツール実行画面" src="readmeImage/tutorial.png">


# LICENSE
Please read [LICENSE](LICENSE).
