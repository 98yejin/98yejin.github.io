---
layout: post
title: IBM 클라우더스 - 클라우드 에센셜 코스 모듈1 내용 정리
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

1.자동화(automation)

2. 가시성(Visibility)

3. 규제, 컴플라이언스 정책(Governance)

#### [쿠버네티스](https://kubernetes.io/ko/docs/concepts/overview/what-is-kubernetes/)

위에서 Hybrid cloud를 설명할 때 컨테이너와 쿠버네티스를 언급했다. 
쿠버네티스가 무엇인지 알아보기위해 배포의 짧은 역사를 알아보자.

![deployment](https://d33wubrfki0l68.cloudfront.net/26a177ede4d7b032362289c6fccd448fc4a91174/eb693/images/docs/container_evolution.svg)

1. Traditional Deployment : 초기 조직은 애플리케이션을 물리 서버에서 실행했었다. 한 물리 서버에서 여러 애플리케이션의 리소스 한계를 정의할 방법이 없었기에, 리소스 할당의 문제가 발생했다. 예를 들어 물리 서버 하나에서 여러 애플리케이션을 실행하면, 리소스 전부를 차지하는 애플리케이션 인스턴스가 있을 수 있고, 결과적으로는 다른 애플리케이션의 성능이 저하될 수 있었다. 이에 대한 해결책은 서로 다른 여러 물리 서버에서 각 애플리케이션을 실행하는 것이 있다. 그러나 이는 리소스가 충분히 활용되지 않는다는 점에서 확장 가능하지 않았으므로, 물리 서버를 많이 유지하기 위해서 조직에게 많은 비용이 들었다.

2. Virtualized Deployment : 그 해결책으로 가상화가 도입되었다. 이는 단일 물리 서버의 CPU에서 여러 가상 시스템 (VM)을 실행할 수 있게 한다. 가상화를 사용하면 VM간에 애플리케이션을 격리하고 애플리케이션의 정보를 다른 애플리케이션에서 자유롭게 액세스 할 수 없으므로, 일정 수준의 보안성을 제공할 수 있다.
가상화를 사용하면 물리 서버에서 리소스를 보다 효율적으로 활용할 수 있으며, 쉽게 애플리케이션을 추가하거나 업데이트할 수 있고 하드웨어 비용을 절감할 수 있어 더 나은 확장성을 제공한다. 가상화를 통해 일련의 물리 리소스를 폐기 가능한(disposable) 가상 머신으로 구성된 클러스터로 만들 수 있다.
각 VM은 가상화된 하드웨어 상에서 자체 운영체제를 포함한 모든 구성 요소를 실행하는 하나의 완전한 머신이다.

3. Container Deployment : 컨테이너는 VM과 유사하지만 격리 속성을 완화하여 애플리케이션 간에 운영체제(OS)를 공유한다. 그러므로 컨테이너는 가볍다고 여겨진다. VM과 마찬가지로 컨테이너에는 자체 파일 시스템, CPU, 메모리, 프로세스 공간 등이 있다. 기본 인프라와의 종속성을 끊었기 때문에, 클라우드나 OS 배포본에 모두 이식할 수 있다.

컨테이너는 다음과 같은 장점이 있다.

- 기민한 애플리케이션 생성과 배포: VM 이미지를 사용하는 것에 비해 컨테이너 이미지 생성이 보다 쉽고 효율적임.
- 지속적인 개발, 통합 및 배포: 안정적이고 주기적으로 컨테이너 이미지를 빌드해서 배포할 수 있고 (이미지의 불변성 덕에) 빠르고 쉽게 롤백할 수 있다.
- 개발과 운영의 관심사 분리: 배포 시점이 아닌 빌드/릴리스 시점에 애플리케이션 컨테이너 이미지를 만들기 때문에, 애플리케이션이 인프라스트럭처에서 분리된다.
- 가시성은 OS 수준의 정보와 메트릭에 머무르지 않고, 애플리케이션의 헬스와 그 밖의 시그널을 볼 수 있다.
- 개발, 테스팅 및 운영 환경에 걸친 일관성: 랩탑에서도 클라우드에서와 동일하게 구동된다.
- 클라우드 및 OS 배포판 간 이식성: Ubuntu, RHEL, CoreOS, 온-프레미스, 주요 퍼블릭 클라우드와 어디에서든 구동된다.
- 애플리케이션 중심 관리: 가상 하드웨어 상에서 OS를 실행하는 수준에서 논리적인 리소스를 사용하는 OS 상에서 애플리케이션을 실행하는 수준으로 추상화 수준이 높아진다.
- 느슨하게 커플되고, 분산되고, 유연하며, 자유로운 마이크로서비스: 애플리케이션은 단일 목적의 머신에서 모놀리식 스택으로 구동되지 않고 보다 작고 독립적인 단위로 쪼개져서 동적으로 배포되고 관리될 수 있다.
- 리소스 격리: 애플리케이션 성능을 예측할 수 있다.
- 자원 사용량: 리소스 사용량: 고효율 고집적.

![Kubernetes](https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/Kubernetes_logo_without_workmark.svg/200px-Kubernetes_logo_without_workmark.svg.png)

Q. 그래서 쿠버네티스가 왜 필요한데?

A1. 쿠버네티스(Kubernetes, 쿠베르네테스, "K8s")는 컨테이너화된 애플리케이션의 자동 디플로이, 스케일링 등을 제공하는 관리시스템으로, 오픈 소스 기반이다. 목적은 여러 클러스터의 호스트 간에 애플리케이션 컨테이너의 배치, 스케일링, 운영을 자동화하기 위한 플랫폼을 제공하기 위함이다.[3] 도커를 포함하여 일련의 컨테이너 도구들과 함께 동작한다.(출처: [위키백과](https://ko.wikipedia.org/wiki/%EC%BF%A0%EB%B2%84%EB%84%A4%ED%8B%B0%EC%8A%A4)

A2. 컨테이너는 애플리케이션을 포장하고 실행하는 좋은 방법이다. 프로덕션 환경에서는 애플리케이션을 실행하는 컨테이너를 관리하고 가동 중지 시간이 없는지 확인해야한다. 예를 들어 컨테이너가 다운되면 다른 컨테이너를 다시 시작해야한다. 이 문제를 시스템에 의해 처리한다면 더 쉽지 않을까? 그것이 쿠버네티스가 필요한 이유이다! 쿠버네티스는 분산 시스템을 탄력적으로 실행하기 위한 프레임 워크를 제공한다. 애플리케이션의 확장과 장애 조치를 처리하고, 배포 패턴 등을 제공한다. 예를 들어, 쿠버네티스는 시스템의 카나리아 배포를 쉽게 관리 할 수 있다.

쿠버네티스는 전통적인, 모든 것이 포함된 Platform as a Service(PaaS)가 아니다. 쿠버네티스는 하드웨어 수준보다는 컨테이너 수준에서 운영되기 때문에, PaaS가 일반적으로 제공하는 배포, 스케일링, 로드 밸런싱과 같은 기능을 제공하며, 사용자가 로깅, 모니터링 및 알림 솔루션을 통합할 수 있다. 하지만, 쿠버네티스는 모놀리식(monolithic)이 아니어서, 이런 기본 솔루션이 선택적이며 추가나 제거가 용이하다. 쿠버네티스는 개발자 플랫폼을 만드는 구성 요소를 제공하지만, 필요한 경우 사용자의 선택권과 유연성을 지켜준다.

> 쿠버네티스는 오류가 발생한 컨테이너를 제거 및 재시작 하며 현재 상태를 요구된 상태로 일치시키려고 끊임없이 확인하는 과정을 수행합니다. 직접 장애를 복구하는 일련의 과정을 생략할 수 있어 부담이 줄어들고, 정상 상태로 더 빨리 복구할 수 있게 되어 시스템 전체의 신뢰성이 향상되었습니다. - <우리는 불편함을 어떻게 마주하고 있는가> 포스팅 중
[우아한형제들 기술 블로그](https://woowabros.github.io/experience/2020/10/06/thiiing-system-improvement.html)에 따르면 쿠버네티스의 자가치유 기능을 바탕으로 서비스 안정성이 증가했다고 한다. 


#### On-Premise

사내, 직접 설치 

### IBM Cloud locations and Availability Zones🍚

#### Where is the IBM Cloud?🧇
[IBM Data center map](https://www.ibm.com/cloud/data-centers/#datacentermap)

> IBM Cloud is a global cloud with hosting locations across the globe in addition to the hardware and software offerings which allow you to host a private cloud in your own datacenters

IBM Cloud는 자체 데이터 센터에서 사설 클라우드를 호스팅 할 수있는 하드웨어 및 소프트웨어 오퍼링 외에도 전 세계에 호스팅 위치가있는 글로벌 클라우드다.

### IBM Cloud 'As a Service' summary and offerings·🧀

#### Iaas, PaaS and SaaS explained🧂

1.[IaaS](https://ko.wikipedia.org/wiki/%EC%84%9C%EB%B9%84%EC%8A%A4%EB%A1%9C%EC%84%9C%EC%9D%98_%EC%9D%B8%ED%94%84%EB%9D%BC%EC%8A%A4%ED%8A%B8%EB%9F%AD%EC%B2%98) 
- I : infrastructure
- aaS : as-a-Service 

서버, 스토리지, 네트워크를 필요에 따라 인프라 자원을 사용할 수 있게 클라우드 서비스를 제공하는 형태이다. 대표적인 기술로는 서버 가상화, 데스크톱 가상화 등이 있다.

ex. 네이버클라우드플랫폼 Compute, 아마존 EC2(Elastic Cloud Compute),
마이크로소프트 애저, 오픈스택 Rackspace 클라우드에서 유래됨,
구글 컴퓨트 엔진, RightScale,
FlexCloud 등, IBM의 베어메탈 클라우드,
대표적인 하이퍼바이저: ESXi, KVM, XenServer...

2. [PaaS](https://ko.wikipedia.org/wiki/%EC%84%9C%EB%B9%84%EC%8A%A4%EB%A1%9C%EC%84%9C%EC%9D%98_%ED%94%8C%EB%9E%AB%ED%8F%BC)
- P : Platform
- aaS : as-a-Service

일반적으로 앱을 개발하거나 구현할 때, 관련 인프라를 만들고 유지보수하는 복잡함 없이 애플리케이션을 개발, 실행, 관리할 수 있게 하는 플랫폼을 제공한다.구글이나 네이버, 다음 등에서 제공하는 공개 API가 PaaS의 일종이다. 구글의 '앱 엔진'이나 Bungee Labs 의 '번지커넥트' 등은 직접 온라인 서비스를 개발에서 배포, 관리 까지 할 수 있는 플랫폼을 제공하고 있다.


3. SaaS (Software as a Service)는 구독 모델을 기반으로하는 인터넷을 통해 애플리케이션을 제공하는 방법이다. 소프트웨어는 서비스 공급자가 호스팅한다. 소비자는 서비스 공급자가 모든 작업을 수행하므로 애플리케이션 호스팅이나 인프라, 소프트웨어 종속성 또는 소프트웨어 자체 유지에 대해 걱정할 필요가 없다. 


### IBM Cloud account types and support options🍗

#### [IBM Cloud Account Types](https://courses.cognitiveclass.ai/courses/course-v1:IBMDeveloperSkillsNetwork+CC0103EN+2020_T1/courseware/407a9f86565c44189740699636b4fb85/f52155c5007c413c901754dec3d58b9f/?child=first)🥫

세 가지 계정 유형
> Lite accounts are free of charge and allow you to explore IBM Cloud and create and use services that have a 'Lite' service plan. The account never expires (although you can deactivate it, should you choose to do so) but any Lite services that you create will automatically deprovision after 30 days, if they have not been used. Lite accounts are good for exploring IBM Cloud and for some limited development work. 
- 라이트
> Many users choose to move to a PAYGO account. This is simply done by entering credit card information to your account. You can still use all of the free of charge Lite services and you will also gain access to some services with 'Free' plan. Most importantly, you will unlock the whole IBM Cloud catalog and be able to create any service you want to. Your payment card will be automatically billed once a month and you will be charged for the services that you have used.
- 종량제 (PAYGO)
> Customers who consume larger amounts of services on IBM Cloud (typically $USD 1K and above), may choose to purchase a Subscription. With a subscription, a commitment to a certain spend is being made and so IBM Cloud provides discounted pricing based on the size of the subscription. 
- 신청


#### Support in IBM Cloud🧁

계정 별로 어떤 서비스를 받을 수 있는지 [소개](https://courses.cognitiveclass.ai/courses/course-v1:IBMDeveloperSkillsNetwork+CC0103EN+2020_T1/courseware/407a9f86565c44189740699636b4fb85/f52155c5007c413c901754dec3d58b9f/?child=first)

> The Free tier level of support applies to Lite Accounts only. To access other tiers of support, you must upgrade your account to a PAYGO or Subscription account.
- 라이트
> The Basic tier of support is provided to all PAYGO and Subscription customers by default and is free of charge.
- 종량제 (PAYGO)
> Customers can upgrade to paid-for Advanced Support and are encouraged to do so where they need guaranteed response times to tickets which they raise. Typically, customers who are running a small number of business critical, production workloads or who are undertaking non-production development work which is time critical will upgrade to Advanced Support.
- 신청


### The Cost Estimator Tool🥠

#### The Cost Estimator Tool🍫

IBM Cloud 내에서 서비스 인스턴스 또는 환경을 작성하기 전에 비용을 추정해야하는 경우 Cost Estimator 도구를 사용할 수 있다. 이 도구는 IBM Cloud 카탈로그를 통해 서비스 사양을 만든 다음 해당 사양에 대한 예상 비용을 제공하는 사용하기 쉬운 도구다. 도구 내에서 필요한만큼 견적을 저장할 수 있으며 pdf 형식으로 견적을 다운로드 할 수 있다. 


### IBM Cloud supports cloud native🍱

#### Cloud Native🍺

IBM - [클라우드 네이티브란 무엇입니까?](https://cloud.ibm.com/docs/cloud-native?topic=cloud-native-overview&locale=ko)

클라우드 컴퓨팅 환경은 가상화된 공유 풀에서 리소스를 온디맨드로 할당하고 해제하는 동적인 환경이다. 이러한 탄력적 환경은 기존의 온프레미스 데이터 센터에서 일반적으로 사용되는 초기 리소스 할당에 비해 보다 유연한 확장 옵션을 지원한다.

- 애플리케이션 또는 프로세스는 소프트웨어 컨테이너에서 분리된 단위로 실행된다.
- 프로세스는 리소스 사용을 개선하고 유지보수 비용을 줄이기 위해 중앙 오케스트레이션 프로세스에 의해 관리된다.
- 애플리케이션 또는 서비스(마이크로서비스)는 명시적으로 설명된 종속 항목과 느슨하게 결합된다.

MS - [클라우드 네이티브 정의](https://docs.microsoft.com/ko-kr/dotnet/architecture/cloud-native/definition)

CNCF [공식 클라우드 네이티브 정의](https://github.com/cncf/foundation/blob/master/charter.md)

- 클라우드 네이티브 기술은 조직이 퍼블릭, 프라이빗 및 하이브리드 클라우드와 같은 현대적이고 동적 인 환경에서 확장 가능한 애플리케이션을 구축하고 실행할 수 있도록 지원한다. 컨테이너, 서비스 메시, 마이크로 서비스, 변경 불가능한 인프라 및 선언적 API가 이러한 접근 방식을 잘 보여준다.
- 이러한 기술은 탄력적이고 관리 가능하며 관찰 가능한 느슨하게 결합 된 시스템을 가능하한다. 강력한 자동화와 결합되어 엔지니어는 최소한의 노력으로 자주 예측 가능하게 영향을 많이 미치는 변경을 수행 할 수 있다.

Cloud Native Computing Foundation은 오픈 소스, 공급 업체 중립 프로젝트의 에코 시스템을 육성하고 유지함으로써이 패러다임의 채택을 촉진하고자합니다.


### Identity and Access Management(IAM)🍛 

#### IAM🥢

> Identity and Access Management (IAM) is a major component of IBM Cloud and provides the means for an Account Owner to grant access rights to IAM-enabled services to other users that they 'invite' to their account. 

Identity and Access Management (IAM)는 IBM Cloud의 주요 구성 요소이며 계정 소유자가 자신의 계정에 '초대'한 다른 사용자에게 IAM 사용 서비스에 대한 액세스 권한을 부여 할 수있는 수단을 제공한다. 

> IAM means that access rights can be granted in a highly granular way, either directly to users and services or indirectly via Access Groups.

IAM은 액세스 권한이 사용자 및 서비스에 직접적으로 또는 액세스 그룹을 통해 간접적으로 매우 세분화 된 방식으로 부여 될 수 있음을 의미한다.

#### Granting Other User Access🎂




