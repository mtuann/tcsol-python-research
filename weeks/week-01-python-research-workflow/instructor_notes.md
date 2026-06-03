# Tuần 01 Instructor Notes

## Teaching Goal

Người học chưa có nền tảng lập trình. Tuần 01 nên giảm sợ hãi, không tối đa hóa lượng kỹ thuật.

Thông điệp chính:

```text
Python giúp quy trình viết paper có thể tái lập.
Bạn không cần trở thành software engineer.
```

## Giữ Core thật nhẹ

Khái niệm bắt buộc ở phần learner-facing:

- notebook cells;
- Markdown vs code;
- variables;
- strings;
- CSV như một bảng;
- one row = one observation.

Tránh:

- pandas;
- thống kê;
- xử lý lỗi cài đặt trong phần chính;
- COMET, BLEU, regression, APIs, scraping;
- yêu cầu người học viết HTML, CSS, hoặc JavaScript.

## Suggested Teaching Script

1. Bắt đầu từ việc học thuật quen thuộc: "Tôi cần viết phần Methods."
2. Cho thấy Methods cần nguồn dữ liệu, dòng, cột, và quy trình.
3. Mở `slides.html`.
4. Mở `interactive_demo.html` và cho thấy dataset nhỏ có thể thành bảng/hình.
5. Mở `live_coding.ipynb`.
6. Để người học chỉ sửa variables.
7. Cùng chạy các CSV cells.
8. Hỏi người học muốn chọn hướng nào cho tương lai.

## Common Learner Reactions

| Phản ứng | Câu trả lời của giảng viên |
|---|---|
| "Em không hiểu hết code." | "Hôm nay chưa cần. Em chỉ cần chạy được và biết điều gì thay đổi." |
| "Python có viết paper giúp em không?" | "Python tạo bằng chứng và quy trình minh bạch; phần diễn giải vẫn là của em." |
| "Sao không dùng Excel?" | "Excel hữu ích. Python mạnh khi quy trình cần lặp lại, kiểm tra, và ghi lại rõ." |
| "Em có cần machine learning không?" | "Không. Nghiên cứu tốt thường bắt đầu bằng dữ liệu sạch, bảng, hình, và diễn giải cẩn thận." |

## Bilingual Teaching Note

- Website mặc định tiếng Việt; English là lựa chọn.
- Không đọc cả hai ngôn ngữ trên lớp.
- Khi thuật ngữ quan trọng xuất hiện lần đầu, dùng Vietnamese + English anchor: `biến (variable)`, `đơn vị quan sát (unit of observation)`.
- Nếu người học học ở Trung Quốc và cần viết tiếng Anh học thuật, dùng English toggle để review cách diễn đạt, không biến nó thành bài dịch riêng.

## Optional Demonstration

Nếu người học tò mò, cho xem HTML interactive demo. Không giải thích JavaScript. Nói:

```text
Sau này Python có thể xuất biểu đồ tương tác kiểu này. Hiện tại nhiệm vụ của em là đọc và diễn giải nó.
```

## Success Criteria

Tuần này thành công nếu người học nói được:

- "Em chạy được notebook."
- "Em biết câu hỏi của mình cần loại dữ liệu nào."
- "Em viết được diễn giải ngắn cho một output đơn giản."
