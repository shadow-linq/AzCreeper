# AzCreeper
Simple python script used for fuzzing users from a given organization. Similar to o365creeper, but uses an alternate method for user identification for federated Azure deployments (checks for the presence of `Credentials.CertAuthParams`).

# Usage
```
azcreeper.py <DOMAIN> <USERLIST>
```
