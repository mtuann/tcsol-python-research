# Tuần 01 Lecture Notes: Python như một quy trình nghiên cứu

## Ý chính

Python không phải là mục tiêu của khóa học. Python là công cụ giúp công việc nghiên cứu rõ ràng hơn, có thể kiểm tra lại, và dễ chuyển thành bằng chứng trong paper.

Với hướng học của bạn, Python thường giúp bốn việc:

1. tổ chức dữ liệu từ lớp học, bài kiểm tra, khảo sát, bài dịch, hoặc văn bản chính sách;
2. kiểm tra dữ liệu thay vì đếm thủ công hoặc dựa vào trí nhớ;
3. tạo bảng hoặc hình;
4. viết phần Methods và Results minh bạch hơn.

## Jupyter Notebook là gì?

Jupyter notebook có hai loại ô quan trọng.

| Loại ô | Dùng để làm gì |
|---|---|
| Markdown | Viết giải thích, tiêu đề, câu hỏi nghiên cứu, caption, và diễn giải. |
| Code | Chạy lệnh Python. |

Một notebook nghiên cứu tốt nên đọc giống một bản nháp paper nhỏ:

```text
câu hỏi nghiên cứu
nguồn dữ liệu
code
bảng hoặc hình
caption
diễn giải
hạn chế
```

Tuần 01 chưa cần Word/Zotero hoặc Overleaf. Bạn viết ngay trong Markdown cell để tập thói quen: mỗi output nhỏ đều phải có câu giải thích. Các công cụ viết paper sẽ được thêm dần sau khi bạn đã có dữ liệu, bảng, hình và nguồn trích dẫn.

## Ý tưởng Python đầu tiên

### 1. `print`

`print` hiển thị một thông điệp hoặc kết quả.

```python
print("My research topic is short-term Chinese teaching.")
```

### 2. Biến (variable)

Biến là một tên dùng để lưu giá trị.

```python
topic = "Chinese measure words"
research_area = "TCSOL"
```

Hãy tưởng tượng biến như một mảnh giấy có nhãn. Python ghi nhớ giá trị đó để mình dùng lại sau.

### 3. Chuỗi văn bản (string)

Text trong Python thường đặt trong dấu ngoặc kép.

```python
question = "How do learner answers change after a short measure-word lesson?"
```

### 4. Danh sách các dòng

Khi đọc một tệp CSV, Python có thể lưu các dòng vào một danh sách.

```python
rows = [
    {"track": "TCSOL"},
    {"track": "MTPE"}
]
```

Trong Tuần 01, bạn chỉ cần biết:

- danh sách có thể chứa nhiều dòng;
- `len(rows)` đếm có bao nhiêu dòng;
- `rows[0]` cho xem dòng đầu tiên.

## Kỹ năng nghiên cứu: chủ đề rộng và câu hỏi nghiên cứu

Chủ đề rộng chưa đủ để phân tích dữ liệu.

| Chủ đề rộng | Câu hỏi tốt hơn |
|---|---|
| Dạy ngữ pháp tiếng Trung | Câu trả lời của người học thay đổi thế nào trước và sau một hoạt động ngắn về lượng từ? |
| Đối chiếu Hán-Việt | Ví dụ cấu trúc 把 nào tạo vấn đề chuyển di về trật tự từ cho người học Việt Nam? |
| Dịch máy | Loại lỗi MT nào xuất hiện nhiều nhất trong câu chính sách giáo dục Hán-Việt? |
| Chính sách giáo dục | Các trích đoạn chính sách gần đây nói về phát triển giáo viên như thế nào? |

Một câu hỏi nghiên cứu tốt cho người mới nên:

- đủ nhỏ cho một project;
- gắn với dữ liệu quan sát được;
- nói rõ đơn vị quan sát (unit of observation);
- có thể tạo ít nhất một bảng hoặc hình.

Sentence frame cho Tuần 01:

```text
This project asks [small question] because [research reason]. The first dataset would contain [unit of observation], so Python can help by [table/figure/output].
```

## Ví dụ đã làm mẫu

Sở thích rộng:

```text
Tôi quan tâm đến giảng dạy Hán ngữ ngắn hạn.
```

Câu hỏi sẵn sàng cho dữ liệu:

```text
Câu trả lời của người học thay đổi thế nào trước và sau một hoạt động hai tuần về lượng từ?
```

Dữ liệu có thể cần:

```text
một dòng = câu trả lời của một người học cho một item kiểm tra
```

Kết quả có thể tạo:

```text
bảng mô tả so sánh câu trả lời trước và sau hoạt động
```

Hạn chế quan trọng:

```text
Thay đổi pre/post chỉ mang tính mô tả. Tự nó chưa chứng minh quan hệ nhân quả.
```

## Bốn ví dụ dữ liệu rất nhỏ

Các ví dụ này chỉ giúp bạn hình dung dữ liệu tương lai. Tuần 01 chưa yêu cầu phân tích chúng.

| Hướng | Một dòng có thể là |
|---|---|
| TCSOL | `learner_id=S001; item_id=Q03; pre_answer=一书; post_answer=一本书; target=measure_word` |
| Đối chiếu | `zh=我把书放在桌子上; vi=Tôi đặt sách lên bàn; predicted_difficulty=把 omitted` |
| MTPE | `zh_source=教育数字化推动资源共享; vi_mt=Giáo dục số thúc đẩy tài nguyên chia sẻ; vi_postedit=Giáo dục số thúc đẩy việc chia sẻ tài nguyên` |
| Policy | `title=教育强国建设规划纲要（2024-2035年）; theme=digitalization; excerpt=教育数字化` |

## Lỗi thường gặp

### Lỗi 1: Muốn học mọi thứ cùng lúc

Đừng cố học pandas, thống kê, MT metrics, và visualization ngay ở Tuần 01. Mục tiêu chỉ là chạy notebook và hiểu quy trình nghiên cứu.

### Lỗi 2: Chọn câu hỏi quá rộng

Quá rộng:

```text
Nên dạy tiếng Trung cho sinh viên Việt Nam như thế nào?
```

Tốt hơn:

```text
Ba lỗi lượng từ nào xuất hiện nhiều nhất trong lớp beginner sau một bài học ngắn?
```

### Lỗi 3: Quên đơn vị quan sát

Luôn hỏi:

```text
Một dòng trong dataset của mình đại diện cho điều gì?
```

Ví dụ:

- một người học;
- một câu trả lời kiểm tra;
- một cặp câu Hán-Việt;
- một đoạn dịch;
- một trích đoạn chính sách đã mã hóa.

## Mini Cheat Sheet

```python
print("message")              # hiển thị thông điệp
topic = "TCSOL"               # lưu text vào biến
len(rows)                     # đếm số phần tử
rows[0]                       # phần tử đầu tiên
row["track"]                  # giá trị ở cột track
```

## Liên hệ với project cuối khóa

Cuối khóa, bạn có thể chọn một trong các hướng:

- TCSOL: pre-test/post-test và lỗi người học;
- Đối chiếu Hán-Việt: cặp câu và ghi chú giảng dạy;
- MTPE: bản dịch máy, hậu hiệu đính của con người, nhãn lỗi;
- Chính sách giáo dục: trích đoạn chính sách, chủ đề, metadata, timeline.

Tuần 01 tạo nền tảng: mọi project đều cần câu hỏi rõ, đơn vị dữ liệu rõ, và một output nhỏ có thể đưa vào paper.
