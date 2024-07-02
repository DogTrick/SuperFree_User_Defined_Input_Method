### After obtaining custom-written images from the backend, follow these steps:

1. Use `deform_img.py` to deform the custom-written images.

2. Use `img2csv.py` to convert and integrate all images (deformed and original) into a CSV file.

3. Use `merge_datasets.py` to merge all CSV datasets (original and custom-written) and split them into training and testing sets.

**Caution:** Use `reset_dir.py` to clear all custom-written image datasets. Use with caution!

### 後端取得自寫圖片後，可按以下順序操作：

1. 使用 `deform_img.py` 將自寫圖片變形。

2. 使用 `img2csv.py` 將所有圖片(變形&無變形)轉換並統合為 CSV file。

3. 使用 `merge_datasets.py` 將所有 CSV 資料集(原有&自寫)合併，且分作訓練集與測試集。

**使用 `reset_dir.py` 可清空所有自寫圖片資料集，慎用！**