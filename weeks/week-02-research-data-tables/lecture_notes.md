# Tuần 02 Lecture Notes: Dữ liệu nghiên cứu dưới dạng bảng

## 1. Vấn đề của tuần này

Tuần 01 đã chọn câu hỏi nhỏ. Tuần 02 hỏi tiếp:

```text
Nếu muốn trả lời câu hỏi đó, một dòng dữ liệu sẽ là gì?
```

Một bảng nghiên cứu tốt không bắt đầu từ Python. Nó bắt đầu từ quyết định phương pháp:

- one row = một đơn vị quan sát;
- one column = một biến hoặc thuộc tính;
- one value = thông tin cụ thể trong một ô;
- schema = danh sách cột và ý nghĩa của từng cột.

## 2. Ví dụ theo track

| Track | Một dòng là | Cột bắt buộc |
|---|---|---|
| TCSOL | một bản ghi điểm trước/sau của người học | `learner_id`, `pre_score`, `post_score`, `focus` |
| Đối chiếu | một ví dụ ngữ pháp Hán-Việt kèm ghi chú | `zh_sentence`, `vi_equivalent`, `feature`, `teaching_note` |
| MTPE | một segment dịch có hậu hiệu đính | `zh_source`, `vi_mt`, `vi_postedit`, `local_error_label` |
| Policy | một trích đoạn chính sách đã mã hóa | `doc_id`, `date`, `excerpt`, `theme_code` |

## 3. Python concept: list of dictionaries

Khi đọc CSV bằng `csv.DictReader`, Python có thể tạo ra một danh sách. Mỗi phần tử là một dictionary.

```python
rows = [
    {"track": "TCSOL", "data_unit": "learner pre/post score record"},
    {"track": "MTPE", "data_unit": "translation segment"}
]
```

Ở Week 2, người học chỉ cần hiểu ý tưởng này:

- list = nhiều dòng;
- dictionary = một dòng có tên cột và giá trị;
- key = tên cột;
- value = giá trị trong ô.

## 4. Lỗi thường gặp

| Lỗi | Vì sao nguy hiểm | Cách sửa |
|---|---|---|
| Cột quá mơ hồ | không biết đo cái gì | đổi `result` thành `pre_score`, `post_score` |
| Một dòng chứa quá nhiều thứ | khó phân tích | tách thành đơn vị nhỏ hơn |
| Thiếu source note | paper khó kiểm tra | thêm `source_note` hoặc `access_date` |
| Dữ liệu riêng tư | không thể public | dùng ID ẩn danh và không đưa tên thật |

## 5. Paper bridge

Data description cần nói rõ:

1. dataset dùng cho câu hỏi nào;
2. một dòng đại diện cho điều gì;
3. cột bắt buộc là gì;
4. nguồn dữ liệu và privacy risk;
5. giới hạn của dataset.

Sentence frame:

```text
The dataset is organized at the level of [unit of observation]. Each row contains [required columns], which allows the study to [paper purpose].
```
