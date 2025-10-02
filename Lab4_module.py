# sinh viên xây dựng các hàm trong lớp 4 ở đây
def timh_tien_nuoc(so_nuoc):
    gia_ban_nuoc = (7500, 8000, 12000, 24000)
    if so_nuoc <= 10 and so_nuoc > 0:
        tien_nuoc_thang = so_nuoc * gia_ban_nuoc[0]
    elif so_nuoc <= 20:
        tien_nuoc_thang = 10 * gia_ban_nuoc[0] + (so_nuoc - 10) * gia_ban_nuoc[1]
    elif so_nuoc <= 30:
        tien_nuoc_thang = 10 * gia_ban_nuoc[0] + 10 * gia_ban_nuoc[1] + (so_nuoc - 20) * gia_ban_nuoc[2]
    else:
        tien_nuoc_thang = 10 * gia_ban_nuoc[0] + 10 * gia_ban_nuoc[1] + 10 * gia_ban_nuoc[2] + (so_nuoc - 30) * gia_ban_nuoc[3]
    return tien_nuoc_thang
print("Chương trình tính tiền nước sinh hoạt")
so_nuoc = float(input("Nhập số nước tiêu thụ trong tháng (m3): "))
tien_nuoc = timh_tien_nuoc(so_nuoc)
print(f"Số tiền nước phải trả trong tháng là: {tien_nuoc} đồng")
# --- IGNORE ---
def tinh_nguyen_lieu(s1_bdx, s2_btc, s3_bd):
    banh_dau_xanh = {"đường": 0.04, "đậu":0.07}
    banh_thap_cam = {"đường": 0.06 , "đậu":0}
    banh_dẻo ={"đường": 0.05, "đậu":0.02}
    duong_lam_banh = s1_bdx * banh_dau_xanh["đường"] + s2_btc * banh_thap_cam["đường"] + s3_bd * banh_dẻo["đường"]
    dau_lam_banh = s1_bdx * banh_dau_xanh["đậu"] + s2_btc * banh_thap_cam["đậu"] + s3_bd * banh_dẻo["đậu"]
    return duong_lam_banh, dau_lam_banh