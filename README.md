# SuperFree User Defined Input Method

Here is the translation:

---

This is a "customized" input method based on AI image recognition! Users can define gestures for all letters and symbols to customize their own input method!

**Features:**
- Define gestures for new inputs and store them in a database to train an AI model.
- Use the trained input method for writing.

**Instructions:**
Run `main.py` to begin. Instructions will be provided upon entering the page.

**Adding a new category for the input method:**
1. Manually create folders named with consecutive numbers in `./data/image_store/images` and `./data/image_store/deformed_images`.
2. Add the new category to the menu `select` in `./templates/create_data.html`.
3. Run `main.py`, create handwritten data, and submit it.
4. Follow the instructions in `./modules` to create a CSV file.
5. Use `handwrite_training.py` in `./predict_model` to retrain the model (modifications to the model structure are possible).
6. Modify the mapping table `lb_map` in `main.py` to complete the process.

這是一個基於AI影像辨識的「自定義」輸入法！用戶可以為所有字母、符號定義手勢，客製化屬於自己的輸入法！
## 功能
1. 為新輸入定義手勢，並存入資料庫以訓練AI模型。
2. 使用訓練完畢的輸入法進行寫作。
## 使用方法
執行 `main.py` 即可，進入頁面會提示使用說明。 
\
輸入法添加新類別流程：

1. 手動在 `./data/image_store/` 下的 `images`、`deformed_images` 中建立資料夾，名稱是接續下去的數字。

2. 在 `./templates` 中 `create_data.html` 的 `select` 選單中增添新類別。

3. 執行 `main.py`，製作手寫資料並呈交。

4. 按 `./modules` 中的說明製作 CSV 文件。

5. 使用 `./predict_model` 中的 `handwrite_training.py` 重新訓練模型。(可修改模型結構)

6. 修改 `main.py` 中的映射表 `lb_map` 即完成所有程序。