delivery_orders = [
    "GE001",
    "GE002",
    "GE003-CANCEL"
]

# Thêm đơn mới
delivery_orders.append("GE004")

# Chèn đơn ưu tiên
delivery_orders.insert(0, "GE000")

# Cập nhật mã đơn
delivery_orders[2] = "GE002-UPDATED"

# Xóa đơn bị hủy
delivery_orders.remove("GE003-CANCEL")

# Bàn giao đơn cuối
transferred_order = delivery_orders.pop()

print("Danh sách đơn hàng còn lại:", delivery_orders)
print("Đơn hàng được bàn giao:", transferred_order)