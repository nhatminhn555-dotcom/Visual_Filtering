import cv2
import numpy as np

# Đọc ảnh (thay đường dẫn bằng ảnh thật của bạn)
image = cv2.imread('your_image.jpg')  # ← thay bằng ví dụ: 'D:/anh/dep.jpg' hoặc 'cat.jpg'

if image is None:
    print("Không tìm thấy ảnh hoặc đường dẫn sai!")
    print("Kiểm tra lại tên file và đường dẫn nhé")
    exit()


# Hàm callback khi trackbar thay đổi
def update_image(x):
    # Lấy giá trị từ trackbar
    contrast = cv2.getTrackbarPos('Contrast', 'Adjustments') / 50.0  # 0.0 → 2.0
    brightness = cv2.getTrackbarPos('Brightness', 'Adjustments') - 100  # -100 → +100

    # Áp dụng contrast + brightness
    adjusted_img = cv2.convertScaleAbs(image, alpha=contrast, beta=brightness)

    # Hiển thị ảnh đã chỉnh
    cv2.imshow('Adjustments', adjusted_img)


# Tạo cửa sổ
cv2.namedWindow('Adjustments')

# Tạo 2 trackbar
cv2.createTrackbar('Contrast', 'Adjustments', 50, 100, update_image)  # mặc định = 50 → contrast = 1.0
cv2.createTrackbar('Brightness', 'Adjustments', 100, 200, update_image)  # mặc định = 100 → brightness = 0

# Hiển thị ảnh ban đầu
update_image(0)

print("Dùng chuột kéo thanh Contrast và Brightness để chỉnh ảnh")
print("Nhấn phím bất kỳ để thoát...")

cv2.waitKey(0)
cv2.destroyAllWindows()