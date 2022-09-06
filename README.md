# SuperFree User Defined Input Method

這是一個基於AI影像辨識的「自定義」輸入法！用戶可以為所有字母、符號定義手勢，客製化屬於自己的輸入法！
## 功能
1. 為新輸入定義手勢，並存入資料庫以訓練AI模型。
2. 使用訓練完畢的輸入法進行寫作。
## 使用方法
執行 main.py 即可，進入頁面會提示使用說明。 
\
輸入法添加新類別流程：

1. 手動在 ./data/image_store/ 下的 images、deformed_images 中建立資料夾，名稱是接續下去的數字。

2. 在 ./templates 中 create_data.html 的 select 選單中增添新類別。

3. 執行 main.py，製作手寫資料並呈交。

4. 按 ./modules 中的說明製作 csv 文件。

5. 使用 ./predict_model 中的 handwrite_training.py 重新訓練模型。(可修改模型結構)

6. 修改 main.py 中的映射表 lb_map 即完成所有程序。