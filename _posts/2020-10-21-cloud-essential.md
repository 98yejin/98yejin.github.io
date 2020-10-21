---
layout: post
title: IBM 클라우더스 - 클라우드 에센셜 코스 내용 정리
subtitle: IBM Cloud Portfolio, Infra, run applications and workloads, some of the services
tags: [ibm, clouders, cloud, cloud essential]
comments: true
---

# [클라우드 에센셜(Cloud essential)](https://courses.cognitiveclass.ai/courses/course-v1:IBMDeveloperSkillsNetwork+CC0103EN+2020_T1/course/)

## 코스 구성🥪

1. IBM Cloud portfolio of products and services, the different service offerings available and the global reach of the IBM Cloud

: 제품 및 서비스의 IBM Cloud 포트폴리오, 사용 가능한 다양한 서비스 오퍼링 및 IBM Cloud의 글로벌 범위

2. key IBM Cloud infrastructure components including the compute, storage, and network products and services

: 컴퓨팅, 스토리지, 네트워크 제품 및 서비스를 포함한 주요 IBM Cloud 인프라 구성 요소

3. the options to run applications and workloads on the IBM Cloud

:  IBM Cloud에서 애플리케이션 및 워크로드를 실행하는 옵션

4. some of the services available on the IBM Cloud such as Data and AI, Analytics, Internet of Things and Blockchain

: 데이터 및 AI, 분석, 사물 인터넷 및 블록 체인과 같이 IBM Cloud에서 사용 가능한 일부 서비스

## 학습 목표🍧

1. Relate how the IBM Cloud enables the different service (IaaS, PaaS and SaaS) models and the different deployment (Public, Hybrid and Private) models of cloud computing

2. Access the IBM Cloud using graphical interfaces, command line tools and the API

3. Discover appropriate IBM Cloud products or services available to deliver specific functionality

4. Articulate the different ways IBM Cloud delivers services to developers and operational teams

5. Summarise core groups of available services 

## 강의 계획서🍕

1. 모듈 1-IBM Cloud 소개

- IBM Cloud 배치 옵션(IBM Cloud deployment options)
- IBM Cloud 위치
- IBM Cloud 'As A Service'요약
- IBM Cloud 계정 유형
- 비용 추정기 및 권한(Cost Estimator and permissions)
- 클라우드 네이티브 


2. 모듈 2-인프라 서비스

- 가상 사설 클라우드(Virtual Private Cloud)
- 네트워크 서비스
- 블록 및 파일 저장소
- 개체(Object) 저장소
- 백업, 복구 및 복제(replication) 서비스
- VMWare


3. 모듈 3-IBM Cloud의 워크로드

- 클라우드 파운드리
- 컨테이너 및 Kubernetes
- Red Hat OpenShift
- 클라우드 기능 및 서버리스


4. 모듈 4-IBM Cloud의 서비스 및 솔루션

- IBM Cloud Paks
- 데이터 저장 서비스
- 분석 서비스
- AI 및 딥 러닝 서비스
- 통합 서비스
- 개발자 및 운영 서비스

## 모듈 1-IBM Cloud 소개🍿

### 학습 목표🍳

- Summarize what the IBM Cloud is IBM Cloud가 무엇인지 요약하고,
- Explain the various categories of services and offerings available on IBM Cloud  IBM Cloud에서 가능한 다양한 서비스, 제공되는 것들의 카테고리를 설명하고, 
- Work with the cloud dashboard to view, manage, and work with some of IBM Cloud's portfolio of products cloud dashboard를 사용하여 IBM Cloud의 일부 제품 포트폴리오를보고 관리하고 작업하고,
- Explain the different ways to interract with the IBM Cloud  IBM cloud와 상호작용하는 다양한 방법들을 설명할 수 있게 되는 것

### IBM Cloud 개요🥗

> The IBM Cloud is a range of offerings and services from IBM covering all aspects of cloud computing to allow you to leverage the cloud resources where and how you want.

IBM Cloud는 클라우드 컴퓨팅의 모든 측면을 포괄하는 IBM의 다양한 오퍼링 및 서비스로, 원하는 위치와 방식으로 클라우드 리소스를 활용할 수 있다.

> Many businesses need more than a single public cloud provider, so IBM Cloud covers hybrid cloud and multi cloud.  These are terms that will be explored more in the course, but to summarise:  

많은 기업이 하나 이상의 퍼블릭 클라우드 프로파이더를 필요로하므로 IBM Cloud는 하이브리드 클라우드와 멀티 클라우드를 제공한다.

> Hybrid cloud is where a business wants to leverage their own data centre resources, both traditional infrastructure and private cloud, as well as a public cloud.  IBM Cloud can securely deliver the private cloud and services needed to create and manage a hybrid cloud

하이브리드 클라우드는 기업이 기존 인프라와 프라이빗 클라우드는 물론 퍼블릭 클라우드와 같은 자체 데이터 센터 리소스를 활용하고자하는 것이다. IBM Cloud는 하이브리드 클라우드를 생성하고 관리하는 데 필요한 프라이빗 클라우드 및 서비스를 안전하게 제공한다.

> Multi-cloud is where a business wants to spread their IT across multiple clouds, public and private to get the required levels of privacy, security and resilience, avoiding a single vendor lock-in.  However, adopting a multi-cloud approach introduces many challenges around the management and interoperability of applications and services.  IBM Cloud can help with offerings such as multi-cloud management, where applications and services spanning multiple clouds can be managed through a single console

멀티 클라우드는 기업이 IT를 퍼블릭 및 프라이빗 여러 클라우드에 분산시켜 필요한 수준의 개인 정보 보호, 보안 및 복원력을 확보하여 단일 공급 업체에 종속되지 않도록하는 것이다. 그러나 멀티 클라우드 접근 방식을 채택하면 애플리케이션 및 서비스의 관리 및 상호 운용성과 관련하여 많은 문제가 발생한다. IBM Cloud는 단일 콘솔을 통해 여러 클라우드에 걸친 애플리케이션 및 서비스를 관리 할 수있는 다중 클라우드 관리와 같은 오퍼링을 지원한다.

> Another important feature of cloud is the transformation needed within a company to fully benefit from moving to cloud.  To get the speed and agility that cloud promises the entire application lifecycle from design, through development to operations needs to evolve.  IBM Cloud can help with this transformation journey, providing access to the latest open source technology, and the best practices for adopting that technology, along with services to support the cultural and process change within a business.

클라우드의 또 다른 중요한 특징은 회사 내에서 클라우드로의 전환으로 인한 혜택을 완전히 누리는 데 변화가 필요하다는 것이다. 클라우드가 설계에서 개발, 운영에 이르기까지 전체 애플리케이션 수명주기를 약속하는 속도와 민첩성을 얻으려면 진화(power~up↗)해야 한다. IBM Cloud는 비즈니스 내에서 문화 및 프로세스 변화를 지원하는 서비스와 함께 최신 오픈 소스 기술 및 해당 기술을 채택하기위한 모범 사례에 대한 액세스를 제공하여 이러한 전환 여정을 지원한다.

> On the IBM Public cloud there are infrastructure, platform and software 'as a service' capabilities allowing you to consume the features you need and getting the right balance of customisation versus ease of use.  So you can choose to specify the exact compute (CPU and GPU), memory, networking and storage requirements, bringing your choice of operating system on dedicated hardware, move your VMWare virtual machines to the IBM Cloud, create a virtual private cloud within the IBM data centres, have IBM manage dedicated cloud resources for you or consume the multi-tenant public cloud offerings.

IBM 퍼블릭 클라우드에는 인프라, 플랫폼 및 소프트웨어 'as a service'기능이있어 필요한 기능을 사용하고 사용자 정의와 사용 용이성의 적절한 균형을 맞출 수 있다. 따라서 정확한(exact) 컴퓨팅 (CPU 및 GPU), 메모리, 네트워킹 및 스토리지 요구 사항을 지정하도록 선택하여 전용 하드웨어에서 운영 체제를 선택하고 VMWare 가상 머신을 IBM Cloud로 이동하고 IBM 내에 가상 사설 클라우드를 생성 할 수 있다.

### IBM Cloud and compliance🥞

![cycle](https://github.com/98yejin/98yejin.github.io/blob/master/assets/img/cloud_cycle.PNG?raw=true)

현재 20%는 클라우드로의 전환이 완료되었고 나머지 80% 가 남아있는데, 이 부분이 어려운 부분이다.
전환된 20%는 public cloud, 나머지 80%는 hybrid cloud라고 생각하면 된다.
즉, hybrid cloud가 클라우드 전환의 제 2막이다.

기업 수준 고객의 workload는 어느 정도의 private cloud, public cloud, legacy system들로 구성되어 있다. 어떤 한가지로만 구성이 되어있는게 아니다.

Public cloud로 전환할 때는 2가지가 요구된다.
1. Hybrid cloud expertise
- providers who understand hybrid cloud is more than a sigular environment
2. Secure platform
- cutting edge security, privacy and compliance

### Cloud deployment options🧇

- IBM Cloud Public : IBM Cloud hosted in IBM's data centers, accessible over the internet

- IBM Cloud Private : IBM Cloud delivered behind your firewall and in your data center

IBM Cloud Public provides the option to consume resources in a multi-tenant environment, where multiple customers workloads are isolated, but co-exist within a single physical machine.  If this is not desirable then single-tenant options are available.  You will learn more about options for isolating resources within the IBM Cloud as you work through this course.

IBM Cloud Public는 고객들의 workload는 독립되어있지만, 단일 물리 머신(single physical machine) 내에 공존하는 multi-tenant 환경에서 리소스를 소비하는 옵션을 제공한다.

#### HybridCloud🍣

장점
1. Interoperable 상호운용성
2. Scalable 확장성
3. Portable 이식성
4. Secure 보안

본질적으로 Hybrid Cloud는 개인(private)환경과 공공(public)환경의 혼합이다. 그리고 private env.와 public env.는 함께 hybrid cloud 사용자의
workload와 application을 실행한다.

Hybrid Cloud env.에서는 private env.와 public env.의 상호 운용이 가능해야 한다. 
본질적으로 public components는  private components와 동시에 작동한다. 

예를 들어 어떤 가상의 회사에서 개인환경과 공공환경을 둘 다 사용한다고 생각해보자. 
private env.에는 BFF(back, front), ERP, USER 서비스가 돌아가고 있다. public env에는 m(mobile)BFF가 대시보드를 보여준다. 
회사는 private env.에 있는 ERP 영역을 public env.로 옮기고 싶다.
Private env.에 있는 ERP 영역을 public env.로 옮기기 위해, linux container(like Docker), kubernetes 기술을 사용하면 성공적으로 옮길 수 있으나.. 쉬운 일은 아니다. 

다양한 서비스들이 Docker, Kubernetes tech.를 사용해 public cloud에서 서비스 되고 있다.
이런식으로 Public cloud 활용에는 끝이 없는 것 처럼 보이는 것! 그것이 public cloud의 장점이다. 

또한 특정 업체에 종속되지 않을 수 있다. 예를 들어 전통적인 app 개발에서는.. Java EE 스택을 사용해서 개발하고.. Java EE 스택에서 허용하는 기능들만 쓰고.. 

하지만 public cloud에서는 window shopping이 가능하다. 다양한 오픈소스 프로젝트들이 있고, 사용할 수 있는 프로그래밍 언어들도 다양하다. 

위의 예시에서 들었던 ERP application(on-premises)에서, private env.에 ERP layer를 계속 유지할 수 있듯이.. Hybrid computing에서는
특정 리소스에 계속 방화벽을 유지할 수 있다. 그리고 on-premises, public cloud의 장점을 계속 가지고 가면서 application과 workload를 계속 실행한다.

#### Multicloud🦪

> Multicloud is a cloud computing approach made up of 2 or more cloud environments

멀티클라우드는 2개 이상의 클라우드 환경으로 구성된 클라우드 컴퓨팅접근 방식이다. 
여기서 중요한 점은, Hybrid cloud와 Multi cloud가 완전히 같은 것은 아니라는 것이다.

>Hybrid cloud implies that your workloads a working together across multiple clouds - so
interoperability and portability of your workloads.

하이브리드 클라우드는 워크로드가 여러 클라우드에서 함께 작동한다는 것을 의미하므로 워크로드의 상호운용성과 이식성이 향상된다.

>Multicloud doesn't have that same requirement, but we are seeing that, you know, a lot of
enterprise users and customers are using multi and hybrid cloud strategy together.

멀티클라우드에는 동일한 요구사항이 없지만, 많은 엔터프라이즈 사용자와 고객이 멀티 클라우드와 하이브리드 클라우드 전략을 함께 사용하고 있다.
컨테이너와 쿠베르네테스 기술의 성장이 정말로 멀티클라우드의 성장을 가능하게 했다.

Q. 왜 멀티 클라우드를 사용하는가?

1. 멀티클라우드 전략은 애플리케이션 워크로드 중 하나의 클라우드가 작동을 멈추더라도 애플리케이션을 지원하는 또 다른 클라우드가 계속 작동하도록 보장한다.

2. 더 나은 사용자 경험을 제공한다. 예를들어, 전 세계에 다양한 사용자가 있다고 가정하자. 가장 가까운 클라우드로 라우팅하면 지연 시간을 줄이고 더 나은 사용자 경험을 제공할 수 있다. 

3. Specific integrations. 퍼블릭 클라우드에 저장하고 싶지 않지만 통합을 구축해야하는 민감한 방화벽 데이터가 있다고 가정하자. 멀티 클라우드 접근 방식을 활용하면 개인(private) 측에서 워크로드를 구축 하고, 개인적이고 민감한 고객 데이터를 활용할 수있다.


Q 멀티 클라우드 도입 전략

1.  

