<html>
  <head>
    <title>AWS Cloud Foundations</title>
  </head>
  <body>
    <h1>AWS Cloud Foundations – One</h1>
<h2>1-Define what IaaS, PaaS and SaaS is.</h2>

<h2>Iaas</h2>
<p>Infrastructure as a service', is on-demand access to cloud-hosted physical and virtual servers, storage and networking - the backend IT infrastructure for running applications and workloads in the cloud.</p>

<h2>PaaS</h2>
<p>platform as a service' is on-demand access to a complete, ready-to-use, cloud-hosted platform for developing, running, maintaining and managing applications.</p>

<h2>SaaS</h2>
<p>Software as a service'is on-demand access to ready-to-use, cloud-hosted application software.</p>

<h2>2-Provide 6 advantages of cloud computing </h2>

<ul>
  <li>Cloud Computing saves money by its very nature, the cloud is designed for cost savings.</li>
  <li>Cloud Computing is fast Cloud Computing enables businesses to send, store, and distribute information more quickly and efficiently than before.</li>
  <li>Cloud Computing grants SMEs access to cutting-edge technology.</li>
  <li>Cloud Computing offers mobility.</li>
  <li>Cloud Computing is secure.</li>
  <li>Cloud Computing means enhanced data storage.</li>
</ul>

<h2>Define what an AWS region and an Availability Zone is</h2>

<p>AWS Regions are large and widely dispersed into separate geographic locations. Availability Zones are distinct locations within an AWS Region that are engineered to be isolated from failures in other Availability Zones.</p>

<h2>List all the AWS regions</h2>

<p>The AWS Cloud spans 99 Availability Zones within 31 geographic regions around the world, with announced plans for 15 more Availability Zones and 5 more AWS Regions in Canada, Israel, Malaysia, New Zealand, and Thailand.</p>

<h2>5-What are the categories in which the AWS services are grouped?</h2>

<p>AWS services are grouped into 10 categories: Compute, Storage, Database, Networking and Content Delivery, Management and Governance, Security, Identity and Compliance, Analytics, Application Integration, Mobile and IoT, and AR and VR.</p>

<h2>6- What is the difference between object storage and block storage?</h2>

<p>The main difference between object storage and block storage is the way they organize and manage data. Object storage is better suited for storing large amounts of unstructured data, while block storage is better suited for structured data that requires fast and low-latency access.</p>

<h2>7-List two AWS compute services and explain them.</h2>

<ul>
  <li>AWS EC2: Amazon Elastic Compute Cloud (EC2) offers granular control for managing your infrastructure with the choice of processors, storage, and networking.</li>
  <li>AWS Elastic Beanstalk: A fully managed service that makes it easy to deploy and run applications in multiple languages.</li>
</ul>

<h2>8-List two AWS storage services and explain them.</h2>

<ul>
  <li>S3: Amazon S3 is a highly scalable and durable object storage service that allows users to store and retrieve data from anywhere on the web.</li>
  <li>Amazon EBS (Elastic Block Store): A high-performance block storage service that provides persistent.
  <br></br>
  <h1>AWS Cloud Foundations - Two</h1>

  <h2>1-Explain the AWS Shared responsibility model.</h2>
<p>A shared responsibility model is a cloud security framework that dictates the security obligations of a cloud computing provider and its users to ensure accountability. Both the customers and AWS have responsibily. AWS is responsible for what is on the cloud and the customers are responsible for what is in the cloud</p>
<p>AWS is responsible for infranstructure, the host operating system, the virtualization layer and the physical security of the cloud servers.</p>
<p>Customers are responsible for managing their data (including encryption options), classifying their assets, and using IAM tools to apply the appropriate permissions.</p>

<h2>2-Explain an Identity and Access Management (IAM) Role.</h2>
<p>An IAM role is similar to an IAM user, in that it is an AWS identity with permission policies that determine what the identity can and cannot do in AWS. However, instead of being uniquely associated with one person, a role is intended to be assumable by anyone who needs it. Also, a role does not have standard long-term credentials such as a password or access keys associated with it. Instead, when you assume a role, it provides you with temporary security credentials for your role session.</p>

<h2>3-Explain an Identity and Access Management (IAM) Policy.</h2>
<p>An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed to provide permissions for many common use cases. They make it easier for you to get started with assigning permissions to users, groups, and roles than if you had to write the policies yourself. An AWS managed policy is a standalone policy that is created and administered by AWS. Standalone policy means that the policy has its own Amazon Resource Name (ARN) that includes the policy name. For example, arn:aws:iam::aws:policy/IAMReadOnlyAccess is an AWS managed policy.</p>

<h2>4-Describe an Amazon Machine Image (AMI).</h2>
<p>Amazon Machine Image (AMI) is a pre-configured virtual machine image used to create an EC2 instance in the AWS cloud.</p>

<h2>5-List the different EC2 instance types with use cases for each type.</h2>
<ul>
	<li>On-demand, which provides instant access to as much compute, memory and storage as you need. However, on-demand pricing is generally the most expensive.</li>
	<li>Spot instances.</li>
	<li>Reserved instances, which give you access to a dedicated but finite amount of resources.</li>
	<li>Dedicated hosts.</li>
</ul>

<h2>6-Explain Virtual Private Cloud (VPC).</h2>
<p>It is a virtual network infrastructure provided by cloud computing platforms such as Amazon Web Services (AWS), Microsoft Azure, and Google Cloud Platform (GCP). A VPC provides a private, secure, and isolated environment for running cloud resources such as virtual machines, databases, and storage, within a defined set of IP addresses. Users can create subnets, route tables, and network gateways to control the traffic flow within the VPC and between the VPC and other resources in the cloud.</p>

<h2>7-Differentiate between a Public and a Private subnet.</h2>
<p>A private subnet sets that route to a NAT gateway/instance. Private subnet instances only need a private ip and internet traffic is routed through

