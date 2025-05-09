---
title: "How My Wife’s Subscription Purge Turned Me Into a Cloud Storage Engineer"
excerpt: "A tale of tech, DIY ambition, and being a cheapskate."
date: "2025-04-06T15:35:07.322Z"
tags: [home-server, samba, Nextcloud, DIY, cloud-storage]
---

**TL;DR**: After my wife canceled all our subscriptions, I repurposed an old ThinkPad and external drive into a private Dropbox—then leveled up by installing Nextcloud for seamless, auto-uploading photo backups, zero fees, and full data control.

## The Subscription Reckoning

Everything’s expensive these days—groceries, electricity, taxes. My wife went on a subscription-cancellation spree and challenged me: “Can’t you do something about it?” Hell yes.

## The Setup

Ingredients on hand:
- An old ThinkPad running Ubuntu Server  
- A dusty external hard drive “maybe I’d be a photographer”  
- Righteous DIY anger  

I configured Samba shares, mounted the drive via `/etc/fstab`, and connected our laptops to `smb://<server-ip>/me`. Feels like 90s hacker chic—but it was manual and clunky.

## The Reality Check

My wife tested it. “Fine,” she said, “but my iCloud photos don’t back up automatically.” Ouch. Manual uploads won’t cut it.

## The Real DIY Cloud

Enter Nextcloud, promising:
- Automatic photo uploads  
- Browser and mobile/desktop access  
- Shared family folders  
- Zero monthly fees  

I installed dependencies, unpacked Nextcloud, configured Apache and MySQL, and completed the web installer at `http://<server-ip>`. Browser access: ✅. Mobile uploads: ❌.

## The Brick Wall

Nextcloud desktop worked, but the mobile app refused to upload. Logs and forums offered no clear answer—until I discovered one setting:

> **Nextcloud App → Media Access → “Always allow all”**

Flip that, and photos flow in the moment we step through the door.

## Victory

Now we have a home-grown iCloud:
- Instant photo backups  
- Shared folders for the family  
- No recurring fees  
- Total control over our data  

My wife’s phone now auto-uploads snapshots without lifting a finger.

## Epilogue

That night, as I tinker on my weather app, my little server hums in the corner—silently preserving our memories, subscription-free.  

