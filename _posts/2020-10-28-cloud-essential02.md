---
layout: post
title: IBM 클라우더스 - 클라우드 에센셜 코스 모듈2 내용 정리
subtitle: Infrastructure Services
tags: [ibm, clouders, cloud, cloud essential]
comments: true
---

# [클라우드 에센셜(Cloud essential)](https://courses.cognitiveclass.ai/courses/course-v1:IBMDeveloperSkillsNetwork+CC0103EN+2020_T1/course/)

## 학습 목표🔴

- Describe the various compute resources that provide Infrastructure as a Service (IaaS) capabilities on the IBM cloud
- Describe the Compute, storage and networking options available in IBM Cloud
- Explain the broad-level architecture of a Virtual Private Cloud (VPC) and the IBM Cloud offerings to enable VPC
- Understand how the IBM Cloud capabilities enable the different deployment models (Public, Hybrid and Private)

## Infrastructure Offerings🟠
### VSIs, Bare Metal and Hyper Protect

IBM Cloud에는 Virtual Server Instances 및 Bare Metal 서버로 구성된 성숙한 '클래식'인프라 오퍼링이 있다. 
이들은 모두 x86 (또는 'Intel 기반') 오퍼링이지만 IBM Cloud는 Power Virtual Server 인스턴스도 제공한다.
이러한 컴퓨팅 옵션 외에도 IBM Cloud는 스토리지, 네트워킹 및 보안에 대한 옵션을 제공하여 고객이 필요에 맞게 간단하거나 복잡한 환경을 구축 할 수 있도록한다. 
<br>
<br>
<br>
계속 나오는 offering.. 어감은 알겠지만 정확히 어떤 것을 의미하는지 헷갈렸다. [여기](https://post.naver.com/viewer/postView.nhn?volumeNo=16180899&memberNo=4042690)에 
오퍼링의 정의가 나와있다. 물론 사전에 나온 것도 아니고, 클라우드 관련 포스팅도 아니지만.. IBM 클라우드도 B2B로 영업을 하니까.. 우리 회사를 선택해라, 우린 이런 것도 제공한다 이런 의미에서 
이런 강의를 하고 있는거니까.. 이 블로그에 나온 정의로 이해해도 될 것 같다.
<br>
> <b>오퍼링은 '고객의 니즈에 부합하는 답Soltuion을 제공함으로써 고객의 선택을 이끌어내는 제안'이라고 정의할 수 있다.</b>
<br>
<br>
#### Virtual Private Server란?
<br>
<br>
가상 사설 서버(Virtual private server) 혹은 가상 전용 서버는 하나의 물리적 서버를 나누어 여러 개의 가상 서버로 사용하는 가상화 방법의 한 형태이다. 이것은 메인 프레임과 같이 예전부터 익히 알려진 것이었으나 최근 VMware, 젠, FreeBSD Jail, 유저 모드 리눅스(UML), 리눅스-V서버, FreeVPS, OpenVZ, 그리고 Virtuozzo와 같은 기술들이 발전함에 따라 다시 주목을 받게 되었다.

- [출처](https://ko.wikipedia.org/wiki/%EA%B0%80%EC%83%81_%EC%82%AC%EC%84%A4_%EC%84%9C%EB%B2%84)
<br>
<br>
<br>

#### Hyper Protect Virtual Servers

Hyper Protect Virtual Servers는 Linux 애플리케이션 및 컨테이너화 된 워크로드를 실행할 수있는 매우 안전한 가상 서버를 제공하는 IBM Cloud 서비스다.

Hyper Protect Virtual Server는 다음과 같은 장점이 있다.

- 보안 - Hyper Protect Virtual Servers를 사용하면 보안 서비스 컨테이너에 가상 서버를 배포 할 수 있다. 그러면 가상 서버 내에서 실행하는 데이터와 코드의 기밀성을 보장 할 수 있다. 클라우드 관리자와 같은 권한이있는 사용자를 포함하여 데이터에 대한 외부 액세스는 허용되지 않는다.

- 클라우드상의 IBM Z 기능 - Hyper Protect Virtual Servers는 IBM Z 기능을 클라우드로 가져와 가장 안전하고 성능이 뛰어난 Linux 가상 서버에 워크로드를 배치하는 데 사용할 수 있다.

- IBM Z 하드웨어나 기술 요구X - Hyper Protect Virtual Server를 배포하면 필요한 하드웨어를 구입, 설치 및 유지 관리 할 필요없이 IBM Z 기술에 액세스 할 수 있다.

- 사용하기 쉽고 개방적이며 유연하다. 퍼블릭 클라우드의 개방성과 유연성을 수용하는 Hyper Protect Virtual Servers는 엔터프라이즈 환경에서 IBM Z 기능을 적용하는 시장 리더와 동등한 사용자 경험을 제공한다.

 

Hyper Protect Virtual Servers를 사용하면 IBM Z를 IBM의 글로벌 공용 클라우드 데이터 센터로 가져올 수 있다. 

- 기업의 모든 보안 및 규정 준수 정책을 준수하면서 공용 클라우드에서 핵심/비핵심 워크로드를 모두 실행할 수 있다.

- 향상된 비즈니스 서비스 수준을 유지하면서 동시에 비즈니스 자산을 보호 할 수 있다.

- 자체 공개 SSH 키를 사용하여 Linux 가상 서버를 인스턴스화 할 수 있다. 따라서 사용자 만 코드와 데이터에 액세스 할 수 있다. IBM Cloud 관리자도 데이터에 액세스 할 수 없다.

- LinuxONE 시스템의 장점을 활용하여 지원되는 모든 워크로드를 가장 안전하고 성능이 뛰어난 Linux 시스템에 배포 할 수 있다.

<br>
<br>
<br>
## Virtual Private Cloud🟡
<br>
<br>
<br>
### Virtual Private Cloud
<br>
<br>
<br>
### Virtual Private Clouds on IBM Cloud
<br>
<br>
<br>
## Network Services🟢
<br>
<br>
<br>
### Cloud Internet Services
<br>
<br>
<br>
### Load Balanceers
<br>
<br>
<br>
## Block and file storage options🔵
<br>
<br>
<br>
### Block Storage in IBM Cloud
<br>
<br>
<br>
### File Storage in IBM Cloud
<br>
<br>
<br>
## Object storage🟣
<br>
<br>
<br>
### Object Storage in IBM Cloud 
<br>
<br>
<br>
## Backup, recovery and replication🟤
<br>
<br>
<br>
### Introduction
<br>
<br>
<br>
### What is IBM Cloud Backup?
<br>
<br>
<br>
### What is Veeam?
<br>
<br>
<br>
### What is Zerto?
<br>
<br>
<br>
### What is Spectrum Protect?
<br>
<br>
<br>
## VMWare⚫
<br>
<br>
<br>
### VMware on IBM Cloud
<br>
<br>
<br>
### IBM Cloud for VMWare Solutions

