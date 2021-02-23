from setuptools import setup

setup(
    name = "wifijammer",
    version = "1.0",
    author = "Sahi Singh",
    description = "Continuously jam all wifi clients and access points within range.",
    keywords = "WiFi 802.11 jammer deauth",
    url = "https://github.com/1SnS1/WiFi-Jammer",
    scripts=['wifijammer'],
    # py_modules=['wifijammer'],
    install_requires=['scapy'],
)
