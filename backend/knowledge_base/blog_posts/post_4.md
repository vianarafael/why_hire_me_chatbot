---
title: "I Tried to Automate My Taxes with AI"
excerpt: "A tale of tech, DIY ambition, and being a cheapskate"
date: "2025-04-14T15:35:07.322Z"
tags: [tax, automation, AI, Flask, Flutter]
---

**TL;DR**: When I lost my receipt bag at tax time, I built “E.L.I.Z.A.B.E.T.H.” — a Flask+SQLite backend with Google Vision OCR and OpenAI categorization, plus a Flutter frontend, to fully automate my 確定申告 process on my homelab.

## The Problem

It’s mid-April and once again I’m late writing my 確定申告 (income tax return). I want to pay only the legal minimum—but sorting receipts feels as appealing as a colonoscopy.

## So I Asked ChatGPT to Do It

I asked, “How can AI do my taxes for me?”  
It replied, “To be free, you have to own the boring parts too.”  
I’d told it to speak like Marcus Aurelius meets a Zen monk—yet this time? “Go fuck yourself, robot Yoda.”

## Then I Lost the Bag

I reached for the Ziploc full of receipts. Gone. No data. After a meltdown, I opened Cursor and started a new repo. Mission: Build a tool so foolproof that even I can’t screw it up—hosted on my homelab, backed up to external HD.

## What I Built

- **Backend:** Flask  
- **DB:** SQLite  
- **OCR:** Tesseract → switched to Google Vision  
- **AI Categorization:** OpenAI API  
- **Storage:** External hard drive (“personal S3 bucket”)

## Frontend — E.L.I.Z.A.B.E.T.H.

A Flutter app that:
1. Takes receipt photos  
2. Allows manual entry when needed  

I asked ChatGPT for a name like J.A.R.V.I.S.—it gave me “E.L.I.Z.A.B.E.T.H.” (Expense Ledger and Income Zone Assistant for Budgeting, Expenditure, Tax, and Household-finance). Yes, it’s ridiculous. No, I’m not changing it.

## The Results

- Snap a コンビニ receipt → E.L.I.Z.A.B.E.T.H parses, tags as “Food,” and logs it.  
- Cron job reminds me via LINE if backups haven’t updated—slightly passive-aggressive.  
- Finally, I can actually see where my money goes.

## What’s Next?

- File the taxes automatically  
- Automate more life admin (this is addictive)  


