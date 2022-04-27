import webbrowser

print("Recommendations: ")
print("web.whatsapp.com, youtube.com, asnschool.org, diksha.gov.in, code.whitehatjr.com/s/dashboard")

oh = input("What do you want to opem: ")

il = input("What is the last thing (.com or .in or .org) ")

#print(oh)

chrome_path = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

webbrowser.register("chrome", None, webbrowser.BackgroundBrowser(chrome_path))

kl = ("https://" + oh + il) 

webbrowser.get("chrome").open_new_tab(kl)