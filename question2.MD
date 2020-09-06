**Question2**

*Explain the Architecture model of this and the Benefit*

*Answer : Foo.com sends data over CDN to various end points across different regions, the end points have load balancers that distribute load across servers. Load balancers could be distributing load based on query string parameters, hostnames, or headers. Also there maybe cookies enabled to redirect traffic from the load balancer to the same user.Benifit of this will be CDN provides caching and users will have lesser delay accessing the same data over the network, because the data will be readily available at the CDN endpoint and user will not have to actually wait until data is fetched all the way from the DB server or instance*

*How do you roll out an update to the service without any downtime impact to the app foo.com*
We can use Kubernetes for it. This is done with rolling updates. Rolling updates allow Deployments’ update to take place with zero downtime by incrementally updating Pods instances with new ones. The new Pods will be scheduled on Nodes with available resources.

*If you have to deploy this App to the Cloud what services would you use and explain the Architecture. You can mention for Cloud of your choice (AWS / Amazon / Google Cloud (GCP) / Oracle / Alibaba Cloud)*

*Answer : I'd use cloud front for CDN and Application load balancer for distributing data across application servers*
