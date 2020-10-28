---
layout: post
title: IBM 클라우더스 - 클라우드 에센셜 코스 모듈2 내용 정리
subtitle: Infrastructure Services
tags: [ibm, clouders, cloud, cloud essential]
comments: true
---

# [클라우드 에센셜(Cloud essential)](https://courses.cognitiveclass.ai/courses/course-v1:IBMDeveloperSkillsNetwork+CC0103EN+2020_T1/course/)

참고 : https://cloud.ibm.com/docs/vpc-on-classic-network?topic=vpc-on-classic-network-security-in-your-ibm-cloud-vpc

## 학습 목표🔴

- Describe the various compute resources that provide Infrastructure as a Service (IaaS) capabilities on the IBM cloud
- Describe the Compute, storage and networking options available in IBM Cloud
- Explain the broad-level architecture of a Virtual Private Cloud (VPC) and the IBM Cloud offerings to enable VPC
- Understand how the IBM Cloud capabilities enable the different deployment models (Public, Hybrid and Private)

<br>
<br>
<br>

## Infrastructure Offerings🟠

### VSIs, Bare Metal and Hyper Protect

IBM Cloud에는 Virtual Server Instances 및 Bare Metal 서버로 구성된 성숙한 '클래식'인프라 오퍼링이 있다. 
이들은 모두 x86 (또는 'Intel 기반') 오퍼링이지만 IBM Cloud는 Power Virtual Server 인스턴스도 제공한다.
이러한 컴퓨팅 옵션 외에도 IBM Cloud는 스토리지, 네트워킹 및 보안에 대한 옵션을 제공하여 고객이 필요에 맞게 간단하거나 복잡한 환경을 구축 할 수 있도록한다. 
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

## Virtual Private Cloud🟡
### Virtual Private Cloud

<br>
Virtual Private Cloud는 격리된 가상 네트워크(isolated virtual networks)를 정의 및 제어한 다음 이러한 네트워크에 클라우드 리소스를 배포할 수 있는 기능을 제공하는 퍼블릭 클라우드의 기능이다. 
<br>
Virtual network는 무엇일까? 이를 이해하기 위해서는 일반적인(standard) 퍼블릭 클라우드에서의 네트워크 배포 방법을 이해해야 한다. 
<br>

![vpc](https://github.com/98yejin/98yejin.github.io/blob/master/assets/img/vpc.PNG?raw=true)

> 백본(backbone) 또는 백본망(backbone network, 문화어: 중추망)은 다양한 네트워크를 상호 연결하는 컴퓨터 네트워크의 일부로서, 각기 다른 LAN이나 부분망 간에 정보를 교환하기 위한 경로를 제공한다. 백본은 같은 건물 안에, 다른 건물 안에, 또 캠퍼스 환경 안에, 아니면 넓은 지역에 걸쳐 다양한 네트워크를 묶을 수 있다. 일반적으로 백본의 용적은 그와 연결된 네트워크보다 더 크다. 수많은 지역의 대형 회사는 지역 전체를 한데 묶는 백본망을 가질 수 있는데, 이를테면 서버 클러스터가 각기 다른 지역에 위치한 여러 회사 부문에 의해 접근할 필요가 있을 경우가 그러하다. 이 부서들을 아우르는 네트워크 연결(예: 이더넷, 무선)을 네트워크 백본이라고 부른다. 백본을 설계할 때 네트워크 혼잡은 고려 대상이다. - What is a Backbone?(Whatis.com), Backbone Networks(Chapter 8)

관리자는 백본을 찾을 것이고, 백본은 클라우드의 모든 트래픽을 전달할 것이다. 한 클라이언트와 다른 클라이언트의 분리를 만들기 위해 그 백본에 어떤 분할이 있을 거다. 
또는 심지어 동일한 클라이언트 내에서 한 애플리케이션과 다른 애플리케이션 간의 분리를 할 수도 있다. 

그래서 이제 그러한 세분화가 이루어졌기 때문에, 우리는 실제로 그러한 세그먼트들 간의 커뮤니케이션을 가능하게 하는 네트워크 기능이 필요하다. 이 기능이 바로 라우터..!
<br>
위의 이미지의 CLOUD 안에
<br>
-------|<br>
       |<br>
       |-------<br>
<br>
이런 부분이 있는데
<br>
-------o|<br>
        |<br>
        |o--------<br>
<br>
이 동그란 부분이 라우터라고 볼리는 네트워크 기능이다. 
<br>
<br>

![vpc2](https://github.com/98yejin/98yejin.github.io/blob/master/assets/img/vpc2.PNG?raw=true)

여기를 보면 A라는 고객과, B라는 고객이 있다. 그리고 B 고객 옆에 있는 라우터를 보면 X표시가 되어있는데, 이는 필터링 기능을 제공하는 방화벽을 의미한다. 
위를 보면 이 클라우드는 완전히 격리되어 있고, 나머지(다른) 클라우드와 연결이 되어있지 않다.  

하지만 여기서 웹 애플리케이션을 호스팅하고 있기때문에 인터넷 연결이 필요하다. 따라서 NAT-ing을 제공할 수 있는 네트워크 기능이 필요하다. 
VPC에서 인터넷에 액세스 하기위해서는 세 가지 옵션을 사용할 수 있다.

1. 전체 서브넷의 인터넷 트래픽에 퍼블릭 게이트웨이를 사용하기
2. 인스턴스에 대한 인터넷 트래픽는 유동 IP를 사용하기
3. 안전한 외부 연결을 위해 VPN을 사용하기

![vpc4](https://cloud.ibm.com/docs-content/v1/content/abc47f4cb85646ad0fd120615f5023320f036e59/nl/ko/vpc-on-classic-network/images/vpc-connectivity-and-security.svg)

VPC는 서브넷으로 분류할 수 있고, 각 서브넷은 원하는 경우 공용 인터넷에 연결 할 수 있다.

<br>
<br>
VPC를 사용했을 때의 대표적인 장점에는 네 가지가 있다.

1. SECURE
2. SCALE 
3. CUSTOM 
4. FLEXIBLE 

어디선가 본 듯 하지 않은가? 바로 애자일 방법론😮! !! ! 
애자일 소프트웨어 개발 선언문을 보면 아래와 같은 것을 가치있게 여긴다.

1. 공정과 도구보다 <b>개인과 상호작용</b>을
2. 포괄적인 문서보다 <b>작동하는 소프트웨어</b>를
3. 계약 협상보다 <b>고객과의 협력</b>을
4. 계획을 따르기보다 <b>변화에 대응</b>하기를

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


