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
sudo ip address add 10.10.10.1/24 dev eth0
sudo ip link set eth0 up
# optional
sudo ip route add default via 10.10.10.1
```
