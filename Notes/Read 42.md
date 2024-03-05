1. Name the six credential-gathering techniques which Mimikatz is able to perform and explain how two of them work.
  * Pass-the-hash: Mimikatz uses stored password hashes (NTLM) to authenticate without needing the actual plaintext password.
  * Pass-the-ticket: It allows users to pass Kerberos tickets to another computer and log in with the user's ticket, exploiting weaknesses in the authentication system.
  * Overpass-the-hash (pass-the-key): This technique passes a unique key obtained from a domain controller to impersonate a user.
  * Kerberoast golden tickets: It provides non-expiring domain admin credentials to any computer on the network by exploiting specific tickets.
  * Kerberoast silver tickets: Exploits a feature in Windows that allows easy authentication to service accounts on the network, bypassing certain safeguards.
  * Pass-the-cache: This attack uses saved and encrypted login data on Mac/UNIX/Linux systems for unauthorized access.
2. What are four ways we can defend against Mimikatz attacks. Explain how two of the mitigations can stop Mimikatz.
  * Restrict admin privileges: Limit admin privileges to only users who need them, reducing the potential attack surface for Mimikatz to exploit.
  * Disable password caching: By configuring Windows settings to cache zero recent passwords, you can prevent Mimikatz from accessing cached password hashes stored in the system registry.
  * Turn off debug privileges: Disable debugging privileges on machines to prevent Mimikatz from exploiting Windows' default settings that allow local admins to debug the system.
  * Configure additional local security authority (LSA) protection: Upgrading to Windows 10 or configuring additional LSA protection settings provided by Microsoft can help mitigate the types of authentication attacks enabled by Mimikatz. These measures reduce the attack surface area and enhance overall security.
