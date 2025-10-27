# 🔐 GitTrend Zoho Security Policy

This document outlines how to report vulnerabilities, what happens after you do, and the best practices we follow to keep GitTrend Zoho secure.

---

## 🧩 Supported Versions

| Version | Supported | Notes |
|----------|------------|-------|
| Latest (main) | ✅ | Actively maintained with security patches |
| Older releases | ❌ | Use the latest version for best protection |

---

## 🛡️ Our Security Principles

1. **Transparency:** All fixes and patches are made publicly available once verified.
2. **Privacy:** We never collect sensitive user data without consent.
3. **Responsible Disclosure:** We encourage private reporting before public announcements.
4. **Open Collaboration:** Security improvements are welcomed from the community.

---

## 📢 Reporting a Vulnerability

If you discover a potential security issue within **GitTrend Zoho**, please contact us **privately** first:

- 📧 **Email:** `gittrendrepos@gmail.com`
- 🧾 **Include Details:**
  - Description of the issue
  - Steps to reproduce
  - Impact or possible exploit
  - Suggested mitigation (optional)

Please **avoid posting the issue publicly** (e.g., GitHub issues) until it’s reviewed and resolved.

---

## 🔒 Handling Process

Once you report a vulnerability:

   - 🟢 Low — minor or informational
   - 🟡 Medium — limited exploitability 
3. A patch or fix will be developed and tested.  
4. You’ll be informed when the issue is fixed and credited (if you wish).  

---

## 🧠 Security Best Practices for Contributors

If you’re contributing code to GitTrend Zoho:
- Do **not** commit credentials or API keys.  
- Avoid hardcoding secrets (use `.env` or `config/settings.json`).  
- Validate user inputs in FastAPI routes.  
- Test your changes in a local environment before committing.  
- Run `pip-audit` or `safety check` to detect insecure dependencies.

---

## 🚫 Data Collection Policy

- GitTrend Zoho **does not store or sell** user data.  
- Only email credentials (Zoho SMTP) configured **locally by the user** are used for sending mail.  
- No tracking, analytics, or third-party cookies are used in the open-source version.

---

## 🙌 Credits

We appreciate everyone who reports vulnerabilities responsibly.  
Your contribution helps make GitTrend Zoho safer for all users.

Thank you for supporting secure open-source development 💙
