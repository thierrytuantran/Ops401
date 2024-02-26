1. Explain how a cross-site scripting attack works in non-technical terms.
  * Cross-site scripting is like tricking a website into delivering a letter with secret instructions (malicious code) to other users, which when opened, allows the sender (attacker) to manipulate or steal information from the recipients (users).
2. What are the three types of XSS attacks?
  * Reflected XSS: The malicious instructions are included in a link and activated when a user clicks on it.
  * Stored XSS: The malicious instructions are stored on the website itself, like a booby-trapped message on a forum.
  * DOM-based XSS: The malicious instructions are hidden in the website’s code and get activated when a user interacts with the website in a certain way.
3. If an attacker successfully exploits a XSS vulnerability, what malicious actions would they be able to perform?
  * The attacker can pretend to be the user, do anything the user can do on the website, access the user's private information, steal login details, or even alter the appearance or function of the website for that user.
4. What are some security controls that can be implemented to prevent XSS attacks?
  * To prevent such attacks, websites can rigorously check and clean user inputs (like comments or form entries), encode information before displaying it back to users, and use security policies in browsers to restrict unauthorized code execution.
