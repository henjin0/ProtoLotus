# ProtoLotus 仕様書

## 概要

ProtoLotus は、試作・メイカー向けのパンチングプレート（穴あきプレート）を 3D モデル（STL 形式）として設計・生成するための CAD ユーティリティソフトウェアです。
グリッドベースの GUI 上でブロックの配置を操作し、リアルタイムで 3D プレビューを確認しながら、3D プリント可能な STL ファイルを出力できます。

- GitHub: https://github.com/henjin0/ProtoLotus

## バージョン

- 現バージョン: 0.2.1
- ライセンス: GPLv3
- 著作権: © Inoue Minoru 2022

---

## 対応プラットフォーム

| OS | バージョン |
|----|-----------|
| macOS | Ventura 13.0 以降 |
| Windows 10 | Home / Pro (x64) |
| Windows 11 | Home / Pro (x64) |

---

## 技術スタック

| 役割 | ライブラリ / ツール | バージョン |
|------|-------------------|-----------|
| 言語 | Python | 3.9.1 |
| GUI フレームワーク | PyQt6 | 6.3.0 |
| 3D 可視化 | PyQtGraph (OpenGL) | 0.12.4 |
| 3D メッシュ処理 | numpy-stl / NumPy | 2.17.1 / 1.22.4 |
| OpenGL バインディング | PyOpenGL | 3.1.6 |
| バイナリ配布 | PyInstaller | 5.1 |
| UI 設計 | Qt Designer (.ui) | - |

---

## 主な機能

### 1. ブロックタイプの選択と配置

グリッド上の各セルに 0〜3 の値を設定し、以下のブロックタイプを配置できます。

| ブロック種別 | 説明 | 対応 STL |
|------------|------|---------|
| BU3.2mm | 3mm 穴・標準配置 | BU3.2mm.stl |
| ABU3.2mm | 3mm 穴・斜め配置 | ABU3.2mm.stl |
| NU3.2mm | 3mm 穴・狭幅配置 | NU3.2mm.stl |
| BU4.8mm | 4.8mm 穴・標準配置（LEGO Technic 互換） | BU4.8mm.stl |
| ABU4.8mm | 4.8mm 穴・斜め配置 | ABU4.8mm.stl |
| NU4.8mm | 4.8mm 穴・狭幅配置 | NU4.8mm.stl |
| BUC4.8mm | 4.8mm 角穴・標準配置（Technic 軸対応） | BUC4.8mm.stl |
| ABUC4.8mm | 4.8mm 角穴・斜め配置 | ABUC4.8mm.stl |
| NUC4.8mm | 4.8mm 角穴・狭幅配置 | NUC4.8mm.stl |
| 1x1CBS | LEGO クラシック 1×1 互換ブロック（LEGO_CB 規格） | 1x1CBS.stl |
| 2x2CBS | LEGO クラシック 2×2 互換ブロック（LEGO_CB 規格） | 2x2CBS.stl |
| 2x2CCBS | LEGO クラシック 2×2（円穴）互換ブロック（LEGO_CB 規格） | 2x2CCBS.stl |

各ブロックタイプは `setting/setting.json` で定義されており、参照する STL ファイルのパスが記載されています。

### 2. グリッド操作

- グリッドサイズを X・Y 方向に変更可能（デフォルト 10×10）
- セルをクリックして値を 0〜3 でトグル
- セルを範囲選択した状態で **数字キー 0〜3** を押すと、選択セルを一括入力
- セルの値に応じて色分け表示（9 色）

### 3. リアルタイム 3D プレビュー

- OpenGL ベースの 3D ビューポートでプレートをリアルタイム表示
- セルの編集に連動してメッシュを即座に更新

### 4. 保存・読み込み・エクスポート

- プロジェクトを JSON 形式で保存／読み込み（Ctrl+S / Ctrl+O）
- グリッドの状態を STL ファイルとしてエクスポート（3D プリント用）

---

## ファイル構成

```
ProtoLotus/
├── main.py                              # アプリケーションエントリポイント（app_1 クラス）
├── requirement.txt                      # Python 依存ライブラリ一覧
├── main.spec                            # PyInstaller ビルド設定
├── LICENSE                              # GPLv3 ライセンス
├── README.md                            # ユーザー向けドキュメント
│
├── HolePlateMaker/                      # 3D メッシュ生成モジュール群
│   ├── NumpyArrayToHolePlate.py        # メッシュ生成・GL 操作のコア（OP, GLViewOperation クラス）
│   ├── set32.py                        # 3mm プレートジェネレータ
│   ├── set48.py                        # 4.8mm Technic プレートジェネレータ
│   ├── set48c.py                       # 4.8mm 角穴プレートジェネレータ
│   ├── set1x1ClassicBlock.py           # LEGO 1×1 クラシックブロックジェネレータ
│   ├── set2x2ClassicBlock.py           # LEGO 2×2 クラシックブロックジェネレータ
│   ├── set2x2CircleHoleClassicBlock.py # LEGO 2×2 円穴バリアントジェネレータ
│   ├── addBlock.py                     # メッシュ結合ユーティリティ
│   ├── cube_model.py                   # キューブ形状ジェネレータ
│   ├── mesh_location_zero.py           # メッシュ座標正規化
│   ├── mesh_scale.py                   # メッシュスケーリング
│   ├── mesh_update.py                  # メッシュ更新ユーティリティ
│   └── resourcePath.py                 # リソースファイルパス解決
│
├── ui_files/                            # Qt UI ファイル
│   ├── MainWindow.ui                   # Qt Designer UI 定義
│   └── MainWindow.py                   # pyuic6 による自動生成 Python クラス
│
├── setting/                             # 設定・アセット
│   ├── setting.json                    # ブロック定義（STL パス参照）
│   └── blocks/                         # 事前生成済み STL ブロックモデル（18 ファイル以上）
│
├── icon/                                # アプリアイコン・UI 画像
│   ├── protolotus.png / .icns          # アプリアイコン
│   └── 0.png〜3.png, savefloppy.png…  # ツールバー用アイコン
│
└── readmeImage/                         # README 用スクリーンショット
```

---

## アーキテクチャ

### 設計原則

**画面設定を単一の情報源とする。**
JSON 読み込み → 画面へ反映 → 画面の状態からメッシュ生成 / STL 出力、という一方向のフローを維持する。
STL ファイルやメッシュを直接操作・生成するコードを画面設定を経由せずに書いてはならない。

### アプリケーション層（main.py）

- `app_1` クラス: `QMainWindow` を継承したメインウィンドウ
- グリッドテーブルの管理、セルクリックイベント処理、ツールバーアクションを担当
- OpenGL ウィジェット（`GLViewOperation`）を初期化し、グリッド変更に応じてメッシュを更新
- `tableWidget` にイベントフィルタをインストールし、数字キー入力による一括設定を処理

### 3D メッシュ生成層（HolePlateMaker/）

| クラス / 関数 | 役割 |
|-------------|------|
| `OP` | 個々のブロック配置操作を表現し、OpenGL メッシュをレンダリング |
| `GLViewOperation` | ブロックの追加・削除・変更をリアルタイムで管理 |
| `NumpyArrayToPlate()` | 2D グリッド配列を結合 STL メッシュに変換してエクスポート（for ループで全セルを走査） |
| `set*.py` 各モジュール | ブロック種別ごとの STL 読み込みと座標変換（平行移動・スケーリング） |

### テーブル（OPlist）の構造

OPlist はブロック単位のデータではなく、**ブロックを配置する操作**のリストとして管理される。
現在はメッシュデータの表示管理のみに使用し、STL 出力時は OPlist を参照せず `NumpyArrayToPlate()` でグリッド配列を直接走査する。

`OP` クラスの主なフィールド:

| フィールド | 型 | 説明 |
|-----------|-----|------|
| `row` | int | テーブルの行インデックス |
| `column` | int | テーブルの列インデックス |
| `rowMax` | int | 行の最大インデックス（`shape[0]-1`） |
| `columnMax` | int | 列の最大インデックス（`shape[1]-1`） |
| `rowCount` | int | 行数（`shape[1]`）。ハッシュ計算に使用 |
| `value` | int | セル値（0〜3） |
| `hashValue` | int | 位置を一意に識別するハッシュ（`行 + 行数 × 列`） |
| `glMesh` | GLMeshItem | OpenGL 表示用メッシュ |

### データモデル

- グリッドは 2D NumPy 配列として保持（インデックス順: `[列][行]`）
- セル値 0〜3: 0=空白、1〜3=配置するブロック種別（方向は現状未実装・固定 0）
- ブロックの同一性はハッシュ値（`行 + 行数 × 列`）で管理

#### ブロックの方向（way）

- 方向を持たないブロック: `0` 固定
- 方向を持つブロック: `1`, `2`, `3`, `4` のいずれか
- **現状は方向機能は未実装**（セル値は 0〜3 のブロック種別のみ）

---

## プロジェクトファイル（JSON）フォーマット

ファイルは JSON 形式で保存される。

| キー | 型 | 説明 |
|-----|----|------|
| `tableWidgetDatas` | `number[][]` | グリッドデータ。インデックス順は `[列][行]`、値は 0〜3 |
| `holePatternComboboxValue` | `string` | 選択中のブロックタイプ名 |
| `maxXScaleComboBoxValue` | `string` | グリッドの X サイズ（列数）|
| `maxYScaleComboBoxValue` | `string` | グリッドの Y サイズ（行数）|

> **TODO（未対応）**: キー名 `maxXScaleComboBoxValue` / `maxYScaleComboBoxValue` は意味が分かりにくいため `maxRowComboBoxValue` / `maxColumnComboBoxValue` などへの改名が検討されている。

### 例

```json
{
  "tableWidgetDatas": [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [2, 1, 2, 1, 2, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  ],
  "holePatternComboboxValue": "4.8mm",
  "maxXScaleComboBoxValue": "10",
  "maxYScaleComboBoxValue": "10"
}
```

### 旧フォーマット（後方互換）

`"type"` キーが存在する場合は旧フォーマットとして処理される。
グリッドサイズは 10×10 固定として扱う。

---

## ビルド・配布

```bash
# 依存ライブラリのインストール
pip install -r requirement.txt

# UI ファイルのコンパイル（変更時のみ）
pyuic6 ui_files/MainWindow.ui -o ui_files/MainWindow.py

# バイナリのビルド
pyinstaller main.spec
```

ビルド成果物:
- macOS: `dist/protolotus.app`
- Windows: `dist/protolotus.exe`

---

## 依存ライブラリ一覧

```
numpy
numpy-stl
PyOpenGL
PyQt6
pyqtgraph
pyinstaller
```

---

## 既知の注意事項

- macOS + PyQt6 6.3 の組み合わせで起動時に `qt.qpa.keymapper` 警告が出力されることがある。これは Qt の既知バグであり、アプリの動作には影響しない。
