import streamlit as st
from PIL import Image

def main():
    # 1. Cài đặt layout rộng (wide)
    st.set_page_config(page_title="Thiệp ngày nhà giáo - Teachers' day card", layout="wide")

    # 2. Sử dụng CSS tùy chỉnh để loại bỏ padding mặc định
    st.markdown(
        """
        <style>
        .css-usf63n {
            padding: 0px; /* Loại bỏ padding trên và dưới của main content */
        }
        .css-18e3th9 {
            padding-top: 0rem; 
            padding-bottom: 0rem;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    try:
        # Đường dẫn tới file ảnh
        image = Image.open('Thiệp 2011-new.png') 

        # 3. Hiển thị hình ảnh với use_column_width=True
        # Streamlit sẽ điều chỉnh hình ảnh để lấp đầy chiều rộng của cột.
        st.image(image, caption="Happy Teachers' Day 20/11", use_column_width=True)

    except FileNotFoundError:
        st.error("Lỗi: Không tìm thấy file hình ảnh 'Thiệp 2011-new.png'.")
    except Exception as e:
        st.error(f"Đã xảy ra lỗi: {e}")

if __name__ == "__main__":
    main()
