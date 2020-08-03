# Docker In One Page(30 minutes)

- Docker Overview
- Docker Process
- Docker image
- Docker Components

## 5. Docker Usage

- Data
- Networking
- Security
- Configuration
- Monitoring

Requirements for Container Cloud:
```shell
• Scalability
• Isolation
• Dynamics
• Virtual address (IP, Port) • Service Discovery
• QoS
• Integration
• And ...
```


## 5.1 Data

```shell
/var/lib/docker 
• aufs:UFS storage
• containers: Information of each container
• execdriver/native: Running container information
• graph: Images information
• init: docker init binary versions
• linkgraph.db:  SQLite db file keeping the links between containers
• repositories-aufs: Info for images
• trust: signatures
• volumes:Randomly created volumes on host
• -s to select one
• Device Mapper: Thin provisioning/loopback mounted spare file
• Btrfs: Docker upstream/no selinux/no page caching sharing
• OverlayFS: supported by linux upstream

```



## 5.2 Networking

- veth
- macvlan
- namespace
- iptables
- DHCP:
  * assign IP when init/restart
- bridge,routing table and /etc/resolve.conf
- DHCP service: fast
- iptables NAT rules/slow
- nftables
- Networking: k8s-flannel

Solutions:
- Libnetwork
- SDN: Neutron Core concepts
- Flannel?
- Weave?
- Calico
- Kubernetes

Two basic questions:
- How to Access the network?
- How to design the network?

## 5.3 Security

- container as application
- validate external images
- mutually-trusted containers on the same host
- Use AppArmor/SELinux
- Minimize privileges/Limit Resources using CGroups
```shell
docker run -it –rm –u user1 --cap-drop SETUID --cap-drop SETGID ...
docker run -it --rm --cpuset=0,1 -c 2 -m 128m ...
docker -d --storage-opt dm.basesize=5G
```
- mount volume with permission
- [docker security guide](https://github.com/GDSSecurity/Docker-Secure-Deployment-Guidelines)

## 5.4 Configuration

- YML configuration
- Decouple from application itself
- Configuration= Key+Value
  store in db or env options

## 5.5 Monitoring

- Container
   * CPU
   * Memory
   * IO
   * Network
   * FD
- Root Tracing
   * docker logs
   * Tools like ELK

## 5.6 Miscellaneous

- Supervisor
- Discovery
- Boot order
- Fat Container
- Zoombie-reaping,syslog-ng,ssh,cron,runit

## 5.7 Toolings

- Docker Compose/Machine/Swarm
- K8S
- Mesos/Openstck?

## 6. Principles

- Don't Use Container Before understanding enough
- transient, stateless, and fault-tolerant
- IO or Security trade-off

## 6. Container Ecosystem

- Runtime
- packing & distribution
- service composition
- machine management 
- clustering
- networking - Docker Networking
- extensibility - Docker Plugin

## 6.1 Docker Machine

- create docker host on computer or cloud providers
- multiple drivers: vm,host,cloud platform
- docker-machine

## 6.2 Docker Compose

- Define and run mutiple-container application
- YAML Template to define cluster and manager it with compose

## 6.3 Docker Swarm

- Docker Swarm is native clusting 
- Serves the standard Docker API
- Pluggable backends

## 6.4 Docker Distribution

- Registry: Habor
- Docker-hub
- [noaty](https://github.com/theupdateframework/notary)

## 6.5 Docker Security

-[dickerbench](dockerbench.com)

## Others

- CoreOS
- Rancher
- Cloud Native Application
    * One Codee base
    * Dependencies
    * Config
    * Backing Services
    * Build,Release,Run
    * Processes
    * Port Binding
    * Concurrency
    * Disposablity
    * Dev/Prod Parity
    * Logs
    * Admin Process
- LibContainer,appC,runC
- Panamax/Shipyard,cadvisor
- Flynn/Denis/solumn.io
- Drone.io/Travis