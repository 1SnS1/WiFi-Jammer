wifijammer
==========

Continuously jam all wifi clients and access points within range. The effectiveness of this script is constrained by your wireless card. Alfa cards seem to effectively jam within about a block radius with heavy access point saturation. Granularity is given in the options for more effective targeting.


Requires: python 2.7, python-scapy, a wireless card capable of injection


Usage
-----

``` shell
python wifijammer
```

This will find the most powerful wireless interface and turn on monitor mode. If a monitor mode interface is already up it will use the first one it finds instead. It will then start sequentially hopping channels 1 per second from channel 1 to 11 identifying all access points and clients connected to those access points. On the first pass through all the wireless channels it is only identifying targets. After that the 1sec per channel time limit is eliminated and channels are hopped as soon as the deauth packets finish sending. Note that it will still add clients and APs as it finds them after the first pass through.

Upon hopping to a new channel it will identify targets that are on that channel and send 1 deauth packet to the client from the AP, 1 deauth to the AP from the client, and 1 deauth to the AP destined for the broadcast address to deauth all clients connected to the AP. Many APs ignore deauths to broadcast addresses.

```shell
python wifijammer -a 00:0E:DA:DE:24:8E -c 2
```

Deauthenticate all devices with which 00:0E:DA:DE:24:8E communicates and skips channel hopping by setting the channel to the target AP's channel (2 in this case). This would mainly be an access point's MAC so all clients associated with that AP would be deauthenticated, but you can also put a client MAC here to target that one client and any other devices that communicate with it.

All options:

```shell
python wifijammer [-a AP MAC] [-c CHANNEL] [-d] [-i INTERFACE] [-m MAXIMUM] [-n] [-p PACKETS] [-s SKIP] [-t TIME INTERVAL]
```
