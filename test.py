import requests

print(requests.get("http://progressquest.com/alpaquil.php?cmd=b&t=b&n=Ancrieb&r=Hob-Hobbit&c=Runeloremaster&l=1&x=54&i=Sharp Rock&z=&k=INT 17&a=Act I&h=Alpaquil&rev=6&p=-174157950&m=", headers={
    "X-Requested-With": "XMLHttpRequest"
}).text)