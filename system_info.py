import platform, psutil, socket, speedtest, requests, time

def get_ip_address():
    """IP của máy hiện tại."""
    try:
        host_name = socket.gethostname()
        ip_address = socket.gethostbyname(host_name)
        return ip_address
    except socket.error as e:
        # pass
        return f"Đã xảy ra lỗi: {e}"

ip_address = get_ip_address()

def get_wifi_speed(ip_address):
    """Tốc độ của wifi hiện tại"""
    try:
        st = speedtest.Speedtest()
        st.get_best_server()

        url = f"http://{ip_address}"

        response = requests.get(url)

        while response.status_code != 200:
            time.sleep(1)
            response = requests.get(url)
        
        download_speed = st.download() / 1024 / 1024  
        upload_speed = st.upload() / 1024 / 1024  
        return f"Download: {download_speed:.2f} Mbps, Upload: {upload_speed:.2f} Mbps"
    except Exception as e:
        # pass
        return f"Đã xảy ra lỗi: {e}"
    
def get_system_info():
    """Thông tin hệ thống"""
    system_info = {}
    system_info['- Tên thiết bị'] = f"{platform.node()}"
    system_info['- Kiểu máy thiết bị'] = f"{platform.machine()}"
    system_info['- IP thiết bị'] = f"{get_ip_address()}"
    system_info['- Tốc độ WIFI'] = f"{get_wifi_speed(ip_address)} (Đang UPDATE!!)"
    system_info['- CPU thiết bị'] = f"{platform.processor()}"
    system_info['- Phần trăm CPU đã sử dụng'] = f"{psutil.cpu_percent(interval=1)}%"
    system_info['- RAM thiết bị'] = round(psutil.virtual_memory().total / (1024 ** 2), 2), "MB"
    system_info['- Bộ nhớ đã dùng'] = round(psutil.disk_usage('/').used / (1024 ** 3), 2), "GB"
    system_info['- Tổng bộ nhớ thiết bị'] = round(psutil.disk_usage('/').total / (1024 ** 3), 2), "GB"
    system_info['- Còn thừa bao nhiêu bộ nhớ'] = round(psutil.disk_usage('/').free / (1024 ** 3), 2), "GB"
    return system_info

def main():
    system_info = get_system_info()
    print("Thông tin hệ thống")
    for key, value in system_info.items():
        if isinstance(value, tuple):
            print(f"{key}: {value[0]} {value[1]}")
        else:
            print(f"{key}: {value}")

if __name__ == "__main__":
    main()
