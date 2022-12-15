from datetime import datetime as dt

end_time = dt(2023, 12, 31) 

sites_to_block = ["www.facebook.com", "facebook.com"]

hosts_path = "/etc/hosts"

redirect = "127.0.0.1"

def main():
    block_sites()

def block_sites():
    if dt.now() < end_time:
        print("Sites Blocked")
        with open(hosts_path, "r+") as hostsfile:
            hosts_content = hostsfile.read()
            for site in sites_to_block:
                if site not in hosts_content:
                    hostsfile.write(redirect + " " + site + "\n") 

    else:
        print("Sites Unblocked")
        with open(hosts_path, "r+") as hostsfile:
            lines = hostsfile.readlines()
            hostsfile.seek(0)
            for line in lines:
                if not any(site in line for site in sites_to_block):
                    hostsfile.write(line)  
            hostsfile.truncate() 

if __name__ == "__main__":
    main()                        