# Linux Q&A

- Problem: vs code is set as the default explorer
- Solution: create the file ~/.config/mimeapps.list if necessary:

```text
[Default Applications]
inode/directory = org.gnome.Nautilus.desktop
```

----

# IP

```bash
sudo ip addr add 192.168.10.1/24 dev eth0
sudo ip link set eth0 up
sudo ip route add default via 192.168.10.254
sudo ip route add 192.168.20.0/24 via 192.168.10.254 dev eth0
```

[https://www.cyberciti.biz/faq/ip-route-add-network-command-for-linux-explained/](https://www.cyberciti.biz/faq/ip-route-add-network-command-for-linux-explained/)
