import ipaddress

def ip_range_to_list(start_ip, end_ip):
    """将IP地址范围转换为列表"""
    start_int = int(ipaddress.IPv4Address(start_ip))
    end_int = int(ipaddress.IPv4Address(end_ip))
    return [ipaddress.IPv4Address(ip) for ip in range(start_int, end_int + 1)]

def cidr_to_list(cidr):
    """将CIDR表示法的网段转换为列表"""
    return [str(ip) for ip in ipaddress.ip_network(cidr).hosts()]

def process_ip_entry(ip_entry):
    """处理单个IP条目，返回IP列表"""
    if '-' in ip_entry:
        # IP地址范围
        start_ip, end_ip = ip_entry.split('-')
        return [str(ip) for ip in ip_range_to_list(start_ip, end_ip)]
    elif '/' in ip_entry:
        # CIDR表示法的网段
        return cidr_to_list(ip_entry)
    else:
        # 单个IP地址
        return [ip_entry]

def generate_ip_list(ip_entries, output_file):
    """生成IP列表并写入到文件"""
    with open(output_file, 'w') as file:
        for ip_entry in ip_entries:
            ip_list = process_ip_entry(ip_entry)
            for ip in ip_list:
                file.write(ip + '\n')

# 读取IP.txt文件内容
with open('IP.txt', 'r') as file:
    ip_entries = [line.strip() for line in file.readlines() if line.strip()]

# 生成IP列表并写入到iplist.txt
generate_ip_list(ip_entries, 'iplist.txt')

print("IP地址列表已生成并保存到iplist.txt中。")
