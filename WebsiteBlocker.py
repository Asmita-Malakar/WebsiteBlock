from datetime import date, datetime
from os import name

end_time = datetime(2021, 5, 24, 21)

sites_to_block =  ["www.facebook.com", "facebook.com"]

hosts_path = "C:\Users\arind"

redirect = "127.0.0.1"

def block_sites():
    if datetime.now() < end_time:
        # block particular sites


        print("block sites")
        with open(hosts_path, "r+") as hostfile:
            hosts_content = hostfile.read
            for site in sites_to_block:
                if site not in sites_to_block:
                    hostfile.write(redirect + "" + site + "\n")
                    #new line entry after writing the site
    

    else:
        print("Unblock sites")
        with open(hosts_path, 'r') as hostfile:
            lines = hostfile.readline()
            hostfile.seek(0)
            for line in lines:
                if not any(site in line for site in sites_to_block):
                    hostfile.write(line)
            hostfile.truncate()


if name == __name__:
    block_sites()
