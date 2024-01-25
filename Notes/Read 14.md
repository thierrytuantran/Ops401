1. List 2 differences between firewalls and an IDS?

  * Unlike firewalls which block threats, an IDS detects and alerts administrators to threats but does not block them. Also, firewalls filter traffic while an IDS analyzes packet contents looking for attack signatures.
    
2. Under what circumstances would you choose a network-based IDS over a host-based IDS?
 
  * A network-based IDS is easier and cheaper to deploy as it does not require software on each host, provides faster response times, and can detect attacks that a host-based IDS would miss by analyzing network traffic.
    
3. Name 3 major drawbacks of a NIDS?

  * It cannot process encrypted packets so attackers can slip by undetected.
  * IP packets can still use spoofed addresses making threats harder to pinpoint.
  * They generate frequent false positives that must be investigated.
