network:
    ethernets:
        enp0s3:  # Dit is de Host-only adapter
            dhcp4: no
            addresses: [192.168.56.10/24] # Je statische IP-adres
            gateway4: 192.168.56.1 
            nameservers:
                addresses: [8.8.8.8, 8.8.4.4]
        enp0s8:  # Dit is de NAT-adapter (voor internet)
            dhcp4: yes
    version: 2
