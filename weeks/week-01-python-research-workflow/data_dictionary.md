# Tuần 01 Data Dictionary

## Dataset

- File: `data/raw/week01_research_tracks.csv`
- Source: instructor-created teaching dataset.
- Access date: 2026-06-03.
- License/reuse note: may be reused for this course.
- Đơn vị quan sát: một hướng project nghiên cứu có thể phát triển.
- Số dòng: 4 dòng synthetic do giảng viên tạo.
- Missing values: không kỳ vọng có missing; ô trống không hợp lệ trong teaching dataset này.
- Private data: không có dữ liệu riêng tư hoặc định danh người học.

## Columns

| Column | Ý nghĩa | Ví dụ |
|---|---|---|
| `track_id` | ID ngắn, ổn định cho hướng nghiên cứu. | `TCSOL_SHORT` |
| `track` | Tên hướng nghiên cứu. | `Short-term Chinese teaching` |
| `broad_interest` | Chủ đề rộng trước khi trở thành câu hỏi có thể nghiên cứu. | `Improving short-term Chinese classes...` |
| `small_research_question` | Câu hỏi hẹp hơn, có thể gắn với dữ liệu. | `How do learner answers change...` |
| `unit_of_observation` | Một dòng trong dataset tương lai sẽ đại diện cho điều gì. | `learner test item` |
| `starter_dataset` | Dataset template có thể dùng cho hướng đó. | `pre_post_scores.csv` |
| `likely_output` | Bảng hoặc hình có thể xuất hiện trong paper. | `pre/post score table` |
| `beginner_python_task` | Tác vụ Python rất đơn giản cho loại dataset đó. | `count learners...` |

## Vì sao dataset này tồn tại?

Tuần 01 dùng dataset lập kế hoạch rất nhỏ thay vì dữ liệu lớp học hoặc dịch thuật thật. Như vậy bài học tập trung vào quy trình:

```text
topic -> question -> data unit -> Python task -> paper output
```

Bạn chưa cần lo về phân tích nâng cao. Câu hỏi quan trọng là: "Mình cần dữ liệu gì để trả lời câu hỏi nghiên cứu này?"

## Mini Data Examples

Tuần 01 cũng có:

- File: `data/raw/week01_mini_examples.csv`
- Purpose: cho thấy một dòng dữ liệu tương lai có thể trông như thế nào ở từng hướng.
- Required for learner: không; chỉ dùng cho instructor demo.

| Hướng | Example unit | Vì sao quan trọng |
|---|---|---|
| TCSOL | một câu trả lời của người học trong một item kiểm tra | nối hoạt động giảng dạy với output có thể đo |
| Đối chiếu Hán-Việt | một cặp câu Hán-Việt | nối phân tích ngữ pháp với ghi chú giảng dạy |
| MTPE | một segment source-MT-postedit | nối bản dịch máy với hậu hiệu đính và nhãn lỗi |
| Policy | một trích đoạn chính sách đã mã hóa hoặc cặp document-theme | nối văn bản chính sách với metadata và theme |

Không thêm tên thật, email, hoặc dữ liệu lớp học có thể định danh vào file dữ liệu Tuần 01.
