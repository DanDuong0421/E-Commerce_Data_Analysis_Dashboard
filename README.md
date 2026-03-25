# 📊 Tiki E-Commerce Data Analysis Dashboard

## 📌 Tổng quan dự án (Project Overview)
Dự án thực hiện quy trình **End-to-End Data Analysis**: Từ việc thu thập dữ liệu (Web Scraping) trên sàn thương mại điện tử Tiki, xử lý dữ liệu thô (Data Cleaning) bằng **Python**, đến trực quan hóa và khai thác Insight bằng **Power BI**.

Mục tiêu chính là phân tích hiệu suất kinh doanh, hành vi người bán và tìm kiếm các yếu tố ảnh hưởng đến doanh số trong nhóm ngành hàng Phụ kiện du lịch & Thời trang.

## 🛠 Công nghệ sử dụng (Tech Stack)
* **Ngôn ngữ:** Python (Pandas, Numpy, Selenium/Requests).
* **Công cụ BI:** Power BI Desktop.
* **Kỹ thuật:** Data Cleaning, Feature Engineering, DAX Measures (Dynamic Calculation), Correlation Analysis.

## 💡 Khai thác Insight (Data Insights)

Dựa trên Dashboard thực tế với tổng doanh thu **~29 tỷ VNĐ**, dự án rút ra các Insight quan trọng sau:

### 1. Nhóm ngành hàng chủ lực (Top Revenue Drivers)
* **Vali nhựa, Thời trang, Balo nam** và **Balo laptop** là những mặt hàng mang về doanh thu lớn nhất cho hệ thống.
* Đặc biệt, nhóm **Phụ kiện vali** dù có kích thước sản phẩm nhỏ nhưng đóng góp đáng kể vào tổng giá trị giao dịch.

### 2. Hành vi giá & Phân khúc thị trường (Price Point Analysis)
Đây là điểm khác biệt lớn nhất được phát hiện thông qua biểu đồ **Tương quan Giá & Sản lượng**:
* **Phân khúc Phổ thông (<5 triệu VNĐ):** Đa số các mặt hàng (Vali, Thời trang, Balo nam) tập trung dày đặc ở mức giá này. Lượng bán (Quantity Sold) cao nhất nằm ở vùng giá rẻ.
* **Phân khúc Cao cấp (>10 triệu VNĐ):** Một Insight cực kỳ đắt giá là đối với **Balo laptop** và **Phụ kiện vali**, khách hàng sẵn sàng chi trả mức giá cao (trên 10 triệu VNĐ) để mua sắm. 
* => **Kết luận:** Khách hàng ưu tiên tính bảo vệ và chất lượng cao cấp cho thiết bị điện tử (Balo laptop) hơn là yếu tố giá rẻ đơn thuần.

### 3. Sức mạnh thương hiệu (Brand Dominance)
* Hàng có thương hiệu (**Branded**) chiếm đến **81.93%** doanh thu (tương đương 24 tỷ VNĐ). Điều này khẳng định người tiêu dùng trên Tiki có xu hướng tin tưởng tuyệt đối vào các **Official Stores**.

## 📊 Hình ảnh Dashboard
![Tiki Dashboard](https://github.com/DanDuong0421/AlvinPDF_Chatbox/raw/main/path_to_your_image.png) 
*(Lưu ý: Alvin thay link ảnh thực tế của bạn vào đây nhé)*

## 📂 Cấu trúc thư mục
* `/data`: Chứa dữ liệu thô và file sạch `tiki_final_for_bi.csv`.
* `/scripts`: Các file Python xử lý dữ liệu (`staging_pipeline.py`, `main.py`).
* `/docs`: Tài liệu hướng dẫn và báo cáo phân tích.

---
**Thực hiện bởi:** Alvin (Information Systems Student)
