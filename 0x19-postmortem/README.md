# Summary of the Aplication web service disruption and related in Nancy company, Bogotá, Colombia

The following is the incident report for the Aplication service outage that occurred on April 25, 2020. We understand this service issue has impacted our valued users on Nancy Aplicatiors Server, and we apologize to everyone who was affected.

## Issue Summary
On Sunday, at 06:13pm to 07:22pm UTC-5, there was a brief network disruption that impacted a portion of Aplication  service. Normally, this type of networking disruption is handled seamlessly and without change to the performance, as affected storage servers query, process any updates, and reconfirm their availability to accept requests. The issue affected 100% of traffic to this service, all modules were down for a period of 1 hour aprox, and the root cause was an invalid configuration change in the main nginx file.

## Timeline (all times UTC-5)
* 08:00pm: service down is detected by a final user
* 08:22pm: look for error in server log files to detect the issue
* 08:29pm: Alert all tech and engineering team
* 08:36pm: Try to restore last backup taken
* 08:47pm: Try to reconnect data base and config the main nginx file again
* 09:08pm: Successful configuration change rollback
* 09:10pm: Server restarts begin
* 09:12pm: we carry out several tests
* 09:16pm: 100% of traffic back online

## Root Cause, resolution and recovery
At 6:00PM UTC-5, a configuration change was inadvertently released to our production environment without first being released to the testing enviroment. The change specified an invalid parameter for the performance servers in production nginx file for the proxy reverse. When the service was restarted, this generated a conflict in all service which the company could not open and work the main modules like sales, purchases and inventory. In addition, the internal monitoring systems permanently alert us, but this time it didn't and we overlooked it. Traffic was permanently queued waiting for a serving thread to become available. The file changed was restore as before we had it, commenting the lines added to analyze and test them later. The server began repeatedly hanging and restarting as they attempted to recover and at 09:16 PM UTC-5, the service outage began.

## Corrective and Preventative Measures
In the last two days, we’ve conducted an internal review and analysis of the outage. The following are actions we are taking to address the underlying causes of the issue and to help prevent recurrence and improve response times:
* Improve the monitoring on server config files or changes
* Patch Nginx server
* Disable the current configuration release mechanism until safer measures are implemented.
* Tests all changes in other cloud server for testing purposes.
* Change rollback process to be quicker and more robust.
* Improve process for auditing all high-risk configuration options.
* Develop better mechanism for quickly delivering status notifications during incidents.

Nancy Aplication  company is committed to continually and quickly improving our technology and operational processes to prevent outages. We appreciate your patience and again apologize for the impact to you, your users, and your organization. We thank you for your business and continued support.

Sincerely,

Nancy Aplication Inc, Bogotá, Colombia.

Posted by [Camilo Araque](https://twitter.com/AraqueGD)
