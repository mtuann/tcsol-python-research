# Tuần 02 Data Dictionary

## Dataset 1

- File: `data/raw/week02_research_table_examples.csv`
- Source: instructor-created teaching dataset.
- Access date: 2026-06-03.
- Unit of observation: one possible research table design for a track.
- Rows: 4 synthetic rows.
- Private data: none.

| Column | Ý nghĩa | Ví dụ |
|---|---|---|
| `track_id` | ID ổn định của track. | `TCSOL_SHORT` |
| `track` | Tên track nghiên cứu. | `Short-term Chinese teaching` |
| `data_unit` | Một dòng trong dataset tương lai sẽ đại diện cho điều gì. | `learner pre/post score record` |
| `starter_table` | Tên file CSV gợi ý. | `pre_post_scores.csv` |
| `required_columns` | Cột bắt buộc, phân tách bằng dấu phẩy. | `learner_id,pre_score,post_score` |
| `optional_columns` | Cột có thể thêm nếu cần. | `attendance_hours,notes` |
| `paper_output` | Output có thể dùng trong paper. | `clean data template` |
| `beginner_task` | Việc Python ở mức beginner. | `read columns and explain one row` |

## Dataset 2

- File: `data/raw/week02_column_planning_template.csv`
- Purpose: ví dụ một data dictionary nhỏ ở mức cột.
- Required for learner: đọc và có thể chỉnh trong bản notebook cá nhân.

| Column | Ý nghĩa |
|---|---|
| `column_name` | Tên cột nên dùng trong CSV. |
| `plain_language_meaning` | Giải thích bằng ngôn ngữ thường. |
| `example_value` | Một giá trị minh họa. |
| `required` | Cột có bắt buộc không. |
| `private_data_risk` | Rủi ro dữ liệu riêng tư. |
| `notes` | Ghi chú thiết kế. |

## Privacy Reminder

Trong project thật, không public:

- tên thật của người học;
- email/số điện thoại/mã sinh viên thật;
- bài làm có thể truy ngược danh tính;
- ảnh lớp học hoặc thông tin trường/lớp nếu chưa có consent.
