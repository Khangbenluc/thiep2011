import streamlit as st
from PIL import Image

def main():
    # Cài đặt tiêu đề trang web
    st.set_page_config(page_title="Thiệp 20/11 online - 20/11 online card", layout="wide")

    # Mở hình ảnh. Thay 'Thiệp 2011.jpg' bằng đường dẫn đến file của bạn nếu cần.
    try:
        image = Image.open('Thiệp 2011.png')

        # Hiển thị hình ảnh
        # Sử dụng caption để cung cấp mô tả ngắn
        # Dùng use_column_width=True để hình ảnh điều chỉnh theo chiều rộng của cột
        st.image(image, caption='Happy Teachers' Day 20/11 ', use_column_width=True)

    except FileNotFoundError:
        st.error("Lỗi: Không tìm thấy file hình ảnh 'Thiệp 2011.png'. Vui lòng đảm bảo file nằm cùng thư mục với app.py.")
    except Exception as e:
        st.error(f"Đã xảy ra lỗi: {e}")

if __name__ == "__main__":
    main()
