### 後端取得自寫圖片後，可按以下順序操作：

1. 使用 deform_img.py 將自寫圖片變形。

2. 使用 img2csv.py 將所有圖片(變形&無變形)轉換並統合為 csv file。

3. 使用 merge_datasets.py 將所有csv資料集(原有&自寫)合併，且分作訓練集與測試集。

**使用 reset_dir.py 可清空所有自寫圖片資料集，慎用！**