# Sinh viên code Lab ở đây
menu = """
1. Tính tiền nước
2. Tính nguyên liệu làm bánh
3. Thoát
"""

def main():
    while True:
        print(menu)
        chon_chuc_nang = input("Chọn chức năng (1-3): ")
        if chon_chuc_nang == '1':
            so_nuoc = int(input("Nhập số nước tiêu thụ trong tháng (m3): "))
            tien_nuoc = tinh_tien_nuoc(so_nuoc)
            print(f"Tiền nước tháng này là: {tien_nuoc:,} VND")
        elif chon_chuc_nang == '2':
            s1_bdx = int(input("Nhập số bánh đậu xanh cần làm: "))
            s2_btc = int(input("Nhập số bánh thập cẩm cần làm: "))
            s3_bd = int(input("Nhập số bánh dẻo cần làm: "))
            duong, dau = tinh_nguyen_lieu(s1_bdx, s2_btc, s3_bd)
            print(f"Số đường cần dùng: {duong:.2f} kg")
            print(f"Số đậu cần dùng: {dau:.2f} kg")
        elif chon_chuc_nang == '3':
            print("Thoát chương trình.")
            break
        else:
            print(" Vui lòng chọn 1-3!")

def tinh_tien_nuoc(so_nuoc):
    gia_ban_nuoc = (7500, 8000, 12000, 24000)
    if so_nuoc <= 0:
        return 0
    elif so_nuoc <= 10:
        tien_nuoc_thang = so_nuoc * gia_ban_nuoc[0]
    elif so_nuoc <= 20:
        tien_nuoc_thang = 10 * gia_ban_nuoc[0] + (so_nuoc - 10) * gia_ban_nuoc[1]
    elif so_nuoc <= 30:
        tien_nuoc_thang = 10 * gia_ban_nuoc[0] + 10 * gia_ban_nuoc[1] + (so_nuoc - 20) * gia_ban_nuoc[2]
    else:
        tien_nuoc_thang = 10 * gia_ban_nuoc[0] + 10 * gia_ban_nuoc[1] + 10 * gia_ban_nuoc[2] + (so_nuoc - 30) * gia_ban_nuoc[3]
    return tien_nuoc_thang

def tinh_nguyen_lieu(s1_bdx, s2_btc, s3_bd):
    banh_dau_xanh = {"đường": 0.04, "đậu":0.07}
    banh_thap_cam = {"đường": 0.06 , "đậu":0}
    banh_dẻo = {"đường": 0.05, "đậu":0.02}
    duong_lam_banh = s1_bdx * banh_dau_xanh["đường"] + s2_btc * banh_thap_cam["đường"] + s3_bd * banh_dẻo["đường"]
    dau_lam_banh = s1_bdx * banh_dau_xanh["đậu"] + s2_btc * banh_thap_cam["đậu"] + s3_bd * banh_dẻo["đậu"]
    return duong_lam_banh, dau_lam_banh 
if __name__ == "__main__":
    main()