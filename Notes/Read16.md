1. What were the three commands used for the attack?
  * Get Credentials - Obtained credentials for the ***WAF-Role account.
  * List Buckets - Used the ***WAF-Role credentials to list S3 buckets.
  * Download Files - Used the ***WAF-Role account to download files from accessible S3 buckets.
2. What misconfiguration of AWS components allowed the attacker to access sensitive data?
  * The misconfiguration was an EC2 instance running a misconfigured WAF that enabled SSRF attack to access the AWS metadata service and gain credentials.
3. What are two of the AWS Governance practices that could have prevented such attack?
  * Review all access paths and permissions from identities to data storages using CIEM solutions.
Scope IAM role permissions to only required AWS resources.
