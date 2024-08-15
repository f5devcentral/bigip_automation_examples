import csv
import sys
import json

def generate_csv_report(output_file, migrate_apps, migrate_app_prefix, ip_map):
    headers = ['Old_App_Name', 'New_App_Name', 'Status', 'Old_IP_Address', 'New_IP_Address', 'as3_unsupported']
    with open(output_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()

        for app in migrate_apps['applications']:
            for vs in app.get('virtual_servers', []):
                app_name = vs['name']
                old_ip = vs['ip_addresses'][0] if vs.get('ip_addresses') else '-'
                old_ip_without_port = old_ip.split('/')[0] if old_ip else '-'
                new_ip = ip_map.get(old_ip_without_port, '-')
                as3_unsupported = '-'
                if vs.get('status', 'unknown') == 'yellow':
                    as3_unsupported_list = vs.get('as3_unsupported', [])
                    as3_unsupported = ';'.join(as3_unsupported_list)
                
                row = {
                    'Old_App_Name': app_name.replace(migrate_app_prefix, '', 1),
                    'New_App_Name': app_name,
                    'Status': vs.get('status', 'unknown'),
                    'Old_IP_Address': old_ip_without_port,
                    'New_IP_Address': new_ip,
                    'as3_unsupported': as3_unsupported
                }
                writer.writerow(row)

if __name__ == "__main__":
    output_file = sys.argv[1]
    json_file = sys.argv[2]
    migrate_app_prefix = sys.argv[3]
    ip_map = json.loads(sys.argv[4])

    with open(json_file, 'r') as file:
        migrate_apps = json.load(file)

    generate_csv_report(output_file, migrate_apps, migrate_app_prefix, ip_map)
