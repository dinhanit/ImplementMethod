import cv2

def select_points(image_path):
    image = cv2.imread(image_path)
    clone = image.copy()

    selected_points = []

    def mouse_callback(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            selected_points.append((x, y))
            cv2.circle(clone, (x, y), 5, (0, 0, 255), -1)
            cv2.imshow("Image", clone)

    cv2.namedWindow("Image")
    cv2.setMouseCallback("Image", mouse_callback)

    while True:
        cv2.imshow("Image", clone)
        key = cv2.waitKey(1) & 0xFF

        if key == ord("r"):
            clone = image.copy()
            selected_points = []
        elif key == ord("c"):
            if len(selected_points) == 2:
                break

    cv2.destroyAllWindows()

    return selected_points

def Select():
    # Đường dẫn đến ảnh của bạn
    image_path = "mecung.jpg"

    # Chọn hai điểm trên ảnh bằng chuột
    selected_points = select_points(image_path)

    if len(selected_points) == 2:
        point1, point2 = selected_points
        return point1,point2
    else:
        return None
