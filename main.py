import staging_pipeline
import analytics_pipeline

def main():
    # Đường dẫn file
    raw_path = 'data/tiki_products.csv'
    
    # Chạy quy trình
    print("Đang dọn dẹp dữ liệu...")
    df_staged = staging_pipeline.run_staging(raw_path)
    
    print("Đang phân tích chỉ số...")
    df_final, seller_rpt, cat_rpt = analytics_pipeline.run_analytics(df_staged)
    
    # Lưu file để làm Dashboard
    df_final.to_csv('data/tiki_final_for_bi.csv', index=False)
    seller_rpt.to_csv('data/top_sellers.csv')
    print("Thành công! Hãy mở Power BI và dùng file 'tiki_final_for_bi.csv'.")

if __name__ == "__main__":
    main()