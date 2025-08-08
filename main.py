import cv2
import numpy as np

# الدالة اللي تحدد اللون عند الضغط
def get_color(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        b, g, r = frame[y, x]
        color_name = classify_color(r, g, b)
        print(f"Color at ({x},{y}): {color_name} - RGB({r},{g},{b})")
        # نعرض مستطيل بلون النقطة + الاسم
        cv2.rectangle(frame, (x, y - 20), (x + 150, y), (b, g, r), -1)
        cv2.putText(frame, color_name, (x + 5, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (255 - b, 255 - g, 255 - r), 1, cv2.LINE_AA)

# تصنيف اللون حسب قيمة RGB
def classify_color(r, g, b):
    if r > 200 and g < 100 and b < 100:
        return "Red"
    elif r < 100 and g > 200 and b < 100:
        return "Green"
    elif r < 100 and g < 100 and b > 200:
        return "Blue"
    elif r > 200 and g > 200 and b < 100:
        return "Yellow"
    elif r > 200 and g > 200 and b > 200:
        return "White"
    elif r < 50 and g < 50 and b < 50:
        return "Black"
    else:
        return "Other"

# فتح الكاميرا
cap = cv2.VideoCapture(0)

cv2.namedWindow('Color Recognition')
cv2.setMouseCallback('Color Recognition', get_color)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow('Color Recognition', frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC للخروج
        break

cap.release()
cv2.destroyAllWindows()
