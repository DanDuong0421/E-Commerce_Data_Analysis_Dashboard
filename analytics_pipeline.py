import pandas as pd

def run_analytics(df):
    print("--- Đang bắt đầu quá trình Analytics (Tính toán chỉ số) ---")
    
    # 1. Tính doanh thu ước tính (Revenue) cho từng sản phẩm
    # Công thức: Giá hiện tại * Số lượng đã bán
    df['estimated_revenue'] = df['price'] * df['quantity_sold']
    
    # 2. Báo cáo theo Nhà bán hàng (Seller Report)
    # Gom nhóm theo seller để xem ai bán chạy nhất
    seller_report = df.groupby('current_seller').agg({
        'estimated_revenue': 'sum',
        'quantity_sold': 'sum',
        'rating_average': 'mean',
        'id': 'count'
    }).rename(columns={'id': 'product_count'}).sort_values(by='estimated_revenue', ascending=False)
    
    # 3. Báo cáo theo Ngành hàng (Category Report)
    # Xem ngành hàng nào đang chiếm lĩnh doanh thu
    category_report = df.groupby('category')['estimated_revenue'].sum().sort_values(ascending=False)
    
    print("Hoàn thành tính toán các báo cáo.")
    return df, seller_report, category_report