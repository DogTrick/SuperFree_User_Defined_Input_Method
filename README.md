執行 app.py 即部署上線，進入網頁會提示使用說明。 
\
\
輸入法添加新類別流程：

1. 手動在 ./data/image_store/ 下的 images、deformed_images 中建立資料夾，名稱是接續下去的數字。

2. 在 ./templates 中 create_data.html 的 select 選單中增添新類別。

3. 執行 app.py，製作手寫資料並呈交。

4. 按 ./modules 中的說明製作 csv 文件。

5. 使用 ./predict_model 中的 handwrite_training.py 重新訓練模型。(可修改模型結構)

6. 修改 app.py 中的映射表 lb_map 即完成所有程序。