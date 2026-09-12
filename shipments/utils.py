AVG_SPEED_KMH = {"air": 700, "sea": 35, "road": 60}


def estimate_delivery_hours(distance_km, mode):
    """Ước tính số giờ giao hàng dựa trên khoảng cách và tốc độ trung bình
    của phương thức vận chuyển. Đơn giản nhưng đủ để giải thích trong phỏng vấn:
    - air nhanh nhất (700 km/h)
    - road trung bình (60 km/h)
    - sea chậm nhất (35 km/h)
    """
    speed = AVG_SPEED_KMH.get(mode, 50)
    return round(distance_km / speed, 1)
