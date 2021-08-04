---
title:  "Copy files from/to Kubernetes"
date:   "2021-03-19"
categories:
- IT
tags: 
- kubernetes
- cheatsheet
---

This is kind of analogue of ``scp`` command for copying files from/to K8s pods.

There are a command:

```
kubectl cp <from> <to>
```

Copy file from Pod to local machine:

```
kubectl cp my-namespace/some-pod:/path/to/file /path/to/file/at/my/laptop
```

Copy file from the local machine to Pod:

```
kubectl cp /path/to/my/local/file my-namespace/some-pod:/path/to/file
``` 
