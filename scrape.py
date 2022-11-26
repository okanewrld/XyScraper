import os
import time
from colored import fg, attr
g = fg('#875cd3')

y = fg('#ffffff')
os.system(f'cls & mode 85,20 & title Proxy Scraper [Created By Okane]')



print(f"""
                                   {g}██   ██ ██    ██ 
                                   {y} ██ ██   ██  ██  
                                   {g}  ███     ████   
                                   {y} ██ ██     ██    
                                   {g}██   ██    ██    
                                   {y}
                        - https://github.com/okanewrld
                        - https://youtube.com/@okanewrld
""")
time.sleep(2)
print(f"                            {g}Scraping Proxies For You...")
time.sleep(3)
print("")
os.system(
        "curl https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt -o proxies.txt"
    )
os.system('cls')
print("")
print(f"""
{y}
			        Check : proxies.txt

			   Thanks For Using Okane's TOOLS

			      You May Exit The Program!
""")
time.sleep(69)
