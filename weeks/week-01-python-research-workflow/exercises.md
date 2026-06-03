# Tuần 01 Exercises

## Core Exercise A: Copy and Modify

Mở `live_coding.ipynb`. Tìm cell có các biến này:

```python
my_name = "Your name"
my_research_area = "TCSOL"
my_topic = "short-term Chinese teaching"
```

Chỉ sửa phần text nằm trong dấu ngoặc kép để phù hợp với hướng bạn quan tâm.

Chạy cell. Sau đó viết một câu:

```text
My current research area is ..., and I want to study ...
```

Bạn có thể viết câu này bằng tiếng Việt hoặc English.

## Core Exercise B: Guided Problem

Dùng dataset `data/raw/week01_research_tracks.csv`.

Hoàn thành các việc sau trong notebook:

1. Đếm có bao nhiêu hướng nghiên cứu.
2. In tên từng hướng.
3. Chọn một hướng gần nhất với dự định học Master của bạn.
4. Copy câu hỏi nghiên cứu nhỏ của hướng đó vào notebook.

Code đọc CSV là code mẫu. Tuần này nhiệm vụ của bạn là chạy và đọc output, chưa cần hiểu mọi ký hiệu.

Checklist:

- [ ] Tôi đã chạy cell đọc CSV.
- [ ] Tôi thấy có bốn dòng.
- [ ] Tôi giải thích được một dòng nghĩa là gì.
- [ ] Tôi đã chọn một hướng nghiên cứu.

## Core Exercise C: Research-Style Task

Đây là bản nháp memo sẽ nộp trong assignment, không phải một memo riêng thứ hai.

Viết 100-150 từ trả lời:

```text
Hướng nghiên cứu nào hữu ích nhất cho việc học Master của bạn, và bạn cần dữ liệu gì trước tiên?
```

Đoạn viết nên có:

- một hướng nghiên cứu;
- một câu hỏi nhỏ;
- một dataset có thể cần;
- một hạn chế.

## Stretch Exercise

Thêm một dòng mới vào **bản sao** của tệp CSV. Dòng mới nên mô tả một project bạn thật sự có thể muốn làm.

Cột gợi ý:

- `track_id`
- `track`
- `broad_interest`
- `small_research_question`
- `unit_of_observation`
- `starter_dataset`
- `likely_output`
- `beginner_python_task`

Không sửa file raw gốc. Lưu bản sao thành:

```text
data/processed/week01_my_research_track.csv
```
