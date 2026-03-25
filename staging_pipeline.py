import pandas as pd
import numpy as np

def run_staging(input_path):
    print("--- Đang bắt đầu quá trình Staging (Làm sạch dữ liệu) ---")
    
    # Đọc dữ liệu từ file csv
    df = pd.read_csv(input_path)

    # 1. Chuẩn hóa cột Brand (Standardization)
    # Danh sách các giá trị được coi là không có thương hiệu
    no_brand_aliases = ['oem', 'nan', 'no brand', 'unknown', 'none', 'n/a', 'chưa có thương hiệu']
    
    # Chuyển về chữ thường, xóa khoảng trắng để so sánh chính xác
    df['brand'] = df['brand'].astype(str).str.strip().str.lower()
    
    # Quy đổi tất cả về nhãn 'No Brand', nếu có tên riêng thì viết hoa chữ cái đầu (Title Case)
    df['brand'] = df['brand'].apply(
        lambda x: 'No Brand' if x in no_brand_aliases or x == '' else x.title()
    )
    
    # 2. Phân loại nhóm thương hiệu (Feature Engineering cho Power BI)
    # Tạo cột brand_type để dễ dàng so sánh Branded vs Non-Branded
    df['brand_type'] = df['brand'].apply(lambda x: 'Non-Branded' if x == 'No Brand' else 'Branded')

    # 3. Chuẩn hóa kiểu dữ liệu số (Data Integrity)
    # date_created, price, quantity_sold... đôi khi bị dính ký tự lạ, cần ép về numeric
    cols_to_fix = ['price', 'original_price', 'quantity_sold', 'date_created']
    for col in cols_to_fix:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

    # 4. Tính toán các cột chỉ số (Business Logic)
    # Tính số tiền giảm giá
    df['discount_amount'] = df['original_price'] - df['price']
    
    # Tính % giảm giá (sử dụng np.where để tránh lỗi chia cho 0)
    df['discount_percent'] = np.where(
        df['original_price'] > 0, 
        (df['discount_amount'] / df['original_price']) * 100, 
        0
    )
    
    # Chuyển đổi True/False của has_video sang 1/0 để tính toán nhanh trong BI
    df['has_video_int'] = df['has_video'].astype(int)

    # 5. Loại bỏ dữ liệu rác
    # Loại bỏ các sản phẩm có giá bằng 0 hoặc bé hơn 0
    df = df[df['price'] > 0].copy()

    print(f"Hoàn thành! Đã xử lý xong {len(df)} dòng dữ liệu hợp lệ.")
    return df
