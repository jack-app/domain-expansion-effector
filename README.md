# 領域展開エフェクター

## 概要

呪術会戦に登場する「領域展開」を再現するエフェクター。
リアルタイムでカメラに映る手の形を判定し、特定の形になったらカメラに写っている映像にエフェクトを付けます。

## 環境構築

### 推奨環境
- uv : 0.5.26

### セットアップ
Linux上で行う

1. このリポジトリをクローンする

2. uvをインストールする

    ``` curl -LsSf https://astral.sh/uv/install.sh | sh ```

    を実行。

    インストール後に`exec $SHELL -l`などでshellを再読み込みした後、

    ```uv --version```

    を実行し、バージョンが表示されるか確認する。

3. ` uv sync `　
    を実行。
