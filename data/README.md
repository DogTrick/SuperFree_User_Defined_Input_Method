# 各資料夾解說：

* emnist_balanced 是手寫數字、字母的大雜燴。
訓練集每個類別有2400個實例，測試集每個類別有400個實例。(balanced 意味每個類別數目相當)
但須注意部分字母並無小寫類別，因這些字母大小寫相似，一律歸為大寫類別。因檔案過大，有請網上自行搜索。

* image_store 中，images 存放使用者手寫的各類別圖片，deformed_images 存放這些圖片變形後的模樣。

* new_datasets 存放 image_store 所有圖片轉化得到的 csv 檔案。(一張圖片為一列)

* merged_datasets 存放 new_datasets 與 emnist_balanced 的資料合併得到的總資料集，並拆分為訓練集與驗證集。

* temp_img 與資料庫擴建無關，僅用以存放使用輸入法時的暫存圖片。